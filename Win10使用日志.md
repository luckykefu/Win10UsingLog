---
created: '1970-01-01 '
tags:
  - project
---
# Win10 使用日志

## 安装

### 下载 Win 10 ISO 镜像

### make usb live

https://www.ventoy.net/en/download.html

### Install

### update

##### 1. 系统更新

##### 2. Microsoft Store更新

### 激活

https://github.com/zbezj/HEU_KMS_Activator/releases

# Software

## VirtualBox

https://www.virtualbox.org/wiki/Downloads

## NVIDIA

https://www.nvidia.cn/geforce/drivers/

## Dell Drive

https://www.dell.com/support/home/zhcn?app=drivers

`5ZC5RH2`

## Browser

proxy switchyomega

Chrome：[Chrome官方网站](https://www.google.cn/intl/en_uk/chrome/dev/)。

## Office

https://www.openoffice.org/zhcn/download/index.html

## Bandizip

[Bandizip官方网站](https://cn.bandisoft.com/bandizip/)

## DSM++

https://github.com/Chuyu-Team/Dism-Multi-language/releases

## Vlc

https://www.videolan.org/vlc/

## Miniconda 3

https://docs.anaconda.com/miniconda/index.html

```

C:\Users\31245\.conda\envs

```
## Obsidian

https://obsidian.md/download

## vscode

https://vscode.github.net.cn/

## QuickLook 空格预览

https://github.com/QL-Win/QuickLook/releases

## IDM 下载器

## OBS 直播录屏软件

https://obsproject.com/download

## Git 版本控制工具

https://github.com/git-for-windows/git/releases/

## 火绒安全软件

https://www.huorong.cn/

## 搜狗输入法

https://pinyin.sogou.com/zhihui/?indexbanner

## Telegram

https://desktop.telegram.org/

## Every Proxy apk

## Imaging Edge Desktop

https://www.sonystyle.com.cn/minisite/cross/app/imaging_edge.htm

## Focusrite Control

https://downloads.focusrite.com/focusrite/scarlett-3rd-gen/scarlett-solo-3rd-gen

## qbittorrent

https://sourceforge.net/projects/qbittorrent/

# Usage

## Make Link

```

rmdir %USERPROFILE%\.conda

cmd /c mklink /D %USERPROFILE%\.conda D:\Win\.conda

rmdir %USERPROFILE%\.ssh

cmd /c mklink /D %USERPROFILE%\.ssh D:\.ssh

rmdir “%USERPROFILE%\Documents\Studio One\Presets\PreSonus\FX Chains”

cmd /c mklink /D “%USERPROFILE%\Documents\Studio One\Presets\PreSonus\FX Chains” "D:\Documents\MySyncData\StudioOne6\FX Chains"

```

set PIP_INDEX_URL=https://pypi.mirrors.ustc.edu.cn/simple/

.pip

| pip.ini

[global]

index-url = https://pypi.mirrors.ustc.edu.cn/simple/

[install]

trusted-host = pypi.mirrors.ustc.edu.cn

del %USERPROFILE%\pip
cmd /c mklink /D %USERPROFILE%\pip D:\Win\pip

```

## VirtualBox

挂载 D 盘

```

sudo mount -t vboxsf D_DRIVE /mnt

```

```

set all_proxy=socks5://192.168.43.1:1088

```

