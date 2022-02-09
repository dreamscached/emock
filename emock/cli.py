import argparse
import pathlib
import typing

_Dimensions = typing.Tuple[int, int]


def dimension(arg: str) -> _Dimensions:
    v = tuple(map(int, arg.split("x")))
    if len(v) != 2:
        raise ValueError("dimension must be two numbers separated by x (like 8x4)")
    return v[0], v[1]


_parser = argparse.ArgumentParser(
    prog="emock", description="convert image into square emote mosaic")
_parser.add_argument(
    "image", type=pathlib.Path, help="path to image to convert")
_parser.add_argument(
    "-b", "--bubblewrap", action="store_true", help="wrap block emotes into spoilers")
_parser.add_argument(
    "-s", "--size", type=dimension, default=(8, 4), help="dimensions of output blocky art")

args = _parser.parse_args()
