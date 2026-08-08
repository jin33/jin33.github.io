#!/usr/bin/env python3
"""トップページを生成する。

入力は _build/appstore.json（fetch_apps.py が作るスナップショット）。
出力は index.html。手で編集しない。

apps/<slug>.html は**生成しない**。各アプリのページはそれぞれ別の参考サイトを元に
個別に作り込んでおり、共通テンプレートに載らないため、手書きの独立したHTMLにしてある。
アプリを増やしたときは、ここの CARDS に1行足し、apps/ にページを1枚書く。

    python3 _build/build_site.py
"""

from __future__ import annotations

import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = Path(__file__).resolve().parent / "appstore.json"

FACEBOOK = "https://www.facebook.com/pages/Holy-inc-Apps/136263789773255"
DEVELOPER = "https://apps.apple.com/jp/developer/holy-inc/id359389894"

# 各アプリの一言と、アクセント色。カード自体の地色は共通（site.css の --surface）で、
# ここで指定する色は左端のバー・アイコンの影・矢印にだけ使う。値はそれぞれの
# apps/<slug>.html が使っている基調色そのものを転記している。トップと遷移先で
# 色が食い違わないように、ここだけ見て変えず、まず個別ページ側の色を変えてから
# 合わせること。
# 一言はApp Storeの説明文から機械的に切り出さず、一覧で並べたとき違いが分かる長さで書く。
CARDS = {
    "replay":        ("覚えた曲を、忘れないために。", "#9a6b3f"),
    "homekarte":     ("家族の体調を、そっと記録する。", "#b4653a"),
    "taptaptown":    ("ぺたっと置いて、街が動きだす。", "#ff8a5b"),
    "average100":    ("入力するだけで、平均が出る。", "#7c8cff"),
    "kanji":         ("さわって、きいて、漢字を覚える。", "#58cc02"),
    "hiragana":      ("ひらがなに、はじめてふれる日に。", "#b7412f"),
    "katakana":      ("カタカナを、かたちから覚える。", "#e03127"),
    "drawingciao":   ("むずかしい操作は、ぜんぶ捨てた。", "#ef7d57"),
    "zengamentimer": ("画面いっぱいの、ただのタイマー。", "#ff6a3d"),
    "lifecounter":   ("ライフ管理は、指一本で。", "#36d1dc"),
}


def e(text: str) -> str:
    return html.escape(text, quote=True)


def build_index(apps: list[dict]) -> None:
    cards = []
    for a in apps:
        tagline, accent = CARDS[a["slug"]]
        cards.append(
            f'      <a class="card" href="apps/{a["slug"]}.html"'
            f' style="--accent-app:{accent}">\n'
            f'        <img src="{a["icon"]}" alt="" width="72" height="72" loading="lazy">\n'
            f'        <span class="card-text">\n'
            f'          <span class="card-name">{e(a["name"].split(" - ")[0].split("　")[0])}</span>\n'
            f'          <span class="card-tag">{e(tagline)}</span>\n'
            f'        </span>\n'
            f'        <svg class="card-arrow" viewBox="0 0 16 16" aria-hidden="true">'
            f'<path d="M6 3l5 5-5 5" fill="none" stroke="currentColor"'
            f' stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg>\n'
            f'      </a>'
        )

    html_out = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Holy App</title>
<meta name="description" content="Holy App が公開している iPhone・iPad アプリ{len(apps)}本の一覧。">
<link rel="stylesheet" href="assets/site.css">
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="./">Holy App</a>
    <a class="back" href="{DEVELOPER}">App Store</a>
  </div>
</header>

<main>
  <section class="hero wrap">
    <p class="hero-eyebrow">iPhone &amp; iPad</p>
    <h1>ちいさな道具を、<br>ていねいに。</h1>
    <p class="hero-lead">暮らしと学びのすきまを埋めるアプリを、{len(apps)}本つくっています。</p>
  </section>

  <section class="wrap">
    <div class="grid">
{chr(10).join(cards)}
    </div>
  </section>
</main>

<footer class="site-foot">
  <div class="wrap">
    <ul>
      <li><a href="{DEVELOPER}">App Store</a></li>
      <li><a href="{FACEBOOK}">お問い合わせ</a></li>
    </ul>
    <p>&copy; 2026 Holy App</p>
  </div>
</footer>
</body>
</html>
"""
    (ROOT / "index.html").write_text(html_out, encoding="utf-8")


def main() -> None:
    apps = json.loads(DATA.read_text(encoding="utf-8"))["apps"]
    missing = [a["slug"] for a in apps if a["slug"] not in CARDS]
    if missing:
        raise SystemExit(f"CARDS に一言と色がないアプリ: {', '.join(missing)}")
    build_index(apps)
    print(f"generated index.html ({len(apps)} apps)")


if __name__ == "__main__":
    main()
