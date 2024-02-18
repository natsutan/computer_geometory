from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw
import mylib.leda as leda


def main():
    # 3点 p0, p1, p2の定義
    p0 = leda.Point(200, 400)
    p1 = leda.Point(400, 120)
    p2 = leda.Point (110, 190)

    # 500x500の白い画像を作成
    img = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw(img)

    # p0, p1の中点を求める
    m01 = leda.midpoint(p0, p1)
    # p0, p2の中点を求める
    m02 = leda.midpoint(p0, p2)
    # p1, p2の中点を求める
    m12 = leda.midpoint(p1, p2)

    # p2とm01の直線を描画
    draw.line([p2.x, p2.y, m01.x, m01.y], fill=(255, 0, 0))
    # p0とm12の直線を描画
    draw.line([p0.x, p0.y, m12.x, m12.y], fill=(255, 0, 0))
    # p1とm02の直線を描画
    draw.line([p1.x, p1.y, m02.x, m02.y], fill=(255, 0, 0))


    # 三角形を描画
    draw.line([p0.x, p0.y, p1.x, p1.y], fill=(0, 0, 0))
    draw.line([p1.x, p1.y, p2.x, p2.y], fill=(0, 0, 0))
    draw.line([p2.x, p2.y, p0.x, p0.y], fill=(0, 0, 0))

    # 座標近くにp0, p1, p2と書く
    font = ImageFont.truetype("arial.ttf", size=8)
    draw.text((p0.x + 5, p0.y + 5), "p0", font=font, fill=(255, 0, 0))
    draw.text((p1.x + 5, p1.y + 5), "p1", font=font, fill=(255, 0, 0))
    draw.text((p2.x + 5, p2.y + 5), "p2", font=font, fill=(255, 0, 0))


    # exer3.1.pngという名前でresultフォルダに保存
    img.save("result/exer3.1.png")


if __name__ == "__main__":
    main()