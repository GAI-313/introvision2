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

# rclpy ライブラリを初期化して、このプログラムから ROS2 を扱えるようにする
rclpy.init()

# このプログラム内でノード宣言する。
# ノード宣言することで ROS2 の各種インターフェースにアクセスできる
# 引数にノード名を記述する。
node = Node("image_publisher")

# CvBridge を初期化する
bridge = CvBridge()


# 画像メッセージを取得したときに実行される関数
def callback(msg:Image):
    node.get_logger().info("get image !")

    image = bridge.imgmsg_to_cv2(msg, "bgr8")

    cv2.imshow("subscribed image", image)
    cv2.waitKey(1)


# サブスクライバーを作成
subscriber = node.create_subscription(Image, "image", callback, 10)

# ノードをスピンさせる
rclpy.spin(node)