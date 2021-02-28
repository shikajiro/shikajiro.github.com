---
layout: single
title: EclipseでContent Assistの候補をctrl+N or P で選択したい
date: 2012-11-19 17:12
comments: true
Category: Eclipse
Authors: shikajiro
slug: eclipse-ctrlnp
---

## ctrl+nで選択したい ##
Eclipse Juno (Eclipse Platform 4.2) から ctrl + n or pでContent Assistの候補一覧を選択できなくなった。ctrl + nすると、カーソルが動いちゃう。

![assit](/images/eclipse/contentassist.png)

## キー設定確認 ##

キー設定を見てみよう。

![](/images/eclipse/key-setting.png)

* Line Down
* Line Up

にキー設定されてるので、おかしくはない。
Eclipse 4.x の仕様かな。  
Eclipseの設定ではどうしようもなさそう・・・。

## OSのキー設定ごと変える ##

KeyRemap4MacBook を使って**OSのカーソル操作そのものを設定**することにした。

![](/images/eclipse/emacs-setting.png)

* Control+PNBF to Up/Down/Left/Right
* In Eclipse

にチェックを入れればいい感じになる。これで0.5%くらい開発効率が挙がったと思う。
