estado_inicial = [ # Bolinhas no copo...
    ['v', 'a', 'v', 'l'],
    ['a', 'l', 'a', 'v'],
    ['l', 'v', 'a', 'l'],
    [],
    []
]

# auxiliares
limite_qtd = 4 # maximo de bolinhas no copo
qtd_de_copos = len(estado_inicial)   # qtd de copos
aux_estado_inicial = () # aux para marcar como um estado visitado
lista_temp = [] # guardar temporariamente

for copo in estado_inicial:
    # cria uma tupla para cada copo (imutável)
    copo_tuple = ()
    for bola in copo:
        copo_tuple = copo_tuple + (bola,) # adiciona o copo como tupla à lista temporária
    lista_temp.append(copo_tuple)

aux_estado_inicial = ()
for copo_tuple in lista_temp: # transforma a lista de tuplas em uma tupla final
    aux_estado_inicial = aux_estado_inicial + (copo_tuple)

fila = [estado_inicial] # fila de estados ainda p/ explorar (cada item é uma lista de listas)
visitados = [aux_estado_inicial] # lista de estados já vistos, como tuplas imutáveis
movimentos = [[estado_inicial]] # caminhos: cada item é uma lista com o caminho (sequência de estados) até aquele estado

achou = False
passos = 0

while len(fila) > 0:
    # pegar o primeiro estado e seu caminho
    atual = fila[0]
    caminho_atual = movimentos[0]

    # remover o primeiro elemento de fila e movimentos
    fila = fila[1:]
    movimentos = movimentos[1:]
    passos = passos + 1
    completos = 0 # Conta qts copos estão completos...
    indice_copo = 0

    # percorre cada copo e verifica se:
    #  - tem limite_qtd bolinhas
    #  - todas as bolinhas dentro dele são da mesma cor
    for copo in atual:
        tamanho_copo = len(copo)
        if tamanho_copo == limite_qtd:
            # construir conjunto de cores do copo manualmente
            conjunto_cores = set()
            for bola in copo:
                conjunto_cores.add(bola)
            # se o conjunto tiver tamanho 1, todas as bolas são iguais
            if len(conjunto_cores) == 1:
                completos = completos + 1
        indice_copo = indice_copo + 1

    if completos >= 3: # Encheu três copos com as mesmas cores, se sim deu bom
        print("Estado final encontrado em", passos, "iterações!\n")
        achou = True
        break

    i = 0 # para cada copo origem i
    for i in range(qtd_de_copos):
        if len(atual[i]) == 0: # Verifica se o copo tá vazio, se estiver não tem como tirar
            continue # Ai ele pula

        cor_bola = atual[i][-1] # Pega a cor da bola no primeiro copo

        j = 0 # tentar mover essa bola para cada copo destino j
        for j in range(qtd_de_copos):
            if i == j: # verifica p/ não cair no msm copo
                continue

            tamanho_destino = len(atual[j]) # pega a qtd de espaços p/ colocar uma bolinha
            destino_tem_espaco = (tamanho_destino < limite_qtd) # vê sem tem espaço para colocar a bolinha
            destino_vazio = (tamanho_destino == 0)
            topo_compatível = False

            if destino_vazio == False: # se o copo não estiver vazio
                cor_topo_destino = atual[j][-1] # pega a cor do topo do copo de destino
                if cor_topo_destino == cor_bola: # vê se a cor bate com a outra cor
                    topo_compatível = True # se bater deixa como verdadiero

            # só é válido se houver espaço e (vazio ou compatível)
            movimento_valido = destino_tem_espaco and (destino_vazio or topo_compatível)

            if movimento_valido:
                novo_estado = [] # criar a cópia manual
                for copo in atual:
                    copia = [] # cria uma nova lista contendo os mesmos elementos do copo atual
                    for item in copo: # pega cada bolinha
                        copia.append(item) # adiciona uma copia dessa bolinha
                    novo_estado.append(copia) # e no final vira uma copia do geral de copos

                # efetua o movimento no novo_estado
                bola = novo_estado[i].pop()   # remove topo do copo origem
                novo_estado[j].append(bola)   # adiciona ao topo do copo destino

                lista_temp2 = [] # lista temporária de tuplas
                for copo_novo in novo_estado:
                    copo_tuple = ()
                    for b in copo_novo:
                        copo_tuple = copo_tuple + (b,)
                    lista_temp2.append(copo_tuple)
                # transforma a lista em tupla final
                estado_normalizado = ()
                for copo_tuple in lista_temp2:
                    estado_normalizado = estado_normalizado + (copo_tuple,)

                # verificar se já visitamos esse estado ( p/ evitar repetir)
                ja_visitado = False
                for v in visitados:
                    if v == estado_normalizado:
                        ja_visitado = True
                        break

                if not ja_visitado:
                    visitados.append(estado_normalizado) # marcar como visitado
                    fila.append(novo_estado) # enfileirar o novo estado para explorar depois
                    novo_caminho = [] # armazenar o caminho até esse novo estado (caminho_atual + [novo_estado])
                    
                    # copiar passo a passo o caminho_atual para novo_caminho
                    for estado_no_caminho in caminho_atual:
                        copia_estado_caminho = []
                        for copo in estado_no_caminho:
                            copo_copia = []
                            for item in copo:
                                copo_copia.append(item)
                            copia_estado_caminho.append(copo_copia)
                        novo_caminho.append(copia_estado_caminho)
                        
                    # agora adicionar o novo_estado como uma cópia tbm
                    copia_para_armazenar = []
                    for copo in novo_estado:
                        copo_copy = []
                        for it in copo:
                            copo_copy.append(it)
                        copia_para_armazenar.append(copo_copy)
                    novo_caminho.append(copia_para_armazenar)

                    movimentos.append(novo_caminho)

if achou == True:
    print("Movimentos até o resultado:\n")
    # caminho_atual já contém os estados até o estado atual
    caminho_para_imprimir = []
    
    # copiar caminho_atual para evitar referências
    for estado_no_caminho in caminho_atual:
        copia_estado = []
        for copo in estado_no_caminho:
            copo_copia = []
            for item in copo:
                copo_copia.append(item)
            copia_estado.append(copo_copia)
        caminho_para_imprimir.append(copia_estado)
    # adicionar o estado final (atual)
    copia_final = []
    for copo in atual:
        c = []
        for b in copo:
            c.append(b)
        copia_final.append(c)
    caminho_para_imprimir.append(copia_final)

    for passo, estado in enumerate(caminho_para_imprimir):
        print(f"Movimento {passo}:")
        for num_copo, copo in enumerate(estado):
            print(f" Copo {num_copo + 1}: {copo}")
        print("-" * 40)
else:
    print("B.o na sequencia dos copos...")

print("\nTotal de estados gerados:", len(visitados))
print("Total de iterações:", passos)
