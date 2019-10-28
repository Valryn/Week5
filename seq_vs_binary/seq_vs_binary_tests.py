import unittest
import time
import seq_vs_binary
import random

class seq_vs_binary_tests(unittest.TestCase):
    randomints = [random.randint(0, 100000) for i in range(100)]
    randomints.sort()
    randomtarget = randomints[random.randint(0, (len(randomints) - 1))]

    def setUp(self):
        self.start_time = time.time()

    def test_binarySearch(self):
        print("Binary Search Operations: " + str(seq_vs_binary.binarySearch(self.randomints, self.randomtarget)))


    def test_sequentialSearch(self):
        print("Sequential Search Operations: " + str(seq_vs_binary.sequentialSearch(self.randomints, self.randomtarget)))


    def test_binarySearchRec(self):
        print("Recursive Binary Search Operations: ("
              + str(seq_vs_binary.binarySearchRec(self.randomints, self.randomtarget)) +
              ", " + str(seq_vs_binary.rec_count) +")")

    def tearDown(self):
        run_time = time.time() - self.start_time
        print("%s: %.3f" % (self.id(), run_time))

if __name__ == '__main__':
    unittest.main()
