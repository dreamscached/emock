import argparse
import typing

from PIL import Image
from emock import color


async def run_with_args(args: argparse.Namespace) -> None:
    with args.image.open("rb") as fp:
        im = Image.open(fp)
        rgb = im.convert("RGB")

    if not args.no_resize:
        rgb = rgb.resize(args.size, Image.NEAREST)

    print("\n".join("".join(_process_block(color.get_block(rgb.getpixel((x, y))), args)
                            for x in range(rgb.width)) for y in range(rgb.height)))


def _process_block(block: typing.Tuple[str, str], args: argparse.Namespace) -> str:
    if not args.emoji:
        res = [":", block[0], ":"]
    else:
        res = [block[1]]

    if args.bubblewrap:
        res.insert(0, "||")
        res.append("||")

    return "".join(res)
