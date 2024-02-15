from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw


def signed_area(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])


# 線分の交差判定を行う
def is_cross(p1, p2, p3, p4):
    d1 = signed_area(p1, p2, p3)
    d2 = signed_area(p1, p2, p4)
    d3 = signed_area(p3, p4, p1)
    d4 = signed_area(p3, p4, p2)

    if d1 * d2 < 0 and d3 * d4 < 0:
        return True
    else:
        return False


# 交差する線分を2本定義する
l1 = [(100, 100), (400, 400)]
l2 = [(100, 400), (400, 100)]

# 線分の交差チェックを行い、結果を表示する。
print(is_cross(l1[0], l1[1], l2[0], l2[1]))

# 交差しない線分を2本用意する。
l3 = [(100, 100), (400, 100)]
l4 = [(100, 400), (400, 400)]

# 線分の交差チェックを行い、結果を表示する。
print(is_cross(l3[0], l3[1], l4[0], l4[1]))

# 500x500の白い画像を作成
img = Image.new("RGB", (500, 500), (255, 255, 255))

# l1とl2を描画して、result/line_segment_intersection.pngとして保存する
draw = ImageDraw(img)
draw.line(l1, fill=(0, 0, 0))
draw.line(l2, fill=(0, 0, 0))
img.save("result/line_segment_intersection.png")

# 500x500の白い画像を作成
img = Image.new("RGB", (500, 500), (255, 255, 255))
# l3とl4を描画して、result/line_segment_intersection2.pngとして保存する


draw = ImageDraw(img)
draw.line(l3, fill=(0, 0, 0))
draw.line(l4, fill=(0, 0, 0))
img.save("result/line_segment_intersection2.png")
