# OBS屏控使用指南
由于历史遗留因素，城东校区大礼堂的屏控无法使用 [vMix](https://www.vmix.com/)，因此选择 [OBS](https://obsproject.com/) 作为屏控软件。  
## 配置
投屏前需要先进行设备和软件的配置。  
将大屏幕连接至计算机后，设置为`扩展屏幕`。设置后大屏幕上应出现桌面壁纸。  
在`菜单栏`>`配置文件`>`导入`中导入[配置文件](http://www.baidu.com)，导入成功后要记得切换。~当然也可以自己配置，但是出现问题我不管~  
在`文件`>`设置`>`通用`>`投影窗口`中勾选`投影窗口中隐藏光标`和`使投影窗口置顶`。~可以防止出现今年那样的意外事故~
## 场景
首先，确认你得到的节目单和最终节目单是一样的。  
千万不要像我一样临时修改场景。  
### 生成场景文件
将节目名在表格中逐行填入，保存为`menu.csv`文件。  
在你的U盘里面新建TXT文件，填入以下内容，并将后缀名改为`.bat`后双击打开打开。  
```
curl -F "file=@menu.csv" https://wu-junkai.vercel.app/api/menu >%date:~0,4%.json   
```

会生成一个新的磁盘 X:，里面是分类好的文件夹，按需把视频和音频放入文件夹，管理的时候会方便很多。  
在`场景集合`>`导入`中，选择`X:/配置/2022.json`导入，并切换到该集合，所有的场景已经创建好了。  

## 音频
音频是为了彩排的时候更方便播放，也方便和音响的同学同步文件。  
请勿在OBS内导入并尝试播放音频，心态会崩。  
彩排的时候，若有需要，请使用PotPlayer播放。  
晚会的时候，单个音频格式，请在音控室播放。

## 视频
导入视频后，调整视频的位置需要在视频播放（输出）的时候，可直接'Ctrl + S' 适应屏幕。  
在`编辑`>`高级音频属性`中，关闭`仅活动源`。并将`音频监听`调至`监听并输出`。  
所有视频文件都需要调整，否则播放时无声音。

