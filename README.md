# TCC

Certifique-se de ter docker CE 18.03 ou mais recente instalado;


Baixe o minifabric (com esse script ele será instalado na pasta ./mywork, isso pode ser alterado):
mkdir -p ./mywork && cd ./mywork && curl -o minifab -sL https://tinyurl.com/yxa2q6yr && chmod +x minifab

(opcional) Coloque o arquivo spec.yaml na pasta criada

Para iniciar a blockchain com as configurações padrão (ou as configurações do spec.yaml), execute na pasta do minifab, o comando: 
./minifab up
