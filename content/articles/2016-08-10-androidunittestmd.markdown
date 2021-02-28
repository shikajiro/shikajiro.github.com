---
layout: single
title: AndroidのTestまとめ
date: 2016-08-10 06:20
slug: androidunittestmd
url: 2016/08/09/androidunittestmd/
Category: Android
Authors: shikajiro
save_as: 2016/08/09/androidunittestmd/index.html
---

この記事をまとめるにあたって
[Best Practices for Testing | Android Developers](https://developer.android.com/training/testing/index.html) を主に参考にしています。

Androidのテストは大きく分けて `Unit test` と `UI test` の２種類があり、実装方法や対象などで分けると5種類ある。

|ジャンル| テストの種類  | Androidへの依存 | 主に利用するツール|特徴|
|-|-|:-|:-|:-|
|Unit Test| local unit Test   | なし | Mockito|java VMで動作する|
|         | instrumentation Test| あり | hamcrest|Android上で動作する|
||App Component Test|あり||Serviceなどのテスト|
|UI Test  | single app Test| あり | espresso||
|         | multi app Test| あり | uiautomator|v18以上。|



## local unit test
android framework に依存しないテスト。java vm で実行されるため、他のAndroidOSに依存するテストに比べて高速。

android.jar は実際のコードが存在しないため、例外をスローしてしまう。そのため、以下の対応をする必要がある。

* Mockito で代替となるモックの処理を実装する
* テスト対象を android.jar に依存しないコードにがんばってする

### Mockitoで処理する場合

1. `unitTests.returnDefaultValues = true` を設定し、android.jarの中を呼んだ場合に、例外ではなくデフォルト値を返すようにする。
2. Mockitoでモックを実装する

```
#build.gradle
android{
    testOptions {
        unitTests.returnDefaultValues = true
    }
}
```

### kotlinでMockito

Mockitoがkotlinの予約語を使っているので、バッククォートが入ってちょっと書きづらい

>    Mockito.\`when\`()

[nhaarman/mockito-kotlin](github.com/nhaarman/mockito-kotlin) の`   whenever()`を使えばいい感じに出来そうだったけど、引数がnullを許容していないので使いづらい。

```
fun <T> whenever(methodCall: T?) = Mockito.`when`(methodCall)
```
こんな感じで定義し直せばそれっぽく使える。
[shikajiro/mockito-kotlin](github.com/shikajiro/mockito-kotlin) にfork する予定。


## instrumentation test
android framework に依存したテスト。Android のエミュレータや実機 で実行される

### 直ぐにテストを実行できない問題にはまる
Android Studio の右クリック > Run すると、JUnitテストとして動いてしまい、 `Empty test suite.` とエラーになりテストできない。
以下の雛形を元に Android Testとしてビルド設定を作り実行するとちゃんと動く。
![](/assets/Screen_Shot_2016-08-16_at_6_27_14.png)


## single app for espresso

後で書く

## multi app for uiautomator

後で書く

## Tips

### android library のテストで 64k 問題にはまる

テストと直接関係ない話だけど、テストライブラリとか追加してたらはまった。デバッグビルドの時だけ、multidexにする。

```
android{
     buildTypes {
        debug{
            multiDexEnabled true
        }
    }
}

dependencies {
    debugCompile 'com.android.support:multidex:1.0.1'
}
```
