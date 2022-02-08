import argparse
import pathlib
import typing

Dimensions = typing.Tuple[int, int]


# noinspection PyTypeChecker
def dimension(arg: str) -> Dimensions:
    return tuple(map(int, arg.split("x")))


_parser = argparse.ArgumentParser(prog="bioblocks", description="build Discord bio of blocky emotes")
_parser.add_argument("image", type=pathlib.Path, help="path to image to convert to blocks")
_parser.add_argument("-b", "--bubblewrap", action="store_true", help="wrap block emotes into spoilers")
_parser.add_argument("-s", "--size", type=dimension, default=(8, 4), help="dimensions of output blocky art")


def parse_args() -> argparse.Namespace:
    return _parser.parse_args()
