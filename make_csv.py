from pathlib import Path
import json
import sys
import csv


def make_attachment_link(p, idx):
    attachments = p["ListData"]["Attachments"]
    if not attachments:
        return ""

    id = p["ItemAttributes"]["Id"]
    if not idx < len(attachments["Attachments"]):
        return ""

    filename = attachments["Attachments"][idx]["FileName"]
    return f"https://github.com/minilek/cmfv3_public_comment/blob/master/attachments/{id}_{filename}"


FIELDS = [
    ("Name", lambda p: p["ListData"]["Name"]),
    ("Organization", lambda p: p["ListData"]["Organization"]),
    ("Email", lambda p: p["ListData"]["Email"]),
    ("Topic", lambda p: p["ListData"]["Topic"]),
    ("Stance", lambda p: p["ListData"]["StanceontheMatter"]),
    ("Comment", lambda p: p["ListData"]["Comments"]),
    ("Title", lambda p: p["ListData"]["Title"]),
    ("Created at", lambda p: p["ListData"]["Created"]),
    ("Attachment 1 Link", lambda p: make_attachment_link(p, idx=0)),
    ("Attachment 2 Link", lambda p: make_attachment_link(p, idx=1)),
    ("Attachment 3 Link", lambda p: make_attachment_link(p, idx=2)),
    ("Attachment 4 Link", lambda p: make_attachment_link(p, idx=3)),
]


def main(filepaths):
    with open("comments.csv", "w", newline="") as csvfile:
        fieldnames = [f[0] for f in FIELDS]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for path in filepaths:
            with open(path, "r") as f:
                parsed = json.load(f)
                row_dict = {}
                for fieldname, getter in FIELDS:
                    row_dict[fieldname] = getter(parsed)
            writer.writerow(row_dict)


if __name__ == "__main__":
    main(sys.argv[1:])
