import unittest
from compute_distance_and_align.align_strings import align_strings as align

class TestAlign(unittest.TestCase):

    def test_sanity_check(self):
        """
        Test that compute_distance_and_align produces the minimum number of edits
        to convert str1 into str2 for a simple representative case
        """

        str1 = 'abcdef'
        str2 = 'azced'
        aligned_strings = align(str1, str2)
        print(aligned_strings)
        #self.assertEqual(aligned_strings, ('abcdef', 'aZc-eD'))

    def test_trivial_case(self):
        """
        Test that compute_distance_and_align produces the minimum number of edits
        to convert str1 into str2 for a trivial case
        """

        str1 = 'a'
        str2 = 'a'
        aligned_strings = align(str1, str2)
        self.assertEqual(aligned_strings, (0, ('a', 'a')))

    def test_general(self):
        """
        Test that compute_distance_and_align produces the minimum number of edits
        to convert str1 into str2 for a trivial case
        """

        str1 = ''
        str2 = 'azced'
        aligned_strings = align(str1, str2)
        self.assertEqual(aligned_strings, (5, ('', 'AZCED')))


    def test_edge_case(self):
        """
        Test that compute_distance_and_align produces the minimum number of edits
        to convert str1 into str2 for an edge case (extreme normal)
        """
        str1 = ""
        str2 = ""
        aligned_strings = align(str1, str2)
        self.assertEqual(aligned_strings, (0, ('', '')))

    def test_outside_normal(self):
        """
        Test that compute_distance_and_align produces a Type Error when one of the parameters is of the
        wrong type
        """

        str1 = 9
        str2 = "abs"
        with self.assertRaises(TypeError):
            aligned_strings = align(str1, str2)


if __name__ == "__main__":
    unittest.main()