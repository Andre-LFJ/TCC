import re
import json
import subprocess
import matplotlib.pyplot as plt
import math



# def invoke_minifab_queryallcars():
#     command = f"./minifab invoke -n fabcar -p '\"queryAllCars\"'"
  
#     subprocess.run(command, shell=True)
#     #print(command)


def transforma_barras(string):
    return string.replace("\\\\", "\\")


def invoke_minifab_queryallcars():
  command = f"./minifab invoke -n fabcar -p '\"queryAllCars\"'"

  # executa o comando e redireciona a saída padrão para PIPE
  process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)

  # obtém a saída do comando como uma string
  output = process.stdout.decode('utf-8')

  #print(output)
  return output

def invoke_minifab_history(placa):
  command = f"./minifab invoke -n fabcar -p '\"getHistoryForAsset\",\"{placa}\"'"

  # executa o comando e redireciona a saída padrão para PIPE
  process = subprocess.run(command, shell=True, stdout=subprocess.PIPE)

  # obtém a saída do comando como uma string
  output = process.stdout.decode('utf-8')

  #print(output)
  return output


# input string

# input_string = '''root@DESKTOP-7REN7KG:/mnt/g/wsl/bolsa/mywork# ./minifab invoke -n fabcar -p '"getHistoryForAsset","AAA-3333"' -o org1.example.com
# Using spec file: /mnt/g/wsl/bolsa/mywork/spec.yaml
# Minifab Execution Context:
#     FABRIC_RELEASE=2.3.0
#     CHANNEL_NAME=mychannel
#     PEER_DATABASE_TYPE=golevel
#     CHAINCODE_LANGUAGE=go
#     CHAINCODE_NAME=fabcar
#     CHAINCODE_VERSION=0.2.6
#     CHAINCODE_INIT_REQUIRED=true
#     CHAINCODE_PARAMETERS="getHistoryForAsset","AAA-3333"
#     CHAINCODE_PRIVATE=false
#     CHAINCODE_POLICY=
#     TRANSIENT_DATA=
#     BLOCK_NUMBER=39
#     EXPOSE_ENDPOINTS=false
#     CURRENT_ORG=org1.example.com
#     HOST_ADDRESSES=172.31.204.224
#     TARGET_ENV=DOCKER
#     WORKING_DIRECTORY: /mnt/g/wsl/bolsa/mywork
# .....
# # Preparing for the following operations: *********************
#   verify options, cc invoke
# .......
# # Running operation: ******************************************
#   verify options
# ..
# # Running operation: ******************************************
#   cc invoke
# ...............
# # Chaincode invocation results ********************************
#   ['\x1b[34m2023-03-24 23:28:11.594 UTC [chaincodeCmd] chaincodeInvokeOrQuery -> INFO 001\x1b[0m Chaincode invoke successful. result: status:200 payload:"[{\\"TxId\\":\\"0a33fdd9b7ae7f0197aea395a4a34bc1ada23980ad9c2c7e549b50ea1eb5bfde\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"976\\",\\"TempoFuncionamento\\":\\"105.22367315575478\\",\\"DistanciaPercorrida_Rodovia\\":\\"714\\",\\"TempoFuncionamento_Rodovia\\":\\"31.04143109773401\\",\\"DistanciaPercorrida_Urbana\\":\\"262\\",\\"TempoFuncionamento_Urbana\\":\\"74.18224205802078\\",\\"TempoHorarioPico\\":\\"10.9608730880377\\",\\"TempoNoite\\":\\"23.0101314621161\\"}, \\"Timestamp\\":\\"2023-03-21 09:00:00.360308974 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"9245da9eb29ee2a7f7e109b961598c5d01eefb8d62142d79ecb34b15be24b18c\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"748\\",\\"TempoFuncionamento\\":\\"84.58239732655119\\",\\"DistanciaPercorrida_Rodovia\\":\\"4\\",\\"TempoFuncionamento_Rodovia\\":\\"30.061753392324164\\",\\"DistanciaPercorrida_Urbana\\":\\"744\\",\\"TempoFuncionamento_Urbana\\":\\"54.520643934227024\\",\\"TempoHorarioPico\\":\\"8.923033199062846\\",\\"TempoNoite\\":\\"17.965615815296257\\"}, \\"Timestamp\\":\\"2023-03-21 08:59:31.165102201 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"d43cb862cb9739564d881be90a6b685310b0de18d2fa03e8853e3c8fcfc56412\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"655\\",\\"TempoFuncionamento\\":\\"64.37562484555977\\",\\"DistanciaPercorrida_Rodovia\\":\\"444\\",\\"TempoFuncionamento_Rodovia\\":\\"12.586491080324715\\",\\"DistanciaPercorrida_Urbana\\":\\"211\\",\\"TempoFuncionamento_Urbana\\":\\"51.78913376523506\\",\\"TempoHorarioPico\\":\\"6.982190006330194\\",\\"TempoNoite\\":\\"14.786210900654229\\"}, \\"Timestamp\\":\\"2023-03-21 08:59:02.338449851 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"4606ade737f4d83d3123e12ceb262783455c0cba73f50f79029cd1a194a84659\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"363\\",\\"TempoFuncionamento\\":\\"42.07838584930636\\",\\"DistanciaPercorrida_Rodovia\\":\\"202\\",\\"TempoFuncionamento_Rodovia\\":\\"38.24680772898244\\",\\"DistanciaPercorrida_Urbana\\":\\"161\\",\\"TempoFuncionamento_Urbana\\":\\"3.8315781203239183\\",\\"TempoHorarioPico\\":\\"2.766399140669364\\",\\"TempoNoite\\":\\"10.466200876799173\\"}, \\"Timestamp\\":\\"2023-03-21 08:58:32.975687529 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"f752eed55fb45c9b8eda1bfde633bc209a4cf70155c2c1f7d02e99baa3931f8b\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"357\\",\\"TempoFuncionamento\\":\\"26.62382087773879\\",\\"DistanciaPercorrida_Rodovia\\":\\"239\\",\\"TempoFuncionamento_Rodovia\\":\\"2.8031574579949616\\",\\"DistanciaPercorrida_Urbana\\":\\"118\\",\\"TempoFuncionamento_Urbana\\":\\"23.82066341974383\\",\\"TempoHorarioPico\\":\\"2.2358278914587997\\",\\"TempoNoite\\":\\"8.458485460524109\\"}, \\"Timestamp\\":\\"2023-03-21 08:58:14.187255378 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"6e8618b5f89709919d74a66253cd96e077a1b584ec0a6156f1915a4e0acdaf63\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"255\\",\\"TempoFuncionamento\\":\\"14.901598197607107\\",\\"DistanciaPercorrida_Rodovia\\":\\"4\\",\\"TempoFuncionamento_Rodovia\\":\\"6.752700808811091\\",\\"DistanciaPercorrida_Urbana\\":\\"251\\",\\"TempoFuncionamento_Urbana\\":\\"8.148897388796016\\",\\"TempoHorarioPico\\":\\"3.75193776351671\\",\\"TempoNoite\\":\\"7.459250405552112\\"}, \\"Timestamp\\":\\"2023-03-21 08:57:55.083626382 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"ce4d32effbe802e4805c0d84999ee1cf6da928e74f298147ca36c392852ccfbe\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"59\\",\\"TempoFuncionamento\\":\\"9.598163823704708\\",\\"DistanciaPercorrida_Rodovia\\":\\"14\\",\\"TempoFuncionamento_Rodovia\\":\\"6.2754952538362065\\",\\"DistanciaPercorrida_Urbana\\":\\"45\\",\\"TempoFuncionamento_Urbana\\":\\"3.322668569868501\\",\\"TempoHorarioPico\\":\\"1.9583535346974976\\",\\"TempoNoite\\":\\"0.20400187094650601\\"}, \\"Timestamp\\":\\"2023-03-21 08:57:36.493320008 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"79e65899f8813f9d6dd62b9698c421b99aa99ab437fe75fb716e04319308eae9\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"809\\",\\"TempoFuncionamento\\":\\"106.7747222784767\\",\\"DistanciaPercorrida_Rodovia\\":\\"639\\",\\"TempoFuncionamento_Rodovia\\":\\"86.80071795504372\\",\\"DistanciaPercorrida_Urbana\\":\\"170\\",\\"TempoFuncionamento_Urbana\\":\\"19.97400432343298\\",\\"TempoHorarioPico\\":\\"11.69056168032645\\",\\"TempoNoite\\":\\"23.1747800652895\\"}, \\"Timestamp\\":\\"2023-03-21 08:55:34.775847053 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"f1c08749a87e16f052098995c3c7862d0a469d6a8d883183189d07e13c332951\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"626\\",\\"TempoFuncionamento\\":\\"72.76109792210332\\",\\"DistanciaPercorrida_Rodovia\\":\\"247\\",\\"TempoFuncionamento_Rodovia\\":\\"63.263599729867764\\",\\"DistanciaPercorrida_Urbana\\":\\"379\\",\\"TempoFuncionamento_Urbana\\":\\"9.497498192235554\\",\\"TempoHorarioPico\\":\\"8.930475543369218\\",\\"TempoNoite\\":\\"13.276612039239243\\"}, \\"Timestamp\\":\\"2023-03-21 08:55:06.088456423 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"20311931894c7b2604d73d1aeb99b40e811aee8f8210af0d863f9e8ecc74121f\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"530\\",\\"TempoFuncionamento\\":\\"62.655610901391455\\",\\"DistanciaPercorrida_Rodovia\\":\\"333\\",\\"TempoFuncionamento_Rodovia\\":\\"9.892696304035752\\",\\"DistanciaPercorrida_Urbana\\":\\"197\\",\\"TempoFuncionamento_Urbana\\":\\"52.7629145973557\\",\\"TempoHorarioPico\\":\\"7.144564617000222\\",\\"TempoNoite\\":\\"16.799393814263098\\"}, \\"Timestamp\\":\\"2023-03-21 08:54:46.256553552 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"3a67e83b12854c10b7457956fa1ac8e79b29b834d840b69489693a3ec24aad43\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"455\\",\\"TempoFuncionamento\\":\\"61.62722992137088\\",\\"DistanciaPercorrida_Rodovia\\":\\"210\\",\\"TempoFuncionamento_Rodovia\\":\\"35.72575742575393\\",\\"DistanciaPercorrida_Urbana\\":\\"245\\",\\"TempoFuncionamento_Urbana\\":\\"25.90147249561695\\",\\"TempoHorarioPico\\":\\"6.073261422125626\\",\\"TempoNoite\\":\\"11.560720754679826\\"}, \\"Timestamp\\":\\"2023-03-21 08:54:27.142341736 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"79e4426daae76b0bad7b2b159f3048c5787f877996541a4f451bf2ef235c9f56\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"349\\",\\"TempoFuncionamento\\":\\"51.02547976276915\\",\\"DistanciaPercorrida_Rodovia\\":\\"115\\",\\"TempoFuncionamento_Rodovia\\":\\"14.083725341002589\\",\\"DistanciaPercorrida_Urbana\\":\\"234\\",\\"TempoFuncionamento_Urbana\\":\\"36.94175442176656\\",\\"TempoHorarioPico\\":\\"4.2430512547346995\\",\\"TempoNoite\\":\\"9.925235990781795\\"}, \\"Timestamp\\":\\"2023-03-21 08:54:07.964634737 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"1aed476c68c1fc7296cda2e4ba7a8af75203c37b9ff7e7f228d66075755af2cf\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"293\\",\\"TempoFuncionamento\\":\\"49.7995278290469\\",\\"DistanciaPercorrida_Rodovia\\":\\"110\\",\\"TempoFuncionamento_Rodovia\\":\\"11.650024815456542\\",\\"DistanciaPercorrida_Urbana\\":\\"183\\",\\"TempoFuncionamento_Urbana\\":\\"38.14950301359036\\",\\"TempoHorarioPico\\":\\"4.10024557959741\\",\\"TempoNoite\\":\\"5.713484921941805\\"}, \\"Timestamp\\":\\"2023-03-21 08:53:49.131312107 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"01d97bfac7bf06c26adb7d7698273173216f269e3a0323e38b5b0737b20ae3b6\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"196\\",\\"TempoFuncionamento\\":\\"26.543312068070406\\",\\"DistanciaPercorrida_Rodovia\\":\\"21\\",\\"TempoFuncionamento_Rodovia\\":\\"16.82453700687467\\",\\"DistanciaPercorrida_Urbana\\":\\"175\\",\\"TempoFuncionamento_Urbana\\":\\"9.718775061195736\\",\\"TempoHorarioPico\\":\\"1.9465687534040028\\",\\"TempoNoite\\":\\"6.66700460332831\\"}, \\"Timestamp\\":\\"2023-03-21 08:53:30.262398327 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"9d960fc35fd2d280ae1e837f91d5868eb88facc7a677ff4092dd8fec3c4f4af4\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"174\\",\\"TempoFuncionamento\\":\\"13.312263044746215\\",\\"DistanciaPercorrida_Rodovia\\":\\"23\\",\\"TempoFuncionamento_Rodovia\\":\\"6.670260736899855\\",\\"DistanciaPercorrida_Urbana\\":\\"151\\",\\"TempoFuncionamento_Urbana\\":\\"6.642002307846361\\",\\"TempoHorarioPico\\":\\"2.1246013504749186\\",\\"TempoNoite\\":\\"3.356101978967357\\"}, \\"Timestamp\\":\\"2023-03-21 08:53:11.059889218 +0000 UTC\\", \\"IsDelete\\":\\"false\\"},{\\"TxId\\":\\"3e680623275fc5d3cc53c8febaacf5b243e63a2919c98b2488734a564ab1efd3\\", \\"Value\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"26\\",\\"TempoFuncionamento\\":\\"9.116154668423835\\",\\"DistanciaPercorrida_Rodovia\\":\\"23\\",\\"TempoFuncionamento_Rodovia\\":\\"8.51267527756868\\",\\"DistanciaPercorrida_Urbana\\":\\"3\\",\\"TempoFuncionamento_Urbana\\":\\"0.6034793908551546\\",\\"TempoHorarioPico\\":\\"1.0695591714504702\\",\\"TempoNoite\\":\\"3.238829623414327\\"}, \\"Timestamp\\":\\"2023-03-21 08:52:52.255333448 +0000 UTC\\", \\"IsDelete\\":\\"false\\"}]" ']

