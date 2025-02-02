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

# このプログラム内でノードを宣言する
# ノードを宣言することで ROS2 の各種インターフェースにアクセスできる
# 引数にノード名を記述する
node = Node("image_publisher")

# CvBridge を初期化する
bridge = CvBridge()  # OpenCV 画像と ROS2 画像メッセージの相互変換を行うためのブリッジを作成


# 画像メッセージを取得したときに実行される関数
def callback(msg: Image):
    # 受信した画像メッセージのログを表示
    node.get_logger().info("get image !")

    # ROS2 画像メッセージを OpenCV 画像に変換
    image = bridge.imgmsg_to_cv2(msg, "bgr8")

    # 変換した画像を表示
    cv2.imshow("subscribed image", image)  # 受信した画像をウィンドウに表示
    cv2.waitKey(1)  # 1ミリ秒待機してウィンドウの更新を行う


# サブスクライバーを作成
# "image" トピックから Image メッセージを受信し、callback 関数を呼び出す
subscriber = node.create_subscription(Image, "image", callback, 10)

# ノードをスピンさせる
# これにより、ノードはメッセージを受信し続ける
rclpy.spin(node)
