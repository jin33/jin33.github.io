#!/usr/bin/env python3
"""公開中アプリの日本語・英語プライバシーポリシーを生成する。

各アプリの本文はこのファイルの APP_POLICIES にまとめ、HTMLの構造と
言語切り替えは共通化する。App Store Connect には各アプリの ja / en-US
ページを直接設定できるよう、アプリごとに privacy ディレクトリを作る。
"""

from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
UPDATED_JA = "最終更新日: 2026年8月11日"
UPDATED_EN = "Last updated: August 11, 2026"

LOCALES = {
    "ja": {"html_lang": "ja", "label": "日本語"},
    "en-US": {"html_lang": "en", "label": "English"},
}


def section(ja: str, en: str) -> dict[str, str]:
    return {"ja": ja, "en-US": en}


def paragraph(text: str) -> str:
    return f"<p>{text}</p>"


COMMON_NOT_COLLECTED = section(
    paragraph(
        "本アプリは、氏名、住所、電話番号、メールアドレスなど、利用者を直接特定する情報を収集しません。アカウント登録やログインの仕組みもありません。"
    ),
    paragraph(
        "The App does not collect information that directly identifies you, such as your name, address, phone number, or email address. There is no account registration or sign-in."
    ),
)

ADVERTISING = section(
    paragraph(
        "本アプリは、Google LLCが提供する広告配信サービス「Google AdMob」を利用して広告を表示します。AdMobおよびその広告パートナーは、広告の配信・表示回数の測定・不正防止などのために、広告識別子、端末情報、広告の利用状況、診断情報などを取得することがあります。"
    )
    + paragraph(
        "欧州経済領域、英国、スイスなど、同意取得が求められる地域では、Google User Messaging Platform（UMP）などの同意管理画面を表示し、利用者の選択に従って広告を配信します。App Tracking Transparencyを利用するアプリでは、追跡の許可・拒否が広告の扱いに反映されます。"
    )
    + "<ul><li><a href=\"https://policies.google.com/privacy\">Googleのプライバシーポリシー</a></li><li><a href=\"https://policies.google.com/technologies/partner-sites\">広告におけるGoogleのデータ利用</a></li></ul>",
    paragraph(
        "The App displays advertising through Google AdMob, provided by Google LLC. AdMob and its advertising partners may collect advertising identifiers, device information, ad interaction data, and diagnostic information to deliver ads, measure impressions, and prevent fraud."
    )
    + paragraph(
        "Where consent is required, including the European Economic Area, the United Kingdom, and Switzerland, the App presents a consent screen through Google User Messaging Platform (UMP) or a similar tool and serves ads according to your choice. Apps that use App Tracking Transparency reflect your allow or deny choice in how advertising is handled."
    )
    + "<ul><li><a href=\"https://policies.google.com/privacy\">Google Privacy Policy</a></li><li><a href=\"https://policies.google.com/technologies/partner-sites\">How Google uses data in advertising</a></li></ul>",
)

GENERIC_THIRD_PARTY = section(
    paragraph(
        "当方は、広告配信、分析、クラッシュ情報の収集など、各サービスの提供に必要な範囲で第三者サービスを利用します。それ以外に、当方が取得した情報を第三者へ提供・販売することはありません。ただし、法令に基づく開示請求があった場合はこの限りではありません。"
    ),
    paragraph(
        "We use third-party services only as necessary to provide advertising, analytics, crash reporting, and related functions. We do not otherwise sell or share information we obtain with third parties, except when disclosure is required by law."
    ),
)

GENERIC_RETENTION = section(
    paragraph(
        "本アプリ内で利用者が作成・入力したデータは、利用者が削除するまで端末に保存されます。本アプリを端末から削除すると、端末内に保存されたデータも削除されます。広告、分析、診断サービスが取得する情報の保存期間や削除方法は、各サービス提供者のポリシーに従います。"
    ),
    paragraph(
        "Content you create or enter in the App remains on your device until you delete it. Deleting the App removes data stored on your device. The retention and deletion of information collected by advertising, analytics, and diagnostic services are governed by the policies of those service providers."
    ),
)

CHANGES = section(
    paragraph(
        "当方は、法令の変更や本アプリの機能追加に応じて、本ポリシーを改定することがあります。改定した場合は、本ページに最新の内容と最終更新日を掲載します。"
    ),
    paragraph(
        "We may revise this policy as laws change or as the App gains new features. When we do, we will publish the updated text and revision date on this page."
    ),
)

