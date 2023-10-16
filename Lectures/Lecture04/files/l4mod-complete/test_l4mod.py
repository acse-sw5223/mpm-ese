import numpy as np
import pytest

from l4mod import gauss, matmul, zeromat


class TestUnits(object):
    """
    Class for testing the functions upon which `gauss`
    depends.
    """

    @pytest.mark.parametrize('a, b, ce', [
        ([[6, 9, 8, 3, 5], [3, 4, 8, 9, 6]],
         [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]],
         np.dot([[6, 9, 8, 3, 5], [3, 4, 8, 9, 6]],
                [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]).tolist()),
        ([[101, 678, 134, 675]], [[1], [2], [3], [4]], [[4559]]),
        ([[678, 395], [576, 983]], [[101, 5, 22, 78, 90], [1, 4, 7, 22, 90]],
         np.dot([[678, 395], [576, 983]],
                [[101, 5, 22, 78, 90], [1, 4, 7, 22, 90]]).tolist()),
        ([[0.996, 0.511, 0.303], [0.618, 0.175, 0.363]],
         [[0.249, 0.498, 0.066, 0.992],
          [0.495, 0.166, 0.318, 0.772],
          [0.698, 0.097, 0.155, 0.035]],
         [[0.712443, 0.610225, 0.275199, 1.393129],
          [0.493881, 0.372025, 0.152703, 0.760861]])
    ])
    def test_matmul(self, a, b, ce):
        """ Test the matmul function """
        c = matmul(a, b)

        assert np.allclose(c, ce)

    @pytest.mark.parametrize('p, q, zme', [
        (1, 1, [[0]]),
        (1000, 10000, np.zeros((1000, 10000)).tolist()),
        (8, 6, np.zeros((8, 6)).tolist())
    ])
    def test_zeromat(self, p, q, zme):
        """ Test the zeromat function """
        zm = zeromat(p, q)

        assert np.allclose(zm, zme)


class TestModule(object):
    """
    Class for testing the Gaussian elimination algorithm Gauss.
    """

    @pytest.mark.parametrize('a, b, dete, xe', [
        ([[2, 9, 4], [7, 5, 3], [6, 1, 8]],
         [[1, 0, 0], [0, 1, 0], [0, 0, 1]], -360.0,
         [[-0.10277777777777776, 0.18888888888888888, -0.019444444444444438],
          [0.10555555555555554, 0.02222222222222223, -0.061111111111111116],
          [0.0638888888888889, -0.14444444444444446, 0.14722222222222223]]),
        ([[1]], [[1, 2, 3]], 1, [[1, 2, 3]]),
        ([[2.8, 7.6], [5.3, 9.2]],
         [[0, 0, 0], [0, 0, 0]], -14.519999999999998,
         [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]),
        ([[1, 2, 3], [66, 8, 55], [5, 6, 7]], [[0], [0], [0]],
         420.0, [[0.0], [0.0], [0.0]])
    ])
    def test_gauss(self, a, b, dete, xe):
        """ Test the gauss function """
        det, x = gauss(a, b)

        assert np.isclose(det, dete)
        assert np.allclose(x, xe)
