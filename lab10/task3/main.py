from find_smallest import find_two_smallest
from int_lists import a, b, c, d

if __name__ == "__main__":
    with open("result.txt", "w", encoding="utf-8") as file:
        for values in (a, b, c, d):
            file.write(f"{values} -> {find_two_smallest(values)}\n")
