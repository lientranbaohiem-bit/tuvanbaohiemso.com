"""Tao anh dai dien 1200x630 cho bai moi (tu 07/10/2026).

Dung: python3 tao_anh_bia.py <slug> "<cau hoi>" <anh-nen.jpg>
Ghi ra assets/img/bai/<slug>.jpg. Chi dung cho bai moi, khong sua bai cu.
"""
import os
import sys
import textwrap
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1200, 630
FONT_B = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_R = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def cover(src, w, h):
    im = Image.open(src).convert("RGB")
    r = max(w / im.width, h / im.height)
    im = im.resize((int(im.width * r) + 1, int(im.height * r) + 1), Image.LANCZOS)
    x = (im.width - w) // 2
    y = (im.height - h) // 2
    return im.crop((x, y, x + w, y + h))


def tao(slug, cau_hoi, nen):
    im = cover(nen, W, H).filter(ImageFilter.GaussianBlur(1.5))
    # lop phu toi o nua trai de chu doc ro
    lop = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lop)
    for x in range(W):
        a = int(215 - 150 * (x / W))
        d.line([(x, 0), (x, H)], fill=(12, 38, 64, max(a, 60)))
    im = Image.alpha_composite(im.convert("RGBA"), lop)
    d = ImageDraw.Draw(im)
    size = 58
    while size > 34:
        f = ImageFont.truetype(FONT_B, size)
        dong = textwrap.wrap(cau_hoi, width=int(1700 / size))
        cao = len(dong) * int(size * 1.25)
        if len(dong) <= 4 and cao < 360:
            break
        size -= 4
    y = (H - cao) // 2 - 30
    for t in dong:
        d.text((70, y), t, font=f, fill=(255, 255, 255))
        y += int(size * 1.25)
    d.rectangle([70, H - 110, 150, H - 104], fill=(242, 169, 59))
    d.text((70, H - 90), "Lien Tran - Đại lý AIA  ·  tuvanbaohiemso.com",
           font=ImageFont.truetype(FONT_R, 26), fill=(230, 236, 242))
    os.makedirs("assets/img/bai", exist_ok=True)
    out = "assets/img/bai/%s.jpg" % slug
    im.convert("RGB").save(out, "JPEG", quality=82, optimize=True, progressive=True)
    return out


if __name__ == "__main__":
    print(tao(sys.argv[1], sys.argv[2], sys.argv[3]))
