def ler_matriz_txt(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        matriz = [list(map(int, linha.strip().split())) for linha in linhas]
    return matriz

def matriz_quadrada(matriz):
    return all(len(linha) == len(matriz) for linha in matriz)

def somar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

def multiplicar_matrizes(A, B):
    n = len(A)
    resultado = [[0] * n for _ in range(n)]

    print("Passo a passo da multiplicação:")
    for i in range(n):
        for j in range(n):
            soma = 0
            for k in range(n):
                produto = multiplicar(A[i][k], B[k][j])
                soma = somar(soma, produto)
                print(f"Resultado[{i}][{j}] += {A[i][k]} * {B[k][j]} => {produto} (soma parcial: {soma})")
            resultado[i][j] = soma
    return resultado

def exibir_matriz(matriz, nome="Matriz"):
    print(f"\n{nome}:")
    for linha in matriz:
        print(" ".join(map(str, linha)))

# Programa principal
matriz1 = ler_matriz_txt("matriz1.txt")
matriz2 = ler_matriz_txt("matriz2.txt")

if not (matriz_quadrada(matriz1) and matriz_quadrada(matriz2)):
    print("Erro: As matrizes não são quadradas!")
else:
    exibir_matriz(matriz1, "Matriz 1")
    exibir_matriz(matriz2, "Matriz 2")
    
    resultado = multiplicar_matrizes(matriz1, matriz2)
    exibir_matriz(resultado, "Resultado")
    input("\nPressione Enter para sair...")
