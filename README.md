# RoboSys2018 HW2
16C1069 島田 滉己

# 浮かび上がる邪神
カメラで撮影された画像内の黒色をマスクすることで黒い文字や絵を表示する

# Usage
```
$roslaunch ./launch/usb_cam-test.launch
$python scripts/camera.py
```

#Install
* usb_camのインストール
```
$cd ~/catkin_ws/src
$git clone https://github.com/bosch-ros-pkg/usb_cam.git
$cd ..
$catkin_make
```

* launchとscriptsにそれぞれ必要なファイルを入れる
```
$git clone https://github.com/tiger0421/RoboSys2018-2.git
```

# License
BSD
