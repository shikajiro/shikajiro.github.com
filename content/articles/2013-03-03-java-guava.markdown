---
layout: single
title: Google製Javaライブラリ Guavaを使ってみた。
date: 2013-03-03 19:43
comments: true
Category: Java
Authors: shikajiro
slug: java-guava
---
<center>
<img src="/images/indian_guava.jpg">
</center>

しかだよ。Guavaってライブラリが良いってインターネットに書いてたので調べてみたよ。
サンプルソースのほとんどは本家からコピペしたよ。

[guava-libraries - Guava: Google Core Libraries for Java 1.6+ - Google Project Hosting](https://code.google.com/p/guava-libraries/)

##Basic

### Using/avoiding null
nullぽを避けるための仕組み
{% highlight java %}
    Optional<Integer> possible = Optional.of(5);
    possible.isPresent(); // returns true
    possible.get(); // returns 5
{% endhighlight %}

###Preconditions
引数の値チェックなど、前提条件をチェックする仕組み。assertとかに似てると思う。
条件がfalseだと対応するExceptionがスローされる。

###Ordering
Comparatorをスマートにしたやつ。Comparatorはめんどいよね・・・。

{% highlight java %}
    Ordering<String> byLengthOrdering = new Ordering<String>() {
         public int compare(String left, String right) {
           return Ints.compare(left.length(), right.length());
         }
       };

    if (Ordering.from(comparator).reverse().isOrdered(list)) { ... }
{% endhighlight %}
あら素敵。

###Object methods
なにやら便利メソッド。
####equals
nullぽを気にせずnullチェックができるよ。

{% highlight java %}
    Objects.equal("a", "a"); // returns true
    Objects.equal(null, "a"); // returns false
    Objects.equal("a", null); // returns false
    Objects.equal(null, null); // returns true
{% endhighlight %}

####hashCode
安全なハッシュが簡単に作れます。
{% highlight java %}
    Objects.hashCode(Object...)
{% endhighlight %}

####toString
toStringメソッドの構築・保守が楽になるよ。
{% highlight java %}
@override public String toString(){
        // Returns "ClassName{x=1}"
        return Objects.toStringHelper(this)
           .add("x", this.x)//変数名とその値
           .toString();
        //or
        // Returns "MyObject{x=1}"
        return Objects.toStringHelper("MyObject")
           .add("x", 1)
           .toString();
}
{% endhighlight %}
eclipseのジェネレーターでもいいと思うけど。

####compare/compareTo
ComparisonChainを使うと、連続した比較が簡単に。
{% highlight java %}
   public int compareTo(Foo that) {
     return ComparisonChain.start()
         .compare(this.aString, that.aString)
         .compare(this.anInt, that.anInt)
         .compare(this.anEnum, that.anEnum, Ordering.natural().nullsLast())
         .result();
   }
{% endhighlight %}

###Throwables
case文のように、連鎖したtry catch文が書けるようになります。
例えば、以下の処理で IKnowWhatToDoWithThisException が発生した場合、1 2 3 の順番で処理が発生します。
{% highlight java %}
    try {
        // 1
        someMethodThatCouldThrowAnything();
    } catch (IKnowWhatToDoWithThisException e) {
        // 2
        handle(e);
    } catch (Throwable t) {
        // 3
        Throwables.propagateIfInstanceOf(t, IOException.class);
        Throwables.propagateIfInstanceOf(t, SQLException.class);
        throw Throwables.propagate(t);
   }
{% endhighlight %}
java7だと簡潔に書けるけど、Androidとかはまだ使えないからありがたいね。

##Collections
###Immutable collections
不変のコレクションを作りたい時に扱う。防御的コピー(defensive copy)したい時とかに便利。

{% highlight java %}
    public static final ImmutableSet<String> COLOR_NAMES = ImmutableSet.of(
      "red",
      "orange",
      "yellow",
      "green",
      "blue",
      "purple");

    class Foo {
      Set<Bar> bars;
      Foo(Set<Bar> bars) {
        this.bars = ImmutableSet.copyOf(bars); // defensive copy!
      }
    }
{% endhighlight %}
### New Collection Types
コレクション型の追加
#### Multiset
例えば、要素の中に特定の単語がいくつ含まれるかを検出できる。
{% highlight java %}
    Multiset<String> wordsMultiset = HashMultiset.create();
    wordsMultiset.addAll(words);
    wordsMultiset.count(String);
{% endhighlight %}
#### Multimap
1つのkeyに対して、valueがたくさんaddできます。
{% highlight java %}
    Set<Person> aliceChildren = childrenMultimap.get(alice);
    aliceChildren.clear();
    aliceChildren.add(bob);
    aliceChildren.add(carol);
{% endhighlight %}

#### BiMap
BindingMapの略かな？Mapに保持する値と取り出して利用している値で整合性が保ちやすくする仕組み。
mapのkeyに値が紐付いているのにputした場合、IllegalArgumentExceptionが発生する。
削除する時はforcePutメソッドを利用する。
※よく分かってない

#### Table
行と列の構造を持ったコレクション。２次元配列とが違い、行からも列からもアクセスできる。
#### ClassToInstanceMap
クラスの型をキーにする、変わったMapです。（使い道が思い浮かばない）

#### RangeSet / RangeMap
範囲のコレクション。  
java6必須。GWTは非対応。

###CollectionUtilitiesExplained
Collection操作のユーティリティ
#### Static Constructors
##### 鬱陶しいジェネリクスの解消
{% highlight java %}
    List<TypeThatsTooLongForItsOwnGood> list = new ArrayList<TypeThatsTooLongForItsOwnGood>();
{% endhighlight %}

{% highlight java %}
    List<TypeThatsTooLongForItsOwnGood> list = Lists.newArrayList();
    Map<KeyType, LongishValueType> map = Maps.newLinkedHashMap();
{% endhighlight %}

##### 初期化の簡潔化
配列の初期化みたいに自由に追加できる。
{% highlight java %}
    Set<Type> copySet = Sets.newHashSet(elements);
    List<String> theseElements = Lists.newArrayList("alpha", "beta", "gamma");
{% endhighlight %}

#### Iterables
guavaはCollectionよりIterableなのが好きらしい。
{% highlight java %}
  Iterable<Integer> concatenated = Iterables.concat(
    Ints.asList(1, 2, 3),
    Ints.asList(4, 5, 6));
  // concatenated has elements 1, 2, 3, 4, 5, 6

  String lastAdded = Iterables.getLast(myLinkedHashSet);

  String theElement = Iterables.getOnlyElement(thisSetIsDefinitelyASingleton);
    // if this set isn't a singleton, something is wrong!
{% endhighlight %}

その他、Collectionの便利クラスが色々。

### Extension Utilities
#### Forwarding Decorators
デザインパターンの decorator pattern が簡単に実装できる仕組み。
以下のサンプルだと addにlogの処理をdecorateしている。

{% highlight java %}
  class AddLoggingList<E> extends ForwardingList<E> {
    final List<E> delegate; // backing list
    @Override protected List<E> delegate() {
      return delegate;
    }
    @Override public void add(int index, E elem) {
      log(index, elem);
      super.add(index, elem);
    }
    @Override public boolean add(E elem) {
      return standardAdd(elem); // implements in terms of add(int, E)
    }
    @Override public boolean addAll(Collection<? extends E> c) {
      return standardAddAll(c); // implements in terms of add
    }
  }
{% endhighlight %}

#### PeekingIterator
Iteratorで次の要素を見たいけどindexを進めたくない時に使うpeekメソッドが拡張されている。
{% highlight java%}
  List<E> result = Lists.newArrayList();
  PeekingIterator<E> iter = Iterators.peekingIterator(source.iterator());
  while (iter.hasNext()) {
    E current = iter.next();
    while (iter.hasNext() && iter.peek().equals(current)) {
      // skip this duplicate element
      iter.next();
    }
    result.add(current);
  }
{% endhighlight %}

#### AbstractIterator
独自のイテレーターを楽に実装する。
{% highlight java%}
  public static Iterator<String> skipNulls(final Iterator<String> in) {
    return new AbstractIterator<String>() {
      protected String computeNext() {
        while (in.hasNext()) {
          String s = in.next();
          if (s != null) {
            return s;
          }
        }
        return endOfData();
      }
    };
  }
{% endhighlight %}

## Caches
いきなりサンプルである。
{% highlight java %}
LoadingCache<Key, Graph> graphs = CacheBuilder.newBuilder()
       .maximumSize(1000)
       .expireAfterWrite(10, TimeUnit.MINUTES)
       .removalListener(MY_LISTENER)
       .build(
           new CacheLoader<Key, Graph>() {
             public Graph load(Key key) throws AnyException {
               return createExpensiveGraph(key);
             }
           });
{% endhighlight %}

### Applicability

### Population

### Eviction

### Features

### Interruption
