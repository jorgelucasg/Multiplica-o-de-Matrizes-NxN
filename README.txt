# 🧮 Atividade 06/08 – Multiplicação de Matrizes (Python)

Trabalho da disciplina de **Programação Orientada a Objetos**, com o objetivo de:

- Ler duas matrizes quadradas de arquivos `.txt`
- Verificar se as matrizes são quadradas (NxN)
- Multiplicar as matrizes utilizando funções próprias de soma e multiplicação
- Mostrar o passo a passo da multiplicação
- Pedir ao usuário dois números para demonstrar o funcionamento das funções `somar()` e `multiplicar()`

---

# ✅ Como executar o projeto

## 🔧 Requisitos

- Python instalado no sistema:  
  👉 https://www.python.org/downloads/

- VS Code (recomendado):  
  👉 https://code.visualstudio.com/

---

## 🚀 Executar o programa

1. Coloque os arquivos em uma pasta:
   - `main.py`
   - `matriz1.txt`
   - `matriz2.txt`

2. Abra essa pasta no VS Code.

3. No terminal do VS Code, execute:

```
py main.py
```

---

## 📌 O que o programa faz

- Lê os arquivos `matriz1.txt` e `matriz2.txt`
- Verifica se são matrizes quadradas
- Realiza a multiplicação das matrizes com explicação passo a passo
- Exibe a matriz resultado
- Solicita dois números ao usuário e exibe:
  - A **soma** usando a função `somar(a, b)`
  - A **multiplicação** usando a função `multiplicar(a, b)`

---

# 📄 Exemplo dos arquivos `.txt`

### `matriz1.txt`
```
1 2
3 4
```

### `matriz2.txt`
```
5 6
7 8
```

---

# 💻 Exemplo de saída (resumo)

```
Matriz 1:
1 2
3 4

Matriz 2:
5 6
7 8

Passo a passo da multiplicação:
Resultado[0][0] += 1 * 5 => 5 (soma parcial: 5)
Resultado[0][0] += 2 * 7 => 14 (soma parcial: 19)
...

Resultado:
19 22
43 50

Digite o primeiro número: 3
Digite o segundo número: 4
3 + 4 = 7
3 * 4 = 12
```

---

# 📁 Organização da pasta

```
atividade_matrizes/
├── main.py
├── matriz1.txt
├── matriz2.txt
└── README.md
```

---

# 👨‍💻 Autor

Desenvolvido como atividade acadêmica para o curso de **Análise e Desenvolvimento de Sistemas - UniCesumar (Unidade Portão - Curitiba)**.