# # STATS *******************************************************
# minifab: ok=34  failed=0

# real    0m8.553s
# user    0m7.293s
# sys     0m0.863s'''




def extract_payload(string):
    start = string.find("payload:")
    end = string.rfind("']")
    if start != -1 and end != -1:
        return transforma_barras(string[start+len("payload:"):end])
    return ""


def inverter_array(arr):
    return list(reversed(arr))


# string_json = json.loads(extract_payload(input_string))
# objeto_python = json.loads(string_json)



# print("-----------------")

# distanciatotal = 0

# for obj in objeto_python:
#   print(obj['Value']['placa'] + " : " + obj['Value']['DistanciaPercorrida'] + " : " + obj['Timestamp'])
#   distanciatotal = int(obj['Value']['DistanciaPercorrida']) + distanciatotal

# print("dist total: " + str(distanciatotal))


# print("===========")




# outputString = '''
# real    0m6.597s
# user    0m5.627s
# sys     0m0.567s
# Using spec file: /mnt/g/wsl/bolsa/mywork/spec.yaml
# Minifab Execution Context:
#     FABRIC_RELEASE=2.3.0
#     CHANNEL_NAME=mychannel
#     PEER_DATABASE_TYPE=golevel
#     CHAINCODE_LANGUAGE=go
#     CHAINCODE_NAME=fabcar
#     CHAINCODE_VERSION=0.3.1
#     CHAINCODE_INIT_REQUIRED=true
#     CHAINCODE_PARAMETERS="queryAllCars"
#     CHAINCODE_PRIVATE=false
#     CHAINCODE_POLICY=
#     TRANSIENT_DATA=
#     BLOCK_NUMBER=39
#     EXPOSE_ENDPOINTS=false
#     CURRENT_ORG=org1.example.com
#     HOST_ADDRESSES=192.168.7.241
#     TARGET_ENV=DOCKER
#     WORKING_DIRECTORY: /mnt/g/wsl/bolsa/mywork
# .....
# # Preparing for the following operations: *********************
#   verify options, cc invoke
# .......
# # Running operation: ******************************************
#   verify options
# ..
# # Running operation: ******************************************
#   cc invoke
# ...............
# # Chaincode invocation results ********************************
#   ['\x1b[34m2023-03-31 07:20:34.937 UTC [chaincodeCmd] chaincodeInvokeOrQuery -> INFO 001\x1b[0m Chaincode invoke successful. result: status:200 payload:"[{\\"Key\\":\\"AAA-2222\\", \\"Record\\":{\\"placa\\":\\"AAA-2222\\",\\"DistanciaPercorrida\\":\\"1000\\",\\"TempoFuncionamento\\":\\"30\\",\\"DistanciaPercorrida_Rodovia\\":\\"700\\",\\"TempoFuncionamento_Rodovia\\":\\"10\\",\\"DistanciaPercorrida_Urbana\\":\\"300\\",\\"TempoFuncionamento_Urbana\\":\\"20\\",\\"TempoHorarioPico\\":\\"10\\",\\"TempoNoite\\":\\"0\\"}},{\\"Key\\":\\"AAA-3330\\", \\"Record\\":{\\"placa\\":\\"AAA-3330\\",\\"DistanciaPercorrida\\":\\"8\\",\\"TempoFuncionamento\\":\\"6.202041422269354\\",\\"DistanciaPercorrida_Rodovia\\":\\"3\\",\\"TempoFuncionamento_Rodovia\\":\\"1.5901993688904232\\",\\"DistanciaPercorrida_Urbana\\":\\"5\\",\\"TempoFuncionamento_Urbana\\":\\"4.611842053378931\\",\\"TempoHorarioPico\\":\\"1.4028467380545575\\",\\"TempoNoite\\":\\"0.7751308051234257\\"}},{\\"Key\\":\\"AAA-3333\\", \\"Record\\":{\\"placa\\":\\"AAA-3333\\",\\"DistanciaPercorrida\\":\\"976\\",\\"TempoFuncionamento\\":\\"105.22367315575478\\",\\"DistanciaPercorrida_Rodovia\\":\\"714\\",\\"TempoFuncionamento_Rodovia\\":\\"31.04143109773401\\",\\"DistanciaPercorrida_Urbana\\":\\"262\\",\\"TempoFuncionamento_Urbana\\":\\"74.18224205802078\\",\\"TempoHorarioPico\\":\\"10.9608730880377\\",\\"TempoNoite\\":\\"23.0101314621161\\"}},{\\"Key\\":\\"AAA-3334\\", \\"Record\\":{\\"placa\\":\\"AAA-3334\\",\\"DistanciaPercorrida\\":\\"1079\\",\\"TempoFuncionamento\\":\\"105.98229377808391\\",\\"DistanciaPercorrida_Rodovia\\":\\"545\\",\\"TempoFuncionamento_Rodovia\\":\\"61.14452772835518\\",\\"DistanciaPercorrida_Urbana\\":\\"534\\",\\"TempoFuncionamento_Urbana\\":\\"44.837766049728735\\",\\"TempoHorarioPico\\":\\"10.619227976214582\\",\\"TempoNoite\\":\\"22.443359373949885\\"}},{\\"Key\\":\\"BBB-1111\\", \\"Record\\":{\\"placa\\":\\"BBB-1111\\",\\"fcv\\":\\"0.9273688181365444\\",\\"DistanciaPercorrida\\":\\"9\\",\\"TempoFuncionamento\\":\\"0.2759767783788747\\",\\"DistanciaPercorrida_Rodovia\\":\\"1\\",\\"TempoFuncionamento_Rodovia\\":\\"0.011551829994443607\\",\\"DistanciaPercorrida_Urbana\\":\\"8\\",\\"TempoFuncionamento_Urbana\\":\\"0.2644249483844311\\",\\"TempoHorarioPico\\":\\"0.09834917722852357\\",\\"TempoNoite\\":\\"0.16341938995635533\\"}},{\\"Key\\":\\"CAR0\\", \\"Record\\":{\\"placa\\":\\"AAA-1111\\",\\"DistanciaPercorrida\\":\\"100\\",\\"TempoFuncionamento\\":\\"3\\",\\"DistanciaPercorrida_Rodovia\\":\\"70\\",\\"TempoFuncionamento_Rodovia\\":\\"1\\",\\"DistanciaPercorrida_Urbana\\":\\"30\\",\\"TempoFuncionamento_Urbana\\":\\"2\\",\\"TempoHorarioPico\\":\\"1\\",\\"TempoNoite\\":\\"0\\"}}]" ']

