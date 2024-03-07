"""
The problem:

Vowel Square Have the function VowelSquare(strArr) take the strArr parameter being passed which will be a 2D matrix of some arbitrary size filled with letters from the alphabet, and determine if a 2x2 square composed entirely of vowels exists in the matrix. For example: strArr is ["abcd", "eikr", "oufj"] then this matrix looks like the following:

a b c d

e i k r

o u f j
Within this matrix there is a 2x2 square of vowels starting in the second row and first column, namely, ei, ou. If a 2x2 square of vowels is found your program should return the top-left position (row-column) of the square, so for this example your program should return 1-0. If no 2x2 square of vowels exists, then return the string not found. If there are multiple squares of vowels, return the one that is at the most top-left position in the whole matrix. The input matrix will at least be of size 2x2.

Examples:

Input: ["aqrst", "ukaei", "ffooo"]
Output: 1-2,
Input: ["gg", "ff"]
Output: not found
"""

import numpy as np

def _get_auxiliar_matrix(arr):
    vowels = "aeiou"
    _matrix = []
    
    for _line in arr:
        _lines = []
        for _element in _line:
            if _element in vowels:
                _lines.append(1)
            else:
                _lines.append(0)
        _matrix.append(_lines)
    return _matrix
                

def VowelSquare(arr):
    _matrix = np.array(_get_auxiliar_matrix(arr))
    if np.sum(_matrix) < 4:
        return "not found"
    
    _shape = _matrix.shape
    
    for i in range(_shape[0]-1):
        for j in range(_shape[1]-1):
            if (_matrix[i][j] + _matrix[i][j+1] + _matrix[i+1][j] + _matrix[i+1][j+1]) == 4:
                return "-".join([str(i), str(j)])

    return "not found"

def main():
    inputs = [
        ["gg", "ff"],
        ["aqrst", "ukaei", "ffooo"],
    ]
    for array in inputs:
        print(VowelSquare(array))

if __name__== '__main__':
    main()
