from pathlib import Path
import json
import subprocess
import time

CURL_COMMAND_PATH = Path.cwd() / "scrape_one.sh"
COMMAND = CURL_COMMAND_PATH.read_text();
RESPONSES = Path.cwd() / "responses.json"

with RESPONSES.open('r') as f:
    parsed = json.load(f)

    for item in parsed:
        id = item["ID"]
        # left pad
        if len(id) < 3:
            id = '0' * (3 - len(id)) + id

        command = COMMAND.replace("ITEM_ID", id)
        subprocess.run(["bash", "-c", command])
        time.sleep(1)