# # STATS *******************************************************
# minifab: ok=34  failed=0'''


# print("Digite:")
# print("1 - consultar um veículo")
# print("2 - consultar todos os veículos")


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



def fcv2(new_values, placa, placasDict):
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

    return(topsis(veiculo))















# entrada = input()
# if(entrada == '1'):
#    print("em manutenção")

# if(entrada == '2'):
#------------------------------
#outputString = invoke_minifab_queryallcars()
#string_json = json.loads(extract_payload(outputString))
#objeto_python = json.loads(string_json)
#------------------------------
# print(objeto_python)
placas = []
fcv = []
values = []


dist = []
temp = []
drod = []
trod = []
durb = []
turb = []
tpic = []
tnoi = []


fcvDict = {}



mediaFCV = []

# for obj in objeto_python:
#   print(obj['Record']['placa'])
#   placas.append(obj['Record']['placa'])

#placas.append('ZZZ-1111')
placas.append('ZZZ-2222')
#placas.append('ZZZ-3333')
#placas.append('ZZZ-8888')
#placas.append('ZZZ-9999')

print(placas)





def media(vetor):
  pedaço = [float(valor) for valor in vetor[i:i+tamanho_pedaço]]
  soma = sum(pedaço)
  media = soma / len(pedaço)
  mediaFCV.append(media)
  #print(f"{media}", end=", ")
  return (media)


