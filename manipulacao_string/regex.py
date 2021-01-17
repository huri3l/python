import re

email1 = "Meu número é 1234-1234"
email2 = "Fale comigo em 123451234 e 3242-2342 errado: 3242-23425 esse é meu telefone 9847-9872"
email3 = "1234-1234 é o meu celular"
email4 = "sdhfsdufsd 99324-2134 shufshdufshduf asudhfsudfhuas"

padrao = "[0-9]{4,5}[-]*[0-9]{4}"

retorno = re.findall(padrao, email2)
print(retorno)