CONTACT = section(
    paragraph(
        "本ポリシーおよび本アプリにおける情報の取り扱いに関するお問い合わせは、以下までご連絡ください。"
    )
    + paragraph(
        "Holy App<br><a href=\"https://www.facebook.com/pages/Holy-inc-Apps/136263789773255\">Facebookページ</a>"
    ),
    paragraph(
        "For questions about this policy or how information is handled in the App, please contact us."
    )
    + paragraph(
        "Holy App<br><a href=\"https://www.facebook.com/pages/Holy-inc-Apps/136263789773255\">Facebook page</a>"
    ),
)


APP_POLICIES = {
    "average100": {
        "name": {"ja": "平均点のための計算機 - Average100 Lite", "en-US": "Average100 Lite"},
        "back": {"ja": "平均点のための計算機", "en-US": "Average100 Lite"},
        "intro": {
            "ja": "Holy App（以下「当方」）は、iOSアプリ「平均点のための計算機 - Average100 Lite」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。",
            "en-US": "Holy App (\"we\") provides the iOS app Average100 Lite (the \"App\"). This policy explains how information is handled in the App.",
        },
        "data": section(
            paragraph(
                "本アプリでは、平均を計算するための数字、履歴、メモ、表示設定などを入力・保存できます。これらは本アプリの機能を提供するために利用者の端末内へ保存され、当方のサーバーへ送信・保存されません。"
            ),
            paragraph(
                "The App lets you enter and store numbers, calculation history, notes, and display settings. This data is stored on your device to provide the App's features and is not sent to or stored on our servers."
            ),
        ),
        "analytics": section(
            paragraph(
                "本アプリは、機能改善や不具合の把握のため、Google LLCが提供するFirebase AnalyticsおよびFirebase Crashlyticsを利用しています。これらのサービスは、アプリの起動や機能の利用状況、端末の種類、OSのバージョン、クラッシュ情報、パフォーマンスなどの診断情報を取得することがあります。入力した数字、履歴、メモなどのアプリ内データを、当方が分析目的で取得することはありません。"
            ),
            paragraph(
                "To improve features and identify problems, the App uses Firebase Analytics and Firebase Crashlytics, provided by Google LLC. These services may collect app usage, device model, OS version, crash information, performance data, and other diagnostics. We do not obtain your numbers, history, or notes for analytics purposes."
            ),
        ),
    },
    "homekarte": {
        "name": {"ja": "おうちカルテ", "en-US": "HomeKarte"},
        "back": {"ja": "おうちカルテ", "en-US": "HomeKarte"},
        "intro": {
            "ja": "Holy App（以下「当方」）は、iOSアプリ「おうちカルテ」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。",
            "en-US": "Holy App (\"we\") provides the iOS app HomeKarte (the \"App\"). This policy explains how information is handled in the App.",
        },
        "data": section(
            paragraph(
                "本アプリでは、家族の名前、体温、体調、服薬、メモ、日付、写真など、利用者が家族の健康状態を記録するためのデータを保存できます。これらのデータは本アプリの機能を提供するために端末内へ保存され、当方のサーバーへ送信・保存されません。"
            ),
            paragraph(
                "The App lets you store family member names, temperature, symptoms, medication records, notes, dates, and photos for keeping health-related records. This data is stored on your device to provide the App's features and is not sent to or stored on our servers."
            ),
        ),
        "permissions": section(
            paragraph(
                "写真の登録や記録への添付を選択した場合、写真ライブラリまたはカメラへのアクセスを求めます。アクセスは利用者が許可した場合に限られ、取得した画像は本アプリの端末内データとして扱われます。"
            ),
            paragraph(
                "If you choose to add a photo or attach one to a record, the App may ask for access to your photo library or camera. Access occurs only with your permission, and the resulting image is handled as data stored by the App on your device."
            ),
        ),
        "sharing": section(
            paragraph(
                "本アプリには、利用者が選択した記録をメールやメッセージなどで共有する機能があります。共有を実行した場合、データは利用者が選択したAppleまたは通信サービスの仕組みを通じて送信され、その取り扱いは各サービスのポリシーに従います。当方が共有先や送信内容を管理することはありません。"
            ),
            paragraph(
                "The App may let you share selected records through email, Messages, or similar functions. When you choose to share, the data is sent through the Apple or communications service you select and is governed by that service's policy. We do not control the recipient or the content you choose to send."
            ),
        ),
        "analytics": section(
            paragraph(
                "本アプリは、機能改善や不具合の把握のため、Google LLCが提供するFirebase AnalyticsおよびFirebase Crashlyticsを利用しています。アプリの利用状況、端末情報、クラッシュ情報、パフォーマンスなどの診断情報を取得することがありますが、家族の名前、体温、体調、服薬、写真などの記録内容を当方が分析目的で取得することはありません。"
            ),
            paragraph(
                "To improve features and identify problems, the App uses Firebase Analytics and Firebase Crashlytics, provided by Google LLC. These services may collect app usage, device information, crash information, performance data, and other diagnostics. We do not obtain family names, temperatures, symptoms, medication records, or photos for analytics purposes."
            ),
        ),
    },
    "kanji": {
        "name": {"ja": "漢字ボード 1年生 しゃべる漢字表 FREE", "en-US": "Kanji Board: 1st Grade"},
        "back": {"ja": "漢字ボード 1年生", "en-US": "Kanji Board"},
        "intro": {
            "ja": "Holy App（以下「当方」）は、iOSアプリ「漢字ボード 1年生 しゃべる漢字表 FREE」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。",
            "en-US": "Holy App (\"we\") provides the iOS app Kanji Board: 1st Grade (the \"App\"). This policy explains how information is handled in the App.",
        },
        "data": section(
            paragraph(
                "本アプリでは、漢字の学習や読み上げのために、画面へ入力した文字、学習設定、表示設定などを扱います。これらは本アプリの機能を提供するために端末内で処理・保存され、当方のサーバーへ送信・保存されません。"
            ),
            paragraph(
                "The App handles text entered for kanji practice and speech, along with learning and display settings. This information is processed and stored on your device to provide the App's features and is not sent to or stored on our servers."
            ),
        ),
        "analytics": section(
            paragraph(
                "本アプリは、広告配信および機能改善・不具合把握のため、Google AdMob、Firebase Analytics、Firebase Crashlyticsを利用しています。これらのサービスが端末情報、広告識別子、利用状況、クラッシュ情報などを取得することがありますが、入力した漢字や学習内容を当方が分析目的で取得することはありません。"
            ),
            paragraph(
                "The App uses Google AdMob, Firebase Analytics, and Firebase Crashlytics for advertising, feature improvement, and problem diagnosis. These services may collect device information, advertising identifiers, usage information, and crash data. We do not obtain the kanji or learning content you enter for analytics purposes."
            ),
        ),
    },
    "lifecounter": {
        "name": {"ja": "バディライフ - Life Counter", "en-US": "Buddy Life - Life Counter"},
        "back": {"ja": "バディライフ", "en-US": "Buddy Life"},
        "intro": {
            "ja": "Holy App（以下「当方」）は、iOSアプリ「バディライフ - Life Counter」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。",
            "en-US": "Holy App (\"we\") provides the iOS app Buddy Life - Life Counter (the \"App\"). This policy explains how information is handled in the App.",
        },
        "data": section(
            paragraph(
                "本アプリでは、ライフカウンターの数値、プレイヤー名、背景画像、表示設定などを扱います。これらは本アプリの機能を提供するために端末内へ保存され、当方のサーバーへ送信・保存されません。"
            ),
            paragraph(
                "The App handles life-counter values, player names, background images, and display settings. This information is stored on your device to provide the App's features and is not sent to or stored on our servers."
            ),
        ),
        "permissions": section(
            paragraph(
                "背景画像を選択・撮影する場合、写真ライブラリまたはカメラへのアクセスを求めます。アクセスは利用者が許可した場合に限られ、画像は端末内で利用されます。"
            ),
            paragraph(
                "If you choose or capture a background image, the App may ask for access to your photo library or camera. Access occurs only with your permission, and the image is used on your device."
            ),
        ),
        "purchase": section(
            paragraph(
                "プレミアム版などのアプリ内購入はAppleのApp Storeを通じて処理されます。当方がクレジットカード番号などの決済情報を取得・保存することはありません。購入状態の確認には、Appleが提供する購入情報が利用されます。"
            ),
            paragraph(
                "In-app purchases, including the premium version, are processed through Apple's App Store. We do not receive or store payment details such as credit card numbers. Apple-provided purchase information may be used to verify your purchase status."
            ),
        ),
        "analytics": section(
            paragraph(
                "本アプリは、機能改善や不具合の把握のため、Google LLCが提供するFirebase Analyticsを利用しています。アプリの利用状況、端末情報、広告識別子、パフォーマンスなどを取得することがありますが、ライフの数値やプレイヤー名、画像を当方が分析目的で取得することはありません。"
            ),
            paragraph(
                "To improve features and identify problems, the App uses Firebase Analytics, provided by Google LLC. It may collect app usage, device information, advertising identifiers, and performance data. We do not obtain life values, player names, or images for analytics purposes."
            ),
        ),
    },
    "taptaptown": {
        "name": {"ja": "ぺたシティ", "en-US": "TapTapTown"},
        "back": {"ja": "ぺたシティ", "en-US": "TapTapTown"},
        "intro": {
            "ja": "Holy App（以下「当方」）は、iOSアプリ「ぺたシティ」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。",
            "en-US": "Holy App (\"we\") provides the iOS app TapTapTown (the \"App\"). This policy explains how information is handled in the App.",
        },
        "data": section(
            paragraph(
                "本アプリでは、街の配置、背景の選択、表示設定などのゲームデータを扱います。これらは本アプリの機能を提供するために端末内へ保存され、当方のサーバーへ送信・保存されません。"
            ),
            paragraph(
                "The App handles game data such as town layout, background selection, and display settings. This data is stored on your device to provide the App's features and is not sent to or stored on our servers."
            ),
        ),
        "analytics": section(
            paragraph(
                "本アプリは、広告配信のためGoogle AdMobを、クラッシュや不具合の把握のためFirebase Crashlyticsを利用しています。これらのサービスは広告識別子、端末情報、クラッシュ情報、パフォーマンスなどを取得することがありますが、街の配置や遊び方の内容を当方が個人と結びつけて取得することはありません。"
            ),
            paragraph(
                "The App uses Google AdMob for advertising and Firebase Crashlytics for crash and problem reporting. These services may collect advertising identifiers, device information, crash data, performance data, and other diagnostics. We do not link your town layout or gameplay content to your identity."
            ),
        ),
    },
    "zengamentimer": {
        "name": {"ja": "全画面タイマー", "en-US": "Full Screen Timer"},
        "back": {"ja": "全画面タイマー", "en-US": "Full Screen Timer"},
        "intro": {
            "ja": "Holy App（以下「当方」）は、iOSアプリ「全画面タイマー」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。",
            "en-US": "Holy App (\"we\") provides the iOS app Full Screen Timer (the \"App\"). This policy explains how information is handled in the App.",
        },
        "data": section(
            paragraph(
                "本アプリでは、タイマーの時間、インターバル、繰り返し、音声、プリセット名、表示設定などを扱います。これらは本アプリの機能を提供するために端末内へ保存され、当方のサーバーへ送信・保存されません。"
            ),
            paragraph(
                "The App handles timer durations, intervals, repetitions, sounds, preset names, and display settings. This information is stored on your device to provide the App's features and is not sent to or stored on our servers."
            ),
        ),
        "analytics": section(
            paragraph(
                "本アプリは、広告配信のためGoogle AdMobを、機能改善や不具合の把握のためFirebase AnalyticsおよびFirebase Crashlyticsを利用しています。これらのサービスは端末情報、広告識別子、利用状況、クラッシュ情報、パフォーマンスなどを取得することがありますが、タイマー設定やプリセット名を当方が分析目的で取得することはありません。"
            ),
            paragraph(
                "The App uses Google AdMob for advertising and Firebase Analytics and Firebase Crashlytics for feature improvement and problem diagnosis. These services may collect device information, advertising identifiers, usage information, crash data, and performance data. We do not obtain your timer settings or preset names for analytics purposes."
            ),
        ),
    },
    "hiragana": {
        "name": {"ja": "平仮名ボード しゃべる50音表", "en-US": "Hiragana Board"},
        "back": {"ja": "平仮名ボード", "en-US": "Hiragana Board"},
        "intro": {
            "ja": "Holy App（以下「当方」）は、iOSアプリ「平仮名ボード しゃべる50音表」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。",
            "en-US": "Holy App (\"we\") provides the iOS app Hiragana Board (the \"App\"). This policy explains how information is handled in the App.",
        },
        "data": section(
            paragraph(
                "本アプリでは、ひらがなの入力、読み上げ、表示設定、学習に関する設定などを扱います。これらは本アプリの機能を提供するために端末内で処理され、当方のサーバーへ送信・保存されません。"
            ),
            paragraph(
                "The App handles hiragana entered for practice and speech, along with display and learning settings. This information is processed on your device to provide the App's features and is not sent to or stored on our servers."
            ),
        ),
        "analytics": section(
            paragraph(
                "本アプリは、広告配信のためGoogle AdMobを、クラッシュや不具合の把握のためFirebase Crashlyticsを利用しています。これらのサービスは広告識別子、端末情報、クラッシュ情報、パフォーマンスなどを取得することがありますが、入力した文字や学習内容を当方が取得することはありません。"
            ),
            paragraph(
                "The App uses Google AdMob for advertising and Firebase Crashlytics for crash and problem reporting. These services may collect advertising identifiers, device information, crash data, performance data, and other diagnostics. We do not obtain the characters or learning content you enter."
            ),
        ),
    },
    "katakana": {
        "name": {"ja": "片仮名ボード しゃべる50音表", "en-US": "Katakana Board"},
        "back": {"ja": "片仮名ボード", "en-US": "Katakana Board"},
        "intro": {
            "ja": "Holy App（以下「当方」）は、iOSアプリ「片仮名ボード しゃべる50音表」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。",
            "en-US": "Holy App (\"we\") provides the iOS app Katakana Board (the \"App\"). This policy explains how information is handled in the App.",
        },
        "data": section(
            paragraph(
                "本アプリでは、カタカナの入力、読み上げ、表示設定、学習に関する設定などを扱います。これらは本アプリの機能を提供するために端末内で処理され、当方のサーバーへ送信・保存されません。"
            ),
            paragraph(
                "The App handles katakana entered for practice and speech, along with display and learning settings. This information is processed on your device to provide the App's features and is not sent to or stored on our servers."
            ),
        ),
        "analytics": section(
            paragraph(
                "本アプリは、広告配信のためGoogle AdMobを、クラッシュや不具合の把握のためFirebase Crashlyticsを利用しています。これらのサービスは広告識別子、端末情報、クラッシュ情報、パフォーマンスなどを取得することがありますが、入力した文字や学習内容を当方が取得することはありません。"
            ),
            paragraph(
                "The App uses Google AdMob for advertising and Firebase Crashlytics for crash and problem reporting. These services may collect advertising identifiers, device information, crash data, performance data, and other diagnostics. We do not obtain the characters or learning content you enter."
            ),
        ),
    },
    "drawingciao": {
        "name": {"ja": "かんたんお絵描き - おえかきっチャオ", "en-US": "Easy Drawing - Drawing Ciao"},
        "back": {"ja": "おえかきっチャオ", "en-US": "Drawing Ciao"},
        "intro": {
            "ja": "Holy App（以下「当方」）は、iOSアプリ「かんたんお絵描き - おえかきっチャオ」（以下「本アプリ」）における利用者の情報の取り扱いについて、以下のとおり定めます。",
            "en-US": "Holy App (\"we\") provides the iOS app Easy Drawing - Drawing Ciao (the \"App\"). This policy explains how information is handled in the App.",
        },
        "data": section(
            paragraph(
                "本アプリでは、利用者が描いた絵や描画設定を端末内で扱います。作品は本アプリの機能を提供するために端末内で処理・保存され、当方のサーバーへ送信・保存されません。"
            ),
            paragraph(
                "The App handles drawings and drawing settings on your device. Drawings are processed and stored on your device to provide the App's features and are not sent to or stored on our servers."
            ),
        ),
        "permissions": section(
            paragraph(
                "作品を写真ライブラリへ保存する場合、写真へのアクセスを求めます。アクセスは利用者が許可した場合に限られ、保存先の写真ライブラリにおけるデータの取り扱いはAppleのポリシーに従います。"
            ),
            paragraph(
                "If you choose to save a drawing to your photo library, the App may ask for Photos access. Access occurs only with your permission, and data in the destination photo library is governed by Apple's policies."
            ),
        ),
        "analytics": section(
            paragraph(
                "本アプリは、広告配信およびアプリの動作・パフォーマンスの診断のため、第三者の広告・診断サービスを利用することがあります。これらのサービスは、広告識別子、端末ID、パフォーマンスデータ、その他の診断情報を取得することがあります。作品の内容を当方が取得・分析することはありません。"
            ),
            paragraph(
                "The App may use third-party advertising and diagnostic services to provide ads and diagnose app operation and performance. These services may collect advertising identifiers, device IDs, performance data, and other diagnostics. We do not obtain or analyze the content of your drawings."
            ),
        ),
    },
}


