# Python Boot Camp for　筑波

## この研修の開催目的

* 初学者のが、Pythonの基礎習得を短時間ででき、かつ自走できるまでの内容を習得する

## ゼロから始めるPython講座との切り分けについて

### ゼロから始めるPython講座

**pythonの導入**が目的で、ゼロからPythonを学び、Pythonがどんなところで利用されているのか学び、そしてプログラミングを経験する研修。

### Python Boot Camp for 筑波

**pythonの基礎**を習得することが目的。

## この問題の対象者

* Pythonこれから勉強してみたい人
* 主にME向けの研修
* あんまりPythonを自宅で勉強する気が起きない

## この研修のクリア条件

* 問題を20~50問ほど解く
* 解いた問題をアンケートに記入して提出して研修達成
* 6時間の研修でしっかりプログラムを書くことを第一に優先するため、解いた問題数はさほど重要ではない。

## Pythonのレベル感の指標

Python研修が複数立ち上がるので、指標としてレベルテーブルを用意する。これをもとに研修を立案・企画する。  
自分の考える、どこまで習得した人が、どのレベルなのかという、Pythonのレベル感をまとめる。(かなり難しい)  
ただし、pure Pythonに限る。  

| レベル | 説明                                          | EC内での人数的な割合 |
| :----- | :------------------------------------------ | :---------------- |
| 初歩    | プログラミング未経験 or Pythonに触れたことがない  | 70%              |
| 初心者  | Pythonの基本構文がわかる<br>エラーに果敢に立ち向かえる<br>公式ドキュメントが読めて理解できる<br>自分の作りたいものがなんとなく作れる | 25% |
| 中級者  | returnとyieldの使い分けができる<br>スタックフレーム・メタクラス・<br>特殊メソッドを理解している<br>@propertyが何なのか理解できている | 5% |
| 上級者・プロ  | pythonの構文木変換が理解できている<br>APIリファレンスの記述から実装ができる<br>他のシステムと組み合わせた時、Pythonを正しく最適化できる | ?? |

上記の表から、上級者や中級者を対象とした研修はやる必要はない。

## ディレクトリの構成と構築環境について

* 仮想環境 : `venv`
* pythonバージョン : `>3.8`
* OS : `Windows` / `MacOS` / `Unix系OS`
* ライブラリ : `pyproject.toml`に記載

```bash
(対称ディレクトリ)
| -- Doc
| -- source
| -- poetry.lock
| -- pyproject.toml
| -- README.md
```

> .gitignore記載のファイルは記載しない

## Python Boot Campの内容

Python問題一覧は、以下の通りです。

