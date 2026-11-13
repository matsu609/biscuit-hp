# ペットサロン ビスケット

添付デザインを基にした静的サイトです。`index.html` に料金・ホテル・アクセス・法定標識をまとめています。旧 `/price/`、`/hotel/`、`/about/` は該当セクションへ移動します。WordPressやデータベース、ビルドは不要です。

## ローカル確認

リポジトリ直下で `python3 -m http.server 8000` を実行してください。

## お店への確認

[確認リスト](docs/review-checklist.md) と [現行サイトの照合データ](docs/content-reference.json) を参照してください。料金表の「2027年1月改定」、営業時間・定休日、写真の利用許諾は最終確認が必要です。本番公開用に検索エンジン向けの `noindex` は設定していません。

## Cloudflare Pages

- Production branch: `main`
- Framework preset: `None`
- Build command: 空欄
- Build output directory: `/`（リポジトリ直下）

`biscuit-site-backup.zip` と `WordPress.2026-11-12.xml` は元資料です。`main` への反映後、Cloudflare Pages の自動デプロイ結果を確認してください。
