#!/usr/bin/env python3
"""プライバシーポリシーのHTMLを言語ごとに生成する。

文面の正本は _build/content/<locale>.json。このスクリプトが
replay/privacy/<locale>.html を書き出す。19言語ぶんのHTMLを手で揃えると
リンクや章番号がすぐズレるため、テンプレートを1つに寄せている。

ファイル名は App Store Connect のロケール名（en-US, zh-Hans など）に
そろえてある。privacyPolicyUrl を一括設定するとき、ロケール名をそのまま
URLに使えるようにするため。

    python3 _build/build_policies.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CONTENT_DIR = Path(__file__).resolve().parent / "content"
OUT_DIR = ROOT / "replay" / "privacy"

# 言語切り替えの並び順。ここに無いロケールは末尾へ回る。
LOCALE_ORDER = [
    "ja", "en-US", "de-DE", "es-ES", "fr-FR", "it", "nl-NL", "pl", "pt-BR",
    "ru", "tr", "uk", "ko", "zh-Hans", "zh-Hant", "th", "vi", "id", "hi",
]

PAGE = """<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="stylesheet" href="../../assets/site.css">
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="../../">Holy App</a>
    <a class="back" href="../../apps/replay.html">RePlay Repertory</a>
  </div>
</header>
<main class="wrap-narrow doc">
  <h1>{h1}</h1>
  <p class="doc-app">RePlay Repertory</p>
  <p class="doc-date">{updated}</p>

  <p>{intro}</p>
{sections}  <nav class="langs">{langs}</nav>
</main>
<footer class="site-foot">
  <div class="wrap">
    <p>&copy; 2026 Holy App</p>
  </div>
</footer>
</body>
</html>
"""


def load_locales() -> dict[str, dict]:
    found = {p.stem: json.loads(p.read_text(encoding="utf-8"))
             for p in CONTENT_DIR.glob("*.json")}
    ordered = {code: found[code] for code in LOCALE_ORDER if code in found}
    for code in sorted(found):
        ordered.setdefault(code, found[code])
    return ordered


def render_sections(sections: list[dict]) -> str:
    out = []
    for index, section in enumerate(sections, start=1):
        out.append(f'  <h2>{index}. {section["h"]}</h2>')
        out.extend(f"  {block}" for block in section["body"])
        out.append("")
    return "\n".join(out)


def render_langs(locales: dict[str, dict], current: str) -> str:
    links = [
        f'<span>{data["endonym"]}</span>' if code == current
        else f'<a href="{code}.html">{data["endonym"]}</a>'
        for code, data in locales.items()
    ]
    return "\n    " + "\n    ".join(links) + "\n  "


INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Privacy Policy | RePlay Repertory</title>
<link rel="stylesheet" href="../../assets/site.css">
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="../../">Holy App</a>
    <a class="back" href="../../apps/replay.html">RePlay Repertory</a>
  </div>
</header>
<main class="wrap-narrow doc">
  <h1>Privacy Policy</h1>
  <p class="doc-app">RePlay Repertory</p>
  <p>Choose a language.</p>
  <nav class="langs">{langs}</nav>
</main>
<footer class="site-foot">
  <div class="wrap">
    <p>&copy; 2026 Holy App</p>
  </div>
</footer>
</body>
</html>
"""


def write_index(locales: dict[str, dict]) -> None:
    """言語一覧だけの入口ページ。ASCには各言語のURLを直接設定するため、
    ここは人が手で辿ってきたとき用の受け皿にとどめている。"""
    links = "\n    ".join(
        f'<a href="{code}.html">{data["endonym"]}</a>'
        for code, data in locales.items()
    )
    (OUT_DIR / "index.html").write_text(
        INDEX.format(langs="\n    " + links + "\n  "), encoding="utf-8"
    )


def main() -> None:
    locales = load_locales()
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    for code, data in locales.items():
        html = PAGE.format(
            lang=data["lang"],
            title=data["title"],
            h1=data["h1"],
            updated=data["updated"],
            intro=data["intro"],
            sections=render_sections(data["sections"]),
            langs=render_langs(locales, code),
        )
        (OUT_DIR / f"{code}.html").write_text(html, encoding="utf-8")

    write_index(locales)

    missing = [c for c in LOCALE_ORDER if c not in locales]
    print(f"generated {len(locales)} pages in {OUT_DIR.relative_to(ROOT)}")
    if missing:
        print("missing translations: " + ", ".join(missing))


if __name__ == "__main__":
    main()
