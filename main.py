class Estado:

    def __init__(self, final=False):
        self.transicoes = {}  # Dicionário com as possíveis transicoes do estado
        self.final = final  # Igual a True se o estado for final

    def adicionar_transicao(self, letra, estado):
        self.transicoes[letra] = estado

    def next(self, letra):
        if letra in self.transicoes:
            return self.transicoes[letra]
        else:
            return None


def validar_palavra(estado_inicial, palavra):
    estado_atual = estado_inicial

    for letra in palavra:
        estado_atual = estado_atual.next(letra)
        if estado_atual is None:
            return False
    """ 
    Se a função chegou até aqui, então a palavra foi totalmente processada.
    A função então verifica se o estado atual é um estado final. Se for um
    estado final, então a palavra é aceita.
    """
    return estado_atual.final


if __name__ == '__main__':

    q0 = Estado()
    q1 = Estado()
    q2 = Estado(final=True)

    q0.adicionar_transicao('a', q0)
    q0.adicionar_transicao('b', q1)
    q1.adicionar_transicao('b', q2)
    q2.adicionar_transicao('c', q1)

    palavra = input('Digite uma palavra: ')

    if validar_palavra(q0, palavra):
        print('aceita')
    else:
        print('rejeita')
