import unittest
from compute_levenshtein_distance import compute_levenshtein_distance

compute_distance = compute_levenshtein_distance.compute_levenshtein_distance

'''
assert compute_levenshtein_distance("", "abc") == 3
assert compute_levenshtein_distance("abc", "") == 3
assert compute_levenshtein_distance("a", "a") == 0
assert compute_levenshtein_distance("a", "b") == 1
assert compute_levenshtein_distance("333", "3") == 2
assert compute_levenshtein_distance("hello", "hili") == 3
assert compute_levenshtein_distance("", "") == 0
assert compute_levenshtein_distance("abc", "abc") == 0
'''


class TestSum(unittest.TestCase):

    def test_sanity_check(self):
        """
        Test that compute_levenshtein_distance produces the minimum number of edits
        to convert str1 into str2
        """

        str1 = "ab"
        str2 = "bc"
        shortest_distance = compute_distance(str1, str2)
        self.assertEqual(shortest_distance, 2)

    def test_trivial_case(self):
        """
        Test that compute_levenshtein_distance produces the minimum number of edits
        to convert str1 into str2
        """

        str1 = "a"
        str2 = "a"
        shortest_distance = compute_distance(str1, str2)
        self.assertEqual(shortest_distance, 0)


if __name__ == "__main__":
    unittest.main()