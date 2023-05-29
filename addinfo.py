import subprocess
import random
import time
import math
import datetime
import json


#carro BOM
def generate_random_values_bom(): 
    new_values = {}
    new_values['DistanciaPercorrida_Rodovia'] = random.randint(0, 5)
    new_values['DistanciaPercorrida_Urbana'] = random.randint(1, 10)
    new_values['DistanciaPercorrida'] = new_values['DistanciaPercorrida_Rodovia'] + new_values['DistanciaPercorrida_Urbana']

    DistanciaPercorrida_Rodovia = (new_values['DistanciaPercorrida_Rodovia'])
    DistanciaPercorrida_Urbana = (new_values['DistanciaPercorrida_Urbana'])

    new_values['TempoFuncionamento_Rodovia'] = random.uniform(DistanciaPercorrida_Rodovia/100, DistanciaPercorrida_Rodovia/60)
    new_values['TempoFuncionamento_Urbana'] = random.uniform(DistanciaPercorrida_Urbana/60, DistanciaPercorrida_Urbana/30)
    new_values['TempoFuncionamento'] = new_values['TempoFuncionamento_Rodovia'] + new_values['TempoFuncionamento_Urbana']

    new_values['TempoHorarioPico'] = random.uniform(0.0, min(new_values['TempoFuncionamento'], 0.05))
    new_values['TempoNoite'] = random.uniform(0, 0)

    return new_values

#carro MEDIO BOM
def generate_random_values_medio_bom(): 
    new_values = {}
    new_values['DistanciaPercorrida_Rodovia'] = random.randint(0, 5)
    new_values['DistanciaPercorrida_Urbana'] = random.randint(1, 10)
    new_values['DistanciaPercorrida'] = new_values['DistanciaPercorrida_Rodovia'] + new_values['DistanciaPercorrida_Urbana']

    DistanciaPercorrida_Rodovia = (new_values['DistanciaPercorrida_Rodovia'])
    DistanciaPercorrida_Urbana = (new_values['DistanciaPercorrida_Urbana'])

    new_values['TempoFuncionamento_Rodovia'] = random.uniform(DistanciaPercorrida_Rodovia/130, DistanciaPercorrida_Rodovia/80)
    new_values['TempoFuncionamento_Urbana'] = random.uniform(DistanciaPercorrida_Urbana/70, DistanciaPercorrida_Urbana/45)
    new_values['TempoFuncionamento'] = new_values['TempoFuncionamento_Rodovia'] + new_values['TempoFuncionamento_Urbana']

    new_values['TempoHorarioPico'] = random.uniform(min(new_values['TempoFuncionamento'], 0.0), min(new_values['TempoFuncionamento'], 0.1))
    new_values['TempoNoite'] = random.uniform(0, 0)

    return new_values


#carro MEDIO
def generate_random_values_medio(): 
    new_values = {}
    new_values['DistanciaPercorrida_Rodovia'] = random.randint(1, 10)
    new_values['DistanciaPercorrida_Urbana'] = random.randint(1, 20)
    new_values['DistanciaPercorrida'] = new_values['DistanciaPercorrida_Rodovia'] + new_values['DistanciaPercorrida_Urbana']

    DistanciaPercorrida_Rodovia = (new_values['DistanciaPercorrida_Rodovia'])
    DistanciaPercorrida_Urbana = (new_values['DistanciaPercorrida_Urbana'])
                                 

    new_values['TempoFuncionamento_Rodovia'] = random.uniform(DistanciaPercorrida_Rodovia/160, DistanciaPercorrida_Rodovia/80)
    new_values['TempoFuncionamento_Urbana'] = random.uniform(DistanciaPercorrida_Urbana/80, DistanciaPercorrida_Urbana/50)
    new_values['TempoFuncionamento'] = new_values['TempoFuncionamento_Rodovia'] + new_values['TempoFuncionamento_Urbana']

    new_values['TempoHorarioPico'] = random.uniform(min(new_values['TempoFuncionamento'], 0.01), min(new_values['TempoFuncionamento'], 0.2))
    new_values['TempoNoite'] = random.uniform(min(new_values['TempoFuncionamento']/2, 0.0), min(new_values['TempoFuncionamento']/2, 0.5))

    return new_values

