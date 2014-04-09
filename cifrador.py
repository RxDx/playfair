#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys

def constroiListaAlfabeto():
    alfabeto = "abcdefghiklmnopqrstuvwxyz"
    lista = []
    for letra in alfabeto:
        lista.append(letra)
        
    return lista

def normalizaTextoOriginal(textoOriginal):
    posicaoAtual = 0
    novoTexto = ""
    textoOriginal = textoOriginal.lower()
    textoOriginal = textoOriginal.replace(" ","")
    textoOriginal = textoOriginal.replace(",","")
    textoOriginal = textoOriginal.replace(".","")
    while (posicaoAtual < len(textoOriginal)-1):
        primeiraLetra = textoOriginal[posicaoAtual]
        segundaLetra = textoOriginal[posicaoAtual+1]
        
        if (primeiraLetra == segundaLetra):
            novoTexto += primeiraLetra + "x"
            posicaoAtual += 1
        else:
            novoTexto += primeiraLetra + segundaLetra
            posicaoAtual += 2
    
    if (posicaoAtual < len(textoOriginal)):
        novoTexto += textoOriginal[posicaoAtual] + "x"

    return novoTexto

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
            
def cifraTextoClaro(textoClaro, matriz):
    posicaoAtual = 0;
    textoCifrado = ""
    while (posicaoAtual < len(textoClaro)):
        primeiraLetra = textoClaro[posicaoAtual]
        segundaLetra = textoClaro[posicaoAtual+1]
        
        indicePrimeiraLetra = indiceDoElementoNaMatriz(matriz, primeiraLetra)
        indiceSegundaLetra = indiceDoElementoNaMatriz(matriz, segundaLetra)
        
        if (indicePrimeiraLetra[0] == indiceSegundaLetra[0]): # estao na mesma linha
            textoCifrado += matriz[indicePrimeiraLetra[0]][(indicePrimeiraLetra[1]+1)%5] + matriz[indiceSegundaLetra[0]][(indiceSegundaLetra[1]+1)%5]
        
        if (indicePrimeiraLetra[1] == indiceSegundaLetra[1]): # estao na mesma coluna
            textoCifrado += matriz[(indicePrimeiraLetra[0]+1)%5][indicePrimeiraLetra[1]] + matriz[(indiceSegundaLetra[0]+1)%5][indiceSegundaLetra[1]]
    
        if (indicePrimeiraLetra[0] != indiceSegundaLetra[0] and indicePrimeiraLetra[1] != indiceSegundaLetra[1]): # estao em linhas e colunas diferentes
            textoCifrado += matriz[indicePrimeiraLetra[0]][indiceSegundaLetra[1]] + matriz[indiceSegundaLetra[0]][indicePrimeiraLetra[1]]
        
        posicaoAtual+=2
        
    return textoCifrado

# CIFRADOR.PY

if (len(sys.argv) != 3):
    print "Modo de uso: ./cifrador chave texto\nOBS: se texto estiver com espaço, colocar entre aspas."
    exit()

f = open("textocifrado.txt", "w")

matriz = constroiMatriz(sys.argv[1])
# print matriz
textoCifrado = cifraTextoClaro(normalizaTextoOriginal(sys.argv[2]), matriz)
print "Texto cifrado: " + textoCifrado
f.write(textoCifrado)
f.close()