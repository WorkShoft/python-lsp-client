# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import asyncio
import logging

from jsonrpcclient import Ok, parse_json, request_json
import websockets


async def initialize(ws):
    await ws.send(request_json("initialize", params={"workspaceFolders": [
        {"uri": "/home/mikel/PycharmProjects/lspTest/", "name": "pylsp", }, ], }))


async def code_action(ws):
    await ws.send(request_json("textDocument/codeAction", params={
        "textDocument": {
            "uri": "/home/mikel/PycharmProjects/lspTest/hello_world.py",
            "text": "logging.error('test')",
            "languageId": "python",
        },
        "range": {
            "start": {
                "line": 2, "character": 0,
            },
            "end": {
                "line": 3, "character": 35,
            },
        },
    }))


async def execute_command(ws):
    await ws.send(request_json("workspace/executeCommand", params={
        "command": "pylsp_rope.refactor.extract.method",
        "arguments": [
            {
                "document_uri": "/home/mikel/PycharmProjects/lspTest/hello_world.py",
                "range": {
                    "start": {
                        "line": 2, "character": 0,
                    },
                    "end": {
                        "line": 3, "character": 35,
                    },
                }, "global_": False,
                "similar": False
            }
        ]
    }
                               ))


async def process_response(ws):
    response = parse_json(await ws.recv())

    if isinstance(response, Ok):
        print(response.result)
    else:
        logging.error(response.message)


async def main():
    request_id = 0
    async with websockets.connect("ws://localhost:2087") as ws:
        await initialize(ws)
        await code_action(ws)
        await execute_command(ws)
        async for message in ws:
            request_id += 1
            print(request_id)
            print(message)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    asyncio.run(main())
