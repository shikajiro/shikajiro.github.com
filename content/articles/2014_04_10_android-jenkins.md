---
layout: single
Title: Gradleで管理されたAndroidProjectのEspressoテストをGenymotionを使ってjenkinsでぐるぐる回すまで(長い)
Date: 2014/04/10
Category: Android
Tags: pelican, python
Slug: android-jenkins
Author: shikajiro
---
![image](../images/menu.png)

Gradleで管理されたAndroidプロジェクトをJenkinsで動かすまで苦しんだのでまとめます。

##環境

- MacOS 10.8.5
- Java 1.7
- Gradle 1.11
- Android Studio 0.5.3
- Espresso 1.1
- Jenkins 1.5558
- git plugin
- gradle plugin

###前提

Android StudioでEspressoのテストが
```
./gradlew connectedAndroidTest
```
で動いてるものとします。

###諦めたこと

Android Emulator Plugin は諦めました。 なぜか以下のメッセージを出して途中で止まります。
```
android completed with result NOT_BUILT
```
動くこともある。動かないこともある。不安定過ぎるのでエミュレーターを断念。

###Genymotionで代用

エミュレーターをGenymotionに置き換えました。 以下Genymotionをjenkinsで呼び出す流れ。
```
$ VBoxManage list vms
```
で作成済みのGenymotionのdeviceを表示します。こんな感じ。
```
"Nexus S - 4.3 - API 18 - 480x800" {209f5db1-6ec1-4dff-9f6f-515a6ece0123}
```
これのスナップショットを作っておきます。
```
$ VBoxManage snapshot "Nexus S - 4.3 - API 18 - 480x800" take "factory"
```
スナップショットができたら、Jenkinsの Item > Build > Execute shell に起動処理を設定します。
```
VBoxManage snapshot "Nexus S - 4.3 - API 18 - 480x800" restore "factory"
{GENYMOTION_DIR}/player --vm-name "Nexus S - 4.3 - API 18 - 480x800" &
sleep 60
```
他には、 Item > Source Code Management > Git >
```
Repository URL : リポジトリのURL
Branch Specifier : */develop とか
```
Item > User Gradle Wrapper >
```
Tasks : *connectedAndroidTest*
```
Item > Post-build Actions > Publish JUnit test result report >

```
Test report XMLs : **/build/androidTest-results/connected/*.xml
```
これで動くはずです。（きっと）

##失敗例

- どんなに設定を変更しても動かなかったが、Itemを作りなおしたらすんなり動いた。
- テスト対象のブランチが違った。
- connectedAndroidTest と connectedInstrumentTest を間違えてた
- Genymotionのデバイスが起動しっぱなし

##参考

[AndroidのCIに纏わる諸々の問題 – Rejasupoem](http://rejasupotaro.github.io/2013/12/14/26.html)

[Use Genymotion with Jenkins for Android testing | Genymobile Blog](http://blog.genymobile.com/genymotion-jenkins-android-testing/)
