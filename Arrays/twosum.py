
from typing import List, Optional, Tuple


def two_sum(nums: List[int], target: int) -> Optional[Tuple[int, int]]:
	"""Return a pair of values from nums that add up to target.

	This returns the first matching pair of values (not indices) found.

	Approach: single-pass hash table mapping seen value -> count (or existence).
	Time: O(n)
	Space: O(n)

	Args:
		nums: list of integers
		target: integer target sum

	Returns:
		Tuple of two integers (a, b) where a + b == target, or None if no pair exists.
	"""
	seen = {}
	for x in nums:
		need = target - x
		if need in seen and seen[need] > 0:
			# found a valid pair
			return (need, x)
		# record current value
		seen[x] = seen.get(x, 0) + 1
	return None


def _demo_and_tests() -> None:
	# quick smoke tests / examples
	examples = [
		(([2, 7, 11, 15], 9), (2, 7)),
		(([3, 2, 4], 6), (2, 4)),
		(([3, 3], 6), (3, 3)),
		(([1, 2, 3], 7), None),
		(([], 0), None),
		(([0, 0], 0), (0, 0)),
	]

	for (nums, target), expected in examples:
		out = two_sum(nums, target)
		# For deterministic comparison, sort the tuple if not None
		if out is not None:
			out_sorted = tuple(sorted(out))
		else:
			out_sorted = None

		if expected is not None:
			expected_sorted = tuple(sorted(expected))
		else:
			expected_sorted = None

		assert out_sorted == expected_sorted, f"two_sum({nums}, {target}) -> {out} != {expected}"

	# Print example usage
	nums = [2, 7, 11, 15]
	target = 9
	pair = two_sum(nums, target)
	print(f"nums={nums}, target={target} -> pair={pair}")


if __name__ == "__main__":
	_demo_and_tests()

