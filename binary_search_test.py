import io
import unittest.mock
from binary_search import binary_search, calculate_bs_worst_case


class MyTestCase(unittest.TestCase):
    def test_bs_found(self):
        my_list = [1, 3, 7, 5, 9]
        res = binary_search(my_list, 7)
        self.assertEqual(res, 2)

    def test_bs_not_found(self):
        my_list = [1, 3, 7, 5, 9]
        res = binary_search(my_list, 8)
        self.assertIsNone(res)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_stdout(self, n, expected_output, mock_stdout):
        calculate_bs_worst_case(n)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_worst_case(self):
        my_list_num = 128
        self.assert_stdout(my_list_num, 'worst case scenario maximum 7 steps is required\n')


if __name__ == '__main__':
    unittest.main()