| No   | 問題  | レベル | ファイル名 |
| :--: | :-- | :----: | :------: |
| 01 | Pythonインタプリタの復習 | 初歩 | training00.ipnb |
| 02 | Jupyter Notebookの使い方 | 初歩 | training00.ipnb |
| 03 | 問題の進め方と答え合わせについて | 初歩 | training00.ipnb |
| 04 | 必要なパッケージについてとrequirements.txtについて | 初歩 | training00.ipnb |
| 05 | 仮想環境の切り分け方とおすすめの環境構築 | 初歩 | training00.ipnb |
| 06 | Pythonの学習とロードマップ | 初歩 | training00.ipnb |
| 07 | Python x 仕事のすすめ | 初歩 | training00.ipnb |
| 1  | 値と変数 | 初歩 | training01.ipnb |
| 2  | 変数と型 | 初歩 | training01.ipnb |
| 3  | 引数の数で大きく挙動が変わるtype()関数を知る | 初歩 | training01.ipnb |
| 4  | 数値と演算 | 初歩 | training01.ipnb |
| 5  | print()関数 | 初歩 | training01.ipnb |
| 6  | 演算子の挙動を変えてみる | 中級 | training01.ipnb |
| 7  | 整数とキャッシュ | 中級 | training01.ipnb |
| 8  | 文字列と演算 | 初歩 | training01.ipnb |  
| 9  | 繰り返し文字 | 初歩 | training01.ipnb |
| 10 | 文字列の抜き出し | 初歩 | training01.ipnb |  
| 11 | f-strings | 初歩 | training01.ipnb |
| 12 | f-stringをシュミレートする | 中級 | training01.ipnb |  
| 13 | 条件文 if文の使い方 | 初歩 | training01.ipnb |
| 14 | if ~ elif ~ elseの使い方について | 初歩 | training01.ipnb |  
| 15 | 値と比較演算子 | 初歩 | training01.ipnb |
| 16 | 値と比較演算子 | 初歩 | training01.ipnb |
| 17 | 三項演算子を使う | 初級 | training01.ipnb |
| 18 | if文の練習問題 | 初歩 | training01.ipnb |
| 19 | for文の基礎：処理を繰り返す | 初歩 | training01.ipnb |
| 20 | for文のネスト | 初歩 | training01.ipnb |
| 21 | for文とリスト | 初歩 | training01.ipnb |
| 22 | for in ~ else 文 | 初歩 | training01.ipnb |
| 23 | FizzBuzz問題に挑戦 | 初歩 | training01.ipnb |
| 24 | ストロボグラム数問題に挑戦 | 初歩 | training01.ipnb |
| 25 | コンテナ型 リストについて | 初歩 | training02.ipnb |
| 26 | スネーク表記に挑戦 | 中級 | training02.ipnb |
| 27 | リストの参照 | 初歩 | training02.ipnb |
| 28 | リストのスライス | 初歩 | training02.ipnb |
| 29 | 多重リスト | 初歩 | training02.ipnb |
| 30 | リストの要素を変更する | 初歩 | training02.ipnb |
| 31 | 重複を削除する その1 | 初級 | training02.ipnb |
| 32 | 重複を削除する その2 | 初級 | training02.ipnb |
| 33 | リスト内包表記を使いこなす | 初級 | training02.ipnb |
| 34 | Pythonらしさは尊重するべき 他言語のベストプラクティスは通用しない時もある | 初級 | training02.ipnb |
| 35 | FizzBuzz問題を１行で実行する | 初級 | training02.ipnb |
| 36 | リストとループカウンタを同時に返す | 初級 | training02.ipnb |
| 37 | 複数のリストを同時にループする | 初級 | training02.ipnb |
| 38 | 数字の出現回数をカウントする | 初級 | training02.ipnb |
| 39 | リストの並び替え | 初歩 | training02.ipnb |
| 40 | リストの複製と注意点 | 初級 | training02.ipnb |
| 41 | appendとリスト内包表記とメソッドの再利用　| 中級 | training02.ipnb |
| 42 | コンテナ型 タプルについて | 初歩 | training02.ipnb |
| 43 | タプルの使い方を知る | 初歩 | training02.ipnb |
| 44 | 休憩：コメントは何を書く？ | 初歩 | training02.ipnb |
| 45 | コンテナ型 辞書について | 初歩 | training02.ipnb |
| 46 | 辞書の値を追加する | 初歩 | training02.ipnb |
| 47 | 辞書の値を削除する | 初歩 | training02.ipnb |
| 48 | 辞書に含まれるキーと値を取得する | 初級 | training02.ipnb |
| 49 | 辞書に値が入っているか調べる| 初級 | training02.ipnb |
| 50 | 辞書内包表記 | 初級 | training02.ipnb |
| 51 | キーが存在しない場合にkeyと値を追加する | 初級 | training02.ipnb |
| 52 | コンテナ型 setについて | 初級 | training02.ipnb |
| 53 | setの要素を変更する | 初級 | training02.ipnb |
| 54 | そのデータは本当に辞書で保持しないとダメ? | 初級 | training02.ipnb |
| 55 | 辞書に存在しないキーを一度に追加する　| 中級 | training02.ipnb |  
| 56 | ユーザー定義関数を使いたい | 初級 | training03.ipnb |
| 57 | 腕試し問題 シーザー暗号 | 初級 | training03.ipnb |
| 58 | ユーザー定義関数と位置引数とキーワード引数 | 初級 | training03.ipnb |
| 59 | ユーザー定義関数と可変長引数 | 初級 | training03.ipnb |
| 60 | デフオルト引数 | 初級 | training03.ipnb | 
| 61 | デフオルト引数の注意点 | 初級 | training03.ipnb |
| 62 | 独自オブジェクトを使う | 初級 | training03.ipnb |
| 63 | クラスの利用例 | 初級 | training03.ipnb |
| 64 | クラスの利用例 | 初級 | training03.ipnb |
| 65 | デコレータを扱う準備：高階関数について | 初級 | training03.ipnb |
| 66 | デコレータを扱う | 中級 | training03.ipnb |
| 67 | デコレータを引数や戻り値に対応させる | 中級 | training03.ipnb |
| 68 | ベンチマークツール作成：実行時間の計測 | 中級 | training03.ipnb |
| 69 | デコレータとキャッシュについて | 中級 |　training03.ipnb |
| 70 | クロージャを扱う | 中級 |　training03.ipnb |
| 71 | クロージャの例題 | 中級 |　training03.ipnb |
| 72 | 初心者でもクロージャ・デコレータとか高度な関数を学習する意味について | 中級 |　training03.ipnb |
| 73 | クロージャーと再帰関数と高速化 | 中級 | training04.ipnb |
| 74 | lambdaを扱う | 初級 |　training03.ipnb |
| 75 | ソート関数をlambdaで作成する | 初級 |　training03.ipnb |
| 76 | lambdaを使って辞書の値で並び替え | 初級 |　training03.ipnb |
| 77 | ジェネレータを扱う | 中級 |　training03.ipnb |
| 78 | ジェネレータを使って単語当てクイズに挑戦 | 中級 |　training03.ipnb |
| 79 | 例外処理について | 初級 |　training03.ipnb |
| 80 | エラーメッセージの見方 | 初級 |　training03.ipnb |
| 81 | 独自例外を実装する | 初級 |　training03.ipnb |
| 82 | トレースバックを間引く | 初級 |　training03.ipnb |
| 83 | まとめ: パスカルのトライアングルを作ろう！ | 初級 |　training03.ipnb |
| 84 | ファイルを読み込む | 初級 | training04.ipnb |
| 85 | ファイルへ書き込む | 初級 | training04.ipnb |
| 86 | ファイルをwith構文を使って操作する | 初級 | training04.ipnb |
| 87 | with構文の理解とベンチマークツールの改良 | 中級 |　training04.ipnb |
| 88 | CSVを読み込む | 初級 | training04.ipnb |
| 89 | CSVを編集して書き込む方法 | 初級 | training04.ipnb |
| 90 | サイズが大きいCSVファイルを読み取るコツ | 初級 | training04.ipnb |
| 91 | pandasを使う | 初級 | training04.ipnb |
| 92 | Seriesを生成したい | 初級 | training04.ipnb |
| 93 | Seriesのデータにアクセスしたい | 初級 | training04.ipnb |
| 94 | DataFrameを生成したい | 初級 | training04.ipnb |
| 95 | pandasを使ってCSVを読み書きしたい | 初級 | training04.ipnb |
| 96 | DataFrameから基礎統計量を求めたい | 初級 | training04.ipnb |
| 97 | DataFrameから列データを取得したい | 初級 | training04.ipnb |
| 98 | DataFrameから行データを取得したい | 初級 | training04.ipnb |
| 99 | DataFrameの行・列を指定してデータを取得したい | 初級 | training04.ipnb |
| 100 | DataFrameで欠損値を扱いたい | 初級 | training04.ipnb |
| 101 | DataFrameの値を置換したい | 初級 | training04.ipnb |
| 102 | DataFrameをフィルタリングしたい | 初級 | training04.ipnb |
| 103 | DataFrameをGroupByで集計したい | 初級 | training04.ipnb |
| 104 | DataFrameをソートしたい | 初級 | training04.ipnb |
| 105 | Excelデータを読み込んでみよう | 初級 | training04.ipnb |
| 106 | カラムを抽出してみよう | 初級 | training04.ipnb |
| 107 | 全シートのデータを読み込んでみよう | 初級 | training04.ipnb |
| 108 | データの値を計算で修正してみよう | 初級 | training04.ipnb |
| 109 | 必要なカラムだけに絞り込もう | 初級 | training04.ipnb |
| 110 | 縦持ちのデータを作成しよう | 初級 | training04.ipnb |
| 111 | 縦持ちのデータを整形しよう | 初級 | training04.ipnb |
| 112 | 発電実績データを加工しよう | 初級 | training04.ipnb |
| 113 | 可視化用データを仕上げよう | 初級 | training04.ipnb |
| 114 | データの分布をヒストグラムで可視化しよう | 初級 | training04.ipnb |
| 115 | データの分布を箱ひげ図で可視化しよう | 初級 | training04.ipnb |
| 116 | 最近の発電量を可視化してみよう | 初級 | training04.ipnb |
| 117 | 電力の時系列変化を可視化してみよう | 初級 | training04.ipnb |
| 118 | 電力の割合を可視化してみよう | 初級 | training04.ipnb |
| 119 | 電力の多い都道府県を比較してみよう | 初級 | training04.ipnb |
| 120 | Excelからpythonのコードを自動生成する:準備 | 初級 | training04.ipnb |
| 121 | Excelからpythonのコードを自動生成する:Excelを読み込む | 初級 | training04.ipnb |
| 122 | Excelからpythonのコードを自動生成する:グラフ化 | 初級 | training04.ipnb |
| 123 | Excelからpythonのコードを自動生成する: 値を変更する | 初級 | training04.ipnb |
| 124 | Excelからpythonのコードを自動生成する:ピポットテーブルを作成する | 初級 | training04.ipnb |
| 125 | モジュールの読み込みとimport文 | 初級 | training05.ipnb |
| 126 | モジュールとパッケージと\_\_init\_\_.pyについて | 初級 | training05.ipnb |
| 127 | \_\_init\_\_.py 不要説と正しい理解 | 初級 | training05.ipnb |
| 128 | \_\_name\_\_= \_\_main\_\_ とは | 初級 | training05.ipnb |
| 129 | Wordを読み込んでみよう | 初級 | training05.ipnb |
| 130 | PythonでWordを処理してみよう | 初級 | training05.ipnb |
| 131 | PDFデータを読み込んでみよう | 初級 | training05.ipnb |
| 132 | PDFデータを結合・分割してみよう | 初級 | training05.ipnb |
| 133 | 画像データを読み込んでみよう | 初級 | training05.ipnb |
| 134 | 画像データを処理してみよう | 初級 | training05.ipnb |
| 135 | PEP8：コーディング規約を知る | 初級 | training06.ipnb |
| 136 | PEP8のlinterを導入する flake8 | 初級 | training06.ipnb |
| 137 | PEP8のformaterを導入する black | 初級 | training06.ipnb |
| 138 | pipの使い方 | 初級 | training06.ipnb |
| 139 | 欲しいパッケージ検索と良し悪しの判断 | 初級 | training06.ipnb |
| 140 | pipが失敗する原因はプロキシ? | 初級 | training06.ipnb |
| 141 | Pythonの基礎のキ 仮想環境は必ず作る | 初級 | training06.ipnb |
| 142 | vnevを使って仮想環境を作成する | 初級 | training06.ipnb |
| 143 | pytestでテストコードを書くなぜテストが必要か | 初級 | training06.ipnb |
| 144 | pytestとテストコードのあれこれ | 初級 | training06.ipnb |
| 145 | pytestのフィクスチャの一歩 | 初級 | training06.ipnb |
| 146 | ドキュメントは残す | 初級 | training06.ipnb |
| 147 | Markdownでドキュメントを書く1 | 初級 | training06.ipnb |
| 148 | Markdownでドキュメントを書く2 | 初級 | training06.ipnb |
| 149 | pythonの型ヒントの書き方: なぜ型が必要か | 初級 | training06.ipnb |
| 150 | 品質の高いコードを目指して: typingモジュール | 初級 | training06.ipnb |
| 151 | 品質の高いコードを目指して: pydanticモジュール | 初級 | training06.ipnb |
| 152 | ファイルパスを扱う | 初級 | training06.ipnb |
| 153 | ファイルパスを扱う: osモジュール | 初級 | training06.ipnb |
| 154 | ファイルパスを扱う: globモジュール | 初級 | training06.ipnb |
| 155 | ファイルパスを扱う: pathlibモジュール | 初級 | training06.ipnb |
| 156 | 1つのPCで複数のpythonバージョンを扱う | 初級 | training06.ipnb |

