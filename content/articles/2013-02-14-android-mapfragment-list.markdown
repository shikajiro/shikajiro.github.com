---
layout: single
title: MapFragmentをTabの要素として表示したい
date: 2013-02-14 23:04
comments: true
Category: Android
Authors: shikajiro
slug: android-mapfragment-list
---
しかだよ。
MapFragmentをTabの一つとして表示したいんだけど、色々問題が出てきつつ解決できたのでメモ。

## 前提条件

+ Android 4.x
+ TabはActionBarを使用
+ Mapはgoogle-play-servicesを使用

とりあえずActionBarにタブを設定するソースコードはこんな感じ。
{% highlight java %}

@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);

    mActionBar = getActionBar();
    mActionBar.setNavigationMode(ActionBar.NAVIGATION_MODE_TABS);
    TabListener tabListener = new ActionBar.TabListener() {
        @Override
        public void onTabSelected(Tab tab, FragmentTransaction ft) {
            if (tab.getText().equals("Map")) {
                if (mMapFragment == null) {
                    mMapFragment = MapFragment.newInstance();
                    ft.add(android.R.id.content, mMapFragment, "map");
                } else {
                    ft.attach(mMapFragment);
                }

            } else {
                if (mListFragment == null) {
                    mListFragment = CustomerListFragment.newInstance();
                    ft.add(android.R.id.content, mListFragment, "list");
                } else {
                    ft.attach(mListFragment);
                }
            }
        }

        @Override
        public void onTabReselected(Tab tab, FragmentTransaction ft) {}

        @Override
        public void onTabUnselected(Tab tab, FragmentTransaction ft) {
            if (tab.getText().equals("Map")) {
                if (mMapFragment != null) {
                    ft.detach(mMapFragment);
                }
            }else{
                if (mListFragment != null) {
                    ft.detach(mListFragment);
                }
            }
        }
    };

    mActionBar.addTab(mActionBar.newTab().setText("List")
            .setTabListener(tabListener));
    mActionBar.addTab(mActionBar.newTab().setText("Map")
            .setTabListener(tabListener));
}
{% endhighlight %}

するときっとこんな画面になる。Manifestの設定は省く。

![](/images/android/device-2013-02-15-010618.png)
![](/images/android/device-2013-02-15-010640.png)

リスト画面が初期に表示され、まだインスタンス化されていないマップ画面が控えている。

## マップに初期設定を行いたいけどできない
上記の参考画像の様に
タブを選択してマップ画面に移ったら、*初期表示で*自分の位置を表示する設定とかマーカーピンを立てたりしたい。

ここで問題が出てくる。
MapFragment.newInstanceした時点ではGoogleMapのインスタンスは生成されていないのだ。なので、以下の様なnewInstanceした直後に設定はできない。

{% highlight java %}

    mMapFragment = MapFragment.newInstance();
    mMap = mMapFragment.getMap();
    //mMapはnullなのでぬるぽ
    mMap.setMyLocationEnabled(true);

{% endhighlight %}

GoogleMapのインスタンスが生成されるのは、MapFragmentのonCreate or onCreateActivityが呼ばれた後らしい。（要出典）

## 解決策1 Activityのライフサイクルと同期する    
GoogleMapのサンプルコードでは、呼び出し元のActivityとMapFragmentを結びつけて、Activity#onResumeのタイミングでGoogleMapのインスタンスを取得していた。

サンプルコードはこんな感じ。
{% highlight java %}

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        //layoutの中でMapFragmentを定義してる前提
        setContentView(R.layout.activity_main);
    }

    @Override
    protected void onResume() {
        super.onResume();
        mMap = mMapFragment.getMap();
    }

{% endhighlight %}

だがこれだと、初期表示されないタブの中のMapFragmentはActivityに紐付けできない。Activity#onResumeではMapFragmentのonCreateが終わった後を検出できない。

## 解決策2 MapFragmentのオーバーライド
したらなんとかなるかなと思ったけど、以下の理由で出来なかった。

- MapFragmentはソースコードが公開されてないので、どう実装したらよいものやら。
- MapFragment#newInstanceの中で new MapFragment(); を呼んでMapFragmentインスタンスを生成しているっぽいので、オーバーライドしても拡張したExtendMapFragmentクラスのインスタンスを扱えない。（または、MapFragmentのnewInstanceはポリモーフィズムになってない。）


ソースコード見れないのがやっぱり辛いね・・・。動いたとしても、バージョン変わって動く保証もないし。

## 解決策3 タブの初期化のタイミングをずらす
結局どうしたかというと、タブの初期表示をMapFragmentにしておいて、表示する寸前に当初のFragmentに挿し替えるという姑息な技を使った。

{% highlight java %}
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        //省略

        mActionBar.addTab(mActionBar.newTab().setText("List")
                .setTabListener(tabListener));
        mActionBar.addTab(mActionBar.newTab().setText("Map")
                .setTabListener(tabListener));
        //onCreateの中でMapFragmentのタグを指定しておく。
        mActionBar.setSelectedNavigationItem(1);
   }

    @Override
    protected void onResume() {
        super.onResume();
        setUpMapIfNeeded();
        //画面に表示される前にタブを戻しておく
        mActionBar.setSelectedNavigationItem(0);
    }
{% endhighlight %}

うん。無理矢理だね。とりあえず動いたからよしとしよう・・・。