#carro MEDIO RUIM
def generate_random_values_medio_ruim(): 
    new_values = {}
    new_values['DistanciaPercorrida_Rodovia'] = random.randint(1, 15)
    new_values['DistanciaPercorrida_Urbana'] = random.randint(2, 40)
    new_values['DistanciaPercorrida'] = new_values['DistanciaPercorrida_Rodovia'] + new_values['DistanciaPercorrida_Urbana']

    DistanciaPercorrida_Rodovia = (new_values['DistanciaPercorrida_Rodovia'])
    DistanciaPercorrida_Urbana = (new_values['DistanciaPercorrida_Urbana'])
                                 
    new_values['TempoFuncionamento_Rodovia'] = random.uniform(DistanciaPercorrida_Rodovia/160, DistanciaPercorrida_Rodovia/80)
    new_values['TempoFuncionamento_Urbana'] = random.uniform(DistanciaPercorrida_Urbana/90, DistanciaPercorrida_Urbana/50)
    new_values['TempoFuncionamento'] = new_values['TempoFuncionamento_Rodovia'] + new_values['TempoFuncionamento_Urbana'] 

    new_values['TempoHorarioPico'] =random.uniform(min(new_values['TempoFuncionamento'], 0.5), min(new_values['TempoFuncionamento'], 1.0))
    new_values['TempoNoite'] = random.uniform(min(new_values['TempoFuncionamento']/2, 0.25), min(new_values['TempoFuncionamento']/2, 2))

    return new_values

#carro RUIM
def generate_random_values_ruim(): 
    new_values = {}
    new_values['DistanciaPercorrida_Rodovia'] = random.randint(5, 100) 
    new_values['DistanciaPercorrida_Urbana'] = random.randint(5, 100) 
    new_values['DistanciaPercorrida'] = new_values['DistanciaPercorrida_Rodovia'] + new_values['DistanciaPercorrida_Urbana']

    DistanciaPercorrida_Rodovia = (new_values['DistanciaPercorrida_Rodovia'])
    DistanciaPercorrida_Urbana = (new_values['DistanciaPercorrida_Urbana'])

    new_values['TempoFuncionamento_Rodovia'] = random.uniform(DistanciaPercorrida_Rodovia/200, DistanciaPercorrida_Rodovia/80) 
    new_values['TempoFuncionamento_Urbana'] = random.uniform(DistanciaPercorrida_Urbana/100, DistanciaPercorrida_Urbana/50)
    new_values['TempoFuncionamento'] = new_values['TempoFuncionamento_Rodovia'] + new_values['TempoFuncionamento_Urbana']

    new_values['TempoHorarioPico'] = random.uniform(min(new_values['TempoFuncionamento'], 0.5), min(new_values['TempoFuncionamento'], 1.0))
    new_values['TempoNoite'] = random.uniform(min(new_values['TempoFuncionamento']/2, 1.0), min(new_values['TempoFuncionamento']/2, 5.0))

    return new_values


def invoke_minifab_createcar(new_values, placa, placasDict):
    #previous_values = {'DistanciaPercorrida': 0, 'TempoFuncionamento': 0, 'DistanciaPercorrida_Rodovia': 0, 'TempoFuncionamento_Rodovia': 0, 'DistanciaPercorrida_Urbana': 0, 'TempoFuncionamento_Urbana': 0, 'TempoHorarioPico': 0, 'TempoNoite': 0}
    #new_values = generate_random_values3(previous_values)
    fcvatual = topsis(fcv(new_values, placa, placasDict))
    #print(fcvatual, end=", ")

    command = f"./minifab invoke -n fabcar -p '\"createCar\", \"{placa}\", \"{fcvatual}\", \"{new_values['DistanciaPercorrida']}\", \"{new_values['TempoFuncionamento']}\", \"{new_values['DistanciaPercorrida_Rodovia']}\", \"{new_values['TempoFuncionamento_Rodovia']}\", \"{new_values['DistanciaPercorrida_Urbana']}\", \"{new_values['TempoFuncionamento_Urbana']}\", \"{new_values['TempoHorarioPico']}\", \"{new_values['TempoNoite']}\"' "
    #subprocess.run(command, shell=True)
    #print(command)


    retorno = [fcvatual, new_values['DistanciaPercorrida'], new_values['TempoFuncionamento'], new_values['DistanciaPercorrida_Rodovia'], new_values['TempoFuncionamento_Rodovia'], new_values['DistanciaPercorrida_Urbana'], new_values['TempoFuncionamento_Urbana'], new_values['TempoHorarioPico'], new_values['TempoNoite']]
    
    return retorno

