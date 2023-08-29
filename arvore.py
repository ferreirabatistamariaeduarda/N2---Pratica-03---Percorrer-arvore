class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None


class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir_em_nivel(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._inserir_em_nivel_recursivo(self.raiz, valor)

    def _inserir_em_nivel_recursivo(self, no, valor):
        if valor < no.valor:
            if no.esquerda is None:
                no.esquerda = No(valor)
            else:
                self._inserir_em_nivel_recursivo(no.esquerda, valor)
        else:
            if no.direita is None:
                no.direita = No(valor)
            else:
                self._inserir_em_nivel_recursivo(no.direita, valor)

    def mostrar_pre_ordem(self):
        if self.raiz is None:
            print('A árvore está vazia.')
        else:
            self.mostrar_pre_ordem_recursivo(self.raiz)

    def mostrar_pre_ordem_recursivo(self, no):
        print(no.valor, end=" ")
        if no.esquerda is not None:
            self.mostrar_pre_ordem_recursivo(no.esquerda)
        if no.direita is not None:
            self.mostrar_pre_ordem_recursivo(no.direita)

    def inOrder(self, no):
        if no != None:
            self.inOrder(no.esquerda)
            print(no.valor, end=" ")
            self.inOrder(no.esquerda)


    def posOrder(self, no):
        if no != None:
            self.posOrder(no.esquerda)
            self.posOrder(no.esquerda)
            print(no.valor, end=" ")
# Exemplo de uso
arvore = ArvoreBinaria()
arvore.inserir_em_nivel(5)
arvore.inserir_em_nivel(3)
arvore.inserir_em_nivel(7)
arvore.inserir_em_nivel(2)
arvore.inserir_em_nivel(4)
arvore.inserir_em_nivel(6)
arvore.inserir_em_nivel(8)
print('pré-Ordem: ')
arvore.mostrar_pre_ordem()
print(' ')
print('in-Ordem: ')
arvore.inOrder(arvore.raiz)
print(' ')
print('pós-Ordem: ')
arvore.posOrder(arvore.raiz)

