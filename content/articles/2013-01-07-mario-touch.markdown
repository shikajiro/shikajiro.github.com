---
layout: single
title: Arduino Fioでスーパーマリオなノックシステム作った
date: 2013-01-07 15:13
comments: true
Category:
slug:mario-touch
---
しかだよ。
Arduino を使ってスーパーマリオな玄関ノックをつくってみたよ。
まずは動画をどうぞ。

<iframe width="640" height="360" src="http://www.youtube.com/embed/q8MxyIBVOKw?feature=player_detailpage" frameborder="0" allowfullscreen></iframe>
タッチするとマリオの「チャリーン」が鳴ります。一定回数以上タッチすると1upします。

![](/images/mario/IMG_2187.jpg)

扉の裏側はこんな感じ。やっつけ感がすごい。部品にはArduino Fio、リチウムイオンバッテリー、
ブレッドボード、スピーカーを使ってます。
![](/images/mario/IMG_2186.jpg)

タッチする部分はNintendo DSのタッチパネルの部分を使ってます。
![](/images/mario/IMG_2188.jpg)
アダプタ込みで1,000円ちょい。
[スイッチサイエンス/商品詳細 Nintendo DSのタッチスクリーン(コネクタ別売)](http://www.switch-science.com/products/detail.php?product_id=105)

ブレッドボード配線はこんな感じ。適当なので参考程度に。スピーカーの配線が気になる。    
![](/images/mario/MarioTouch.png)
リチウムイオンバッテリー使ってるんだけど、すぐ電池が切れちゃう。省エネな使い方があるはずだけど、どうやって運用したらいいのかなぁ。

ソースコード等はこちら。
[shikajiro/MarioTouch](https://github.com/shikajiro/MarioTouch)

んじゃまた。