def media_de_x_em_x(lista_de_listas, x):
    num_colunas = len(lista_de_listas[0])
    media = []
    soma = [0] * num_colunas
    count = 0
    for i, l in enumerate(lista_de_listas):
        for j, valor in enumerate(l):
            soma[j] += valor
        count += 1
        if count == x:
            media.append([soma[k] / x for k in range(num_colunas)])
            soma = [0] * num_colunas
            count = 0
    if count > 0:
        media.append([soma[k] / count for k in range(num_colunas)])
    return media


def media_trinta_em_trinta(lista):
    medias = []
    for i in range(0, len(lista), 30):
        if i + 30 > len(lista):
            medias.append(sum(lista[i:]) / len(lista[i:]))
        else:
            medias.append(sum(lista[i:i+30]) / 30)
    return medias




def topsis(veiculo):
    pesos = [10, 3, 1, 2, 5, 10, 2, 4]
    total = 37

    #populando new_veiculo 
    new_veiculo = {}
    new_veiculo['vm'] = veiculo['vm'] * pesos[0]/37
    new_veiculo['hp'] = veiculo['hp'] * pesos[1]/37
    new_veiculo['td'] = veiculo['td'] * pesos[2]/37
    new_veiculo['km'] = veiculo['km'] * pesos[3]/37
    new_veiculo['tc'] = veiculo['tc'] * pesos[4]/37
    new_veiculo['m']  = veiculo['m']  * pesos[5]/37
    new_veiculo['av'] = veiculo['av'] * pesos[6]/37
    new_veiculo['i']  = veiculo['i']  * pesos[7]/37

    
    #print("*****************")
    #print(veiculo)
    #print(new_veiculo)

    #cria array de 8 posições
    ideal = [None] * 8 
    #print(ideal)
    for i in range(8):
        ideal[i] = pesos[i]/total
        #print(ideal[i])


    di = math.sqrt(math.pow(new_veiculo['vm'] - ideal[0], 2) +
                   math.pow(new_veiculo['hp'] - ideal[1], 2) +
                   math.pow(new_veiculo['td'] - ideal[2], 2) +
                   math.pow(new_veiculo['km'] - ideal[3], 2) +
                   math.pow(new_veiculo['tc'] - ideal[4], 2) +
                   math.pow(new_veiculo['m']  - ideal[5], 2) +
                   math.pow(new_veiculo['av'] - ideal[6], 2) +
                   math.pow(new_veiculo['i']  - ideal[7], 2)
                   )
    
    
    da = math.sqrt(math.pow(new_veiculo['vm'] - 0, 2) +
                   math.pow(new_veiculo['hp'] - 0, 2) +
                   math.pow(new_veiculo['td'] - 0, 2) +
                   math.pow(new_veiculo['km'] - 0, 2) +
                   math.pow(new_veiculo['tc'] - 0, 2) +
                   math.pow(new_veiculo['m']  - 0, 2) +
                   math.pow(new_veiculo['av'] - 0, 2) +
                   math.pow(new_veiculo['i']  - 0, 2)
                   )

    #print("ideal:")
    #print(ideal)
    #print(di)
    #print(da)
    #print(new_veiculo)
    similaridade = da / (da + di)
    return similaridade






