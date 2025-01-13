def flippingMatrix(matrix):
    n = len(matrix) // 2  # Tamanho do sub-quadrante superior esquerdo
    max_sum = 0

    # Itera sobre as posições do sub-quadrante
    for i in range(n):
        for j in range(n):
            # Escolhe o maior valor possível para cada posição no sub-quadrante
            max_sum += max(
                matrix[i][j],                                # Elemento original
                matrix[i][2 * n - j - 1],                    # Espelho na linha
                matrix[2 * n - i - 1][j],                    # Espelho na coluna
                matrix[2 * n - i - 1][2 * n - j - 1]         # Espelho diagonal
            )
    return max_sum

matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for x in matriz:
    print(x)
result = flippingMatrix(matriz)
print(result)