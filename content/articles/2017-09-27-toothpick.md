---
layout: single
title: Android の DI を Dagger から ToothPick に代えた
date: 2017-09-27 19:31
slug: toothpick
url: 2017/09/27/toothpick/
Category: Android
save_as: 2017/09/27/toothpick/index.html
Authors: shikajiro
---

![](https://camo.githubusercontent.com/24ff6ae4cd9e20cddbaf1c027651e1545b912724/68747470733a2f2f7261772e6769746875622e636f6d2f7374657068616e656e69636f6c61732f746f6f74687069636b2f6d61737465722f6173736574732f6c6f676f2e6a7067)

Dagger2 がほんとに辛い。
公式サイト見たり、先駆者の皆さんのブログを見ながらやってみるけど、ややこしくて自分で改善するのはかなり辛い。使っているというより、言われたとおりに設定するだけで精一杯。

そんなことをぼやいてたら Realm と ウフィカ の中の人 [@zaki50](https://twitter.com/zaki50) さんから

<blockquote class="twitter-tweet" data-lang="ja"><p lang="ja" dir="ltr">toothpickためそ？</p>&mdash; zaki50 (@zaki50) <a href="https://twitter.com/zaki50/status/903553963747717121">2017年9月1日</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

とアドバイス頂いたので試してみました。

[stephanenicolas/toothpick: A scope tree based Dependency Injection \(DI\) library for Java](https://github.com/stephanenicolas/toothpick)

サイトを見て設定すれば動くんだけど、どうしても見落としがちなとことかあるので、簡単に紹介します。


## Toothpick とは
Java の DI です。 とはいえ、主に Android を対象にしてる気がします。
ツリースコープなので、「Activity で Inject してたら Fragment でも利用できる」みたいな感じです。（ざっくり）

### Tree Scope
```text
//a typical Toothpick scope tree during the execution of an Android app.

       @ApplicationSingleton 
         /              |    \  
        /               |     \
       /                |      \
   @PresenterSingleton  |   Service 2
         /              | 
        /            Service 1  
       /            
Activity 1
    /   \
   /   Fragment 2
  /
Fragment 1
```

### 特徴
* Dagger2より簡単（個人の感想）
* 高速([Benchmark](https://github.com/stephanenicolas/toothpick/wiki/Benchmark))

などがあります。特に一つ目がホント助かる・・・。

## 使い方
本題です。実際に使えるようになるまでのソースを抜粋して紹介します。バージョンは日々進化してるので、基本公式サイトを信用してください。
また、ここではkotlinを使ってる場合の例になります。

### builg.gradle

[gist:id=f3348df6476f5633fea30b86ba3ffff6,file=build.gradle]

kapt で `toothpick_registry_package_name` を設定する必要があります。ここで指定したパッケージのソースが自動生成されます。ここ大事。

### MainApplication.kt

[gist:id=f3348df6476f5633fea30b86ba3ffff6,file=MainApplication.kt]

Applicationを継承したクラスが必須になります。
 
 `MemberInjectorRegistryLocator` と `FactoryRegistryLocator` に set する Registry が大事なところです。
ここには、 kapt で指定したパッケージに生成される `MemberInjectorRegistry` と `FactoryRegistry` を指定してください。ToothPick自体にもこの２つのクラスは存在するので、そちらを指定しないように気をつけてください。

もし自動生成しない場合は、エラーになってもいいので rebuild や Make Project すると生成するかもしれません。がんばろう。

### Module.kt
[gist:id=f3348df6476f5633fea30b86ba3ffff6,file=Module.kt]

DIの設定をするところです。`bind`メソッドで型とインスタンスを紐付けます。scope毎にModule (ApplicationModule, ActivityModule, FragmentModule, ViewModelModule) を作っています。

### SplashActivity.kt
[gist:id=f3348df6476f5633fea30b86ba3ffff6,SplashActivity.kt]

ActivityでInjectしてみます。 @Inject を使うところはDaggerと一緒です。

onCreate の前で scope に ActivityModule インストールしています。これでActivityからActivityModuleの中でbindしたインスタンスを Inject 出来るようになります。さらに、MainApplicationModuleの中でbindしたインスタンスもInjectできます。それは、ツリー構造でApplicationと紐付いているからです。(後述)

onCreate の後で `Toohpick.inject` することで @Inject が書かれたメンバ変数にインスタンスが代入されます。


### HomeFragment.kt
[gist:id=f3348df6476f5633fea30b86ba3ffff6,file=HomeFragment.kt]

### HomeViewModel.kt
[gist:id=f3348df6476f5633fea30b86ba3ffff6,HomeViewModel.kt]

### Scope
openScopes の引数は可変長です。ここにツリー構造になるようにインスタンスを指定します。MainActivityでは (MainApplication, SplashActivity) を指定しました。これは最初で紹介したツリーだと
```text
     MainApplication 
         /   \
        /   OtherActivity...
       /            
SplashActivity
```
こういう感じになります。

HomeFragmentでは (MainApplication, SplashActivity, HomeFragment) を指定しました。
```text
   MainApplication
         /   \
        /   OtherActivity...
       /            
 SplashActivity
    /   \
   /   OtherFragment...
  /
HomeFragment
```
この時のHomeFragment では MainApplication と SplashActivity がインストールした Module を利用することができます。具体的には ModelRepository, Navigator, DialogDelegation を Injectする事ができます。

（サンプルではなにもbindしてないけど、FragmentModuleがbindしたインスタンスも利用できます。）

（ModelRepository, Navigator, DialogDelegation は架空のクラスです）

## まとめ
ToothpickでDIできたはずです。できたよね。うんよかった。

感想としてはDagger2よりシンプルで使いやすいです。もっと依存関係が複雑になるとどうなるかわかりませんが、複雑になったらDagger2は僕には辛いですし、複雑にならないように頑張りたいです。

