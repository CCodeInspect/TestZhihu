# TestZhihu
## 写在前面：从 搭建环境->学习xcode使用 ->解决zhihu这个包的编译失败(用了一个古老的代码，可以追溯到18年，还是建议各位小伙伴们尽量找一个最近更新的包比较好啦) ->每次往真机上打包时都会调起模拟器 ->找元素找不到 ->成功 耗时有点久😋
###     当前项目只是作为一个练手的demo，可以参照test_3.py
### 以下是使用说明
#### 1.nvm use 21  //切到node21
#### 2.appium -v //检查appium版本
#### 3.xcode编译ios代码到真机 //地址：https://github.com/CCodeInspect/ZhihuDaily
#### 5.xcode编译WebDriverAgent到真机 //地址：https://github.com/facebookarchive/WebDriverAgent
#### 6.本地启动appium gui  //地址：https://github.com/appium/appium-desktop.git
#### 7.本地启动appium inspector  //地址：https://github.com/appium/appium-inspector.git
#### 8.inspector填写对应启动参数，不知道的小伙伴可以看test_3.py //当前参数是ios的传参，安卓需要自己修改传参
#### 9.然后真机被驱动了，可以跑跑我写的demo啦~ 😄😄😄
