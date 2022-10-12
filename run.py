import csv, os

caminho = input('Informe o caminho absoluto do arquivo csv: ')
string_doc = """ESP\t\tEPOCA\tRESP\n"""
try:
    with open (caminho) as arquivo:
        dados = csv.reader(arquivo, delimiter=',')
        for i, j in enumerate(dados):
            if i == 0:
                pass
            else:
                esp = ''
                for l, m in enumerate (j):
                    if ',' in m:
                        m = m.replace(',', '.')
                    if l == 0:
                        esp = m
                    if l == 2: 
                        string_doc += esp + '\t0\t\t' + m + '\n'
                    if l == 3: 
                        string_doc += esp + '\t2\t\t' + m + '\n'
                    if l == 4: 
                        string_doc += esp + '\t4\t\t' + m + '\n'
                    if l == 5: 
                        string_doc += esp + '\t6\t\t' + m + '\n'
                    if l == 6: 
                        string_doc += esp + '\t8\t\t' + m + '\n'
                    if l == 7: 
                        string_doc += esp + '\t12\t\t' + m + '\n'
                    if l == 8: 
                        string_doc += esp + '\t16\t\t' + m + '\n'
                    if l == 9: 
                        string_doc += esp + '\t20\t\t' + m + '\n'
                    if l == 10: 
                        string_doc += esp + '\t24\t\t' + m + '\n'
    # print(string_doc)
except Exception as e:
    print(e)
nome_documento = input('Informe o nome do documento: ')
if '.txt' in nome_documento:
    pass
if '.' in nome_documento and not '.txt' in nome_documento:
    print('Você não informou uma extensão válida')
if not '.txt' in nome_documento:
    nome_documento += '.txt'
try:
    with open(nome_documento, 'w') as txt:
        txt.write(string_doc)
    print(f'Documento salvo em {os.getcwd()}/{nome_documento}')
except Exception as e:
    print(e)