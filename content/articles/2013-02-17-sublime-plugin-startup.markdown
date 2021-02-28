---
layout: single
title: SublimeTextのpluginの作り方
date: 2013-02-17 01:19
comments: true
Category: SublimeText
slug: sublime-plugin-startup
Authors: shikajiro
---
しかだよ。
SublimeTextの簡単なプラグイン作成の依頼があったのでちょっと作ってみたよ。

##お題
コピーしたテキストの最終行の行末に改行があった場合、その改行を消してペーストしたい。

##新規プラグイン

tool > new plugin でテンプレートが作れます。

{% highlight python %}
    import sublime, sublime_plugin

    class ExampleCommand(sublime_plugin.TextCommand):
        def run(self, edit):
            self.view.insert(edit, 0, "Hello, World!")
{% endhighlight %}

###クリップボードの取得

    sublime.get_clipboard()

でクリップボードのデータを取得できるみたい。
あとはpythonの正規表現で良い感じにする。

###テキストの差し替え
command + v の処理を上書きするので、ペーストと同じ働きをさせたい。

    self.view.insert

だと、挿入になってしまい、範囲選択した状態でペーストすると置換されなくなっちゃう。なので

    self.view.replace

でペースト処理を行う。

##カーソル位置の取得
カーソル位置は

    self.view.sel()

で取得できる。戻り値は配列で、

- [0] カーソルの始まりの位置
- [1] カーソルの終わりの位置

を表す。範囲選択とかしてなかったら、[0]と[1]は同じ値を指す。

##パッケージの作成
プラグインはフォルダを作ってパッケージ化すると使いやすい。後述するショートカットキーの割り当てにも必要になる。

    ├Sublime Text 2
        ├─Packages
            ├─新規プラグインフォルダ
こんな感じの構成にするといい。

##キーの割当
キーの設定はプラグインフォルダに下記の設定ファイルを配置することで可能になる。

- Default\ (Linux).sublime-keymap
- Default\ (OSX).sublime-keymap
- Default\ (Windows).sublime-keymap

ファイルの中身はJSONで記述する。command + vにコマンドを割り当てる場合はこんな感じ。

{% highlight json %}
[  
    {  
        "keys": ["super+v"], "command": "garyuten"  
    }  
]
{% endhighlight %}

##出来上がり
完成はこちら。名前 GaryutenPaste。
由来は [@garyuten](http://twitter.com/garyuten) さんに頼まれたから。
[shikajiro/GaryutenPaste · GitHub](https://github.com/shikajiro/GaryutenPaste)

##参考

- [API Reference - Sublime Text 2 Documentation](http://www.sublimetext.com/docs/2/api_reference.html)
- [[Python] Sublime Text 2 のプラグイン開発 | kuminatatu UNDERGROUND](http://www.lackland.jp/13ug/?p=234)