def fcv(new_values, placa, placasDict):
    values = {}
    values['DistanciaPercorrida'] = int(new_values['DistanciaPercorrida'])
    values['TempoFuncionamento'] = float(new_values['TempoFuncionamento']) 
    values['DistanciaPercorrida_Rodovia'] = int(new_values['DistanciaPercorrida_Rodovia'])
    values['TempoFuncionamento_Rodovia'] = float(new_values['TempoFuncionamento_Rodovia'])
    values['DistanciaPercorrida_Urbana'] = int(new_values['DistanciaPercorrida_Urbana'])
    values['TempoFuncionamento_Urbana'] = float(new_values['TempoFuncionamento_Urbana'])
    values['TempoHorarioPico'] = float(new_values['TempoHorarioPico'])
    values['TempoNoite'] = float(new_values['TempoNoite'])


    #print(values)

    #######################################
    # VELOCIDADE MEDIA (VM)               #
    #######################################
    if(values['TempoFuncionamento_Rodovia']>0):
        vmr = values['DistanciaPercorrida_Rodovia']/values['TempoFuncionamento_Rodovia']
    else:
        vmr = 1
    if(values['TempoFuncionamento_Urbana']>0):
        vmu = values['DistanciaPercorrida_Urbana']/values['TempoFuncionamento_Urbana']
    else: 
        vmu = 1

    if(0 <= vmr <= 110):
        vr = 1  
    elif(110 < vmr < 150):
        vr = 0.25
    else:
        vr = 0
    

    if(0 <= vmu <= 40):
        vu = 1
    elif(40 < vmu <= 60):
        vu  = 0.75
    elif(60 < vmu <= 80):
        vu = 0.25
    else:
        vu = 0
    

    vm = (vr*values['TempoFuncionamento_Rodovia'] + vu*values['TempoFuncionamento_Urbana'])/(values['TempoFuncionamento_Rodovia']+values['TempoFuncionamento_Urbana'])
    
    #print(vr)
    #print(vu)
    #print(vm)

    #######################################
    # HORARIO DE PICO (HP)                #
    #######################################

    hd = values['TempoHorarioPico']
    hn = values['TempoNoite']
    tt = values['TempoFuncionamento']
    wd = 0.75
    wn = 0.25

    hp = ((1 - (hd/tt)) * wd) + ((1 - (hn/tt)) * wn)

    #print(hp)

    #######################################
    # TEMPO DIRIGIDO (TD)                 #
    #######################################

    tt = values['TempoFuncionamento']
    if(tt <= 1):
        td = 1.0
    elif(1 < tt <= 2):
        td = 0.75
    elif(2 < tt <= 5):
        td = 0.50
    else:
        td = 0.25

    #print(td)

    #######################################
    # DISTANCIA PERCORRIDA (KM)           #
    #######################################
    
    dp = values['DistanciaPercorrida']
    if(dp <= 10):
        km = 1.0
    elif(10 < dp <= 20):
        km = 0.75
    elif(20 < dp <= 30):
        km = 0.50
    else:
        km = 0.25
    
    #print(td)


    #######################################
    # TEMPO CARTEIRA (TC)                 #
    #######################################

    # tempocarteira = 15

    # if(tempocarteira > 10):
    #     tc = 1.00
    # elif(5 < tempocarteira <= 10):
    #     tc = 0.75
    # elif(2 < tempocarteira <= 5):
    #     tc = 0.50
    # elif(1 < tempocarteira <= 2):
    #     tc = 0.25
    # else:
    #     tc = 0
    
    tc = placasDict[placa][0]
    #print(tc)
    

    #######################################
    # MULTAS (M)                          #
    #######################################
    # REFAZER?

    # pmax = 5
    # mmax = 40
    # multas = 1
    # mmax = 40
    # mm = 1
    # lmmax = 12

    m = placasDict[placa][1]
    
  
    #######################################
    # ANO DE FABRICAÇÃO (AV)              #
    #######################################
    
    aa = 2023
    af = 2015
    iv = aa - af

    if(iv <= 10):
        av = 1.00
    elif(10 < iv <= 20):
        av = 0.75
    elif(20 < iv <= 40):
        av = 0.50
    else:
        av = 0.25

    av = placasDict[placa][2]
    #######################################
    # IDADE (I)                           #
    #######################################

    i = placasDict[placa][3]

    veiculo = {}
    veiculo['vm'] = vm
    veiculo['hp'] = hp
    veiculo['td'] = td
    veiculo['km'] = km
    veiculo['tc'] = tc
    veiculo['m'] = m
    veiculo['av'] = av
    veiculo['i'] = i
    veiculo['fcv'] = topsis(veiculo)

    return(veiculo)




