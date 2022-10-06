import sys
import os
import unittest
import shutil
import random
src_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append(src_path)
import utils  # nopep8


class TestUtils(unittest.TestCase):


    # want to trim a list of lists by the mean of the 
    # individual lists
    # - handle empty lists
    # - test finding the mean of a list def test_find_mean
    #   - make sure the lists have data types that have a mean
    # - test fiding the mean of a lists of lists def 
    #   test_find_means
    # - test removing some elements of the list by a threshold

    def test_find_mean(self):
        A = [2, 2, 2, 2, 2, 2]
        mean = utils.find_mean(A)
        self.assertEquale(mean, 2)

    def test_linear_search(self):
        L = random.sample(range(10, 30), 10)
        L.append(100)
        self.assertTrue(utils.linear_search(L, 100) >= 0)
        self.assertTrue(utils.linear_search(L, 200) == -1)

    def test_bindary_search(self):
        L = random.sample(range(10, 30), 10)
        L.append(100)

        L_idx = utils.index_list(L)

        self.assertTrue(utils.binary_search(L_idx, 100) >= 0)
