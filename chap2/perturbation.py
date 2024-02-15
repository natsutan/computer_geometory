import os

from PIL import Image, ImageFont
from PIL.ImageDraw import ImageDraw


def signed_area(p1, p2, p3):
    return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p3[0] - p1[0]) * (p2[1] - p1[1])



def perturbation(p1, p2, p3, epsilon=0.1, M=2):
    p1s = (p1[0] + epsilon ** (M * 1), p1[1] + epsilon ** (M * 4))
    p2s = (p2[0] + epsilon ** (M * 2), p2[1] + epsilon ** (M * 5))
    p3s = (p3[0] + epsilon ** (M * 3), p3[1] + epsilon ** (M * 6))


    return p1s, p2s, p3s




p1 = (10.0, 10.0)
p2 = (30.0, 10.0)
p3 = (15.0, 10.0)
p1s, p2s, p3s = perturbation(p1, p2, p3)
print(p1s, p2s, p3s)

area = signed_area(p1s, p2s, p3s)
print(f'p1->p2->p3 {area}')

# for y in range(20):
#     p2 = (15.0, float(y))
#     p0s, p1s, p2s = perturbation(p0, p1, p2)
#     area = signed_area(p0s, p1s, p2s)
#     print(f'p0->p1->p2 {area}')