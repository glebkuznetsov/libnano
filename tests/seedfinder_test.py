from __future__ import print_function
import sys

import random
import unittest
import re
import time
from os.path import join, abspath, dirname

# For package imports
sys.path.insert(0, abspath(join(dirname(__file__), '..')))

from libnano.core.seqsearch import seedfinder
import _setup

LOCAL_DIR = abspath(dirname(__file__))

""" TODO Fix this file for the submer module
This also tests
"""
class TestSeedFinder(unittest.TestCase):

    def test_checkSeed(self):
        self.assertEqual(seedfinder.checkSeed("#-##--#-##", 15), 2)
        self.assertEqual(seedfinder.checkSeed("#-##-##-##", 15), 1)
        self.assertNotEqual(seedfinder.checkSeed("#######-##", 15), 2)
        # self.assertEqual(seedfinder.checkSeeds(
        #     ["#-#-#---#-----#-#-#---#-----#-#-#---#", "###-#--###-#--###-#"],
        #      50, k_min=4, k_max=6), 5)

    def test_findSeed(self):
        for x in range(10):
            m = random.randint(5, 20)
            k = random.randint(1, 3)
            sd_list = seedfinder.findSeed(m, k)
            # sds = seedfinder.findSeed(m, k)
            for sd in sd_list:
                the_seed = sd[2]
                self.assertEqual(seedfinder.checkSeed(the_seed, m), k,
                                 msg=('m: %d, k: %d, sd: %s' % (m, k, sd)))
                # self.assertEqual(seedfinder.checkSeeds(sds, m), k)
# end class

if __name__ == '__main__':
    unittest.main(verbosity=2)