def policy_sections(app: dict) -> list[dict[str, str]]:
    sections = [
        {
            "heading": section("収集しない情報", "Information we do not collect"),
            "body": COMMON_NOT_COLLECTED,
        },
        {
            "heading": section("本アプリ内のデータ", "Data in the App"),
            "body": app["data"],
        },
    ]
    if "permissions" in app:
        sections.append({
            "heading": section("端末の権限", "Device permissions"),
            "body": app["permissions"],
        })
    if "sharing" in app:
        sections.append({
            "heading": section("共有機能", "Sharing features"),
            "body": app["sharing"],
        })
    if "purchase" in app:
        sections.append({
            "heading": section("アプリ内購入", "In-app purchases"),
            "body": app["purchase"],
        })
    if app.get("ads", True):
        sections.append({
            "heading": section("広告について", "Advertising"),
            "body": ADVERTISING,
        })
    if "analytics" in app:
        sections.append({
            "heading": section("利用状況の分析と診断", "Analytics and diagnostics"),
            "body": app["analytics"],
        })
    sections.extend([
        {"heading": section("第三者サービス", "Third-party services"), "body": GENERIC_THIRD_PARTY},
        {"heading": section("データの保存期間と削除", "Retention and deletion"), "body": GENERIC_RETENTION},
        {"heading": section("本ポリシーの変更", "Changes to this policy"), "body": CHANGES},
        {"heading": section("お問い合わせ", "Contact"), "body": CONTACT},
    ])
    return sections


