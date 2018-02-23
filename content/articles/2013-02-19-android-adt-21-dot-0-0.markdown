---
layout: single
title: ADT 21.0.0新機能紹介
date: 2013-02-19 00:28
comments: true
Category: Android, ADT
slug: android-adt-21-dot-0-0
---
しかだよ。
Android Developer Toolのリリース文をまとめてるよ。
しかの意訳なので気をつけてね。

#Layout Editor
##複数の端末画面が同時にプレビューできるようになりました。
![](/images/android/Screen Shot 2013-02-20 at 1.08.14.png)

詳しくはGoogle I/Oの20:30を見てね。
<iframe width="560" height="315" src="http://www.youtube.com/embed/Erd2k6EKxCQ#t=20m30s" frameborder="0" allowfullscreen></iframe>

> Added multi-configuration editing feature that was previewed at Google I/O developer tools talk in June. For an overview, see the session recording (starting at: 20:30).

##FragmentまたはListViewのレイアウトの変更が、コンフィグレーションにも適用されるようになりました。
![](/images/android/Screen_Shot_2013-02-20_at_1.05.35.png)

ってことだと思う。
> Modified the layout logic so that setting a Fragment layout or a ListView preview layout is now applied not only to the current layout but to all other configurations of the same layout.

##参照しているライブラリープロジェクトのリソースが選べるようになりました。
以下の操作で参照できるよ。

- GUIでの選択
- XMLエディタでのコード補完
- 参照元へのジャンプ (fn + F3)
最後の "other editing contexts"ってなんだろう。。。
> Updated the editor to include resources from library projects in the resource chooser, XML code completion, Go To Declaration and other editing contexts.

##翻訳中

エディターの中の一つのレイアウトの全てのバリエーションを強制しない。
例えば縦・横画面両方を表示したり、素早く切り替えたりできる。
あるいは同時に編集するには再度結合する。
前の方が良かったのなら元に戻せるよ。
ちょっと意味がわからないのであとで。

> Updated the editor so that it no longer forces all variations of a single layout into a single editor. You can, for example, open both the landscape and portrait versions of a layout as separate editors and quickly switch between them, or even re-dock your editors to edit them simultaneously. If you prefer the previous behavior, set the new option in Preferences > Android > Editors to use the old behavior.

##RelativeLayoutのウィジェット配置が直感的になりました。
> Improved the handling of RelativeLayout in the layout editor, so that dragging widgets around and deleting them should now result in the layout working more intuitively. In particular, deleting a widget causes the constraints flowing through the deleted widgets to be intelligently adjusted, and when moving widgets the constraints are preserved whenever possible.

## グラフィックエディターでテキストが編集可能に
グラフィックエディターでテキストがあるviewを追加してF2を押すと、修正画面が出てきます。
![](/images/android/Screen Shot 2013-02-21 at 1.10.39.png)
> Added the ability to specify a default action in Layout Editor views, which you can invoke with the F2 key. For example, after dropping a button or text view, you can press F2 to edit its text.

##リファクタリングでid名を変えれるようになりました。
ショートカットキーはcommand + shift + r
> Added renaming of an ID (changing the android:id attribute) by invoking the Rename shortcut.

##localeの追加が簡単になりました。
"Add Locale..." が見つからない・・・。
"Add New Translation"のことかな？
![](/images/android/Screen Shot 2013-02-21 at 1.21.17.png)
![](/images/android/Screen Shot 2013-02-21 at 1.21.29.png)
> Adding a new locale is now easier with the new Add Locale... action in the locale menu. In addition to creating the new values folder, it lets you edit an initial set of translations for the new locale.

##customviewのトレースジャンプ
customviewで発生した初期化の例外などはスタックトレースに表示され、トレースからジャンプすることもできます。
> Updated the editor so that when a custom view (or incorrectly configured view) throws an exception during initialization or painting, part of the relevant stack trace is shown inline in the layout editor, and you can click on the stack frames to jump to the relevant location

##customviewのスタックフレームリンク
customviewでレンダリングや初期化で例外が発生し、スタックフレームにリンクが表示された場合、スタックトレースの関係する部分を表示するようになりました。
> Improved the editor error display to show the relevant part of a stack trace when a custom view throws exceptions during rendering or construction, and provides hyperlinks to the stack frames.

##customviewの例外の表示の改善
レンダリング時に表示されるcustomviewの例外の表示の改善
> Improved the stack trace display for exceptions for custom views that are generated during rendering.

##言語と地域名をメニューから選べる
設定ダイアログやその他の編集中に言語と地域名の全てをメニューから選べるようになりました。
> Updated the configuration chooser so that it shows full language and region names (not just 2-letter codes) in menus, in the configuration dialog and other editing contexts.

##設定選択でデバイスメニューを更新しました。
> Improved the device menu in the configuration chooser.

#Lint
##25のlintルールが追加されました。
- 地域設定、
- レイアウトファイル、
- SparseArrayの間違った使い方、
- PowerManager.WakeLock
- manifest
> Added over 25 new lint rules for resources, locale settings, layout files, incorrect use of SparseArray and PowerManager.WakeLock and manifest issues.

##Jenkins Lint PluginによるXML出力機能の改善
> Improved the XML export function to support the Jenkins Lint plugin.

#Editors
##レイアウトエディタのモード記憶
> Modified the plugin to remember which editor mode (text or graphical) you were last using for each type of editor (layout, manifest or values) and uses that mode for newly opened files. This means that if you prefer to work with just XML, the editors start showing you XML text editors after you have switched to them for each type of editor.

最後にレイアウトエディタを開いた時のモードを記憶し、次にレイアウトエディタを開いた時に前回のモードで開くようになりました。
XMLエディタの人はずっとそれ開いて欲しいからね。

##XMLコード補完の更新
テーマリファレンスのコード補完を更新した。例えば ?android:attr/dividerHeight. とか。
> Updated XML code completion so that it completes (and shows documentation for) theme references, such as ?android:attr/dividerHeight.
![](/images/android/Screen Shot 2013-02-26 at 2.56.00.png)

#Android Virtual Devices (AVD)
##新しいデバイス定義の追加
ADVマネージャーにデバイス定義のタブが追加されました。
![](/images/android/Screen Shot 2013-02-26 at 2.57.38.png)
> Added new Device Definitions tab in the AVD Manager for configuring standard size and Nexus virtual devices.

##エミュレータの改善
スキンは動的に生成され、実際のハードウェアの様に反映されます。
> Improved emulators so that they launch with a skin that is dynamically generated and reflects the actual hardware configured in the AVD Manager.

#etc.
##新しいテンプレートメカニズム
現在のテンプレートの一新、いくつかのテンプレートの追加
> Improved the new template mechanism, cleaned up the existing templates and added several new templates

##OpenGL ES toolの向上
トレース機能に画像とフレームを出力する機能追加。
> Added ability to export images and frames in the Tracer for OpenGL ES tool.

##Systrace toolをDDMSに統合
> Integrated the Systrace tool into the DDMS perspective.

##JUnit test runnerの改善
接続されている全てのデバイスで実行できるようになった。
> Improved the JUnit test runner to allow a test to be run on all connected devices simultaneously.
