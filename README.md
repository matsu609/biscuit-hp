# ペットサロン ビスケット

添付デザインを基にした静的サイトです。`index.html` に料金・ホテル・アクセス・法定標識をまとめています。旧 `/price/`、`/hotel/`、`/about/` は該当セクションへ移動します。WordPressやデータベース、ビルドは不要です。

## ローカル確認

リポジトリ直下で `python3 -m http.server 8000` を実行してください。

## 制作方針

今後の内容変更・公開作業の前に、[合意した制作・掲載方針](docs/editorial-policy.md)を確認してください。実際の店内・ホテル写真を使用し、若いトリマーチームを中心に紹介します。正式公開・移行は会長の最終確認後に行います。方針と食い違う指示があれば変更前に指摘します。

## お店への確認

[確認リスト](docs/review-checklist.md) と [現行サイトの照合データ](docs/content-reference.json) を参照してください。料金表の「2027年1月改定」と写真の利用許諾は最終確認が必要です。営業時間10:00〜19:00・原則無休はユーザー指定により掲載しています。現在のローカル変更は撮影・ヒアリング準備版です。写真枠と口コミ欄を維持し、`noindex` を設定しています。確認用ページへの通常の修正は、ユーザーの指示により確認を挟まずGitHubのmainへ反映し、Cloudflare Pagesへデプロイします。正式公開・移行の条件は上記の制作方針を優先します。

## Cloudflare Pages

- Production branch: `main`
- Framework preset: `None`
- Build command: 空欄
- Build output directory: `/`（リポジトリ直下）

`biscuit-site-backup.zip` と `WordPress.2026-11-12.xml` は元資料です。`main` への反映後、Cloudflare Pages の自動デプロイ結果を確認してください。

丸い見出しと本文のフォントは `assets/fonts/` から配信します。元デザインと同じフォントを使用し、外部のフォントサービスへの接続は不要です。ライセンスと出典は同ディレクトリを参照してください。
