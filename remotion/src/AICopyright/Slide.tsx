import React from "react";
import {
  AbsoluteFill,
  Img,
  Audio,
  Sequence,
  useCurrentFrame,
  useVideoConfig,
  interpolate,
  staticFile,
} from "remotion";

const AUDIO_DELAY_FRAMES = 30; // 音声開始まで1秒の遅延
import { SlideData, ProjectStyle } from "./types";


interface SlideProps {
  slide: SlideData;
  style: ProjectStyle;
  assetsPath: string;
  audioPath: string;
}

const removePublicPrefix = (path: string): string => {
  return path.replace(/^public\//, "");
};

export const Slide: React.FC<SlideProps> = ({
  slide,
  style,
  assetsPath,
  audioPath,
}) => {
  const cleanAssetsPath = removePublicPrefix(assetsPath);
  const cleanAudioPath = removePublicPrefix(audioPath);
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // 音声遅延を考慮した時間計算
  const adjustedFrame = Math.max(0, frame - AUDIO_DELAY_FRAMES);
  const currentTimeMs = (adjustedFrame / fps) * 1000;

  const currentSubtitle = slide.subtitles.find(
    (sub) => currentTimeMs >= sub.startMs && currentTimeMs < sub.endMs
  );

  const audioVolume = (f: number) => {
    const fadeIn = interpolate(
      f,
      [0, style.audio.fadeInFrames],
      [0, style.audio.volume],
      { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
    );
    const fadeOut = interpolate(
      f,
      [slide.durationFrames - style.audio.fadeOutFrames, slide.durationFrames],
      [style.audio.volume, 0],
      { extrapolateLeft: "clamp", extrapolateRight: "clamp" }
    );
    return Math.min(fadeIn, fadeOut);
  };

  return (
    <AbsoluteFill style={{ backgroundColor: style.image.backgroundColor }}>
      {/* 白い角丸カード（スライド画像） */}
      <div
        style={{
          position: "absolute",
          top: 25,
          left: 45,
          right: 45,
          bottom: 130,
          backgroundColor: "#FFFFFF",
          borderRadius: 20,
          overflow: "hidden",
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        <Img
          src={staticFile(`${cleanAssetsPath}/${slide.image}`)}
          style={{
            width: "100%",
            height: "100%",
            objectFit: "contain",
          }}
        />
      </div>

      {/* 白い角丸バー（字幕）— 常時表示 */}
      <div
        style={{
          position: "absolute",
          left: 70,
          right: 70,
          bottom: 25,
          height: 75,
          backgroundColor: "#FFFFFF",
          borderRadius: 42,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
        }}
      >
        {currentSubtitle && (
          <span
            style={{
              color: "#1a1a1a",
              fontSize: 38,
              fontWeight: "bold",
              fontFamily: style.subtitle.fontFamily,
            }}
          >
            {currentSubtitle.text}
          </span>
        )}
      </div>

      {/* 音声 */}
      <Sequence from={AUDIO_DELAY_FRAMES}>
        <Audio
          src={staticFile(`${cleanAudioPath}/${slide.audio}`)}
          volume={audioVolume}
        />
      </Sequence>
    </AbsoluteFill>
  );
};