def generateVeiculo():
    placas = ['ZZZ-3333']
    placasDict = {}

    #                          tc  m    av    i                      
    placasDict['ZZZ-1111'] = [1.0, 1.0, 1.0, 1.0]

    placasDict['ZZZ-2222'] = [0.75, 0.75, 0.75, 0.75]

    placasDict['ZZZ-3333'] = [0.5, 0.25, 0.25, 0.5]


    j = 0
    dados = []
    start_time_ = datetime.datetime.now()
    start_time = time.time()
    total = 1095
    for i in range (total): 
        
        #newValues = generate_random_values_bom()
        #newValues = generate_random_values_medio()
        newValues = generate_random_values_ruim()

        #print(newValues)
        #adiciona na blockchain
        dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))
        #print(dados)
        

        j = j + 1
        # if(j >= qtdPlacas):
        #     j = 0

    nomes_campos = ['fcv', 'DistanciaPercorrida', 'TempoFuncionamento', 'DistanciaPercorrida_Rodovia', 
                    'TempoFuncionamento_Rodovia', 'DistanciaPercorrida_Urbana', 'TempoFuncionamento_Urbana', 
                    'TempoHorarioPico', 'TempoNoite']
    #print(dados)
    #dados_json = [dict(zip(nomes_campos, registro)) for registro in dados]

    primeiros_valores = [linha[0] for linha in dados]
    print("fcv")
    print(primeiros_valores)

    #print(json.dumps(dados_json))
    print("media mensal")
    dados2 = media_de_x_em_x(dados,30)
    #dados2 = media_trinta_em_trinta(dados)
    print(dados2)
    print("fcv mensal")
    primeiros_valores2 = [lista[0] for lista in dados2]
    print(primeiros_valores2)
    # for media in range(len(dados2)):
    #     result = [dict(zip(nomes_campos, row)) for row in dados2]
    #     print(topsis(fcv(result[media], placas[0]), end=", "))
    # print()


    print("media total")
    dados2 = media_de_x_em_x(dados,total)
    print(dados2)
    result = [dict(zip(nomes_campos, row)) for row in dados2]

    print("fcv total")
    print(fcv(result[0], placas[0], placasDict))



    print()
    print()
    print()
    end_time = time.time()
    end_time_ = datetime.datetime.now()
    tempo_de_execucao = end_time - start_time
    tempo_de_execucao_ = end_time_ - start_time_
    print(f"início: {start_time:.2f}")
    print(f"fim: {end_time:.2f}")
    print(f"A função levou {tempo_de_execucao:.2f} segundos para ser executada.")
    print("A função levou {} segundos para ser executada.".format(tempo_de_execucao_.total_seconds()))
    print("Início: {}".format(start_time_.strftime('%H:%M:%S %d/%m/%Y')))
    print("Fim: {}".format(end_time_.strftime('%H:%M:%S %d/%m/%Y')))




###################################
###################################
###################################
#começa bom e termina ruim
###################################
###################################
###################################


