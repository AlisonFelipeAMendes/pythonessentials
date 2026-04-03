#!C:\Python\python.exe
"""Hello Word Multi Linguage
Dependendo da liguagem configurada no ambiente o programa o programa exebia a correspondente.

Como usuar: 
Tenha a variavel 
        lang configurada devidamente no ambiente, a exemplo: 
        export Lang=pt_BR
        
        Execução:
        

#shebang é uma linha de código que indica qual interpretador deve ser usado para executar o script. No caso, estamos usando o Python 3.

Curso: Linuxtip Essentials

"""
import os

__version__ = "0.0.1"
__author__ = "Alison Mendes"



current_language = os.getenv("Lang","pt_BR")[:5]
print(current_language)
msg = "Hello, World!"
if current_language == "pt_BR":
        msg = "Olá, Mundo!"
elif current_language == "it_IT":
        msg = "Ciao, mondo!"
 
print(msg) 