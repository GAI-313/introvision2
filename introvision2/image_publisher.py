#!/usr/bin/env python3

# ROS2 を Python で使用するためのライブラリたちをインポート
from rclpy.node import Node
import rclpy

# 画像データを ROS2 画像メッセージに変換するためのライブラリをインポート
from cv_bridge import CvBridge

# ROS2 画像メッセージをインポート
from sensor_msgs.msg import Image

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

# rclpy ライブラリを初期化して、このプログラムから ROS2 を扱えるようにする
rclpy.init()

# このプログラム内でノードを宣言する
# ノードを宣言することで ROS2 の各種インターフェースにアクセスできる
# 引数にノード名を記述する
node = Node("image_publisher")

# パブリッシャーを作成
# "image" というトピックに対して Image メッセージを送信するパブリッシャーを作成
publisher = node.create_publisher(Image, "image", 10)

# CvBridge を初期化する
bridge = CvBridge()  # OpenCV 画像と ROS2 画像メッセージの相互変換を行うためのブリッジを作成

# 画像データをパブリッシュする
while rclpy.ok():  # ROS2 が正常に動作している間ループを続ける

    # OpenCV 画像を ROS2 画像メッセージに変換
    image_msg = bridge.cv2_to_imgmsg(image, encoding="bgr8")

    # 画像メッセージをパブリッシュ
    publisher.publish(image_msg)

    # ログにメッセージを表示
    node.get_logger().info("image publish ...")

    # ノードを一時停止し、他の処理を行う
    rclpy.spin_once(node, timeout_sec=1)  # 1秒間のタイムアウトでノードをスピン
