import os
from pathlib import Path
import json


script_dir = Path(__file__).parent


tile_files = []

for file in os.listdir(script_dir):
    if file.startswith("tile"):
        tile_files.append(file)

json_file = script_dir / "data.json"

if json_file.exists():
    with open(json_file, "r") as f:
        content = f.read().strip()
        data = json.loads(content) if content else []
else:
    data = []

data.extend(tile_files)

with open(json_file, "w") as f:
    json.dump(data, f, indent=2)
