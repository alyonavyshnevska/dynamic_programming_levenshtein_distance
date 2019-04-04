import unittest
from compute_levenshtein_distance import compute_levenshtein_distance

compute_distance = compute_levenshtein_distance.compute_levenshtein_distance


class TestSum(unittest.TestCase):
    def test_shortest_distance(self):
        """
        Test that compute_levenshtein_distance produces the minimum number of edits
        to convert str1 into str2
        """

        str1 = ""
        str2 = "abc"
        shortest_distance = compute_distance(str1, str2)
        self.assertEqual(shortest_distance, 3)


if __name__ == "__main__":
    unittest.main()