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

# 各アプリの一言と、カードの地色。地色は個別ページの基調色と合わせてある。
# 一言はApp Storeの説明文から機械的に切り出さず、一覧で並べたとき違いが分かる長さで書く。
CARDS = {
    "replay":        ("覚えた曲を、忘れないために。", "#f2f0ec", "#2b2a28"),
    "homekarte":     ("家族の体調を、そっと記録する。", "#f7f1e8", "#3a2f24"),
    "taptaptown":    ("ぺたっと置いて、街が動きだす。", "#e8f4ff", "#12395e"),
    "average100":    ("入力するだけで、平均が出る。", "#1c1c1f", "#f4f4f6"),
    "kanji":         ("さわって、きいて、漢字を覚える。", "#fff4e0", "#7a3d00"),
    "hiragana":      ("ひらがなに、はじめてふれる日に。", "#f6f1e7", "#7c2d2d"),
    "katakana":      ("カタカナを、かたちから覚える。", "#f2f2f0", "#1a1a1a"),
    "drawingciao":   ("むずかしい操作は、ぜんぶ捨てた。", "#fdf6ee", "#5a4632"),
    "zengamentimer": ("画面いっぱいの、ただのタイマー。", "#0a0a0a", "#f0f0f0"),
    "lifecounter":   ("ライフ管理は、指一本で。", "#141821", "#e8f0ff"),
}


def e(text: str) -> str:
    return html.escape(text, quote=True)


def build_index(apps: list[dict]) -> None:
    cards = []
    for a in apps:
        tagline, bg, fg = CARDS[a["slug"]]
        cards.append(
            f'      <a class="card" href="apps/{a["slug"]}.html"'
            f' style="--card-bg:{bg};--card-fg:{fg}">\n'
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
