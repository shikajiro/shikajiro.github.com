---
layout: single
title: 犬のためのアプリを作っている
date: 2018-12-16 14:00
slug: flutter_dogs
---

ZOZOテクノロジーズの愉快なエンジニア AdventCalendar その2、16日目です。12月も半分過ぎました。やばいですね。

ZOZOのAdventCalendarですが完全にZOZOとは関係ない、個人的趣味な記事になります。

 *いぬをささえるぎじゅつ* と題して、趣味レベルでコツコツ作っている犬のアプリについて書きます。

## なぜ いぬをささえるぎじゅつ なのか

うちの愛犬のもなかです。 ウェルシュコーギーペンブローク♀推定8歳 [instagram](https://www.instagram.com/monakoala/)

![](https://pbs.twimg.com/profile_images/976974808213733376/XL-QI99V_400x400.jpg)

めちゃくちゃ可愛いですね。我が家のアイドルです。

子供の頃から犬🐶が好きで、大人になったらたくさん犬を飼おうと思ってました。思ったとおりの大人には成れてないですが、最愛の犬と暮らすことができるようになりました。
もなかと暮らすようになって、犬を取り巻く人間社会が見えてくるようになりました。
なにか自分でも犬達の為になることができるんじゃないかと考えました。
僕はIT技術にしか取り柄が無いので、この力を持って彼らの力になろうと思います。


## 愛犬の健康を管理する

![](/images/45550733_163527401272115_1647419605745716597_n.jpg)

もなかは3年前に我が家の一員になりましたが、その時から尿結石を患ってました。
食べ物はPh値を調整するドックフードにし、水は軟水を徹底し、しっこの回数や量なんかをしばらく監視してました。

石は手術で取り、以後尿結石はできてません。しかし、ノミダニ予防、フィラリア予防、狂犬病予防など、健康な犬でも日々予防するものはあります。
最近では膀胱炎にもなりました。薬を飲むと体に負担がかかり、数週間つらい思いをしていました。

そんな自分が欲しかった *愛犬の健康を管理する* アプリを作っています。
王道ですが、愛犬の日々の食事や薬、トイレなどをログするものです。

画面例 愛犬を登録する画面

![開発中の画面](/images/friendog.png)

### 使っている技術
- Flutter 
- Firebase
- rx

紆余曲折を経て、今は流行りの Flutter + Firebaseで作っています。

当初Android向けにKotlinで作ってましたが、iOSもいずれ出したい気持ちでしたし、Flutterの人気が出てきたので思い切って乗り換えました。
サーバーサイドも最初は Google App Engine + Flask で作ってましたが、開発に結構時間がかかってたのと、FirebaseがFlutterとの相性も良かったので乗り換えました。

こちらは最近書いた「複数の入力した内容でOKをクリックしたすると、画像はストレージに保存して、テキストデータはデータベースに保存する」という処理です。
rxのcombineLatestを使ってます。
まだdartのstreamとrxとの使い分けができてませんが、とりあえず動きます。
```dart
Observable postListen() => Observable.combineLatest6(
      dogName.stream,
      dogImage.stream,
      dogSize.stream,
      dogType.stream,
      dogGender.stream,
      post.stream, (name, File image, size, type, gender, click) async {
    // すべての項目を入力してclickするとここに処理が流れてくる
    print("postListen image $image");
    //画像をアップロードする
    final uploadTask = FirebaseStorage.instance
        .ref()
        .child('images')
        .child('dogs')
        .child("${Uuid().v1()}.png")
        .putFile(
          image,
          StorageMetadata(
            contentLanguage: 'en',
            customMetadata: {'activity': 'test'},
          ),
        );
    //アップロードが終わるまで待つ
    final event = await uploadTask.onComplete;
    //参照用URLを取得する
    final url = await event.ref.getDownloadURL();
    print("image url:$url");
    //データベースに保存する
    await Firestore.instance.collection('dogs').document().setData({
      'image': url,
      'name': name,
      'dogGenderId': gender.toJson(),
      'dogType': type.toJson(),
      'dogSize': size.toJson(),
    });
  });
```

作り直しているので進捗はまだまだですが、来年の中頃にはリリースしたいです。

## 迷子の犬をみんなで探す

![](/images/o0450046413361865330.jpg)

もなかは保健所に居ました。保健所は収容してから２週間ほど経っても飼い主が現れない場合は、殺処分します。(行政によって異なります)
期限日ギリギリに引き出してくれたのが 福岡コーギーレスキューさんです。僕たち家族にもなかを紹介してもらい、僕たちの家族の一員になりました。

動物愛護センターのHPを見ると、収容されている犬猫以外にも「迷子になっている犬猫」のページがありました。
誰も助けに来ない犬猫も居れば、飼い主が何年も探している犬猫が居ます。

犬猫と飼い主を不幸を減らすために、迷子になった犬猫をすぐ見つけることはできないだろうか？
一人で探すには限界があるので、ソーシャルの力を使って網の目で探すのがいいんじゃないだろうか？
そんなテーマで作っているのが PetSearcher です。
近隣で犬猫が迷子になると利用者にpush通知が送られるので、飼い主と地域の人みんなで一緒に探そうというものです。

ロゴ

![](/images/petsearcher.png)

迷子になった犬の目撃情報などの情報を集めるページ
![](/images/petsearch_host.png)

### 使っている技術
- vue.js 
- firebase 
- BeautifulSoup 
- FBMessenger

firebase は vue.js とも相性がいいです。firebaseのデータが複雑なプログラミングなしで画面に反映されます。
作成したhtmlは firebase で hosting しているので低コストで運用できそうです。
特定サイトからのスクレイピングには BeautifulSoup を使ってます。
迷子犬の新着情報はFBMessengerを使っています。

## まとめ
技術紹介というより、やってることの紹介な記事になりました。