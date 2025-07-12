#!pip install python-whois

"""
Criar um método que recebe um arquivo com lista de endpoint 
login.php 
admin.php
xpto.php

pega linha a linha. Junta cada linha com o site teste exemplo:
uol.com.br\login.php

e passa para o método testeRequisicao

O método requisicao rebe cada site completo e tenta consulta-lo. Conseguindo é para gravar a resposta em um arquivo.
Exemplo de leitura:

with open("endpoint.txt",'r') as leitura:
    print(leitura.read())

 e gravação:
 
#Atualizando o arquivo sem apagar as linhas anteriores.
with open("saida.txt",'a') as arquivo:
    arquivo.write("\n salvar o arquivo")

"""










"""
criar método que recebe o host como parametro e retorna os dados: headers, content, cookies
host = 'https://www.uol.com.br\{endpoint}
"""

# try:

#     import requests


#     r = requests.get("https://www.uol.com.br")
#     print(r.headers)
#     print(r.content)
#     print(r.cookies)


# except ModuleNotFoundError as e:
#     print(f"Módulo não instalado: {e}")

# except TimeoutError:
#     print("Site não existe ou fora do ar.")


"""


"""



# pip install dnspython


import dns.resolver

def list_dns_records(domain):
    """
    Lists various DNS records for a given domain.
    """
    record_types = ["A", "AAAA", "NS", "MX", "SOA", "TXT"]

    print(f"DNS Records for: {domain}\n")

    for record_type in record_types:
        try:
            answers = dns.resolver.resolve(domain, record_type)
            print(f"--- {record_type} Records ---")
            for rdata in answers:
                print(rdata)
            print()
        except dns.resolver.NoAnswer:
            print(f"No {record_type} records found for {domain}\n")
        except dns.resolver.NXDOMAIN:
            print(f"Domain {domain} does not exist.\n")
            return
        except Exception as e:
            print(f"Error querying {record_type} records: {e}\n")

if __name__ == "__main__":
    target_domain = "example.com"  # Replace with your desired domain
    list_dns_records(target_domain)