import asyncio
from blouc import cli
from blouc import cmd

asyncio.run(cmd.run_with_args(cli.parse_args()))
