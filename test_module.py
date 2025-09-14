import unittest
import mean_var_std


class UnitTests(unittest.TestCase):
    def test_calculate_with_too_few_values(self):
        self.assertRaisesRegex(ValueError,
                               "List must contain nine numbers.",
                               mean_var_std.calculate, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_calculate_with_correct_values(self):
        actual = mean_var_std.calculate([2,6,2,8,4,0,1,5,7])
        expected = {
            'mean': [[3.6666666666666665, 5.0, 3.0],
                     [3.3333333333333335, 4.0, 4.333333333333333],
                     3.888888888888889],
            'variance': [[9.555555555555555, 0.6666666666666666, 8.666666666666666],
                         [6.888888888888889, 10.666666666666666, 6.888888888888889],
                         7.555555555555555],
            'standard deviation': [[3.091206165165235, 0.816496580927726,
                                    2.943920288775949],
                                   [2.6246692913372702, 3.265986323710904,
                                    2.6246692913372702],
                                   2.749545416973503],
            'max': [[8, 6, 7],
                    [8, 8, 7],
                    8],
            'min': [[1, 4, 0],
                    [2, 0, 1],
                    0],
            'sum': [[11, 15, 9],
                    [10, 12, 13],
                    35]
        }
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