def generateVeiculoBomRuim():
    placas = ['ZZZ-9999']#, 'BBB-2222', 'BBB-3333', 'BBB-4444', 'BBB-5555', 'BBB-6666', 'BBB-7777', 'BBB-8888', 'BBB-9999', 'BBB-1010']

    placasDict = {}

    #                          tc  m    av    i                      
    placasDict['ZZZ-9999'] = [0.75, 0.75, 0.75, 0.75]


    #qtdPlacas = len(placas)
    #print("qtd placas: " + str(qtdPlacas))
    j = 0

    dados = []
    start_time_ = datetime.datetime.now()
    start_time = time.time()
    total = 1095
    for i in range (total):
        #bom
        if( 0 <= j < total/7 ):
            placasDict['ZZZ-9999'] = [1.0, 1.0, 1.0, 1.0]
            newValues = generate_random_values_bom()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))

        #bom-mediobom
        elif( total/7 <= j < 2*total/7):
            placasDict['ZZZ-9999'] = [1.0, 1.0, 1.0, 1.0]
            rand = random.randint(0,1)
            if(rand == 0):
                newValues = generate_random_values_bom()
            elif(rand == 1):
                newValues = generate_random_values_medio_bom()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))

        #bom-mediobom-medio
        elif(2*total/7 <= j < 3*total/7):
            placasDict['ZZZ-9999'] = [0.75, 0.75, 0.75, 0.75]
            rand = random.randint(0,2)
            if(rand == 0):
                newValues = generate_random_values_bom()
            elif(rand == 1):
                newValues = generate_random_values_medio_bom()
            elif(rand == 2):
                newValues = generate_random_values_medio()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))
        #medio
        elif(3*total/7 <= j < 4*total/7):
            placasDict['ZZZ-9999'] = [0.75, 0.75, 0.75, 0.75]
            newValues = generate_random_values_medio()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))

        #medio-medioruim-ruim    
        elif(4*total/7 <= j < 5*total/7):
            placasDict['ZZZ-9999'] = [0.75, 0.75, 0.75, 0.75]
            rand = random.randint(0,2)
            if(rand == 0):
                newValues = generate_random_values_medio()
            elif(rand == 1):
                newValues = generate_random_values_medio_ruim()
            elif(rand == 2):
                newValues = generate_random_values_ruim()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))

        #medioruim-ruim
        elif(5*total/7 <= j < 6*total/7):
            placasDict['ZZZ-9999'] = [0.5, 0.5, 0.5, 0.5]

            rand = random.randint(0,1)
            if(rand == 0):
                newValues = generate_random_values_medio_ruim()
            elif(rand == 1):
                newValues = generate_random_values_medio_ruim()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))
            
        #ruim
        else:
            placasDict['ZZZ-9999'] = [0.5, 0.5, 0.5, 0.5]
            newValues = generate_random_values_ruim()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))

        placasDict['ZZZ-9999'] =  [0.714, 0.714, 0.714, 0.714]

        

        #adiciona na blockchain
        #invoke_minifab_createcar(newValues, 0, placas[0], 0)
        #dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))

        oldValues = newValues

        j = j + 1




    nomes_campos = ['fcv', 'DistanciaPercorrida', 'TempoFuncionamento', 'DistanciaPercorrida_Rodovia', 
                    'TempoFuncionamento_Rodovia', 'DistanciaPercorrida_Urbana', 'TempoFuncionamento_Urbana', 
                    'TempoHorarioPico', 'TempoNoite']
    #print(dados)
    #dados_json = [dict(zip(nomes_campos, registro)) for registro in dados]

    primeiros_valores = [linha[0] for linha in dados]
    print("fcv")
    print(primeiros_valores)

    #print(json.dumps(dados_json))
    print("media mensal")
    dados2 = media_de_x_em_x(dados,30)
    #dados2 = media_trinta_em_trinta(dados)
    print(dados2)
    print("fcv mensal")
    primeiros_valores2 = [lista[0] for lista in dados2]
    print(primeiros_valores2)
    # for media in range(len(dados2)):
    #     result = [dict(zip(nomes_campos, row)) for row in dados2]
    #     print(topsis(fcv(result[media], placas[0]), end=", "))
    # print()


    print("media total")
    dados2 = media_de_x_em_x(dados,total)
    print(dados2)
    result = [dict(zip(nomes_campos, row)) for row in dados2]

    print("fcv total")
    print(fcv(result[0], placas[0], placasDict ))

    print(dados[0])


    print()
    print()
    print()


    end_time = time.time()
    end_time_ = datetime.datetime.now()
    tempo_de_execucao = end_time - start_time
    tempo_de_execucao_ = end_time_ - start_time_
    print(f"início: {start_time:.2f}")
    print(f"fim: {end_time:.2f}")
    print(f"A função levou {tempo_de_execucao:.2f} segundos para ser executada.")
    print("A função levou {} segundos para ser executada.".format(tempo_de_execucao_.total_seconds()))
    print("Início: {}".format(start_time_.strftime('%H:%M:%S %d/%m/%Y')))
    print("Fim: {}".format(end_time_.strftime('%H:%M:%S %d/%m/%Y')))


