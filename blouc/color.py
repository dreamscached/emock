import math
import typing

Color = typing.Tuple[int, int, int]

_square_map: typing.Dict[str, Color] = dict(
    green=(0x7c, 0xb3, 0x42),
    brown=(0xb7, 0x6d, 0x54),
    blue=(0x21, 0x96, 0xf3),
    red=(0xf4, 0x43, 0x36),
    purple=(0xab, 0x47, 0xbc),
    orange=(0xff, 0x98, 0x00),
    yellow=(0xff, 0xcc, 0x32),
    black_large=(0x42, 0x42, 0x42),
    white_large=(0xe0, 0xe0, 0xe0))


def get_square(rgb: Color) -> str:
    return sorted(map(lambda it: (it[0], _dist(rgb, it[1])), _square_map.items()), key=lambda it: it[1])[0][0]


def _dist(c1: Color, c2: Color) -> float:
    return math.sqrt(math.pow(c1[0] - c2[0], 2) + math.pow(c1[1] - c2[1], 2) + math.pow(c1[2] - c2[2], 2))
