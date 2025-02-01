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
    get_package_share_directory("introvision2"),
    "img"
)

# 表示させたい画像ファイル名
IMAGE_NAME = "lena.jpg"

# 表示させたい画像ファイルのフルパス
IMAGE_PATH = os.path.join(IMAGE_DIR_PATH, IMAGE_NAME)

# 画像の読み込み
image = cv2.imread(IMAGE_PATH)


# rclpy ライブラリを初期化して、このプログラムから ROS2 を扱えるようにする
rclpy.init()

# このプログラム内でノード宣言する。
# ノード宣言することで ROS2 の各種インターフェースにアクセスできる
# 引数にノード名を記述する。
node = Node("image_publisher")


# パブリッシャーを作成
publisher = node.create_publisher(Image, "image", 10)

# CvBridge を初期化する
bridge = CvBridge()


# 画像データをパブリッシュする
while rclpy.ok():

    image_msg = bridge.cv2_to_imgmsg(image, encoding="bgr8")

    publisher.publish(image_msg)

    node.get_logger().info("image publish ...")

    rclpy.spin_once(node, timeout_sec=1)