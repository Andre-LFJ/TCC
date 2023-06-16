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
