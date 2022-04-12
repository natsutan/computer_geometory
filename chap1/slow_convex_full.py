import itertools

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw

font = ImageFont.truetype("arial.ttf", size=8)

Points = [
    [310, 190],
    [80, 320],
    [310, 310],
    [380, 110],
    [480, 300],
    [250, 250],
    [190, 200],
    [250, 450],
    [120, 100]
]


def draw_points(point):
    img = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw(img)
    i = 1
    for p in Points:
        size = 2
        xy = (p[0] - size, p[1] - size, p[0] + size, p[1] + size)
        draw.ellipse(xy, fill=(255, 0, 0))
        draw.text((p[0] + 5, p[1] + 5), str(i), font=font, fill=(255, 0, 0))
        i = i + 1

    img.save("result/convex.png")


def make_rlist(points, pair):
    p0 = pair[0]
    p1 = pair[1]
    riter = filter(lambda p: not ((p[0] == p0[0] and p[1] == p0[1]) or (p[0] == p1[0] and p[1] == p1[1])), points)

    return riter

# https://imagingsolution.blog.fc2.com/blog-entry-51.html
def is_leftside(p, q, r):
    return True


def slow_convex_hull(points):
    e = []
    for pair in itertools.combinations(points, 2):
        valid = True
        rlist = make_rlist(points, pair)
        for r in rlist:
            if is_leftside(pair[0], pair[1], r):
                valid = False

        if valid:
            e.append(pair)

    return e


def main():
    draw_points(Points)
    result = slow_convex_hull(Points)
    print(result)


if __name__ == '__main__':
    main()
