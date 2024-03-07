"""
The problem:

Vowel Square Have the function VowelSquare(strArr) take the strArr parameter 
being passed which will be a 2D matrix of some arbitrary size filled with 
letters from the alphabet, and determine if a 2x2 square composed entirely of 
vowels exists in the matrix. For example: strArr is ["abcd", "eikr", "oufj"] 
then this matrix looks like the following:

a b c d

e i k r

o u f j
Within this matrix there is a 2x2 square of vowels starting in the second row 
and first column, namely, ei, ou. If a 2x2 square of vowels is found your 
program should return the top-left position (row-column) of the square, so for 
this example your program should return 1-0. If no 2x2 square of vowels exists, 
then return the string not found. If there are multiple squares of vowels, 
return the one that is at the most top-left position in the whole matrix. 
The input matrix will at least be of size 2x2.

Examples:

Input: ["aqrst", "ukaei", "ffooo"]
Output: 1-2,
Input: ["gg", "ff"]
Output: not found
"""

def VowelSquareWithSubmatrix(strArr):
    # Verifica se uma submatriz 2x2 é composta inteiramente por vogais
    def isVowelSubmatrix(r, c):
        return (strArr[r][c] in vowels and strArr[r][c + 1] in vowels and
                strArr[r + 1][c] in vowels and strArr[r + 1][c + 1] in vowels)

    vowels = set('aeiou')  # Conjunto de vogais
    rows = len(strArr)
    cols = len(strArr[0])    

    for row in range(rows - 1):
        for col in range(cols - 1):
            if isVowelSubmatrix(row, col):
                return f'{row}-{col}'

    return "not found"

# Testes
"""
Um caso com múltiplos quadrados 2x2 de vogais, para verificar se a função 
retorna o mais superior e à esquerda.
Um caso onde o quadrado 2x2 de vogais está na borda inferior direita, para 
testar os limites da matriz.
Uma matriz maior sem nenhum quadrado 2x2 de vogais, para testar a eficácia da 
função em não encontrar o que não existe.
Um caso com um quadrado 2x2 de vogais no início da matriz, para confirmar que a 
função captura corretamente os casos nos limites superiores esquerdos.
"""
exemplos = [
    ["aqrst", "ukaei", "ffooo"],
    ["gg", "ff"],                 
    ["aeio", "ouae", "ioup", "aeio"],  # Múltiplos quadrados 2x2 de vogais
    ["abcd", "efgh", "ijkl", "omno"],  # Quadrado 2x2 de vogais na borda inferior direita
    ["qrst", "xyzt", "abcf", "defg"],  # Sem quadrados 2x2 de vogais
    ["ouae", "ioup", "abcd", "efgh"]   # Quadrado 2x2 de vogais no início
]

# Reutilizando os exemplos anteriores para testar essa abordagem
resultados_submatriz = [VowelSquareWithSubmatrix(ex) for ex in exemplos]
print(resultados_submatriz)