###################################
###################################
###################################
#começa ruim e termina bom
###################################
###################################
###################################
def generateVeiculoRuimBom():
    placas = ['ZZZ-4444']
    placasDict = {}
    placasDict['ZZZ-4444'] = [0.4, 0.375, 0.25, 0.75]

    j = 0
    dados =[]
    start_time_ = datetime.datetime.now()
    start_time = time.time()
    total = 1095
    for i in range (total):
        #bom
        if( 0 <= j < total/7 ):
            placasDict['ZZZ-4444'] = [0.25, 0.25, 0.25, 0.25]
            newValues = generate_random_values_ruim()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))
            

        #bom-mediobom
        elif( total/7 <= j < 2*total/7):
            placasDict['ZZZ-4444'] = [0.5, 0.5, 0.5, 0.5]
            rand = random.randint(0,1)
            if(rand == 0):
                newValues = generate_random_values_medio_ruim()
            elif(rand == 1):
                newValues = generate_random_values_medio_ruim()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))
            

        #bom-mediobom-medio
        elif(2*total/7 <= j < 3*total/7):
            placasDict['ZZZ-4444'] = [0.75, 0.75, 0.75, 0.75]
            rand = random.randint(0,2)
            if(rand == 0):
                newValues = generate_random_values_medio()
            elif(rand == 1):
                newValues = generate_random_values_medio_ruim()
            elif(rand == 2):
                newValues = generate_random_values_ruim()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))
            
        #medio
        elif(3*total/7 <= j < 4*total/7):
            placasDict['ZZZ-4444'] = [0.75, 0.75, 0.75, 0.75]
            newValues = generate_random_values_medio()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))

        #medio-medioruim-ruim    
        elif(4*total/7 <= j < 5*total/7):
            placasDict['ZZZ-4444'] = [0.75, 0.75, 0.75, 0.75]
            rand = random.randint(0,2)
            if(rand == 0):
                newValues = generate_random_values_bom()
            elif(rand == 1):
                newValues = generate_random_values_medio_bom()
            elif(rand == 2):
                newValues = generate_random_values_medio()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))

        #medioruim-ruim
        elif(5*total/7 <= j < 6*total/7):
            placasDict['ZZZ-4444'] = [1.0, 1.0, 1.0, 1.0]
            rand = random.randint(0,1)
            if(rand == 0):
                newValues = generate_random_values_bom()
            elif(rand == 1):
                newValues = generate_random_values_medio_bom()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))
            
        #ruim
        else:
            placasDict['ZZZ-4444'] = [1.0, 1.0, 1.0, 1.0]
            newValues = generate_random_values_bom()
            dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))

        placasDict['ZZZ-4444'] = [0.714, 0.714, 0.714, 0.714]
        

        #adiciona na blockchain
        #invoke_minifab_createcar(newValues, 0, placas[0])

        #dados.append(invoke_minifab_createcar(newValues, placas[0], placasDict))


        j = j + 1








    nomes_campos = ['fcv', 'DistanciaPercorrida', 'TempoFuncionamento', 'DistanciaPercorrida_Rodovia', 
                    'TempoFuncionamento_Rodovia', 'DistanciaPercorrida_Urbana', 'TempoFuncionamento_Urbana', 
                    'TempoHorarioPico', 'TempoNoite']
    #print(dados)
    #dados_json = [dict(zip(nomes_campos, registro)) for registro in dados]

    primeiros_valores = [linha[0] for linha in dados]
    print("fcv")
    print(primeiros_valores)

    #print(json.dumps(dados_json))
    print("media mensal")
    dados2 = media_de_x_em_x(dados,30)
    #dados2 = media_trinta_em_trinta(dados)
    print(dados2)
    print("fcv mensal")
    primeiros_valores2 = [lista[0] for lista in dados2]
    print(primeiros_valores2)
    # for media in range(len(dados2)):
    #     result = [dict(zip(nomes_campos, row)) for row in dados2]
    #     print(topsis(fcv(result[media], placas[0]), end=", "))
    # print()


    print("media total")
    dados2 = media_de_x_em_x(dados,total)
    print(dados2)
    result = [dict(zip(nomes_campos, row)) for row in dados2]

    print("fcv total")
    print(fcv(result[0], placas[0], placasDict))

    #print(dados[0])

    print()
    print()
    print()




    end_time = time.time()
    end_time_ = datetime.datetime.now()
    tempo_de_execucao = end_time - start_time
    tempo_de_execucao_ = end_time_ - start_time_
    print(f"início: {start_time:.2f}")
    print(f"fim: {end_time:.2f}")
    print(f"A função levou {tempo_de_execucao:.2f} segundos para ser executada.")
    print("A função levou {} segundos para ser executada.".format(tempo_de_execucao_.total_seconds()))
    print("Início: {}".format(start_time_.strftime('%H:%M:%S %d/%m/%Y')))
    print("Fim: {}".format(end_time_.strftime('%H:%M:%S %d/%m/%Y')))



def main():
    generateVeiculo()
    #generateVeiculoBomRuim()
    #generateVeiculoRuimBom()

if __name__ == "__main__":
    main()
