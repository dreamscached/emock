import argparse

from PIL import Image
from emock import color


async def run_with_args(args: argparse.Namespace) -> None:
    with args.image.open("rb") as fp:
        im = Image.open(fp)
        rgb = im.convert("RGB").resize(args.size, Image.NEAREST)

    print("\n".join("".join(_process_block(color.get_block(rgb.getpixel((x, y))), args)
                            for x in range(rgb.width)) for y in range(rgb.height)))


def _process_block(block: str, args: argparse.Namespace) -> str:
    res = [":", block, "_square", ":"]

    if args.bubblewrap:
        res.insert(0, "||")
        res.append("||")

    return "".join(res)
