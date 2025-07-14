"""
Google dorks

Técnicas para criar pesquisa avançadas e mais elaboradas para buscar páginas indexadas dentro do mecanismo de busca.
Diferente do mecanismo simples. Este trás páginas indexadas e serviços que, em muitos casos, não poderiam estar.
Vamos criar uma ferramenta para ajudar em auditoria / pentest de sites web.

Tabela de comandos:

intitle : Trás informações que estão na barra de cabeçalho do site.
intitle: teste

inurl: Trás informações que estão na URL.
inurl:
intext:teste

intext: trás informações que estão no texto da página
exemplo:
intext:teste

filetype: trás arquivos indexados com a extensão apontada
exemplo:
filetyp:pdf,doc,xls

site: Só trás as páginas que estão neste site / host.

Exemplo de montagem:
https://www.google.com/search?q=intext:documentos+filetype:pdf

host = "https://www.google.com/search?q="

pesquisa=''
for chave,valor in pesquisa_google.items:
    pesquisa += chave+':'+valor

import requests    
host+pesquisa
"""


