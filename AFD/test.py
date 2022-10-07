"""
This file is responsible to test AFD  

This file simplifies your AFD test, you only need to change
the function import below this comment and the call_test

Author: Paulo César
Created At: October 05, 2022
"""

import unittest
from index import start  # CHANGE THIS FOR TEST


def call_test(states, alphabet, edges, start_state, end_state_list, words): return start(
    states, alphabet, edges, start_state, end_state_list, words) # CHANGE THIS FOR TEST


class TestAfd(unittest.TestCase):

    def test_1(self):
        """
        Default Test
        """
        states = ["0", "1"]
        alphabet = ["a", "b"]
        edges = [('0', 'a', '1'), ('1', 'a', '1'), ('1', 'b', '1')]
        words = ["a", "b", "aba", "abb", "b"]
        expected = ["S", "N", "S", "S", "N"]
        start_state = 0
        end_state_list = ['1']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_2(self):
        """
        {w | w has size 3}
        """
        states = ["0", "1", '2', "3"]
        alphabet = ["a", "b"]
        edges = [('0', 'a', '1'), ('0', 'b', '1'), ('1', 'a', '2'),
                 ('1', 'b', '2'), ('2', 'a', '3'), ('2', 'b', '3')]
        words = ["a", "ab", "abb", "abbb", "abc"]
        expected = ["N", "N", "S", "N", "N"]
        start_state = '0'
        end_state_list = ['3']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_3(self):
        """
        {w | w has size than less 3}
        """
        states = ["0", "1", "2"]
        alphabet = ["a", "b"]
        edges = [('0', 'a', '1'), ('0', 'b', '1'),
                 ('1', 'a', '2'), ('1', 'b', '2')]
        words = ["a", "ab", "abb", "abbb", "abc"]
        expected = ["S", "S", "N", "N", "N"]
        start_state = '0'
        end_state_list = ['0', '1', '2']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_4(self):
        """
        {w | w has size greater than 3}
        """
        states = ["0", "1", '2', "3", '4']
        alphabet = ["a", "b"]
        edges = [('0', 'a', '1'), ('0', 'b', '1'), ('1', 'a', '2'),
                 ('1', 'b', '2'), ('2', 'a', '3'), ('2', 'b', '3'), ('3', 'a', '4'), ('3', 'b', '4'), ('4', 'a', '4'), ('4', 'b', '4')]
        words = ["ax", "abbbb", "abb", "abbba", "abc"]
        expected = ["N", "S", "N", "S", "N"]
        start_state = '0'
        end_state_list = ['4']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_5(self):
        """
        {w | w has size multiple of 3}
        """
        states = ["0", "1", '2', "3"]
        alphabet = ["a", "b"]
        edges = [('0', 'a', '1'), ('0', 'b', '1'), ('1', 'a', '2'),
                 ('1', 'b', '2'), ('2', 'a', '3'), ('2', 'b', '3'), ('3', 'a', '1'), ('3', 'b', '1')]
        words = ["", "abba", "abbaba", "abbba", "abc"]
        expected = ["S", "N", "S", "N", "N"]
        start_state = '0'
        end_state_list = ['0', '3']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_7(self):
        """
        {w | w has a max of 3b}
        """
        states = ["0", "1", '2', "3"]
        alphabet = ["a", "b"]
        edges = [('0', 'a', '0'), ('0', 'b', '1'), ('1', 'a', '1'),
                 ('1', 'b', '2'), ('2', 'a', '2'), ('2', 'b', '3'), ('3', 'a', '3')]
        words = ["", "abba", "abbbaba", "abbba", "aba"]
        expected = ["S", "S", "N", "S", "S"]
        start_state = '0'
        end_state_list = ['0', '1', '2', '3']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_8(self):
        """
        {w | which a in w is immediately followed by a minimum of two b}
        """
        states = ["0", "1", '2', "3"]
        alphabet = ["a", "b"]
        edges = [('0', 'b', '0'), ('0', 'a', '1'), ('1', 'b', '2'),
                 ('2', 'b', '3'), ('3', 'b', '3'), ('3', 'a', '1')]
        words = ["", "abb", "abbbaba", "aba", "abaa"]
        expected = ["S", "S", "N", "N", "N"]
        start_state = '0'
        end_state_list = ['0','3']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))


if __name__ == '__main__':
    unittest.main()
