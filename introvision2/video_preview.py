#!/usr/bin/env python3

# 画像処理用ライブラリ OpenCV をインポート
import cv2

# 画像ファイルのパスを取得するモジュールをインポート
from ament_index_python.packages import get_package_share_directory
import os

# 画像ファイルがあるディレクトリのパスを指定
VIDEO_DIR_PATH = os.path.join(
    get_package_share_directory("introvision2"),  # "introvision2"パッケージの共有ディレクトリを取得
    "img"  # その中の"img"フォルダを指定
)

# 表示させたい画像ファイル名
VIDEO_NAME = "nyancat.mp4"

# 表示させたい画像ファイルのフルパスを作成
VIDEO_PATH = os.path.join(VIDEO_DIR_PATH, VIDEO_NAME)

# 動画の読み込み
cap = cv2.VideoCapture(VIDEO_PATH)  # 指定したパスから動画ファイルを読み込む

# フレームレートの取得
fps = cap.get(cv2.CAP_PROP_FPS)  # 動画のフレームレート（秒間のフレーム数）を取得

# 無限ループで動画を再生
while True:
    # 動画から画像を取得
    ret, image = cap.read()  # 動画から次のフレームを読み込む
    # フレームが正常に取得できた場合
    if ret == True:
        cv2.imshow("image view", image)  # 取得したフレームを表示
        cv2.waitKey(int(1000 / fps))  # フレームレートに基づいて待機時間を設定
    else:
        # 動画の終わりに達した場合、最初に戻る
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 動画の再生位置を最初に戻す
