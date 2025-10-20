from typing import List


def reverse_in_place(items: List[str]) -> None:
	i, j = 0, len(items) - 1
	while i < j:
		items[i], items[j] = items[j], items[i]
		i += 1
		j -= 1


if __name__ == "__main__":
	try:
		raw = input("Enter elements separated by space:\n").strip()
		lst = [] if not raw else raw.split()
		reverse_in_place(lst)
		print("Reversed:", " ".join(lst))
	except EOFError:
		pass

