If you need to install UV:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

configure the client as follows:
```json
 "Chess": {
	  "command": "uvx",
	  "args": [
		"--from",
		"git+https://github.com/UriWise/chess_dot_com_mcp_server.git",
		"chess"
		],
		"env": {
		"PATHEXT": ".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC;.PY;.PYW"
      }
```