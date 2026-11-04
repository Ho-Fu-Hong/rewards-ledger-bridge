import json
from pathlib import Path

import requests

CONFIG = json.loads((Path(__file__).resolve().parents[1] / "config" / "appsettings.json").read_text())


def push_batch(entries):
    ledger = CONFIG["Ledger"]
    response = requests.post(ledger["BaseUrl"] + "/batches", json={"entries": entries},
                             auth=(ledger["ClientId"], ledger["ClientSecret"]), timeout=30)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    print(push_batch([]))
