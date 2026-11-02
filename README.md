# LILIFER TAROT — 日本語の手引き

全80枚のカードを日本語で読むための静的サイトです。

## Macで起動

1. ZIPを展開し、`lilifer-tarot` フォルダーを任意の場所へ移動します。
2. ターミナルでそのフォルダーへ移動し、次を実行します。

```bash
bash start.command
```

3. ブラウザーで http://localhost:8000 を開きます。停止は Control+C。

必要なのは Python 3 だけです。`python3 --version` で確認してください。Pythonがなければ https://www.python.org/downloads/macos/ から導入してください。
Node.js、npm、追加Pythonパッケージ、APIキーは起動に不要です。

`index.html` のダブルクリックではJSONの読み込みができないため、必ずHTTPサーバー経由で開いてください。
ポート8000が使用中なら、次のように変更できます。

```bash
python3 -m http.server 8001 --bind 127.0.0.1 --directory dist
```

## 新しいローカルチャットへ引き継ぐ

ローカルで作業できるCodexのチャットを開き、このフォルダーを作業場所に選択してください。以下を送れば引き継げます。

> HANDOFF.md と README.md を読んで、このサイトの開発を引き継いでください。まずローカルで起動し、現在の状態を確認してください。今後の作業はこのフォルダーで行います。

会話履歴そのものは移動しません。実装・仕様・注意点・検証結果をHANDOFF.mdに記録しています。

## ファイル

- `dist/index.html`：ページ構成
- `dist/style.css`：配色・レイアウト・スマートフォン対応
- `dist/app.js`：検索、絞り込み、カード詳細、お気に入り、タブ切替
- `dist/cards.json`：全80枚の日本語解説
- `dist/guide.json`：象徴と読み方
- `dist/spreads.json`：6種類のスプレッドと配置
- `dist/assets/`：カード画像80枚
- `dist/original/`：原文ページ画像79枚
- `dist/manifest.webmanifest`：ホーム画面に追加したときのアプリ名・アイコン・配色
- `dist/sw.js`：一度読んだページをオフラインでも表示するService Worker
- `dist/icons/`：ホーム画面用アイコン（Luciferのカードの星と翼を切り出したもの）
- `content.py`：cards.jsonの生成元（Python標準ライブラリのみ）
- `guide.py`：guide.json・spreads.jsonの生成元（Python標準ライブラリのみ）
- `icons.py`：`dist/icons/` の生成元（Pillowが必要。サイトの起動には不要）
- `.github/workflows/pages.yml`：GitHub Pagesへの公開設定

翻訳を変更するときは生成元のPythonファイルも更新してから `python3 content.py` / `python3 guide.py` を実行してください。JSONを直接編集した場合は、再生成による上書きに注意してください。通常の起動に再生成は必要ありません。

## ホーム画面への追加

AndroidのChromeで公開サイトを開き、メニューの「ホーム画面に追加」または「アプリをインストール」を選ぶと、アプリとして起動できます。iPhoneのSafariでは共有メニューの「ホーム画面に追加」を使います。

一度開いたページ・カード画像は端末に保存され、電波のない場所でも表示されます。まだ開いていないカード画像は表示されません。
`dist/sw.js` の `CACHE` の値を変えると、各端末の保存済みファイルが入れ替わります。HTML・CSS・JS・JSONはつながる場所では毎回公開サイトから読むため、文章や画面の変更では値を変える必要はありません。画像を同じファイル名で差し替えたときだけ変更してください。

## 保存されるデータ

お気に入りはブラウザーのlocalStorageに保存されます。公開サイトとlocalhostは保存先が異なるため、お気に入りは自動移行されません。ポートを変えた場合も別の保存先になります。

## 公開サイト

https://www.azimicat.dev/lilifer-tarot/

GitHubアカウントに設定済みの独自ドメインを引き継いでいます。

`main` へのpush後、GitHub ActionsがJavaScriptの構文を確認し、`dist/` をGitHub Pagesへ公開します。
PRでは構文確認のみ実行します。ローカルの変更を公開するには、PRを作成して `main` へマージしてください。

リポジトリの Settings → Pages → Build and deployment → Source は `GitHub Actions` に設定します。
公開手順は `.github/workflows/pages.yml` にあります。ビルドや追加パッケージの導入は不要です。

元のPDFはリポジトリに含めません。サイトで参照する原文ページ画像は `dist/original/` に含めています。
`.openai/hosting.json` は以前のSites向け設定であり、このリポジトリには含めません。

以前のSites公開先：https://lilifer-tarot-jp-asahi.asahime.chatgpt.site

原著・カードアート：Marion Costentin / Little Darkness © 2023。
添付解説書に基づく非公式の日本語訳です。GitHub Pagesのサイトは誰でも閲覧できます。