def render(app_slug: str, app: dict, locale: str) -> str:
    meta = LOCALES[locale]
    name = app["name"][locale]
    back = app["back"][locale]
    title = f"{'プライバシーポリシー' if locale == 'ja' else 'Privacy Policy'} | {name}"
    h1 = "プライバシーポリシー" if locale == "ja" else "Privacy Policy"
    updated = UPDATED_JA if locale == "ja" else UPDATED_EN
    sections = policy_sections(app)
    body = []
    for index, item in enumerate(sections, start=1):
        heading = item["heading"][locale]
        content = item["body"][locale]
        body.append(f"  <h2>{index}. {heading}</h2>\n  {content}")
    lang_links = []
    for code, data in LOCALES.items():
        if code == locale:
            lang_links.append(f"    <span>{data['label']}</span>")
        else:
            lang_links.append(f"    <a href=\"{code}.html\">{data['label']}</a>")
    return f'''<!DOCTYPE html>
<html lang="{meta["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="../../assets/site.css">
</head>
<body>
<header class="site-head">
  <div class="wrap">
    <a class="brand" href="../../">Holy App</a>
    <a class="back" href="../../apps/{app_slug}.html">{html.escape(back)}</a>
  </div>
</header>
<main class="wrap-narrow doc">
  <h1>{h1}</h1>
  <p class="doc-app">{html.escape(name)}</p>
  <p class="doc-date">{updated}</p>

  <p>{app["intro"][locale]}</p>
{chr(10).join(body)}
  <nav class="langs">
{chr(10).join(lang_links)}
  </nav>
</main>
<footer class="site-foot">
  <div class="wrap">
    <p>&copy; 2026 Holy App</p>
  </div>
</footer>
</body>
</html>
'''


def main() -> None:
    total = 0
    for slug, app in APP_POLICIES.items():
        out_dir = ROOT / slug / "privacy"
        out_dir.mkdir(parents=True, exist_ok=True)
        for locale in LOCALES:
            (out_dir / f"{locale}.html").write_text(
                render(slug, app, locale), encoding="utf-8"
            )
            total += 1
    print(f"generated {total} pages for {len(APP_POLICIES)} apps")


if __name__ == "__main__":
    main()
