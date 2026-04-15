def evaluar_jugada(dados):
    valores = sorted(dados, reverse=True)
    conteo = {x: valores.count(x) for x in set(valores)}
    frecuencias = sorted(conteo.values(), reverse=True)
    orden_v = sorted(conteo.items(), key=lambda x: (x[1], x[0]), reverse=True)
    v_score = [x[0] for x in orden_v]

    if frecuencias == [5]:
        return "Repóker", 800 + v_score[0]
    if frecuencias == [4, 1]:
        return "Póker", 700 + v_score[0]
    if frecuencias == [3, 2]:
        return "Full House", 600 + (v_score[0] * 10) + v_score[1]
    
    es_escalera = all(valores[i] - valores[i+1] == 1 for i in range(len(valores)-1))
    if es_escalera:
        return "Escalera", 500 + valores[0]
    
    if frecuencias == [3, 1, 1]:
        return "Trio", 400 + v_score[0]
    if frecuencias == [2, 2, 1]:
        return "Doble Pareja", 300 + (v_score[0] * 10) + (v_score[1])
    if frecuencias == [2, 1, 1, 1]:
        return "Pareja", 200 + v_score[0]
    
    return "Carta Alta", 100 + valores[0]

def ia_facil(dados):
    return [i for i, _ in enumerate(dados)]

def ia_media(dados):
    conteo = {x: dados.count(x) for x in set(dados)}
    max_frec = max(conteo.values())
    if max_frec >= 2:
        valor_mantener = [v for v, c in conteo.items() if c == max_frec][0]
        return [i for i, v in enumerate(dados) if v != valor_mantener]
    return [i for i, _ in enumerate(dados)]

def ia_inteligente(dados):
    conteo = {x: dados.count(x) for x in set(dados)}
    valor_mantener = max(conteo, key=conteo.get)
    if conteo[valor_mantener] > 1:
        return [i for i, v in enumerate(dados) if v != valor_mantener]
    
    if all(x in dados for x in [2,3,4,5]) or all(x in dados for x in [1,2,3,4]) or all(x in dados for x in [3,4,5,6]):
        return [i for i, v in enumerate(dados) if v not in [1,2,3,4,5,6]]
        
    return [i for i, v in enumerate(dados) if v < 4]