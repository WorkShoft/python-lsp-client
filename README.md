Spec
===============
https://microsoft.github.io/language-server-protocol/specifications

Repos
===============
https://github.com/microsoft/language-server-protocol
https://github.com/explodinglabs/jsonrpcclient
https://github.com/python-lsp/python-lsp-server
https://github.com/python-lsp/python-lsp-jsonrpc
https://websockets.readthedocs.io

Packages
===============
'pycodestyle'
'mccabe'
'pydocstyle'
'pyflakes'
'pylint'
'rope'
'yapf'

Imports
===============
import requests
from jsonrpcclient import parse, request

Websocket client example
===============
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://0.0.0.0:2087/",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt
    rel.dispatch()

Parse response
===============
parsed = parse(response.json())

Initialize
===============
response = requests.post("http://localhost:2087", json=request("initialize", params={"workspaceFolders": [{"uri": "/home/mikel/.virtualenvs/lsp/lib/python3.10/site-packages/pylsp", "name": "pylsp", }, ], }))

/home/mikel/.virtualenvs/lsp/lib/python3.10/site-packages/pylsp

Code action
===============	
response = requests.post("http://localhost:2087", json=request("textDocument/codeAction", params={"textDocument": {"uri": "asdfadf"}, "range": {"start": {"line": 5, "character": 23}, "end": {"line": 6, "character": 0, }}, "context": {}}))
