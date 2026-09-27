# genpark-voice-vad

Energy and transcript heuristics for voice turn endpoint detection.

This is a heuristic endpoint detector over **precomputed dB energies and a transcript**. It does not decode audio, transcribe speech, or run a trained VAD model. Confidence values are heuristic scores, not calibrated probabilities.

## Install from the GitHub release

Python 3.9 or newer. The library and stdio MCP server have no runtime dependencies.

```sh
python -m pip install https://github.com/Alpha-Park/genpark-voice-turn-taking-endpoint-detector-skill/releases/download/v1.0.1/genpark_voice_vad-1.0.1-py3-none-any.whl
```

PyPI publication is pending account setup. The intended PyPI project is `genpark-voice-vad`;
do not assume `pip install genpark-voice-vad` is available until the project is published.

## Python usage

```python
from genpark_voice_vad import VoiceTurnTakingEndpointDetector
client = VoiceTurnTakingEndpointDetector()
print(client.run_benchmark_turn_detection())
```

## MCP stdio configuration

After installing the wheel, configure your MCP client with the installed command:

```json
{
  "mcpServers": {
    "genpark-voice-vad": {
      "command": "genpark-voice-vad",
      "args": []
    }
  }
}
```

If the command is not on PATH, use its absolute path or `python -m genpark_voice_vad`
with the same interpreter where you installed the wheel.
The GitHub release also contains a `.mcpb` bundle for clients supporting desktop extensions.
That bundle requires a Python 3.9+ interpreter on PATH; it bundles the server source.

Available tools: `analyze_turn_status`, `calibrate_acoustic_thresholds`, `predict_semantic_closure`, `run_benchmark_turn_detection`.
`tools/list` returns required arguments and JSON schemas.
Each MCP process holds its own state. Benchmark tools use isolated instances.

## Development

```sh
python -m unittest discover -s tests
python -m pip install mcp
python tests/check_mcp.py
python -m pip install build twine
python -m build
python -m twine check dist/*
```

`python mcp_server.py --test` runs the deterministic example; it is not a protocol conformance test.
The MCP client check exercises initialize, tools/list, tools/call and ping over stdio.

## Distribution

GitHub source and release artifacts are the primary distribution until PyPI is configured.
Registry submissions are tracked separately; a manifest is not proof of registry acceptance.
See [PUBLISHING.md](PUBLISHING.md) for the repeatable PyPI workflow.

MIT license. Maintained by [GenPark](https://genpark.ai).

<!-- mcp-name: io.github.Alpha-Park/genpark-voice-vad -->
