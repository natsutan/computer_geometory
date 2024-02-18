# perpendicular bisector
from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
import mylib.leda as leda


def main():
    # ２点 p0, p1の定義
    p0 = leda.Point(200, 400)
    p1 = leda.Point(400, 120)

    # 500x500の白い画像を作成
    img = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw(img)

    # p0, p1の中点を求める
    m01 = leda.midpoint(p0, p1)

    # p0, p1を通る直線を描画する。直線は画像の端まで伸ばす。
    draw.line([0, p0.y - (p1.y - p0.y) * p0.x / (p1.x - p0.x), 500, p0.y + (p1.y - p0.y) * (500 - p0.x) / (p1.x - p0.x)], fill=(0, 0, 0))

    # p0をm01を中心に９０度回転させた座標を計算する。
    p2 = p0.rotate(m01, 90)
    p3 = p1.rotate(m01, 90)

    # p2, p3を通る直線を描画
    draw.line([p2.x, p2.y, p3.x, p3.y], fill=(255, 0, 0))

    # p0, p1を赤点で描画
    size = 2
    xy = (p0.x - size, p0.y - size, p0.x + size, p0.y + size)
    draw.ellipse(xy, fill=(255, 0, 0))
    xy = (p1.x - size, p1.y - size, p1.x + size, p1.y + size)
    draw.ellipse(xy, fill=(255, 0, 0))

    # p2, p3を青で描画
    size = 2
    xy = (p2.x - size, p2.y - size, p2.x + size, p2.y + size)
    draw.ellipse(xy, fill=(0, 0, 255))
    xy = (p3.x - size, p3.y - size, p3.x + size, p3.y + size)
    draw.ellipse(xy, fill=(0, 0, 255))



    # result/exer3.2.pngという名前でresultフォルダに保存
    img.save("result/exer3.2.png")



if __name__ == "__main__":
    main()