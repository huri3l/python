from extrator_argumentos_url import ExtratorArgumentosUrl

# argumento = "moedaorigem=real"

# lista_argumento = argumento.split("=")
# print(lista_argumento)

# url = "https://www.bytebank.com.br/cambio?moedaorigem=real&moedadestino=dolar"
# url = "moedaorigem=real&moedadestino=dolar"

# argumentos_url = ExtratorArgumentosUrl(url)

# moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
# print(moeda_origem, moeda_destino)

url = "https://bytebank.com.br/cambio?moedaorigem=moedadestino&moedadestino=dolar&valor=1500"

argumentos_url = ExtratorArgumentosUrl(url)
moeda_origem, moeda_destino = argumentos_url.extrai_argumentos()
valor = argumentos_url.extrai_valor()
print(argumentos_url)