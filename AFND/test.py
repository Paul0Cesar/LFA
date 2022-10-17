"""
This file is responsible to test AFND  

This file simplifies your AFND test, you only need to change
the function import below this comment and the call_test

Author: Paulo César
Created At: October 15, 2022
"""

import unittest
from index import start  # CHANGE THIS FOR TEST


def call_test(states, alphabet, edges, start_state, end_state_list, words): return start(
    states, alphabet, edges, start_state, end_state_list, words)  # CHANGE THIS FOR TEST


class TestAfd(unittest.TestCase):

    def test_1(self):
        """
        Default Test
        """
        states = ["0", "1"]
        alphabet = ["a", "b"]
        edges = [('0', 'a', '0'), ('0', 'b', '0'), ('0', 'b', '1')]
        words = ["a", "b", "aba", "abb"]
        expected = ["N", "S", "N", "S"]
        start_state = "0"
        end_state_list = ['1']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_2(self):
        """
        {w | w ending with 00}
        """
        states = ["a", "b", "c"]
        alphabet = ["0", "1"]
        edges = [('a', '0', 'a'), ('a', '1', 'a'),
                 ('a', '0', 'b'), ("b", "0", "c")]
        words = ["10", "100", "10100", "*10"]
        expected = ["N", "S", "S", "N"]
        start_state = "a"
        end_state_list = ['c']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_3(self):
        """
        {w | w contains substring 0101, in other words, w=x0101y for any x and y}
        """
        states = ["a", "b", "c", 'd', 'e']
        alphabet = ["0", "1"]
        edges = [('a', '0', 'a'), ('a', '1', 'a'), ('a', '0', 'b'), ("b", "1", "c"),
                 ("c", "0", "d"), ("d", "1", "e"), ("e", "1", "e"), ("e", "0", "e")]
        words = ["10", "0101", "100101", "00000101"]
        expected = ["N", "S", "S", "S"]
        start_state = "a"
        end_state_list = ['e']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_3(self):
        """
        {w | w contains suffix 01 or 10}
        """
        states = ["a", "b", "c", "d", "e"]
        alphabet = ["0", "1"]
        edges = [('a', '0', 'a'), ('a', '1', 'a'), ("a", "1", "d"),
                 ('a', '0', 'b'), ("b", "1", "c"), ("d", "0", "e")]
        words = ["10", "100", "1010", "00001"]
        expected = ["S", "N", "S", "S"]
        start_state = "a"
        end_state_list = ['c', "e"]
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_4(self):
        """
        {w | w contains 1 in the end}
        """
        states = ["a", "b", "c"]
        alphabet = ["0", "1"]
        edges = [('a', '0', 'a'), ('a', '1', 'a'),
                 ('a', '1', 'b'), ("b", "1", "c"), ("b", "0", "c")]
        words = ["110", "100", "1011", "00001"]
        expected = ["S", "N", "S", "N"]
        start_state = "a"
        end_state_list = ['c']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_5(self):
        """
        {w | w contains 000 as substring}
        """
        states = ["a", "b", "c", "d"]
        alphabet = ["0", "1"]
        edges = [('a', '0', 'a'), ('a', '1', 'a'), ('a', '0', 'b'),
                 ("b", "0", "c"), ("c", "0", "d"), ("d", "0", "d"),
                 ("d", "1", "d")]
        words = ["10001", "100", "11000", "00001"]
        expected = ["S", "N", "S", "S"]
        start_state = "a"
        end_state_list = ['d']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_6(self):
        """
        {w | w contains bb or bab}
        """
        states = ["1", "2", "3", "4"]
        alphabet = ["a", "b"]
        edges = [('1', 'a', '1'), ('1', 'b', '1'), ('1', 'b', '2'),
                 ("2", "b", "3"), ("3", "a", "3"), ("3", "b", "3"),
                 ("2", "a", "4"), ("4", "b", "3")]
        words = ["bb", "bab", "bbbab", "aaa"]
        expected = ["S", "S", "S", "N"]
        start_state = "1"
        end_state_list = ['3']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_7(self):
        """
        {w | w contains two 0 separated for um number of positions multiple of 2}
        """
        states = ["a", "b", "c", "d", "e", "f"]
        alphabet = ["1", "0"]
        edges = [('a', '0', 'a'), ('a', '1', 'a'), ('a', '0', 'b'), ('a', '0', 'c'),
                 ("b", "0", "f"), ("f", "0", "f"), ("f", "1", "f"), ("c", "0", "d"),
                 ("c", "1", "d"), ("d", "0", "e"), ("d", "1", "e"), ("e", "0", "f"),
                 ("e", "1", "d")]
        words = ["010", "0110", "100001", "1000110"]
        expected = ["N", "S", "S", "S"]
        start_state = "a"
        end_state_list = ['f']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_8(self):
        """
        {w | in w, the second and the penultimate are diferents}
        """
        states = ["1", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "11", "12", "13"]
        alphabet = ["a", "b"]
        edges = [('1', 'a', '2'), ('1', 'b', '2'), ('2', 'a', '3'),
                 ('3', 'a', '4'), ('3', 'b', '4'), ('4', 'b', '5'),
                 ('4', 'a', '4'), ('4', 'b', '4'), ('5', 'a', '6'),
                 ('5', 'b', '6'), ('3', 'b', '12'), ('12', 'a', '6'),
                 ('12', 'b', '6'), ('2', 'b', '7'), ('7', 'a', '13'),
                 ('13', 'a', '6'), ('13', 'b', '6'), ('7', 'a', '8'),
                 ('7', 'b', '8'), ('8', 'a', '8'), ('8', 'b', '8'),
                 ('8', 'a', '5'), ('1', 'a', '9'), ('9', 'b', '10'),
                 ('1', 'b', '11'), ('11', 'a', '10')]
        words = ["aba", "abab", "abaaab", "abaabab"]
        expected = ["N", "S", "S", "S"]
        start_state = "1"
        end_state_list = ['6', '10']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))

    def test_9(self):
        """
        {w | w contains two 'a' separated by number par of symbols}
        """
        states = ["1", "2", "3", "4"]
        alphabet = ["a", "b"]
        edges = [('1', 'a', '1'), ('1', 'b', '1'), ('1', 'a', '2'),
                 ("2", "a", "3"), ("2", "b", "3"), ("3", "a", "2"),
                 ("3", "b", "2"), ("2", "a", "4"), ("4", "a", "4"), ("4", "b", "4")]
        words = ["abba", "ab", "babbbba", "a"]
        expected = ["S", "N", "S", "N"]
        start_state = "1"
        end_state_list = ['4']
        result = call_test(states, alphabet, edges,
                           start_state, end_state_list, words)
        self.assertEqual(result, expected, "Should be :{}".format(expected))


if __name__ == '__main__':
    unittest.main()
