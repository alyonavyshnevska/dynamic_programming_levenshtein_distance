import unittest
from compute_levenshtein_distance import compute_levenshtein_distance

compute_distance = compute_levenshtein_distance.compute_levenshtein_distance

class TestSum(unittest.TestCase):

    def test_sanity_check(self):
        """
        Test that compute_levenshtein_distance produces the minimum number of edits
        to convert str1 into str2 for a simple representative case
        """

        str1 = "ab"
        str2 = "bc"
        shortest_distance = compute_distance(str1, str2)
        self.assertEqual(shortest_distance, 2)

    def test_trivial_case(self):
        """
        Test that compute_levenshtein_distance produces the minimum number of edits
        to convert str1 into str2 for a trivial case
        """

        str1 = "a"
        str2 = "a"
        shortest_distance = compute_distance(str1, str2)
        self.assertEqual(shortest_distance, 0)

    def test_general(self):
        """
        Test that compute_levenshtein_distance produces the minimum number of edits
        to convert str1 into str2 for an elaborate representative case
        """

        str1 = "hello"
        str2 = "hili"
        shortest_distance = compute_distance(str1, str2)
        self.assertEqual(shortest_distance, 3)

    def test_edge_case(self):
        """
        Test that compute_levenshtein_distance produces the minimum number of edits
        to convert str1 into str2 for an edge case (extreme normal)
        """
        str1 = ""
        str2 = ""
        shortest_distance = compute_distance(str1, str2)
        self.assertEqual(shortest_distance, 0)

    def test_outside_normal(self):
        """
        Test that compute_levenshtein_distance produces a Type Error when one of the parameters is of the
        wrong type
        """

        str1 = 5
        str2 = "abs"
        with self.assertRaises(TypeError):
            shortest_distance = compute_distance(str1, str2)


if __name__ == "__main__":
    unittest.main()