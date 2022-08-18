# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import asyncio
import logging

from jsonrpcclient import Ok, parse_json, request_json
import websockets


async def main():
    async with websockets.connect("ws://localhost:2087") as ws:
        await ws.send(request_json("initialize", params={"workspaceFolders": [
            {"uri": "/home/mikel/.virtualenvs/lsp/lib/python3.10/site-packages/pylsp", "name": "pylsp", }, ], }))
        response = parse_json(await ws.recv())

    if isinstance(response, Ok):
        print(response.result)
    else:
        logging.error(response.message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
