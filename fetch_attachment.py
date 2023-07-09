from pathlib import Path
import json
import subprocess
import sys
import time

FETCH_ATTACHMENT_PATH = Path.cwd() / "fetch_attachment.sh"
FETCH_ATTACHMENT_COMMAND = FETCH_ATTACHMENT_PATH.read_text()


def main(filepaths):
    for path in filepaths:
        with open(path, "r") as f:
            parsed = json.load(f)
            attachments = parsed["ListData"]["Attachments"]
            if not attachments:
                continue

            for attachment in attachments["Attachments"]:
                command = (
                    FETCH_ATTACHMENT_COMMAND.replace(
                        "URL_PREFIX", attachments["UrlPrefix"].replace(' ', '%20')
                    )
                    .replace("FILE_NAME", attachment["FileName"].replace(' ', '%20').replace('(', '%28').replace(')', '%29'))
                    .replace("ITEM_ID", str(parsed["ItemAttributes"]["Id"]))
                )

                subprocess.run(["bash", "-c", command])
                time.sleep(1)


if __name__ == "__main__":
    main(sys.argv[1:])
