import numpy as np

class Markov:
    def __init__(self):
        print("Selecione o tipo de configuração da matriz de transição:\n")
        print("1. Modelar Matriz Manualmente")
        print("2. Utilizar Matriz Padrão")
        tipo = input("Digite sua escolha: ")

        if tipo == "1":
            print("\nEscolha o tamanho da matriz para modelar:")
            print("1. Matriz 2x2")
            print("2. Matriz 3x3")
            print("3. Matriz 4x4")
            print("4. Matriz 5x5")
            tamanho = input("Digite sua escolha: ")

            if tamanho == "1":
                self._init_2x2()
            elif tamanho == "2":
                self._init_3x3()
            elif tamanho == "3":
                self._init_4x4()
            elif tamanho == "4":
                self._init_5x5()
            else:
                raise ValueError("Tamanho inválido.")
            
        elif tipo == "2":
            print("\nEscolha o tamanho da matriz padrão:")
            print("1. Matriz 2x2")
            print("2. Matriz 3x3")
            print("3. Matriz 4x4")
            print("4. Matriz 5x5")
            tamanho = input("Digite sua escolha: ")

            if tamanho == "1":
                self._init_padrao_2x2()
            elif tamanho == "2":
                self._init_padrao_3x3()
            elif tamanho == "3":
                self._init_padrao_4x4()
            elif tamanho == "4":
                self._init_padrao_5x5()
            else:
                raise ValueError("Tamanho inválido.")
        else:
            raise ValueError("Opção inválida")

    def _init_2x2(self):
        print("Defina as probabilidades da matriz de transição 2x2 por colunas: ")
        
        # Solicita os valores ao usuário com validação
        self.a = self._probabilidades_de_trasicao("Probabilidade a00: ")
        self.b = self._probabilidades_de_trasicao("Probabilidade a10: ")
        
        self.c = self._probabilidades_de_trasicao("Probabilidade a01: ")
        self.d = self._probabilidades_de_trasicao("Probabilidade a11: ")
        
        # Valida se as colunas somam 1
        if not np.isclose(self.a + self.b, 1) or not np.isclose(self.c + self.d, 1):
            raise ValueError("As colunas da matriz devem somar 1!")
        
        self.transicao = np.array([
            [self.a, self.b],   #Coluna 1  #a00, a10   [a c]
            [self.c, self.d]    #Coluna 2  #a01, a11   [b d]   
        ])
        
        # Estado inicial padrão 
        self.estado = np.array([0, 1])
        self.padrao = -1

        print("Matriz de transição 2x2 padrão definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python imprimire a matriz

    def _init_3x3(self):
        print("Defina as probabilidades da matriz de transição 3x3 por colunas: ")
        
        # Solicita os valores ao usuário com validação
        self.a = self._probabilidades_de_trasicao("Probabilidade a00: ")
        self.b = self._probabilidades_de_trasicao("Probabilidade a01: ")
        self.c = self._probabilidades_de_trasicao("Probabilidade a02: ")

        self.d = self._probabilidades_de_trasicao("Probabilidade a10: ")
        self.e = self._probabilidades_de_trasicao("Probabilidade a11: ")
        self.f = self._probabilidades_de_trasicao("Probabilidade a12: ")

        self.g = self._probabilidades_de_trasicao("Probabilidade a20: ")
        self.h = self._probabilidades_de_trasicao("Probabilidade a21: ")
        self.i = self._probabilidades_de_trasicao("Probabilidade a22: ")

        # Valida se as colunas somam 1
        if not np.isclose(self.a + self.b + self.c, 1) or not np.isclose(self.d + self.e + self.f, 1) or not np.isclose(self.g + self.h + self.i, 1) :
            raise ValueError("As colunas da matriz devem somar 1!")
        
        self.transicao = np.array([
            [self.a, self.b, self.c],   #Coluna 1  a00, a10, a20            [a d g]
            [self.d, self.e, self.f],   #Coluna 2  a01, a11, a21            [b e h]   
            [self.g, self.h, self.i]    #Coluna 3  a02, a12, a22            [c f i]
        ])                      
        
        # Estado inicial padrão 
        self.estado = np.array([0, 0, 1])
        self.padrao = -1

        print("Matriz de transição 3x3 definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python imprimire a matriz

    def _init_4x4(self):
        print("Defina as probabilidades da matriz de transição 4x4 por colunas: ")
        
        # Solicita os valores ao usuário com validação
        self.a = self._probabilidades_de_trasicao("Probabilidade a00: ")
        self.b = self._probabilidades_de_trasicao("Probabilidade a01: ")
        self.c = self._probabilidades_de_trasicao("Probabilidade a02: ")
        self.d = self._probabilidades_de_trasicao("Probabilidade a03: ")

        self.e = self._probabilidades_de_trasicao("Probabilidade a10: ")
        self.f = self._probabilidades_de_trasicao("Probabilidade a11: ")
        self.g = self._probabilidades_de_trasicao("Probabilidade a12: ")
        self.h = self._probabilidades_de_trasicao("Probabilidade a13: ")

        self.i = self._probabilidades_de_trasicao("Probabilidade a20: ")
        self.j = self._probabilidades_de_trasicao("Probabilidade a21: ")
        self.k = self._probabilidades_de_trasicao("Probabilidade a22: ")
        self.l = self._probabilidades_de_trasicao("Probabilidade a23: ")

        self.m = self._probabilidades_de_trasicao("Probabilidade a30: ")
        self.n = self._probabilidades_de_trasicao("Probabilidade a31: ")
        self.o = self._probabilidades_de_trasicao("Probabilidade a32: ")
        self.p = self._probabilidades_de_trasicao("Probabilidade a33: ")

        # Valida se as colunas somam 1
        if not np.isclose(self.a + self.b + self.c + self.d, 1) or not np.isclose(self.e + self.f + self.g + self.h, 1) or not np.isclose(self.i + self.j + self.k + self.l, 1) or not np.isclose(self.m + self.n + self.o + self.p, 1) :
            raise ValueError("As colunas da matriz devem somar 1!")
        
        self.transicao = np.array([
            [self.a, self.b, self.c, self.d],    #Coluna 1  a00, a10, a20, a30            [a e i m]
            [self.e, self.f, self.g, self.h],    #Coluna 2  a01, a11, a21, a31            [b f j n]   
            [self.i, self.j, self.k, self.l],    #Coluna 3  a02, a12, a22, a32            [c g k o]
            [self.m, self.n, self.o, self.p]     #Coluna 4  a03, a13, a23, a33            [d h l p]
        ])
        
        # Estado inicial padrão 
        self.estado = np.array([0, 0, 0 ,1])
        self.padrao = -1

        print("Matriz de transição 4x4 definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python imprimire a matriz

    def _init_5x5(self):
        print("Defina as probabilidades da matriz de transição 5x5 por colunas: ")
        
        # Solicita os valores ao usuário com validação
        self.a = self._probabilidades_de_trasicao("Probabilidade a00: ")
        self.b = self._probabilidades_de_trasicao("Probabilidade a01: ")
        self.c = self._probabilidades_de_trasicao("Probabilidade a02: ")
        self.d = self._probabilidades_de_trasicao("Probabilidade a03: ")
        self.e = self._probabilidades_de_trasicao("Probabilidade a04: ")

        self.f = self._probabilidades_de_trasicao("Probabilidade a10: ")
        self.g = self._probabilidades_de_trasicao("Probabilidade a11: ")
        self.h = self._probabilidades_de_trasicao("Probabilidade a12: ")
        self.i = self._probabilidades_de_trasicao("Probabilidade a13: ")
        self.j = self._probabilidades_de_trasicao("Probabilidade a14: ")

        self.k = self._probabilidades_de_trasicao("Probabilidade a20: ")
        self.l = self._probabilidades_de_trasicao("Probabilidade a21: ")
        self.m = self._probabilidades_de_trasicao("Probabilidade a22: ")
        self.n = self._probabilidades_de_trasicao("Probabilidade a23: ")
        self.o = self._probabilidades_de_trasicao("Probabilidade a24: ")

        self.p = self._probabilidades_de_trasicao("Probabilidade a30: ")
        self.q = self._probabilidades_de_trasicao("Probabilidade a31: ")
        self.r = self._probabilidades_de_trasicao("Probabilidade a32: ")
        self.s = self._probabilidades_de_trasicao("Probabilidade a33: ")
        self.t = self._probabilidades_de_trasicao("Probabilidade a34: ")

        self.u = self._probabilidades_de_trasicao("Probabilidade a40: ")
        self.v = self._probabilidades_de_trasicao("Probabilidade a41: ")
        self.w = self._probabilidades_de_trasicao("Probabilidade a42: ")
        self.x = self._probabilidades_de_trasicao("Probabilidade a43: ")
        self.y = self._probabilidades_de_trasicao("Probabilidade a44: ")

        # Valida se as colunas somam 1
        if not np.isclose(self.a + self.b + self.c + self.d + self.e, 1) or not np.isclose(self.f + self.g + self.h + self.i +self.j, 1) or not np.isclose(self.k + self.l + self.m + self.n + self.o, 1) or not np.isclose(self.p + self.q + self.r + self.s + self.t, 1) or not np.isclose(self.u + self.v + self.w + self.x + self.y, 1) :
            raise ValueError("As colunas da matriz devem somar 1!")
        
        self.transicao = np.array([
            [self.a, self.b, self.c, self.d, self.e],    #Coluna 1  a00, a10, a20, a30, a40            [a f k p u]
            [self.f, self.g, self.h, self.i, self.j],    #Coluna 2  a01, a11, a21, a31, a41            [b g l q v]   
            [self.k, self.l, self.m, self.n, self.o],    #Coluna 3  a02, a12, a22, a32, a42            [c h m r w]
            [self.p, self.q, self.r, self.s, self.t],    #Coluna 4  a03, a13, a23, a33, a43            [d i n s x]
            [self.u, self.v, self.w, self.x, self.y]     #Coluna 5  a04, a14, a24, a34, a44            [e j o t y]
        ])
        
        # Estado inicial padrão 
        self.estado = np.array([0, 0, 0, 0 ,1])
        self.padrao = -1

        print("Matriz de transição 5x5 definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python imprimire a matriz

    def _init_padrao_2x2(self):   
        # Solicita os valores ao usuário com validação
        self.a = 0.7                      #[a00, a10]  [0.7, 0.6]
        self.b = 0.3                      #[a01, a11]  [0.3, 0.4]
        self.c = 0.6
        self.d = 0.4
        
        # Valida se as colunas somam 1
        if not np.isclose(self.a + self.b, 1) or not np.isclose(self.c + self.d, 1):
            raise ValueError("As colunas da matriz devem somar 1!")
        
        self.transicao = np.array([
            [self.a, self.b],   #Coluna 1  #a00, a10   [a c]
            [self.c, self.d]    #Coluna 2  #a01, a11   [b d]   
        ])
        
        # Estado inicial padrão 
        self.estado = np.array([0, 1])
        self.padrao = 2

        print("Matriz de transição 2x2 padrão definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python imprimire a matriz

    def _init_padrao_3x3(self):                              #Padrao Exemplo Pronto e Documentado
        # Solicita os valores ao usuário com validação
        self.a = 0.8
        self.b = 0.2
        self.c = 0

        self.d = 0.1
        self.e = 0.8
        self.f = 0.1

        self.g = 0
        self.h = 0.2
        self.i = 0.8

        # Valida se as colunas somam 1
        if not np.isclose(self.a + self.b + self.c, 1) or not np.isclose(self.d + self.e + self.f, 1) or not np.isclose(self.g + self.h + self.i, 1) :
            raise ValueError("As colunas da matriz devem somar 1!")
        
        self.transicao = np.array([
            [self.a, self.b, self.c],   #Coluna 1  a00, a10, a20            [a d g]
            [self.d, self.e, self.f],   #Coluna 2  a01, a11, a21            [b e h]   
            [self.g, self.h, self.i]    #Coluna 3  a02, a12, a22            [c f i]
        ])                      
        
        # Estado inicial padrão 
        self.estado = np.array([0, 0, 1])
        self.padrao = 3

        print("Matriz de transição 3x3 padrão definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python imprimire a matriz

    def _init_padrao_4x4(self):
        self.a = 0.2
        self.b = 0.3
        self.c = 0
        self.d = 0.5

        self.e = 0
        self.f = 0.7
        self.g = 0.1
        self.h = 0.2

        self.i = 0
        self.j = 0
        self.k = 0.5
        self.l = 0.5

        self.m = 1
        self.n = 0
        self.o = 0
        self.p = 0

        # Valida se as colunas somam 1
        if not np.isclose(self.a + self.b + self.c + self.d, 1) or not np.isclose(self.e + self.f + self.g + self.h, 1) or not np.isclose(self.i + self.j + self.k + self.l, 1) or not np.isclose(self.m + self.n + self.o + self.p, 1) :
            raise ValueError("As colunas da matriz devem somar 1!")
        
        self.transicao = np.array([
            [self.a, self.b, self.c, self.d],    #Coluna 1  a00, a10, a20, a30            [a e i m]
            [self.e, self.f, self.g, self.h],    #Coluna 2  a01, a11, a21, a31            [b f j n]   
            [self.i, self.j, self.k, self.l],    #Coluna 3  a02, a12, a22, a32            [c g k o]
            [self.m, self.n, self.o, self.p]     #Coluna 4  a03, a13, a23, a33            [d h l p]
        ])
        
        # Estado inicial padrão 
        self.estado = np.array([0, 0, 0 ,1])
        self.padrao = 4

        print("Matriz de transição 4x4 padrão definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python imprimire a matriz

    def _init_padrao_5x5(self):
        self.a = 0.3
        self.b = 0.7
        self.c = 0
        self.d = 0
        self.e = 0

        self.f = 0.5
        self.g = 0.5
        self.h = 0
        self.i = 0
        self.j = 0

        self.k = 0
        self.l = 0
        self.m = 1
        self.n = 0
        self.o = 0

        self.p = 0
        self.q = 0
        self.r = 0.2
        self.s = 0.8
        self.t = 0

        self.u = 1
        self.v = 0
        self.w = 0
        self.x = 0
        self.y = 0

        # Valida se as colunas somam 1
        if not np.isclose(self.a + self.b + self.c + self.d + self.e, 1) or not np.isclose(self.f + self.g + self.h + self.i +self.j, 1) or not np.isclose(self.k + self.l + self.m + self.n + self.o, 1) or not np.isclose(self.p + self.q + self.r + self.s + self.t, 1) or not np.isclose(self.u + self.v + self.w + self.x + self.y, 1) :
            raise ValueError("As colunas da matriz devem somar 1!")
        
        self.transicao = np.array([
            [self.a, self.b, self.c, self.d, self.e],    #Coluna 1  a00, a10, a20, a30, a40            [a f k p u]
            [self.f, self.g, self.h, self.i, self.j],    #Coluna 2  a01, a11, a21, a31, a41            [b g l q v]   
            [self.k, self.l, self.m, self.n, self.o],    #Coluna 3  a02, a12, a22, a32, a42            [c h m r w]
            [self.p, self.q, self.r, self.s, self.t],    #Coluna 4  a03, a13, a23, a33, a43            [d i n s x]
            [self.u, self.v, self.w, self.x, self.y]     #Coluna 5  a04, a14, a24, a34, a44            [e j o t y]
        ])
        
        # Estado inicial padrão 
        self.estado = np.array([0, 0, 0, 0 ,1])
        self.padrao = 5

        print("Matriz de transição 5x5 padrão definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python imprimire a matriz

    def _probabilidades_de_trasicao(self, mensagem):   
        #Lê uma probabilidade válida (0-1) do usuário
        while True:
            try:
                valor = float(input(mensagem))
                if 0 <= valor <= 1:
                    return valor
                print("Valor deve estar entre 0 e 1!")
            except ValueError:
                print("Digite um número válido!")
    
    def simular(self, interacoes):
        # Executa a simulação para o número de interacoes especificado
        print("\nResultados da Simulação:")
        for i in range(interacoes):
            self.estado = np.dot(self.estado, self.transicao)
            
            if len(self.estado) == 2:
                print(f"Interação {i+1}: Estado 1 = {self.estado[0]:.4f}, Estado 2 = {self.estado[1]:.4f}")
            elif len(self.estado) == 3:
                print(f"Interação {i+1}: Estado 1 = {self.estado[0]:.4f}, Estado 2 = {self.estado[1]:.4f}, Estado 3 = {self.estado[2]:.4f}")
            elif len(self.estado) == 4:
                print(f"Interação {i+1}: Estado 1 = {self.estado[0]:.4f}, Estado 2 = {self.estado[1]:.4f}, Estado 3 = {self.estado[2]:.4f}, Estado 4 = {self.estado[3]:.4f}")
            elif len(self.estado) == 5:
                print(f"Interação {i+1}: Estado 1 = {self.estado[0]:.4f}, Estado 2 = {self.estado[1]:.4f}, Estado 3 = {self.estado[2]:.4f}, Estado 4 = {self.estado[3]:.4f}, Estado 5 = {self.estado[4]:.4f}")

        print("\nDistribuição Final:")
        for i, prob in enumerate(self.estado):
            print(f"Probabilidade do Estado {i+1}: {prob*100:.2f}%")

  
def main():
    try:
        print("Simulação de Cadeia de Markov")
        
        # Cria a cadeia de Markov
        cadeia = Markov()
        
        # Configura o estado inicial
        if len(cadeia.estado) == 2:
            p1 = float(input("\nProbabilidade do Estado 1 inicial (0-1, padrão 0): ") or 0)
            p2 = 1 - p1
            print(f"Probabilidade do Estado 2 inicial (0-1, padrão restante {p2:g}): {p2:g}")
            cadeia.estado = np.array([p1, p2])
        elif len(cadeia.estado) == 3:
            p1 = float(input("\nProbabilidade do Estado 1 inicial (0-1, padrão 0): ") or 0)
            p2 = float(input("Probabilidade do Estado 2 inicial (0-1, padrão 0): ") or 0)
            p3 = 1 - p1 - p2
            print(f"Probabilidade do Estado 3 inicial (0-1, padrão restante {p3:g}): {p3:g}")
            if p3 < 0:
                raise ValueError("A soma das probabilidades iniciais não pode exceder 1!")
            cadeia.estado = np.array([p1, p2, p3])
        elif len(cadeia.estado) == 4:
            p1 = float(input("\nProbabilidade do Estado 1 inicial (0-1, padrão 0): ") or 0)
            p2 = float(input("Probabilidade do Estado 2 inicial (0-1, padrão 0): ") or 0)
            p3 = float(input("Probabilidade do Estado 3 inicial (0-1, padrão 0): ") or 0)
            p4 = 1 - p1 - p2 - p3
            print(f"Probabilidade do Estado 4 inicial (0-1, padrão restante {p4:g}): {p4:g}")
            if p4 < 0:
                raise ValueError("A soma das probabilidades iniciais não pode exceder 1!")
            cadeia.estado = np.array([p1, p2, p3, p4])
        elif len(cadeia.estado) == 5:
            p1 = float(input("\nProbabilidade do Estado 1 inicial (0-1, padrão 0): ") or 0)
            p2 = float(input("Probabilidade do Estado 2 inicial (0-1, padrão 0): ") or 0)
            p3 = float(input("Probabilidade do Estado 3 inicial (0-1, padrão 0): ") or 0)
            p4 = float(input("Probabilidade do Estado 4 inicial (0-1, padrão 0): ") or 0)
            p5 = 1 - p1 - p2 - p3 - p4
            print(f"Probabilidade do Estado 5 inicial (0-1, padrão restante {p5:g}): {p5:g}")
            if p5 < 0:
                raise ValueError("A soma das probabilidades iniciais não pode exceder 1!")
            cadeia.estado = np.array([p1, p2, p3, p4, p5])
        
        if len(cadeia.estado) == 2 and cadeia.padrao == 2:
            interacoes = int(input("\nQuantos interações deseja simular? (padrão 10 Interações) ") or 10) # Padrão 10 interacoes
        elif len(cadeia.estado) == 3 and cadeia.padrao == 3:
            interacoes = int(input("\nQuantos interações deseja simular? (padrão 5 Interações) ") or 5) # Padrão 5 interacoes para o exercicio
        elif len(cadeia.estado) == 4 and cadeia.padrao == 4:
            interacoes = int(input("\nQuantos interações deseja simular? (padrão 20 Interações) ") or 20) # Padrão 20 interacoes
        elif len(cadeia.estado) == 5 and cadeia.padrao == 5:
            interacoes = int(input("\nQuantos interações deseja simular? (padrão 100 Interações) ") or 100) # Padrão 100 interacoes #Nao pronto
        else:
            interacoes = int(input("\nQuantos interações deseja simular? (padrão 100 Interações) ") or 100) # Padrão 100 interacoes
        print(f"\nIniciando simulação para {interacoes:g} interações...")
        cadeia.simular(interacoes)
        
    except ValueError as e:
        print(f"\nErro: {e}")


main()

'''
Cadeias de markov são cadeias de probabilidades que como a matriz de probabilidade de transição é regular
elas chegam a um ponto que as probabilidades nao dependem mais do estado inicial 
assim chegando a forma de matriz estocástica

[a c] . [pi1]  =  [p1]    ->   [a c] . [p1] = [p1]  ... = [pe]
[b d]   [pi2]     [p2]         [b d]   [p2]   [p2]        [pe]

[acbd] = matriz transição
pi = probabilidade inicial
p = probabilidade de condição
pe = probabilidade estocástica

'''