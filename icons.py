"""ホーム画面用アイコンを Lucifer のカード画像から切り出して dist/icons/ に書き出す。

Pillow が必要（python3 -m pip install pillow）。サイトの起動には不要。
"""
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).parent
SOURCE = ROOT / "dist/assets/p55-0.webp"
OUT = ROOT / "dist/icons"

# 星・頭・青い翼が入る正方形（元画像 197x325 の座標）
CROP = (18, 30, 180, 192)
# Android が外周を丸く削っても星の先端が残るよう、広めに取った正方形
CROP_MASKABLE = (8, 20, 190, 202)

ICONS = [
    ("icon-192.png", CROP, 192),
    ("icon-512.png", CROP, 512),
    ("maskable-512.png", CROP_MASKABLE, 512),
    ("apple-touch-icon.png", CROP, 180),
    ("favicon-32.png", CROP, 32),
]


def main() -> None:
    OUT.mkdir(exist_ok=True)
    card = Image.open(SOURCE).convert("RGB")
    for name, box, size in ICONS:
        card.crop(box).resize((size, size), Image.LANCZOS).save(OUT / name, optimize=True)
        print(OUT / name)


if __name__ == "__main__":
    main()
