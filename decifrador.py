#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def constroiListaAlfabeto():
    alfabeto = "abcdefghiklmnopqrstuvwxyz"
    lista = []
    for letra in alfabeto:
        lista.append(letra)
        
    return lista

def normalizaTextoDecifrado(textoDecifrado):
    posicaoAtual = 0
    novoTexto = ""
    textoDecifrado = textoDecifrado.replace(" ", "")

#     while (posicaoAtual < len(textoDecifrado)):
#         primeiraLetra = textoDecifrado[posicaoAtual]
#         segundaLetra = textoDecifrado[posicaoAtual+1]
#         
#         proximaLetra = ""
#         if (posicaoAtual+2 < len(textoDecifrado)):
#             proximaLetra = textoDecifrado[posicaoAtual+2]
#         
#         if (primeiraLetra == proximaLetra):
#             novoTexto += primeiraLetra
#         else:
#             novoTexto += primeiraLetra + segundaLetra
#             
#         posicaoAtual += 2
        
    novoTexto = textoDecifrado.replace("x", "")
    if (novoTexto[len(novoTexto)-1] == "x"):
        novoTexto = novoTexto[0:len(novoTexto)-1]
            
    return novoTexto

def constroiMatriz(key):
    alfabeto = constroiListaAlfabeto()
    
    matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    linha = 0
    coluna = 0
    posicao = 0
    
    for letra in key:
        linha = posicao / 5
        coluna = posicao % 5
        
        if (letra in alfabeto):
            alfabeto.remove(letra)
            matriz[linha][coluna] = letra
            posicao += 1
        
    while (len(alfabeto) > 0):
        linha = posicao / 5
        coluna = posicao % 5
        
        matriz[linha][coluna] = alfabeto.pop(0)
        
        posicao += 1
    
    return matriz

def indiceDoElementoNaMatriz(matriz, elemento):
    posicaoMatriz = 0
    for linha in matriz:
        for coluna in linha:
            if (coluna == elemento):
                return [posicaoMatriz/5, posicaoMatriz%5] # retorna [linha, coluna]
            
            posicaoMatriz += 1

def decifraTextoCifrado(textoCifrado, matriz):
    posicaoAtual = 0;
    textoCifrado = textoCifrado.replace(" ", "")
    textoClaro = ""
    while (posicaoAtual < len(textoCifrado)):
        primeiraLetra = textoCifrado[posicaoAtual]
        segundaLetra = textoCifrado[posicaoAtual+1]
        
        indicePrimeiraLetra = indiceDoElementoNaMatriz(matriz, primeiraLetra)
        indiceSegundaLetra = indiceDoElementoNaMatriz(matriz, segundaLetra)
        
        if (indicePrimeiraLetra[0] == indiceSegundaLetra[0]): # estao na mesma linha
            textoClaro += matriz[indicePrimeiraLetra[0]][(indicePrimeiraLetra[1]-1)%5] + matriz[indiceSegundaLetra[0]][(indiceSegundaLetra[1]-1)%5]
        
        if (indicePrimeiraLetra[1] == indiceSegundaLetra[1]): # estao na mesma coluna
            textoClaro += matriz[(indicePrimeiraLetra[0]-1)%5][indicePrimeiraLetra[1]] + matriz[(indiceSegundaLetra[0]-1)%5][indiceSegundaLetra[1]]
    
        if (indicePrimeiraLetra[0] != indiceSegundaLetra[0] and indicePrimeiraLetra[1] != indiceSegundaLetra[1]): # estao em linhas e colunas diferentes
            textoClaro += matriz[indicePrimeiraLetra[0]][indiceSegundaLetra[1]] + matriz[indiceSegundaLetra[0]][indicePrimeiraLetra[1]]
        
        posicaoAtual+=2
        
    return textoClaro

def analisaTexto(texto):
    posicaoAtual = 0
    
    A, E, O, S, R, I = 0, 0, 0, 0, 0, 0
    DE, RA, ES, OS, AS, DO = 0, 0, 0, 0, 0, 0
    QUE, ENT, COM, NTE, EST, AVA = 0, 0, 0, 0, 0, 0
    
    while (posicaoAtual < len(texto)-3):
        if (texto[posicaoAtual] == "a"):
            A += 1
        if (texto[posicaoAtual] == "e"):
            E += 1
        if (texto[posicaoAtual] == "o"):
            O += 1
        if (texto[posicaoAtual] == "s"):
            S += 1
        if (texto[posicaoAtual] == "r"):
            R += 1
        if (texto[posicaoAtual] == "i"):
            I += 1
            
        if (texto[posicaoAtual]+texto[posicaoAtual+1] == 'de'):
            DE += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1] == 'ra'):
            RA += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1] == 'es'):
            ES += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1] == 'os'):
            OS += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1] == 'as'):
            AS += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1] == 'do'):
            DO += 1

        if (texto[posicaoAtual]+texto[posicaoAtual+1]+texto[posicaoAtual+2] == 'que'):
            QUE += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1]+texto[posicaoAtual+2] == 'ent'):
            ENT += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1]+texto[posicaoAtual+2] == 'com'):
            COM += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1]+texto[posicaoAtual+2] == 'nte'):
            NTE += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1]+texto[posicaoAtual+2] == 'est'):
            EST += 1
        if (texto[posicaoAtual]+texto[posicaoAtual+1]+texto[posicaoAtual+2] == 'ava'):
            AVA += 1
        
        posicaoAtual += 1
        
    return A+E+O+S+R+I+DE+RA+ES+OS+AS+DO+QUE+ENT+COM+NTE+EST+AVA
        


# DECIFRADOR.PY


f = open('dict.txt', 'r')
arquivo = open('textocifrado.txt', 'r')
textoCifrado = arquivo.read()

listaDeTextosClaros = {}
temp = 0
for key in f:
    matriz = constroiMatriz(key.lower())
      
    textoDecifrado = decifraTextoCifrado(textoCifrado, matriz)
    textoClaro = normalizaTextoDecifrado(textoDecifrado)
    
    pontuacao = analisaTexto(textoClaro)
    listaDeTextosClaros[key] = pontuacao
    
    temp += 1
    if (temp%5000 == 0): print "palavras analisados: " + str(temp)
    
pontuacoes = listaDeTextosClaros.values()
pontuacoes.sort()
pontuacoes.reverse()

temp = 0
provavelChave = ""
while (temp < 4):
    for key, pontuacao in listaDeTextosClaros.iteritems():
        if pontuacao == pontuacoes[temp]:
            provavelChave = key
            
    print "Provavel " + str(temp) + ": " + str(provavelChave)
    
    temp += 1



pontuacaoMax = 0
for pontuacao in pontuacoes:
    if (pontuacao > pontuacaoMax):
        pontuacaoMax = pontuacao
 
# print listaDeTextosClaros
provavelChave = ""
for key, pontuacao in listaDeTextosClaros.iteritems():
    if pontuacao == pontuacaoMax:
        provavelChave = key
         
print "AQUI: " + provavelChave

matriz = constroiMatriz(provavelChave)
textoDecifrado = decifraTextoCifrado(textoCifrado, matriz)
textoClaro = normalizaTextoDecifrado(textoDecifrado)
print "Texto claro: " + textoClaro