
import urllib.parse 

def gerar_dork_google(comandos: dict) -> tuple:
 

  host = "http://www.google.com/search?q="

  pesquisa = ''
  for chave, valor in comandos.items():
    pesquisa += f"{chave} : {valor}"

  dork_gerada = pesquisa.strip()
  url_final = host + urllib.parse.quote(dork_gerada)

  return dork_gerada, url_final

#Dicionario com os comandos. 
pesquisa_google= {
   'intile': 'como treinar seu dragao' , 
   'filetype': 'pdf'
   # 'inurl': 'adm'
   # 'intext': 'senha'
   # 'site': 'example.com'
}

# Resultado

dork, url = gerar_dork_google(pesquisa_google)


print("[DORK GERADA]")
print(dork)

print("[URL PRONTA PARA NAVEGADOR]")
print(url) 