from emock import cli
from emock import cmd
import asyncio

asyncio.run(cmd.run_with_args(cli.args))
