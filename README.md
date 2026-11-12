# ペットサロン ビスケット

元サイトの表示用静的バックアップです。公開用ファイルはリポジトリ直下の
`index.html`、`about/`、`price/`、`hotel/`、`assets/` に配置しています。

## Cloudflare Pages

- Production branch: `main`
- Framework preset: `None`
- Build command: 空欄
- Build output directory: `/`（リポジトリ直下）

GitHub に push 後、Cloudflare Pages のデプロイ状況を確認してください。
WordPress 本体・管理画面・データベースは含まれません。
Google Maps、アクセス解析、外部 Web フォントは外部サービスに依存します。

## ローカル確認

リポジトリ直下で `python3 -m http.server 8000` を実行します。
トップ、`/price/`、`/hotel/`、`/about/` が確認対象です。

`biscuit-site-backup.zip` と `WordPress.2026-11-12.xml` は元資料です。
