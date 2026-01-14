"""
ElevenLabs APIクライアントモジュール
"""
import io
import subprocess
import tempfile
import time
from pathlib import Path

import requests


class ElevenLabsError(Exception):
    """ElevenLabs API関連のエラー"""
    pass


class RateLimitError(ElevenLabsError):
    """レート制限エラー"""
    pass


class ElevenLabsAudioGenerator:
    """
    ElevenLabs APIを使用して音声を生成するクラス
    """

    BASE_URL = "https://api.elevenlabs.io/v1"

    def __init__(
        self,
        api_key: str,
        voice_id: str,
        model_id: str = "eleven_multilingual_v2"
    ):
        """
        クライアントを初期化

        Args:
            api_key: ElevenLabs APIキー
            voice_id: 使用するVoice ID
            model_id: 使用するモデルID（デフォルト: eleven_multilingual_v2）
        """
        self.api_key = api_key
        self.voice_id = voice_id
        self.model_id = model_id

    def _get_headers(self) -> dict:
        """APIリクエスト用ヘッダーを取得"""
        return {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }

    def generate_audio(
        self,
        text: str,
        stability: float = 0.5,
        similarity_boost: float = 0.75,
        style: float = 0.0,
        previous_request_ids: list[str] | None = None,
        output_format: str = "mp3_44100_128"
    ) -> bytes:
        """
        テキストから音声を生成

        Args:
            text: 読み上げるテキスト
            stability: 安定性（0.0=Creative, 0.5=Natural, 1.0=Robust）
            similarity_boost: 類似性ブースト（0.0-1.0）
            style: スピーチスタイルの強調度（0.0-1.0、高いほど表現豊か）
            previous_request_ids: 前のリクエストIDリスト（連続性確保用）
            output_format: 出力フォーマット

        Returns:
            音声データ（バイナリ）

        Raises:
            ElevenLabsError: API呼び出しに失敗した場合
            RateLimitError: レート制限に達した場合
        """
        audio_data, _ = self.generate_audio_with_request_id(
            text=text,
            stability=stability,
            similarity_boost=similarity_boost,
            style=style,
            previous_request_ids=previous_request_ids,
            output_format=output_format
        )
        return audio_data

    def generate_audio_with_request_id(
        self,
        text: str,
        stability: float = 0.5,
        similarity_boost: float = 0.75,
        style: float = 0.0,
        previous_request_ids: list[str] | None = None,
        output_format: str = "mp3_44100_128"
    ) -> tuple[bytes, str | None]:
        """
        テキストから音声を生成し、request_idも返す

        Args:
            text: 読み上げるテキスト
            stability: 安定性（0.0=Creative, 0.5=Natural, 1.0=Robust）
            similarity_boost: 類似性ブースト（0.0-1.0）
            style: スピーチスタイルの強調度（0.0-1.0、高いほど表現豊か）
            previous_request_ids: 前のリクエストIDリスト（連続性確保用）
            output_format: 出力フォーマット

        Returns:
            (音声データ, request_id) のタプル

        Raises:
            ElevenLabsError: API呼び出しに失敗した場合
            RateLimitError: レート制限に達した場合
        """
        url = f"{self.BASE_URL}/text-to-speech/{self.voice_id}"

        data = {
            "text": text,
            "model_id": self.model_id,
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity_boost,
                "style": style
            }
        }

        # 前のリクエストIDがあれば追加（連続性確保）
        if previous_request_ids:
            data["previous_request_ids"] = previous_request_ids

        response = requests.post(
            url,
            json=data,
            headers=self._get_headers(),
            params={"output_format": output_format}
        )

        if response.status_code == 200:
            # レスポンスヘッダーからrequest_idを取得
            request_id = response.headers.get("request-id")
            return response.content, request_id
        elif response.status_code == 429:
            raise RateLimitError("レート制限に達しました。しばらく待ってから再試行してください。")
        elif response.status_code == 401:
            raise ElevenLabsError("APIキーが無効です。設定を確認してください。")
        elif response.status_code == 400:
            raise ElevenLabsError(f"リクエストエラー: {response.text}")
        else:
            raise ElevenLabsError(f"APIエラー ({response.status_code}): {response.text}")

    def generate_audio_with_retry(
        self,
        text: str,
        max_retries: int = 3,
        base_delay: float = 1.0,
        return_request_id: bool = False,
        **kwargs
    ) -> bytes | tuple[bytes, str | None]:
        """
        リトライ機能付きで音声を生成

        Args:
            text: 読み上げるテキスト
            max_retries: 最大リトライ回数
            base_delay: 基本待機時間（秒）
            return_request_id: Trueの場合、(音声データ, request_id)を返す
            **kwargs: generate_audioに渡す追加引数

        Returns:
            音声データ（バイナリ）、またはreturn_request_id=Trueの場合は(音声データ, request_id)
        """
        for attempt in range(max_retries):
            try:
                if return_request_id:
                    return self.generate_audio_with_request_id(text, **kwargs)
                else:
                    return self.generate_audio(text, **kwargs)
            except RateLimitError:
                if attempt < max_retries - 1:
                    delay = base_delay * (2 ** attempt)
                    print(f"  レート制限に達しました。{delay}秒後にリトライします...")
                    time.sleep(delay)
                else:
                    raise

        raise ElevenLabsError("最大リトライ回数に達しました")

    def generate_audio_chunks(
        self,
        chunks: list[str],
        show_progress: bool = True,
        **kwargs
    ) -> list[bytes]:
        """
        複数チャンクから音声を生成

        Args:
            chunks: テキストチャンクのリスト
            show_progress: 進捗を表示するか
            **kwargs: generate_audio_with_retryに渡す追加引数

        Returns:
            音声データのリスト
        """
        audio_chunks = []

        for i, chunk in enumerate(chunks, 1):
            if show_progress:
                print(f"  音声生成中... ({i}/{len(chunks)})")

            audio_data = self.generate_audio_with_retry(chunk, **kwargs)
            audio_chunks.append(audio_data)

            # API負荷軽減のため少し待機
            if i < len(chunks):
                time.sleep(0.5)

        return audio_chunks

    def merge_audio_chunks(self, audio_chunks: list[bytes]) -> bytes:
        """
        複数の音声チャンクを1つに結合（ffmpegを使用）

        Args:
            audio_chunks: 音声データのリスト

        Returns:
            結合された音声データ
        """
        if len(audio_chunks) == 1:
            return audio_chunks[0]

        # 一時ファイルを使用してffmpegで結合
        with tempfile.TemporaryDirectory() as tmpdir:
            tmpdir_path = Path(tmpdir)

            # 各チャンクを一時ファイルに保存
            chunk_files = []
            for i, chunk in enumerate(audio_chunks):
                chunk_path = tmpdir_path / f"chunk_{i:03d}.mp3"
                chunk_path.write_bytes(chunk)
                chunk_files.append(chunk_path)

            # ffmpeg用のリストファイルを作成
            list_file = tmpdir_path / "files.txt"
            with open(list_file, "w") as f:
                for chunk_file in chunk_files:
                    f.write(f"file '{chunk_file}'\n")

            # 出力ファイル
            output_file = tmpdir_path / "merged.mp3"

            # ffmpegで結合
            try:
                result = subprocess.run(
                    [
                        "ffmpeg", "-y", "-f", "concat", "-safe", "0",
                        "-i", str(list_file), "-c", "copy", str(output_file)
                    ],
                    capture_output=True,
                    text=True
                )

                if result.returncode != 0:
                    raise ElevenLabsError(f"ffmpegエラー: {result.stderr}")

                return output_file.read_bytes()

            except FileNotFoundError:
                # ffmpegがない場合は単純連結（音質は低下する可能性あり）
                print("  警告: ffmpegが見つかりません。単純連結で代用します。")
                return b"".join(audio_chunks)

    def save_audio(self, audio_data: bytes, output_path: str) -> None:
        """
        音声データをファイルに保存

        Args:
            audio_data: 音声データ（バイナリ）
            output_path: 保存先パス
        """
        path = Path(output_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(audio_data)


def verify_api_key(api_key: str) -> bool:
    """
    APIキーが有効かどうかを確認

    Args:
        api_key: 確認するAPIキー

    Returns:
        有効な場合True
    """
    url = "https://api.elevenlabs.io/v1/user"
    headers = {"xi-api-key": api_key}

    try:
        response = requests.get(url, headers=headers)
        return response.status_code == 200
    except requests.RequestException:
        return False
