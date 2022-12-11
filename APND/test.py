"""
This file is responsible to test APND  

This file simplifies your APND test, you only need to change
the function import below this comment and the call_test

Author: Paulo César
Created At: December 11, 2022
"""

import unittest
from index import start  # CHANGE THIS FOR TEST


def call_test(states, alphabet, stack_alphabet, edges, start_state, end_state_list, words): return start(
    states, alphabet, stack_alphabet, edges, start_state, end_state_list, words)  # CHANGE THIS FOR TEST


class TestAfd(unittest.TestCase):

    def test_1(self):
        """
        Default Test
        """
        states = ["0", "1"]
        alphabet = ["a", "b"]
        stack_alphabet = ["A"]
        edges = [('0', 'a', "*", "0", 'A'), ('0', '*', '*',
                                             "1", "*"), ('1', 'b', "A", '1', "*")]
        words = ["*", "ab", "ba", "abb", "aab"]
        expected = ["S", "S", "N", "N", "N"]
        start_state = "0"
        end_state_list = ['1']
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_2(self):
        """
        The number of 0 in w is the same of 1
        """
        states = ["A"]
        alphabet = ["0", "1"]
        stack_alphabet = ["Z", "U"]
        edges = [('A', '0', "U", "A", '*'), ('A', '0', '*', "A", "Z"),
                 ('A', '1', "*", 'A', "U"), ("A", "1", "Z", "A", "*")]
        words = ["0011", "001", "0101", "000111", "110"]
        expected = ["S", "N", "S", "S", "N"]
        start_state = "A"
        end_state_list = ['A']
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_3(self):
        """
        w=w^R
        """
        states = ["A", "B"]
        alphabet = ["0", "1"]
        stack_alphabet = ["T", "F"]
        edges = [('A', '0', "*", "A", 'F'), ('A', '1', '*', "A", "T"),
                 ('B', '0', "F", 'B', "*"), ("B", "1", "T", "B", "*"),
                 ('A', '*', "*", 'B', "*"), ("A", "0", "*", "B", "*"),
                 ("A", "1", "*", "B", "*")]
        words = ["010", "0110", "011", "010010", "001"]
        expected = ["S", "S", "N", "S", "N"]
        start_state = "A"
        end_state_list = ['B']
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_4(self):
        """
        W=a^i b^j c^i | i,j>=0
        """
        states = ["A", "B", "C"]
        alphabet = ["a", "b", "c"]
        stack_alphabet = ["X"]
        edges = [('A', 'a', "*", "A", 'X'), ('A', '*', '*', 'B', '*'),
                 ('B', 'b', "*", 'B', "*"), ("B", "*", "*", "C", "*"),
                 ('C', 'c', "X", 'C', "*")]
        words = ["aabcc", "aaabbc", "abc", "aaabbbccc", "aaabbbbbbbbbbccc"]
        expected = ["S", "N", "S", "S", "S"]
        start_state = "A"
        end_state_list = ['C']
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_4(self):
        """
        W=a^i+j b^i c^j | i,j>=0
        """
        states = ["A", "B", "C"]
        alphabet = ["a", "b", "c"]
        stack_alphabet = ["X"]
        edges = [('A', 'a', "*", "A", 'X'), ('A', '*', '*', 'B', '*'),
                 ('B', 'b', "X", 'B', "*"), ("B", "*", "*", "C", "*"),
                 ('C', 'c', "X", 'C', "*")]
        words = ["aabc", "abbc", "aaaabc", "aaaabbcc", "aaaaaabbbbcc"]
        expected = ["S", "N", "N", "S", "S"]
        start_state = "A"
        end_state_list = ['C']
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_5(self):
        """
        W=a^3n b^2n | n>=0
        """
        states = ["A", "B", "C", "D", "E"]
        alphabet = ["a", "b"]
        stack_alphabet = ["X"]
        edges = [('A', 'a', "*", "A", 'X'), ('A', '*', '*', 'B', '*'),
                 ('B', 'b', "X", 'B', "*"), ("B", "*", "*", "C", "*"),
                 ('C', 'c', "X", 'C', "*")]
        words = ["aabc", "abbc", "aaaabc", "aaaabbcc", "aaaaaabbbbcc"]
        expected = ["S", "N", "N", "S", "S"]
        start_state = "A"
        end_state_list = ['C']
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_6(self):
        """
        {0 n 1 n | n ≥ 0} U {0 n 1 2n | n ≥ 0}
        """
        states = ["A", "B", "C", "D"]
        alphabet = ["0", "1"]
        stack_alphabet = ["X"]
        edges = [('A', '0', "*", "A", 'X'), ('A', '1', 'X', 'B', '*'),
                 ('B', '1', "X", 'B', "*"), ("A", "1", "*", "C", "*"),
                 ('C', '1', "X", 'D', "*"), ("D", "1", "*", "C", "*")]
        words = ["0011", "011", "0111", "000111111", "01"]
        expected = ["S", "S", "N", "S", "S"]
        start_state = "A"
        end_state_list = ["A", "B", "D"]
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_7(self):
        """

        """
        states = ["A", "B"]
        alphabet = ["0", "1"]
        stack_alphabet = ["X"]
        edges = [('A', '0', "*", "A", 'XX'), ('A', '0', '*', 'A', 'X'),
                 ('A', '1', "X", 'B', "*"), ("B", "1", "X", "B", "*")]
        words = ["00111", "0011111", "01", "00011111", "000011111111"]
        expected = ["S", "N", "S", "S", "S"]
        start_state = "A"
        end_state_list = ["A", "B", "D"]
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_8(self):
        """
        {0 n 1 n 0 k | n, k ≥ 0}:
        """
        states = ["A", "B", "C"]
        alphabet = ["0", "1"]
        stack_alphabet = ["X"]
        edges = [('A', '0', "*", "A", 'X'), ('A', '*', '*', 'B', '*'),
                 ('B', '1', "X", 'B', "*"), ("B", "*", "*", "C", "*"),
                 ("C", "0", "*", "C", "*")]
        words = ["00110", "001110", "000110", "0001110", "00001111000"]
        expected = ["S", "N", "N", "S", "S"]
        start_state = "A"
        end_state_list = ["C"]
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_9(self):
        """
        {0 m 1 n | m > n}
        """
        states = ["A", "B"]
        alphabet = ["0", "1"]
        stack_alphabet = ["X"]
        edges = [('A', '0', "*", "A", 'X'), ('A', '0', '*', 'A', '*'),
                 ('A', '0', "*", 'B', "*"), ("B", "1", "X", "B", "*")]
        words = ["000111", "00111", "0111", "00001", "000011"]
        expected = ["N", "N", "N", "S", "S"]
        start_state = "A"
        end_state_list = ["B"]
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_10(self):
        """
        w has some suffix with more 1s than 0s
        """
        states = ["A", "B"]
        alphabet = ["0", "1"]
        stack_alphabet = ["X"]
        edges = [('A', '0', "*", "A", 'X'), ('A', '*', 'X', 'B', '*'),
                 ('A', '1', "X", 'B', "*"), ("B", "*", "X", "B", "*"),
                 ("B", "1", "X", "B", "*")]
        words = ["0011", "000111", "00111", "000001111", "01"]
        expected = ["S", "S", "N", "S", "S"]
        start_state = "A"
        end_state_list = ["B", "A"]
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_11(self):
        """
         a^{n}b^{m}c^{n} | m,n >=0 - This is a Classmate's Contribution!
        """
        states = ["A", "B", "C"]
        alphabet = ["a", "b", "c"]
        stack_alphabet = ["X"]
        edges = [('A', 'a', '*', 'A', 'X'),
                 ('A', '*', '*', 'B', '*'),
                 ('B', 'b', '*', 'B', '*'),
                 ('B', '*', '*', 'C', '*'),
                 ('C', 'c', 'X', 'C', '*')]
        words = ["*", "ac", "abcc", "b", "abbc"]
        expected = ["S", "S", "N", "S", "S"]
        start_state = "A"
        end_state_list = ["C"]
        result = call_test(states, alphabet, stack_alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))


if __name__ == '__main__':
    unittest.main()
