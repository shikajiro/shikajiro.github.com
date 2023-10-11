元データは source ブランチに保持する
書き出したhtml等を master ブランチに書き出してpushする

# 開発
pelican -r -l

# htmlの作成
pelican content

# gh-pages branch に テキストを書き出す
ghp-import output
特に反応はない

# repository に push する
git push -f origin gh-pages:master

