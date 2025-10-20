from typing import List, TypeVar
T = TypeVar("T")
def bubble_sort(arr: List[T]) -> None:
	n = len(arr)
	if n < 2:
		return

	for end in range(n - 1, 0, -1):
		swapped = False
		for i in range(end):
			if arr[i] > arr[i + 1]:
				arr[i], arr[i + 1] = arr[i + 1], arr[i]
				swapped = True
		if not swapped:
			break


if __name__ == "__main__":
	try:
		raw = input("Enter numbers separated by space:\n").strip()
		nums = [] if not raw else [float(x) if "." in x else int(x) for x in raw.split()]
		bubble_sort(nums)
		print("Sorted:", " ".join(map(str, nums)))
	except EOFError:
		pass

