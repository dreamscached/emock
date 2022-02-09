import math
import typing
import collections
import functools

Pixel = typing.Tuple[int, int, int]
Color = collections.namedtuple("Color", ("r", "g", "b"))

_blocks: typing.List[typing.Tuple[str, Color]] = [
    ("green", Color(r=0x7c, g=0xb3, b=0x42)),
    ("brown", Color(r=0xb7, g=0x6d, b=0x54)),
    ("blue", Color(r=0x21, g=0x96, b=0xf3)),
    ("red", Color(r=0xf4, g=0x43, b=0x36)),
    ("purple", Color(r=0xab, g=0x47, b=0xbc)),
    ("orange", Color(r=0xff, g=0x98, b=0x00)),
    ("yellow", Color(r=0xff, g=0xcc, b=0x32)),
    ("black_large", Color(r=0x42, g=0x42, b=0x42)),
    ("white_large", Color(r=0xe0, g=0xe0, b=0xe0))]


@functools.lru_cache(maxsize=1000)
def get_block(rgb: Color) -> str:
    return sorted(
        map(lambda it: (it[0], _color_distance(rgb, it[1])), _blocks),
        key=lambda it: it[1])[0][0]


def _color_distance(px: Pixel, c2: Color) -> float:
    return math.sqrt(
        math.pow(px[0] - c2.r, 2) +
        math.pow(px[1] - c2.g, 2) +
        math.pow(px[2] - c2.b, 2))
