"""Count str in the list items."""
items = [list, "abba", "123", 123, "list", None, True, ["x"]]
print(f"Number of strings: {sum(isinstance(item, str) for item in items)}")
