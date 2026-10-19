"""Count str in the list items."""
items = [list, "abba", "123", 123, "list", None, True, ["x"]] 
count = 0
for item in items:
    if isinstance(item, str):
        count += 1
print(f"Number of strings: {count}")        