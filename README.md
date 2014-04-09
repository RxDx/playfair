playfair
========

Cifra Playfair

Rodrigo de Toledo Montandon Dumont
GRR20104762

Modo de uso:
Insira o texto a ser cifrado no arquivo "textoclaro.txt"
Execute o script "cifrador.py" com o parametro chave. Exemplo: $ python chave
Ele irá criar uma matriz de acordo com a chave e cifrar o texto e adiciona-lo no arquivo textocifrado.txt

Para quebrar a criptografia simplesmente execute o script "decifrador.py".
Ele irá ler o arquivo "textocifrado.txt" e fazer uma combinacao com todas as palavras presentes no arquivo "dict.txt"
O script irá analisar a frequencia de palavras num algoritmo simples, portanto quanto maior o texto a ser decifrado, menor a chance de falsos positivos.

A versão mais atual do programa encontra-se disponível através do seguinte repositório público Git:
https://github.com/RxDx/playfair