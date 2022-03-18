Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print("Estou aprendendo Python")
Estou aprendendo Python
print("Olá, Mundo!")
Olá, Mundo!
print(7+4)
11
print("7+4")
7+4
print("7"+"4")
74
7+4
11
"7"+"4"
'74'
print("Olá"+5)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("Olá"+5)
TypeError: can only concatenate str (not "int") to str
print("Olá",5)
Olá 5
nome="Amanda"print(nome,idade,peso)
SyntaxError: invalid syntax
nome=Amanda
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    nome=Amanda
NameError: name 'Amanda' is not defined
nome = 'Amanda'
idade = 40
peso = 70
print(nome,idade,peso)
Amanda 40 70
nome = input('Qual é o seu nome?')
Qual é o seu nome? Amanda
idade = input('Qual é a sua idade?')
Qual é a sua idade? 40 anos
peso = input("Qual é o seu peso?")
Qual é o seu peso? 70 quilos
print(nome,idade,peso)
 Amanda  40 anos  70 quilos
