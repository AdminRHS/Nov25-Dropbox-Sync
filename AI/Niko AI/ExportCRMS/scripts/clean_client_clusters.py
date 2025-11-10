"""
Utility to remove null/empty fields from client JSON cluster files.

Reads every `Client_cluster_*.json` file inside `Client_JSON_Clusters`
and rewrites it without entries whose values are null or become empty
after recursive cleanup.
"""
from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _clean_value(value: Any) -> Any | None:
    """
    Recursively strip nulls and empty containers from the provided value.
    Returns the cleaned value or None when the value should be dropped.
    """

    if value is None:
        return None

    if isinstance(value, dict):
        cleaned_dict = {}
        for key, nested_value in value.items():
            cleaned_nested = _clean_value(nested_value)
            if cleaned_nested is not None:
                cleaned_dict[key] = cleaned_nested
        return cleaned_dict or None

    if isinstance(value, list):
        cleaned_list = []
        for item in value:
            cleaned_item = _clean_value(item)
            if cleaned_item is not None:
                cleaned_list.append(cleaned_item)
        return cleaned_list or None

    if isinstance(value, str):
        stripped = value.strip()
        return stripped or None

    return value


def clean_client_clusters(base_dir: Path) -> None:
    """
    Remove null/empty entries from every client cluster file located under
    Client_JSON_Clusters within the provided base directory.
    """

    cluster_dir = base_dir / "Client_JSON_Clusters"
    if not cluster_dir.exists():
        raise FileNotFoundError(f"Missing directory: {cluster_dir}")

    cluster_files = sorted(cluster_dir.glob("Client_cluster_*.json"))
    if not cluster_files:
        raise FileNotFoundError("No client cluster files were found")

    for cluster_file in cluster_files:
        data = json.loads(cluster_file.read_text(encoding="utf-8"))
        cleaned_data = []

        for entry in data:
            cleaned_entry = _clean_value(entry)
            if cleaned_entry is not None:
                cleaned_data.append(cleaned_entry)

        cluster_file.write_text(
            json.dumps(cleaned_data, indent=2, ensure_ascii=False), encoding="utf-8"
        )
        print(f"Cleaned {cluster_file}")


if __name__ == "__main__":
    clean_client_clusters(Path(__file__).parent.parent)
