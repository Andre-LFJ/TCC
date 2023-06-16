# Blockchain + FCV

Todos os códigos e arquivos estão disponíveis em:   
https://github.com/Andre-LFJ/TCC

Certifique-se de ter docker CE 18.03 ou mais recente instalado;  


1- Baixe o minifabric (com esse script ele será instalado na pasta ./mywork, isso pode ser alterado):  
```mkdir -p ./mywork && cd ./mywork && curl -o minifab -sL https://tinyurl.com/yxa2q6yr && chmod +x minifab```;    

1.1- (opcional) Coloque o arquivo spec.yaml na pasta criada  

2- Para iniciar a blockchain com as configurações padrão (ou as configurações do spec.yaml), execute na pasta do minifab, o comando:   
```./minifab up```   

3- Coloque a pasta “fabcar” do arquivo "fabcar.rar" dentro do diretório    
```../vars/chaincode/```;   

A estrutura dos arquivos deve ficar dessa forma:

```../vars/chaincode/fabcar/go```

4- Agora, na pasta do minifab, execute o comando:    
```minifab ccup -n fabcar -l  go -v 1.0```   

Isso irá instalar o chaincode (-n) fabcar, na linguagem (-l) go na versão (-v) 1.0. A versão precisa ser alterada para cada modificação e re-instalação do chaincode (ex: 1.0, 1.1, 1.2…);  

5- Para saber se a blockchain está funcionando execute o comando:   
```minifab stats```

   
_______________________________________
A- Para testar inserir um veículo na blockchain, use o comando:   
```./minifab invoke -n fabcar -p '"createCar", "[INFORMAÇÕES]"'```        

Onde [INFORMAÇÕES] são as informações do veículo, da forma:   
```"DistanciaPercorrida", "TempoFuncionamento", "DistanciaPercorrida_Rodovia", "TempoFuncionamento_Rodovia", "DistanciaPercorrida_Urbana", "TempoFuncionamento_Urbana", "TempoHorarioPico", "TempoNoite"```


B- Para verificar as últimas informações de todos os veículos (informação do último bloco em que cada um aparece) utilize o comando:
```minifab invoke -n fabcar -p '"queryAllCars”’```   

C -Para verificar todo o histórico de um veículo, execute o comando:    
```minifab invoke -n fabcar -p '"getHistoryForAsset”, “[PLACA]”’```   

Onde [PLACA] é a placa do veículo, da forma:   
```AAA-1111```

_______________________________________
addinfo.py:

No fim do arquivo existe a função main();      
Para executar uma função, apenas retire o comentário;     
Para a função "generateVeiculo()", 3 tipos de veículos podem ser criados:     
Bom (ZZZ-1111)    
Médio (ZZZ-2222)    
Ruim (ZZZ-3333)    
Para executar um veículo, descomente sua respectiva linha (entre 388-390) e também sua respectiva função (408-410).    


Para a função "generateVeiculoBomRuim()", um veículo (ZZZ-3333) será gerado, começando Bom e terminando Ruim;  
Para a função "generateVeiculoRuimBom()", um veículo (ZZZ-4444) será gerado, começando Ruim e terminando Bom;   

O algoritmo está configurado para apenas printar na tela o resultado do FCV, se desejar inserir as informações na blockchain, retire o comentário da linha 111:   
```#command = f"./minifab invoke -n fabcar -p '\"createCar\", \"{placa}\", \"{fcvatual}\", \"{new_values['DistanciaPercorrida']}\", \"{new_values['TempoFuncionamento']}\", \"{new_values['DistanciaPercorrida_Rodovia']}\", \"{new_values['TempoFuncionamento_Rodovia']}\", \"{new_values['DistanciaPercorrida_Urbana']}\", \"{new_values['TempoFuncionamento_Urbana']}\", \"{new_values['TempoHorarioPico']}\", \"{new_values['TempoNoite']}\"' "```

