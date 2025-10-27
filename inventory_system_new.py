"""
Inventory management system for tracking stock items.

This module provides functions to add, remove, and track inventory items,
as well as save and load data from JSON files.
"""

import json
from datetime import datetime


# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """
    Add an item to inventory with specified quantity.

    Args:
        item: Name of the item to add (str)
        qty: Quantity to add (int)
        logs: List to append log messages (list, optional)
    """
    if logs is None:
        logs = []

    if not item or not isinstance(item, str):
        return

    if not isinstance(qty, int):
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """
    Remove specified quantity of an item from inventory.

    Args:
        item: Name of the item to remove (str)
        qty: Quantity to remove (int)
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Warning: Item '{item}' not found in inventory")


def get_qty(item):
    """
    Get the current quantity of an item.

    Args:
        item: Name of the item (str)

    Returns:
        int: Current quantity of the item, or 0 if not found
    """
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """
    Load inventory data from a JSON file.

    Args:
        file: Path to the JSON file (str)
    """
    global stock_data
    try:
        with open(file, "r", encoding='utf-8') as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        print(
            f"Warning: File '{file}' not found. "
            "Starting with empty inventory."
        )
        stock_data = {}


def save_data(file="inventory.json"):
    """
    Save current inventory data to a JSON file.

    Args:
        file: Path to the JSON file (str)
    """
    with open(file, "w", encoding='utf-8') as f:
        json.dump(stock_data, f, indent=2)


def print_data():
    """Print current inventory in a formatted report."""
    print("Items Report")
    for item, quantity in stock_data.items():
        print(f"{item} -> {quantity}")


def check_low_items(threshold=5):
    """
    Check for items below a quantity threshold.

    Args:
        threshold: Minimum quantity threshold (int)

    Returns:
        list: Items with quantity below threshold
    """
    result = []
    for item, quantity in stock_data.items():
        if quantity < threshold:
            result.append(item)
    return result


def main():
    """Main function to demonstrate inventory system functionality."""
    add_item("apple", 10)
    add_item("banana", 5)
    # Removed invalid call: add_item(123, "ten")
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()
    # Removed dangerous eval() call
    print("Inventory operations completed successfully")


if __name__ == "__main__":
    main()
