from django.shortcuts import render, HttpResponse

def hello(request, nome, idade):
    return HttpResponse('<h1> Hello {} idade: {}</h1>'.format(nome, idade))

def soma(request, n1, n2):
    soma = n1 + n2
    return HttpResponse('<h3> A soma de {} + {} é: {}</h3>'.format(n1, n2, soma))

def subtracao(request, n1, n2):
    sub = n1 - n2
    return HttpResponse('<h3> A subtração de {} - {} é: {}</h3>'.format(n1, n2, sub))

def divisao(request, n1, n2):
    divisao = n1 / n2
    return HttpResponse('<h3> {} dividido por {} é: {}</h3>'.format(n1, n2, divisao))

def multiplicacao(request, n1, n2):
    multi = n1 * n2
    return HttpResponse('<h3> A multiplicação de {} * {} é: {}</h3>'.format(n1, n2, multi))

