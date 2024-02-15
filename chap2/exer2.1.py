from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw

def signed_area(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

# 3点, x, p1, p2が与えられたとき、xop1とxop2の角度がどちらが大きいかを判定する。
# ただし、xは原点であるとする。
def is_large_xop1(p1, p2, x):
    """
    xop1とxop2の角度がどちらが大きいかを判定する。
    xop1が大きいときはTrue、そうでないときはFalseを返す
    :param p1:
    :param p2:
    :param x:
    :return:
    """
    area = signed_area((0, 0), p1, p2)
    if area > 0:
        return signed_area((0, 0), p1, x) > 0 and signed_area((0, 0), p2, x) > 0
    else:
        return signed_area((0, 0), p1, x) < 0 and signed_area((0, 0), p2, x) < 0


p2 = (310, 190)
p1 = (400, 120)

o = (0, 0)
x = (100, 100)


# 500x500の白い画像を作成
img = Image.new("RGB", (500, 500), (255, 255, 255))
draw = ImageDraw(img)
# o->p1の直線を描画
draw.line([o, p1], fill=(0, 0, 0))
# o->p2の直線を描画
draw.line([o, p2], fill=(0, 0, 0))
# o->xの直線を描画
draw.line([o, x], fill=(0, 0, 0))

# xを描画
size = 2
xy = (x[0] - size, x[1] - size, x[0] + size, x[1] + size)
draw.ellipse(xy, fill=(255, 0, 0))
# p1を描画
size = 2
xy = (p1[0] - size, p1[1] - size, p1[0] + size, p1[1] + size)
draw.ellipse(xy, fill=(255, 0, 0))
# p2を描画
size = 2
xy = (p2[0] - size, p2[1] - size, p2[0] + size, p2[1] + size)
draw.ellipse(xy, fill=(255, 0, 0))


# 座標近くにp1, p2, xと書く
font = ImageFont.truetype("arial.ttf", size=8)
draw.text((p1[0] + 5, p1[1] + 5), "p1", font=font, fill=(255, 0, 0))
draw.text((p2[0] + 5, p2[1] + 5), "p2", font=font, fill=(255, 0, 0))
draw.text((x[0] + 5, x[1] + 5), "x", font=font, fill=(255, 0, 0))

# 画像を保存する
img.save("result/exer2.1.png")

ret = is_large_xop1(p1, p2, x)
if ret:
    print("xop1が大きい")
else:
    print("xop2が大きい")


