元データは source ブランチに保持する
書き出したhtml等を master ブランチに書き出してpushする

#htmlの作成
make html

#gh-pages branch に テキストを書き出す
ghp-import output

#repository に push する
git push -f origin gh-pages:master

