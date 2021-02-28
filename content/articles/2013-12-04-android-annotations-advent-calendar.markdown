---
layout: single
title: とあるプログラマのAndroidAnnotations
date: 2013-12-04 23:23
comments: true
Category: Android
Authors: shikajiro
slug: android-annotations-advent-calendar
---
<center>
<img src="/images/cv_aa.png">
</center>

※この記事は[Android Advent Calendar 2013](http://qiita.com/advent-calendar/2013/android) 12/04担当として書いてます。

　勢いでAdvent Calendar登録したけど、最近新しいこと、突き詰めたことしてない。
Genymotionは 明日の mofmofneko さんが書くみたいだからやめておこう。

　ブログ自体半年くらい放置してた。この半年でやったことをとりあえず箇条書きにしてみる。

+ Android Annotations
+ Android Studio
+ Genymotion
+ GreenDAO
+ Guava
+ デジハリ講師業はじめる。
+ iPhone4SからNexus5に機種変
+ 働き過ぎて瀕死になる


自分の中で一番テンション上がってるのがAndroid Annotationsなので、今回はこれのお話にする。

[AndroidAnnotations](http://androidannotations.org/)

AndroidAnnotationsでできることはコードの軽量化。以下の２つが主なメリット。

+ 開発スピードの向上
+ メンテナンスの簡素化

冗長な処理をシンプルにし、コード量を少なくする。結果、メンテナンスが楽になるメリットがある。

# 設定方法と使い方

書かれ尽くされたネタなので公式サイトをどうぞ。

# 僕なりの書き方

注意：ココ最近の情報は追っかけてません。

## RestとBean

やっぱRestの処理がシンプルになるのがかなり嬉しい。一般的なWegAPIを叩くアプリなら、Interfaceの実装でほぼ終わってしまう。

[gist:id=7789111]

Restで設計されたWebAPIならとてもシンプルに実装できる。（だが、すべての案件はそんなにうまくいかない）

### HttpClientErrorException を必ずチェックする

なぜかわからないけど、HTTPで発生する例外は（404とか）非チェック例外になっている。なにも考えずに実装すると、WebAPIを叩く処理はtry-catchせず書けてしまう。WebAPIを叩く処理はbackground処理必須なので、この例外はUIスレッドに何も言わずbackground処理を止めてしまう。backgroud処理の多くはProgressとか表示してるので、そこでUIもめんどいことになる。
つまり、WebAPIを叩いたら、必ず
~~HttpClientErrorException でtry-catchしよう。~~

*2013/12/12追記* RestClientException か RuntimeException でtry-catchしよう。

## backgroudとUiThread

backgroudとUiThreadが便利すぎて、AsyncTaskとかローダーとか忘れてしまうレベル。

[gist:id=7789442]

楽ちんだね。
ちゃんと制御したい時は、AsyncTaskとかローダーとか使いましょう。そうじゃなければこんな流れで問題ないはず。

## Preference
@SharedPrefで気をつけて欲しいのは、デフォルトのスコープは Activity であること。たぶん、PreferenceActivityで使うことを想定しているからだと思う。

[gist:id=7789652]

一般的にSharedPreferenceはアプリケーションの中で一意として使うことが多いと思う（たぶん）。
そう思って実装してると、設定した値が取れなくってビビることが何度もあので気をつけてね。

## ListView
特に実装が簡単になったと感じるのは子ViewをカスタムするListView。

[gist:id=7789824]

だいたいこんな感じでカスタムしたListViewが動かせる。TimelineAdapterのgetViewは再考の余地があると思うけど、これでもちゃんと動く。

### 2013/12/05 1:24 追記
ViewGroupが入れ子になっちゃうので、いい感じにしないといけないなと思いつつ放置してるのが僕です。

### 2013/12/12 追記
レイアウトファイルのルートを <merge>にすれば上記の問題は解決される。が、ルートレイアウトにpaddingとか設定した場合はmergeするとその設定が消えるので要注意。
id:tumo300-500 さんありがとございました。

## App と DBアクセス
AndroidAnnotationsを使い出してから、Applicationを継承したクラスの有意義性を知った。

[gist:id=7789950]

※DBにはGreenDao使ってる。

DBアクセスは各ActivityなどでApplicationをインジェクションしておけばいつでも呼び出せる。起動時に１回だけ実行する処理とかもココらへんで。

## ViewById と Click と OptionItems

@ViewById に使う layout xmlのidには予めjava変数になることを意識したネーミングがいいと思う。そうすれば

```
@ViewById TextView hogeView;
```

というように書ける。もし変数名がidに存在しなければEclipseが教えてくれる。

@Clickと@OptionItemsは現時点では上記のようにしない方がいい。

```
@Click
void hogeButton(){};
```

としても、もしidにhogeButtonが存在しない場合、Eclipseは教えてくれない。

```
@Click(R.id.hogeButton)
void onClickHogeButton(){}
```

などが妥当だと思う。これならidに存在しなければコンパイル時にエラーになる。

# 無理に使い過ぎない
そろそろまとめるけど、無理して全部AndroidAnnotationsで書こうとしない方がいいと思う。とてもスリムになるけど、やり過ぎると汎用性がなくなるので程よく実装すると良い。
使いこなせばAndroidAnnotationsからは離れられなくなるので、ぜひ試して欲しい。
あと、周りに使ってる人が居ないので、意見とか指摘とかアイデアとかあったらコメントおなしゃす。
