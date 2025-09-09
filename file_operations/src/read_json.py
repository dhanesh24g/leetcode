import json
from pathlib import Path

def read_json():

    file_root_path = Path(__file__).parent.parent / "practice_files"
    file_path = file_root_path / "system_logs.log"

    documents = []
    with open(file=file_path, mode="r") as f:
        for line in f.readlines():
            documents.append(line)

    # print(documents)
    errors = []
    for doc in documents:
        data = json.loads(doc)
        if data.get("level") == "ERROR":
            errors.append(data["event"])

    print(errors)

read_json()