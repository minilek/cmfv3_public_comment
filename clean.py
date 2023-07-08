import json
from pathlib import Path
import sys

def main(filepaths):
    for path in filepaths:
        with open(path, 'r') as f:
            parsed = json.load(f)
            inner_json = parsed['d']['RenderExtendedListFormData']

        dest = path.replace('raw_data', 'clean_data')
        with open(dest, 'w') as f:
            f.write(inner_json)

if __name__ == "__main__":
    main(sys.argv[1:])
