import random
import os

pessoas_cod = {
           "Alex":[],
           "Finn": [],
           "Mordecai": [],
           "Rigby": [],
           "Steve": [], 
           }

numeros_f = (1, 2, 3, 4)

for c, k in (enumerate(pessoas_cod)):
    with open(f'{k}/rsa{c+1}.py', 'r') as arq:
        pessoas_cod[k] = arq.read()


for k, v in pessoas_cod.items():
    pessoas_cod2 = pessoas_cod.copy()
    pessoas_cod2.pop(k)
    pessoa_a_no = pessoas_cod2.copy()
    for l, b in pessoa_a_no.items():
        nl = list(numeros_f)

        for d in pessoa_a_no.values():
            n = nl.pop(random.randrange(0,len(nl)))
            with open(f'{k}/escolha/rsa{n}.py', 'w') as arq:
                arq.write(d)
                print(b[:20])
        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')


resp = input("Exclui? ").strip().lower()

if resp in "sim":
    for k in pessoas_cod.keys():
        for f in os.listdir(f'{k}/escolha'):
            os.remove(f'{k}/escolha/{f}')