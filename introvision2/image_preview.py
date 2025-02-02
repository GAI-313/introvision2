#!/usr/bin/env python3

# 画像処理用ライブラリ OpenCV をインポート
import cv2

# 画像ファイルのパスを取得するモジュールをインポート
from ament_index_python.packages import get_package_share_directory
import os

# 画像ファイルがあるディレクトリのパスを指定
IMAGE_DIR_PATH = os.path.join(
    get_package_share_directory("introvision2"),  # "introvision2"パッケージの共有ディレクトリを取得
    "img"  # その中の"img"フォルダを指定
)

# 表示させたい画像ファイル名
IMAGE_NAME = "lena.jpg"

# 表示させたい画像ファイルのフルパスを作成
IMAGE_PATH = os.path.join(IMAGE_DIR_PATH, IMAGE_NAME)

# 画像の読み込み
image = cv2.imread(IMAGE_PATH)  # 指定したパスから画像ファイルを読み込む

# 画像表示
cv2.imshow("image view", image)  # 読み込んだ画像を表示するウィンドウを作成
cv2.waitKey(0)  # 無限に待機し、キー入力を待つ（何かキーが押されるまで表示を維持）