## 参考文献

### 書籍

* Pythonチュートリアル 第4版　Guido Van Rossum オライリージャパン 2021/2/1
* Pythonエンジニア育成推進協会監修 Python実践 鈴木たかのり 寺田 学 技術評論社 2022/1/19
* Pythonエンジニア育成推進協会監修 Python 3スキルアップ教科書 辻 真吾 技術評論社 2019/10/7
* はじめてのPythonエンジニア入門編 python3対応 松浦健一郎 秀和システム 2019年6月6日発行
* 新・標準プログラマーズライブラリ 試してわかる Python[基礎]入門 谷尻しおり 技術評論社 2020年12月4日発行
* Python実践データ分析100本ノック 下山輝昌 秀和システム 2019/10/10
* Python実践データ加工/可視化100本ノック 下山輝昌 秀和システム 2021/7/31
* interfac2021年3月号 CQ出版 2021/1/25
* interfac2021年6月号 CQ出版 2021/4/24
* interface 2022年9月号 CQ出版 2022/7/25
* Pythonデータ分析／機械学習のための基本コーディング！ pandasライブラリ活用入門 impress top gearシリーズ Daniel Y. Chen インプレス 2019/2/22
* Pythonコードレシピ集 黒住 敬之 技術評論社 2021/1/21
* Effective Python 第2版 ―Pythonプログラムを改良する90項目 Brett Slatkin オライリージャパン 2020/7/16
* オブジェクト指向でなぜつくるのか 第３版　知っておきたいOOP、設計、アジャイル開発の基礎知識 平澤章 日経BP 2021/4/15
* 独学プログラマー Python言語の基本から仕事のやり方まで Cory Althoff 日経BP 2018/2/24
* 独習Python 山田 祥寛 翔泳社 2020/6/22
* Python ゼロからはじめるプログラミング 三谷純 翔泳社 2021/5/24
* プロフェッショナルPython ソフトウェアデザインの原則と実践 impress top gearシリーズ 武舎 広幸 インプレス 2021/11/16
* Python基礎＆実践プログラミング［プロへのスキルアップ+プロジェクトサンプル］ impress top gearシリーズ Magnus Lie Hetland インプレス 2020/2/21
* プロフェッショナルPython ソフトウェアデザインの原則と実践 impress top gearシリーズ Dane Hillard インプレス 2021/11/16
* ちょっと上を行くPythonプログラミング 日経ソフトウエア 日経BP 2021/09/28
* 自走プログラマー ～Pythonの先輩が教えるプロジェクト開発のベストプラクティス120 清水川貴之 技術評論者 2020/2/27
* A Philosophy of Software Design, 2nd Edition (English Edition) John K. Ousterhout Software Design, Testing & Engineering 2021/7/25
* Wantedly Techbook Wantedly執筆部　2022/09/10
* ソフトウェア品質を高める開発者テスト 改訂版　高橋寿一 翔泳社 2022/6/15
* リーダブルコード ―より良いコードを書くためのシンプルで実践的なテクニック Dustin Boswell オライリージャパン 2012/6/23
* テスト駆動Python 第2版 Brian Okken 翔泳社 2022/8/30
* ハイパフォーマンスPython Micha Gorelick オライリージャパン 2015/11/20

