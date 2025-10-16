# 2K25 - Tópicos Especiais
# v = verde, a = azul, l = laranja
inicio = [
    ['verdeClaro', 'ciano', 'amarelo', 'azulEscuro','azulEscuro'],
    ['verdeClaro', 'verdeClaro', 'amarelo', 'rosaEscuro','azulEscuro'],
    ['verdeClaro', 'ciano', 'amarelo', 'azulEscuro','ciano'],
    ['ciano', 'ciano', 'amarelo', 'azulEscuro','azulEscuro'],
    ['verdeClaro', 'rosaEscuro', 'amarelo', 'azulEscuro','azulEscuro'],
    ['verdeClaro', 'ciano', 'amarelo', 'azulEscuro','verdeClaro'],
    ['verdeClaro', 'ciano', 'amarelo', 'azulEscuro','azulEscuro'],
    ['verdeClaro', 'ciano', 'amarelo', 'azulEscuro','rosaEscuro'],
    ['rosaEscuro', 'ciano', 'amarelo', 'azulEscuro','azulEscuro'],
    ['verdeClaro', 'ciano', 'amarelo', 'azulEscuro','verdeClaro'],
    ['verdeClaro', 'ciano', 'azulEscuro', 'ciano','azulEscuro'],
    ['verdeClaro', 'ciano', 'amarelo', 'verdeClaro','rosaEscuro'],
    [],
    []
],

limite = 5
visitados = []
fila = [inicio]
caminhos = [[]]

while len(fila) > 0:
    status = fila[0] # Pega o primeiro status da fila
    caminho = caminhos[0] # Pega o primeiro status para movimento

    fila.pop(0) # Remove esse status da fila(Pq já tá sendo testado os status)
    caminhos.pop(0) # Remove o primeiro status pq é o inicial

    coposCompletos = 0 # Conta quantos copos estão coposCompletos(Tanto na corBolinha quanto no tamanho)

    for copo in status: # Pega cada copo
        if len(copo) == limite and len(set(copo)) == 1: # Verifica a quantidade e se são da msm corBolinha
            coposCompletos += 1 # intera na variavel auxiliar

    if coposCompletos >= 3: # Se já tem 3 copos coposCompletos, o jogo acabou :)
        print("Solução foi encontrada! :)\n")
        for passo, situacao in enumerate(caminho): # Printa os movimentos que foram feitos
            print(f"Movimento {passo}:")
            for n, copo in enumerate(situacao):
                print(f" Copo {n + 1}: {copo}")
            print("-" * 40)
        break

    if status not in visitados: # Marca esse status como visitado caso não tenha sido ainda
        visitados.append(status)

        # Tenta mover bolinhas de um copo para outro
        for i in range(len(status)): # primeiro copo
            if len(status[i]) == 0: # Verifica se o copo tá vazio
                continue  # se tiver pula

            corBolinha = status[i][-1]  # pega a bolinha do topo do copo que encontrou

            for j in range(len(status)): # Vai olhar os outros copos
                if i == j: # Verifica se não é o msm
                    continue  # se for, não move

                # verifica se dá pra colocar
                if len(status[j]) < limite and (len(status[j]) == 0 or status[j][-1] == corBolinha):
                    
                    novoTeste = [list(copo) for copo in status] # faz uma cópia do status atual

                    # tira a bolinha do copo de origem e coloca no destino
                    bola = novoTeste[i].pop() # a bola vai ter o valor da bolinha que vai ser movida ao msm tempo que novoTeste perde esse valor
                    novoTeste[j].append(bola) # aqui a bolinha é adicionada no copo que é pra ser adicionada

                    
                    if novoTeste not in visitados: # se ainda não está foi criado
                        fila.append(novoTeste) # adiciona no fim da fila
                        caminhos.append(caminho + [(i, j)]) # Adiciona o status nos caminhos que foram feitos

else:
    print("Nenhuma solução encontrada. :/")
