import numpy as np

class Markov:
    def __init__(self):
        print("Selecione o tamanho da matriz de transição:")
        print("1. Modelar Matriz 2x2")
        print("2. Modelar Matriz 3x3")
        print("3. Padrão Matriz 2x2")
        print("4. Padrão Matriz 3x3")
        escolha = input("Digite sua escolha: ")
        
        if escolha == "1":
            self._init_2x2()
        elif escolha == "2":
            self._init_3x3()
        elif escolha == "3":
            self._init_padrao_2x2()
        elif escolha == "4":
            self._init_padrao_3x3()
        else:
            raise ValueError("Escolha inválida.")

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
        print("Matriz de transição 2x2 padrão definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python lê a matriz

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
        print("Matriz de transição 2x2 padrão definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python lê a matriz

    def _init_padrao_2x2(self):   
        # Solicita os valores ao usuário com validação
        self.a = 0.97                      #[a00, a10]  [0.97, 0.01]
        self.b = 0.03                      #[a01, a11]  [0.03, 0.99]
        self.c = 0.01
        self.d = 0.99
        
        # Valida se as colunas somam 1
        if not np.isclose(self.a + self.b, 1) or not np.isclose(self.c + self.d, 1):
            raise ValueError("As colunas da matriz devem somar 1!")
        
        self.transicao = np.array([
            [self.a, self.b],   #Coluna 1  #a00, a10   [a c]
            [self.c, self.d]    #Coluna 2  #a01, a11   [b d]   
        ])
        
        # Estado inicial padrão 
        self.estado = np.array([0, 1])

        print("Matriz de transição 2x2 padrão definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python lê a matriz

    def _init_padrao_3x3(self):
        # Solicita os valores ao usuário com validação
        self.a = 0.7
        self.b = 0.2
        self.c = 0.1

        self.d = 0.2
        self.e = 0.6
        self.f = 0.2

        self.g = 0.1
        self.h = 0.3
        self.i = 0.6

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

        print("Matriz de transição 3x3 padrão definida:")
        print(self.transicao.T) #.T para imprimir transposta que é o formato correto por conta do jeito que o python lê a matriz

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
    
    def simular(self, anos):
        # Executa a simulação para o número de anos especificado
        print("\nResultados da Simulação:")
        for i in range(anos):
            self.estado = np.dot(self.estado, self.transicao)
            
            if len(self.estado) == 2:
                print(f"Ano {i+1}: Estado 1 = {self.estado[0]:.4f}, Estado 2 = {self.estado[1]:.4f}")
            else:
                print(f"Ano {i+1}: Estado 1 = {self.estado[0]:.4f}, Estado 2 = {self.estado[1]:.4f}, Estado 3 = {self.estado[2]:.4f}")
        
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
            p1 = float(input("\nProbabilidade do Estado 1 inicial (0-1, padrão 1): ") or 1)
            p2 = 1 - p1
            print(f"Probabilidade do Estado 2 inicial (0-1, padrão {p2:g}): {p2:g}")
            cadeia.estado = np.array([p1, p2])
        else:
            p1 = float(input("\nProbabilidade do Estado 1 inicial (0-1, padrão 1): ") or 1)
            p2 = float(input("Probabilidade do Estado 2 inicial (0-1, padrão 0): ") or 0)
            p3 = 1 - p1 - p2
            print(f"Probabilidade do Estado 3 inicial (0-1, padrão {p3:g}): {p3:g}")
            if p3 < 0:
                raise ValueError("A soma das probabilidades iniciais não pode exceder 1!")
            cadeia.estado = np.array([p1, p2, p3])
        
        anos = int(input("\nQuantos anos deseja simular? "))
        cadeia.simular(anos)
        
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