### Web

* [Our Documentation | Python.org - https://www.python.org/doc/](https://www.python.org/doc/)
* [Python 3.10.7 documentation - https://docs.python.org/3/](https://docs.python.org/3/)
* [Python 3.9.14 documentation - https://docs.python.org/3.9/](https://docs.python.org/3.9/)
* [Python 3.8.13 documentation - https://docs.python.org/3.8/](https://docs.python.org/3.8/)
* [Python 3.6.15 documentation - https://docs.python.org/3.6/](https://docs.python.org/3.6/)
* [Python 3.6.15 documentation - https://docs.python.org/3.6/](https://docs.python.org/3.6/)
* [Python 2.7.18 documentation - https://docs.python.org/2.7/](https://docs.python.org/2.7/)
* [w3resource - https://www.w3resource.com/index.php](https://www.w3resource.com/index.php)
* [note.nkmk.me - https://note.nkmk.me/python/](https://note.nkmk.me/python/)

### Udemy
* [現役シリコンバレーエンジニアが教えるPython 3 入門 + 応用 +アメリカのシリコンバレー流コードスタイル](https://www.udemy.com/course/python-beginner/)
* [独学で身につけるPython〜基礎編〜【業務効率化・自動化で残業を無くそう！】](https://www.udemy.com/course/python-kaizen/)
* [はじめてのPython 少しずつ丁寧に学ぶプログラミング言語Python3のエッセンス](https://www.udemy.com/course/python-python3/)
* [たっぷりの練習問題を楽しみながら学ぶPython講座](https://www.udemy.com/course/python-hz/)
* [【世界で37万人が受講】データサイエンティストを目指すあなたへ〜データサイエンス25時間ブートキャンプ〜](https://www.udemy.com/course/datascience365/)
* [独学で身につけるPython〜応用編〜【業務効率化・自動化で残業を無くそう！】](https://www.udemy.com/course/python-kaizen-advanced/)
* [米国AI開発者がゼロから教えるPython入門講座](https://www.udemy.com/course/python-ai/)
* [Python でわかる オブジェクト指向 とはなにか？【Python オブジェクト指向 の「なぜ？」を「徹底的に」解説】](https://www.udemy.com/course/oop-python/)
* [【丁寧すぎる！】カナダの現役機械学習エンジニアが超丁寧にPythonで教える + プログラミングの"プ"。](https://www.udemy.com/course/python-basic-mb/)
* [はじめてのPython3。経験0からGUIアプリケーションを作れるまでの基礎力を！](https://www.udemy.com/course/python3_for_beginners/)
* [プログラミング言語 Python 3 入門](https://www.udemy.com/course/intro-to-python3/)
* [米国データサイエンティストがやさしく教えるデータサイエンスのためのPython講座](https://www.udemy.com/course/ds_for_python/)
* [【キカガク流】プログラミング力向上のためのPythonで学ぶアルゴリズム論（前編）](https://www.udemy.com/course/algorithm1/)
* [プログラミング初心者でも安心、Python/Django入門講座](https://www.udemy.com/course/pythondjango-a/)
* [Python　デザインパターンマスター講座～Pythonの基本文法、コーディング規約、命名規約、プログラミング技術～](https://www.udemy.com/course/python-mx/)
* [【Pythonではじめる】ラズベリーパイと電子工作入門](https://www.udemy.com/course/raspi-tutorial/)
* [Raspberry Pi とTensorFlow ではじめるAI・IoTアプリ開発入門](https://www.udemy.com/course/raspi-tensorflow/)
* [爆速で5つのPython Webアプリを開発](https://www.udemy.com/course/python-streamlit/)
* [現役シリコンバレーエンジニアが教えるPythonで始めるスクラッチからのブロックチェーン開発入門](https://www.udemy.com/course/python-blockchain/)

## 今後のPythonの展望と他の研修との兼ね合いについて

Pythonを使って特化した分野の研修を立ち上げて回していく(??)

多言語の利用率や普及率を考慮したときに、Pythonを広げていくなら以下の分野がいい。

* プログラミング的な思考能力を身につける基礎的な部分
* 機械学習・深層学習・強化学習などなどMLやDL系
* データサイエンス
* 画像処理技術
* Webアプリケーション(これも正直微妙な感じになっている？)
* バックエンド系の仕事
* 事務処理(Excel)

特に、今後AIの利用は拡大することは間違いないので、ここを強化していくべきだと思う。

以下の分野領域は要注意する

* 組み込み領域全般
  * 理由1：ハードウェアを意識しなくてもコードが記述できる & ハードウェアを意識したくても難しいPythonをどうやってモノを作っていくのか分からない。
  * 理由2：受講者にRaspberrypiがあるじゃないかと聞かれたら、Raspberrypiは教育用に作られたマイコンであって、RaspberrypiにPythonが採用されたのも、教育に最適な言語として採用されたため、組み込みで使える言語として誰も言ってない。(Scrachもそう。)  そして、Pythonが組み込みや制御系に適していると謳った書籍やサイトは本当に信用ならないので注意。財団側も商用利用は自己責任で実施、かつRaspberrypiはセキュリティがガバガバで非常に有名なので、ガッツリ開発ができる企業以外は、導入が難しいのではないかと思われる。理由は以上。
* 制御をPythonでやるなら、MicroPython x ベアメタルでやるのが最適解だと思う。 
* ただ、趣味レベルでPythonで組み込みが簡単にできるのは、非常に素晴らしいし、そういうマニアが増えるのは個人的に素晴らしいと思う。
