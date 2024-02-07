from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw


def signed_area(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])

# 500x500の白い画像を作成
img = Image.new("RGB", (500, 500), (255, 255, 255))

# 画像に描画するためのオブジェクトを作成
draw = ImageDraw(img)

# 三角形の頂点3つを宣言する
p1 = (310, 190)
p2 = (80, 320)
p3 = (310, 310)

# 三角形を描画する
draw.polygon([p1, p2, p3], outline=(0, 0, 0))

# 座標近くにp0, p1, p2と書く
font = ImageFont.truetype("arial.ttf", size=8)
draw.text((p1[0] + 5, p1[1] + 5), "p1", font=font, fill=(255, 0, 0))
draw.text((p2[0] + 5, p2[1] + 5), "p2", font=font, fill=(255, 0, 0))
draw.text((p3[0] + 5, p3[1] + 5), "p3", font=font, fill=(255, 0, 0))


# 画像を保存する
img.save("result/triangle.png")

# 三角形の符号付き面積を計算する
area = signed_area(p1, p2, p3)
print(f'p1->p2->p3 {area}')

# 三角形の符号付き面積を計算する
area = signed_area(p1, p3, p2)
print(f'p1->p3->p2 {area}')




