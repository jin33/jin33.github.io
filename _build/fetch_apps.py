#!/usr/bin/env python3
"""App Store から公開中アプリの情報と画像を取得し、スナップショットを作る。

出力は次の3つ。

    _build/appstore.json   … サイト生成が読む唯一の入力
    assets/icons/<slug>.png
    assets/shots/<slug>-<n>.jpg

ページ生成時にネットワークへ出ないよう、取得と生成を分けている。
App Store 側で説明文やアイコンを変えたときだけこれを実行し直す。

    python3 _build/fetch_apps.py
"""

from __future__ import annotations

import json
import shutil
import subprocess
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "appstore.json"
ICON_DIR = ROOT / "assets" / "icons"
SHOT_DIR = ROOT / "assets" / "shots"
PROJECT_ROOT = ROOT.parents[1]
HANON_PUBLIC_SHOTS = PROJECT_ROOT / "01_Xcodeプロジェクト" / "wip" / "Hanon" / "fastlane" / "screenshots" / "final" / "ja"

# 掲載順とURLのスラッグをここで固定する。trackId から機械的に作ると、
# アプリを足したときにURLが変わってしまうため。
APPS = [
    ("hanon", 6795886409),
    ("replay", 6792226081),
    ("homekarte", 867437900),
    ("taptaptown", 924949601),
    ("average100", 892765668),
    ("kanji", 1075683691),
    ("hiragana", 783511889),
    ("katakana", 783514541),
    ("drawingciao", 720019222),
    ("zengamentimer", 1502189390),
    ("lifecounter", 1186784709),
]

LOOKUP = "https://itunes.apple.com/lookup?id={ids}&country=jp&lang=ja_jp&limit=50"
SHOTS_PER_APP = 5
ICON_PX = 256
SHOT_PX = 900


def fetch_json(url: str) -> dict:
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.loads(r.read().decode("utf-8"))


def download(url: str, dest: Path, max_px: int) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(url, timeout=30) as r:
        dest.write_bytes(r.read())
    # sips は macOS 標準。長辺を縮めるだけなので追加の依存を入れない。
    args = ["sips", "-Z", str(max_px)]
    if dest.suffix == ".jpg":
        # 端末画像は大きいままだと1ページ数MBになる。JPEGへ落として軽くする。
        args += ["-s", "format", "jpeg", "-s", "formatOptions", "90"]
    subprocess.run(args + [str(dest)], check=True, capture_output=True)


def copy_hanon_public_shots() -> list[str]:
    """Hanonはプロジェクトの提出用正本をそのままサイトへ載せる。"""
    shots = []
    names = [
        "01_today-practice.png",
        "02_practice-started.png",
        "03_key-signature-hint.png",
        "04_score.png",
        "05_history-calendar.png",
        "06_metronome.png",
    ]
    for i, name in enumerate(names, start=1):
        source = HANON_PUBLIC_SHOTS / name
        if not source.exists():
            raise FileNotFoundError(f"Hanon公開スクリーンショットがありません: {source}")
        dest = SHOT_DIR / f"hanon-{i}.png"
        shutil.copyfile(source, dest)
        shots.append(dest.relative_to(ROOT).as_posix())
    return shots


def main() -> None:
    ids = ",".join(str(track_id) for _, track_id in APPS)
    results = {r["trackId"]: r for r in fetch_json(LOOKUP.format(ids=ids))["results"]}

    apps = []
    for slug, track_id in APPS:
        r = results.get(track_id)
        if r is None:
            print(f"skip {slug}: not on the App Store")
            continue

        icon = ICON_DIR / f"{slug}.png"
        download(r["artworkUrl512"], icon, ICON_PX)

        # ハノン日和はプロジェクト内の提出用正本を使い、App Store取得画像と混ぜない。
        if slug == "hanon":
            shots = copy_hanon_public_shots()
        else:
            shots = []
            for i, url in enumerate(r.get("screenshotUrls", [])[:SHOTS_PER_APP], start=1):
                path = SHOT_DIR / f"{slug}-{i}.jpg"
                download(url, path, SHOT_PX)
                shots.append(path.relative_to(ROOT).as_posix())

        apps.append({
            "slug": slug,
            "trackId": track_id,
            "name": r["trackName"],
            "genre": r.get("primaryGenreName", ""),
            "description": r.get("description", ""),
            "url": r["trackViewUrl"].split("?")[0],
            "icon": icon.relative_to(ROOT).as_posix(),
            "shots": shots,
        })
        print(f"ok   {slug}: {r['trackName']}")

    OUT.write_text(json.dumps({"apps": apps}, ensure_ascii=False, indent=2) + "\n",
                   encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)} ({len(apps)} apps)")


if __name__ == "__main__":
    main()
