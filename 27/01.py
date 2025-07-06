# нащупать вектора было интересно, но выматывающе
import numpy


def make_field(size: int):
    chessboard = numpy.zeros((size, size), dtype=numpy.int8)
    chessboard[::2, 1::2] = 1
    chessboard[1::2, ::2] = 1
    return chessboard