for placa in placas:
  j = 0
  #print(placa)
  history_output = invoke_minifab_history(placa)
  #print(history_output)
  #print("=====")
  #print(extract_payload(history_output))
  history_json = json.loads(extract_payload(history_output))
  history_objeto = json.loads(history_json)
  for obj in history_objeto:
    #placasDict[placa] = obj['Value']['fcv']
    values.append(obj['Value'])
    fcv.append(obj['Value']['fcv'])
    dist.append(obj['Value']['DistanciaPercorrida'])
    temp.append(obj['Value']['TempoFuncionamento'])
    drod.append(obj['Value']['DistanciaPercorrida_Rodovia'])
    trod.append(obj['Value']['TempoFuncionamento_Rodovia'])
    durb.append(obj['Value']['DistanciaPercorrida_Urbana'])
    turb.append(obj['Value']['TempoFuncionamento_Urbana'])
    tpic.append(obj['Value']['TempoHorarioPico'])
    tnoi.append(obj['Value']['TempoNoite'])
    
 
    #print(obj)
    #print(obj['Value']['placa'] + " : " + obj['Value']['fcv'])
    #fcv = fcv + float(obj['Value']['fcv'])
    j = j+1
  #print(fcv)
  print(placa)
  #print(temp)
  print(j)
  #placasDict[placa] = fcv
  #print(values)
  
  v_fcv = inverter_array(fcv)
  v_dist = inverter_array(dist)
  v_temp = inverter_array(temp)
  v_drod = inverter_array(drod)
  v_trod = inverter_array(trod)
  v_durb = inverter_array(durb)
  v_turb = inverter_array(turb)
  v_tpic = inverter_array(tpic)
  v_tnoi = inverter_array(tnoi)
 

  inicio = 0
  tamanho_pedaço = 1095
  print("")

  m_fcv = []
  m_dist = []
  m_temp = []
  m_drod = []
  m_trod = []
  m_durb = []
  m_turb = []
  m_tpic = []
  m_tnoi = []
  for i in range(inicio, len(v_fcv), tamanho_pedaço):
    #fcv
    # pedaço = [float(valor) for valor in v_fcv[i:i+tamanho_pedaço]]
    # soma = sum(pedaço)
    # media = soma / len(pedaço)
    # mediaFCV.append(media)
    # print(f"{media}", end=", ")
    
    m_fcv.append(media(v_fcv))
    m_dist.append(media(v_dist))
    m_temp.append(media(v_temp))
    m_drod.append(media(v_drod))
    m_trod.append(media(v_trod))
    m_durb.append(media(v_durb))
    m_turb.append(media(v_turb))
    m_tpic.append(media(v_tpic))
    m_tnoi.append(media(v_tnoi))

    #dist

  print("fcv", end=" = ")
  print(m_fcv)
  print("")

  print("DistanciaPercorrida", end=" = ")
  print(m_dist)
  print("")

  print("TempoFuncionamento", end=" = ")
  print(m_temp)
  print("")

  print("DistanciaPercorrida_Rodovia", end=" = ")
  print(m_drod)
  print("")

  print("TempoFuncionamento_Rodovia", end=" = ")
  print(m_trod)
  print("")

  print("DistanciaPercorrida_Urbana", end=" = ")
  print(m_durb)
  print("")

  print("TempoFuncionamento_Urbana", end=" = ")
  print(m_turb)
  print("")

  print("TempoHorarioPico", end=" = ")
  print(m_tpic)
  print("")

  print("TempoNoite", end=" = ")
  print(m_tnoi)
  print("")

  

  
  
  for j in range(len(m_fcv)):
    carro = {}
    carro['DistanciaPercorrida'] = m_dist[j]
    carro['TempoFuncionamento'] = m_temp[j]
    carro['DistanciaPercorrida_Rodovia'] = m_drod[j]
    carro['TempoFuncionamento_Rodovia'] = m_trod[j]
    carro['DistanciaPercorrida_Urbana'] = m_durb[j]
    carro['TempoFuncionamento_Urbana'] = m_turb[j]
    carro['TempoHorarioPico'] = m_tpic[j]
    carro['TempoNoite'] = m_tnoi[j]

    placasDict = {}
    placasDict['ZZZ-1111'] = [1.0, 1.0, 1.0, 1.0]
    placasDict['ZZZ-2222'] = [0.75, 0.5, 0.75, 0.75]
    placasDict['ZZZ-3333'] = [0.5, 0.25, 0.25, 0.5]
    placasDict['ZZZ-8888'] = [0.25, 0.375, 0.25, 1.0]
    placasDict['ZZZ-9999'] = [1.0, 1.0, 1.0, 1.0]

    if( j < len(m_fcv)/7):
      placasDict['ZZZ-8888'] = [0.25, 0.375, 0.25, 1]
      placasDict['ZZZ-9999'] = [1.0, 1.0, 1.0, 1.0]

    elif( len(m_fcv)/7 <= j < 2*len(m_fcv)/7):
      placasDict['ZZZ-8888'] = [0.5, 0.5, 0.75, 1]
      placasDict['ZZZ-9999'] = [1.0, 0.875, 0.75, 1.0]

    elif( 2*len(m_fcv)/7 <= j < 3*len(m_fcv)/7):
      placasDict['ZZZ-8888'] = [0.75, 0.675, 0.75, 1.0]
      placasDict['ZZZ-9999'] = [0.75, 0.75, 0.75, 1.0]

    elif( 3*len(m_fcv)/7 <= j < 4*len(m_fcv)/7):  
      placasDict['ZZZ-8888'] = [0.75, 0.75, 0.75, 1.0]
      placasDict['ZZZ-9999'] = [0.75, 0.75, 0.75, 1.0]

    elif( 4*len(m_fcv)/7 <= j < 5*len(m_fcv)/7):  
      placasDict['ZZZ-8888'] = [0.75, 0.75, 0.75, 1.0]
      placasDict['ZZZ-9999'] = [0.75, 0.675, 0.75, 1.0]

    elif( 5*len(m_fcv)/7 <= j < 6*len(m_fcv)/7):  
      placasDict['ZZZ-8888'] = [1.0, 0.875, 0.75, 1.0]
      placasDict['ZZZ-9999'] = [0.5, 0.5, 0.75, 1]

    else:
      placasDict['ZZZ-8888'] = [1.0, 1.0, 1.0, 1.0]
      placasDict['ZZZ-9999'] = [0.25, 0.375, 0.25, 1]

    print(fcv2(carro, placa, placasDict), end=", ")
  print("")

  # fcv.clear()
  # fcv = []
  
  #print(placasDict)

  # print(i)
  # print("média FCV: ")
  # print(fcv/j)
  # print("qtd:")
  # print(j)

#print(placasDict)

# for obj in objeto_python:
#   print(obj['Value']['placa'] + " : " + obj['Value']['DistanciaPercorrida'] + " : " + obj['Timestamp'])
#   distanciatotal = int(obj['Value']['DistanciaPercorrida']) + distanciatotal




