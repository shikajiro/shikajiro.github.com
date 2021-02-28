---
layout: single
title: fritzingに最初から入っているはずのパーツを使えるようにする
date: 2012-12-25 19:27
comments: true
Category: Make
Authors: shikajiro
slug: fritzing-init
---
![](http://fritzing.org/media/uploads/download_screenshot_jpg_versions/small_download_screenshot.jpg)

しかだよ。
ブレッドボードの配線の設計やメモに最適なツールと言えばFritzingですね。
[Download - Fritzing](http://fritzing.org/download/)

最初から色々パーツが入っているのですが、拡張版(?)のパーツのデータが抜けてる。検索はできるのに・・・。

というわけでなんとかしました。

### ソースコードを落とす
google code から落とせます。
[Source Checkout - fritzing - From prototype to product - Google Project Hosting](http://code.google.com/p/fritzing/source/checkout)

以下の２箇所のデータをまるっとコピー。
```
cp fritzing-read-only/fritzing/pdb/user /Applications/Fritzing/pdb/user
cp fritzing-read-only/fritzing/parts/svg/user /Applications/Fritzing/parts/svg/user
```
![](/images/fritzing/Screen Shot 2012-12-25 at 19.32.45.png)

こんな感じでNintendo DS のタッチパネルも使えます。素敵ですね。
