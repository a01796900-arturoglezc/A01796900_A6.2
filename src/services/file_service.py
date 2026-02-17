"""
File service for JSON persistence.
"""

import json
from typing import Any, List


class FileService:
    """Handles JSON file operations."""

    @staticmethod
    def load_data(file_path: str) -> List[Any]:
        """Load data from a JSON file."""
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: File {file_path} not found.")
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON format in {file_path}.")
            return []
        except Exception as error:
            print(f"Unexpected error while reading {file_path}: {error}")
            return []

    @staticmethod
    def save_data(file_path: str, data: List[Any]) -> None:
        """Save data to a JSON file."""
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=4)
        except Exception as error:
            print(f"Error writing to {file_path}: {error}")