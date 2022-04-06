from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw

font = ImageFont.truetype("arial.ttf", size=8)

Points = [
    [310, 190],
    [80,320],
    [310, 310],
    [380, 110],
    [480, 300],
    [250, 250],
    [190, 200],
    [250, 450],
    [120, 100]
]


def main():
    img = Image.new("RGB", (500, 500), (255, 255, 255))
    draw = ImageDraw(img)
    i = 1
    for p in Points:
        size = 2
        xy = (p[0]-size, p[1]-size, p[0]+size, p[1]+size)
        draw.ellipse(xy, fill=(255, 0, 0))
        draw.text((p[0]+5, p[1]+5), str(i), font=font, fill=(255, 0, 0))
        i = i + 1

    img.save("result/convex.png")

    pass

if __name__ == '__main__':
    main()