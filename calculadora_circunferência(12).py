"""
Programa: Calculadora de área e circunferência de um círculo
Descrição: Este programa calcula a área e a circunferência de um círculo.
Autor: Filipe
Data: 06/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis
import math
pi = math.pi
#Entrada de dados
r = float(input("Qual é o valor do raio do círculo? "))


#Processamento de dados
A = (pi*(r**2))
C = (2*pi*r)
#Saida de dados
print(f"O valor da área do círculo é de {A}.")
print(f"O valor da circunferência do círculo é de {C}.")
