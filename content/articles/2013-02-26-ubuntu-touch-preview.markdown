---
layout: single
title: Ubuntu Touch Developer Preview を Nexus7にインストールしてみた
date: 2013-02-26 20:53
comments: true
Category: Android
Authors: shikajiro
slug: ubuntu-touch-preview
---
<center>
<img src="/images/ubuntu/App-dev-tablet-GoMobile.png">
</center>

しかだよ。
Glaxy Nexus、Nexus7, Nexus10, Nexus4 でubuntu phone or tabletのデモ版がインストールできると聞いたので、早速やってみました。

割りと簡単に出来ました。DLに時間がかかるので、全部で2時間くらいかかりました。    
[Touch/Install - Ubuntu Wiki](https://wiki.ubuntu.com/Touch/Install)

##Desktop Setup
ubuntu os が必須です。
インストールはめんどいので、仮想ハードディスクを使いました。
vmware, virtualboxで動きます。適当にセットアップします。

[Ubuntuの入手 | Ubuntu Japanese Team](http://www.ubuntulinux.jp/download)

    sudo add-apt-repository ppa:phablet-team/tools
で、ubuntuのパッケージ管理システムにubuntu phone用のURLが追加されます。
んで、

    sudo apt-get update
    sudo apt-get install phablet-tools android-tools-adb android-tools-fastboot
で、環境構築完了。

##Device unlock
Nexusの準備をします。今回はNexus7でやりました。

1.とりあえず電源切る。

2.電源ボタンと音量up、音量down同時押しでbootloaderを起動。

![](/images/ubuntu/861796_10200726678831259_1974635631_n.jpeg)

3.USBケーブル接続。仮想環境なのでちゃんとubuntuに接続する。

4.ubuntuのterminal起動

    sudo fastboot oem unlock

5.以下の画面がでるので、unlockを選んで電源ボタンで決定。

![](/images/ubuntu/861692_10200726693911636_1836843598_n.jpeg)

##Initial Device Setup
1.unlockができたら、端末を起動する。

2.開発者モードでUSBデバッグを有効にする。

※OSのバージョンでやることが多かったりするので、公式サイトを要確認。

3.USBをubuntuと接続

※念のためビルド番号を控えておきましょう。

## Deploying Image to Device
ubuntuのターミナルで

    phablet-flash -b

DLやらインストールやらデバイスへのデータ転送が始まります。
１〜２時間くらい全力で放置してください。再起動は勝手にやってくれます。

![](/images/ubuntu/862024_10200726711992088_926917861_n.jpeg)
※ずっとこの画面と言う訳じゃないので注意

我慢して待ってるとubuntu phoneが起動してます。やったね！

![](/images/ubuntu/862704_10200726677191218_544994999_n.jpeg)

##簡単な使い方
いきなりロック解除がわからない。(´・ω・｀)

右"端"または左"端"から中央に向かってスワイプするとロック解除されます。  
![](/images/ubuntu/803886_10200726697191718_158649429_n.jpeg)

後は以下動画とかを参考にどうぞー。

<iframe width="420" height="600" src="http://www.youtube.com/embed/VGeFG86veOA" frameborder="0" allowfullscreen></iframe>
