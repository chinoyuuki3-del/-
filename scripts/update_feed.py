#!/usr/bin/env python3
import json
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

FEATURED_GROUPS = [
  [
    "troll-social",
    "friend-messenger",
    "stream-studio",
    "online-poll",
    "friend-radar",
    "online-board"
  ],
  [
    "notes",
    "todo",
    "flashcards",
    "quiz-maker",
    "school-schedule",
    "project-board"
  ],
  [
    "whiteboard",
    "pixel-art",
    "beat-pad",
    "mini-piano",
    "thumbnail-maker",
    "meme-caption"
  ],
  [
    "troll-arcade",
    "reaction-test",
    "clicker",
    "number-guess",
    "rps",
    "snake"
  ],
  [
    "calculator",
    "timer",
    "unit-converter",
    "random-picker",
    "dice",
    "shopping-list"
  ],
  [
    "friend-plaza",
    "friend-house",
    "map-pinboard",
    "project-lab",
    "event-planner",
    "coin-wallet"
  ],
  [
    "voice-recorder",
    "photo-booth",
    "media-gallery",
    "soundboard",
    "podcast-planner",
    "stream-studio"
  ]
]
DEAL_GROUPS = [
  [{"id": "online-poll", "price": 0, "label": "本日無料"}, {"id": "thumbnail-maker", "price": 30, "label": "日替わりセール"}],
  [{"id": "flashcards", "price": 0, "label": "勉強応援"}, {"id": "project-board", "price": 40, "label": "本日割引"}],
  [{"id": "pixel-art", "price": 20, "label": "創作セール"}, {"id": "beat-pad", "price": 0, "label": "本日無料"}],
  [{"id": "reaction-test", "price": 0, "label": "ゲームデー"}, {"id": "troll-arcade", "price": 50, "label": "特別価格"}],
  [{"id": "unit-converter", "price": 0, "label": "便利ツール無料"}, {"id": "timer", "price": 20, "label": "日替わりセール"}],
  [{"id": "friend-house", "price": 0, "label": "Friend Day"}, {"id": "project-lab", "price": 45, "label": "共同制作割引"}],
  [{"id": "voice-recorder", "price": 0, "label": "配信応援"}, {"id": "photo-booth", "price": 35, "label": "本日割引"}]
]
MESSAGES = [
  "オンライン通信ソフトを中心に配信中。友達とつながる機能を試してみよう！",
  "今日は勉強・計画ツール特集。学校やプロジェクトに使えるソフトをまとめました。",
  "クリエイティブデー！絵・音・画像制作ソフトがおすすめです。",
  "ゲームデー開催中。無料ゲームと日替わりチャレンジを配信しています。",
  "便利ツール特集。毎日の作業を少し楽にするソフトを選びました。",
  "Friend Worldデー。友達との交流や共同制作向けソフトを配信中です。",
  "配信・メディア特集。録音、撮影、配信準備を楽しめます。"
]
HEADLINES = [
  "📡 今日のオンライン通信特集",
  "📚 今日の勉強・計画特集",
  "🎨 今日のクリエイティブ特集",
  "🎮 今日のゲーム配信",
  "🧰 今日の便利ツール特集",
  "🌐 今日のFriend World特集",
  "🎥 今日の配信・メディア特集"
]

now = datetime.now(ZoneInfo("Asia/Tokyo"))
index = now.toordinal() % len(FEATURED_GROUPS)
feed = {
  "schema": 1,
  "channel": "troll-shopping-live",
  "generatedAt": now.isoformat(),
  "timezone": "Asia/Tokyo",
  "daily": {
    "date": now.strftime("%Y-%m-%d"),
    "headline": HEADLINES[index],
    "message": MESSAGES[index],
    "featuredIds": FEATURED_GROUPS[index],
    "deals": DEAL_GROUPS[index]
  },
  "extraApps": [
    {
      "id": "live-daily-board",
      "icon": "📡",
      "name": "オンライン日替わり掲示板",
      "category": "オンライン配信",
      "kind": "board",
      "price": 0,
      "version": "1.0.0",
      "badge": "LIVE",
      "description": "オンライン配信のお知らせや今日の予定を端末内で整理できます。"
    },
    {
      "id": "daily-challenge",
      "icon": "🏆",
      "name": "デイリーチャレンジ",
      "category": "オンライン配信",
      "kind": "game",
      "price": 0,
      "version": "1.0.0",
      "badge": "DAILY",
      "description": "毎日変わるおすすめゲームから今日の記録に挑戦します。"
    }
  ]
}
Path("troll-shopping-feed.json").write_text(
  json.dumps(feed, ensure_ascii=False, indent=2) + "\n",
  encoding="utf-8"
)
