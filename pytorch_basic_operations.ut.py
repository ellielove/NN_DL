import unittest
import torch


class TestPytorchBasicOperations(unittest.TestCase):

    def test_tensor_size_property_returns_tuple(self):
        # works for tuple operations
        tensor = torch.empty(5, 3)
        x, y = tensor.size()
        self.assertTrue(x == 5)
        self.assertTrue(y == 3)
        self.assertTrue(tensor.size() == (5, 3))

    def test_tensor_is_constructible_using_specific_type(self):
        # includes all the basic number types ints, floats, doubles, etc
        tensor = torch.tensor(data=[5, 3], dtype=torch.uint8)
        self.assertTrue(tensor.type() == 'torch.ByteTensor')


if __name__ == '__main__':
    unittest.main()
