from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# データベースファイルのパス

DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'data', 'construction.db')}"

# エンジン作成
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False
)

# セッション作成
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ベースクラス
Base = declarative_base()


def get_db():
    """データベースセッションを取得する依存性関数"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """データベースとテーブルを初期化"""
    # dataディレクトリが存在しない場合は作成
    data_dir = os.path.join(BASE_DIR, 'data')
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # 全モデルをインポートしてテーブル作成
    from models import project, master, vendor
    Base.metadata.create_all(bind=engine)
