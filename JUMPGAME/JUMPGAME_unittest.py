import JUMPGAME
import unittest


class TestJUMPGAME(unittest.TestCase):
    def test_exam1(self):
        input = [[2, 5,  1 ,  6 ,  1 ,  4 ,  1 ],
                 [ 6 ,  1 ,  1 ,  2 ,  2 ,  9 ,  3 ],
                 [ 7 ,  2 ,  3 ,  2 ,  1 ,  3 ,  1 ],
                 [ 1 ,  1 ,  3 ,  1 ,  7 ,  1 ,  2 ],
                 [ 4 ,  1 ,  2 ,  3 ,  4 ,  1 ,  2 ],
                 [ 3 ,  3 ,  1 ,  2 ,  3 ,  4 ,  1 ],
                 [ 1 ,  5 ,  2 ,  9 ,  4 ,  7 ,  0 ]]
        test = JUMPGAME.JumpGame(input)
        self.assertEqual(test.solve(),  'YES' )

    def test_exam2(self):
        input = [[ 2 ,  5 ,  1 ,  6 ,  1 ,  4 ,  1 ],
                 [ 6 ,  1 ,  1 ,  2 ,  2 ,  9 ,  3 ],
                 [ 7 ,  2 ,  3 ,  2 ,  1 ,  3 ,  1 ],
                 [ 1 ,  1 ,  3 ,  1 ,  7 ,  1 ,  2 ],
                 [ 4 ,  1 ,  2 ,  3 ,  4 ,  1 ,  3 ],
                 [ 3 ,  3 ,  1 ,  2 ,  3 ,  4 ,  1 ],
                 [ 1 ,  5 ,  2 ,  9 ,  4 ,  7 ,  0 ]]
        test = JUMPGAME.JumpGame(input)
        self.assertEqual(test.solve(),  'NO' )


if __name__ == "__main__":
    unittest.main()