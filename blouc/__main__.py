from blouc import cli
from blouc import cmd
import asyncio

asyncio.run(cmd.run_with_args(cli.args))
