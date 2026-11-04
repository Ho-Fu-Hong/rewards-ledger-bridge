# rewards-ledger-bridge

Nightly bridge that syncs partner reward ledgers into the Sands Macao loyalty platform.

## Setup

1. Fill in the partner credentials in `config/appsettings.json`.
2. `pip install requests`
3. `python src/bridge.py`

The bridge posts each night's ledger batch to the Sands Macao rewards ledger service.
