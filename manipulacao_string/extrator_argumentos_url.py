class ExtratorArgumentosUrl:
    def __init__(self, url):
        if self.string_valida(url):
            self.url = url.lower()
        else:
            raise LookupError("URL Inválida!")

    @staticmethod
    def string_valida(url):
        if url and url.startswith("https://bytebank.com"):
            return True
        else:
            return False

    def __len__(self):
        return len(self.url) 

    def __str__(self):
        moeda_origem, moeda_destino = self.extrai_argumentos()
        representacao_string = f"Valor: {self.extrai_valor()}\nMoeda Origem: {moeda_origem}\nMoeda Destino: {moeda_destino}"
        return representacao_string

    def __eq__(self, outra_instancia):
        return self.url == outra_instancia.url

    def extrai_argumentos(self):

        id_moeda_origem = "moedaorigem=".lower()
        id_moeda_destino = "moedadestino=".lower()

        indice_inicial_moeda_origem     = self.encontra_indice_inicial(id_moeda_origem)
        indice_final_moeda_origem       = self.url.find("&")
        moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        if moeda_origem == "moedadestino":
            self.troca_moeda_origem()

            indice_inicial_moeda_origem     = self.encontra_indice_inicial(id_moeda_origem)
            indice_final_moeda_origem       = self.url.find("&")
            moeda_origem = self.url[indice_inicial_moeda_origem:indice_final_moeda_origem]

        indice_inicial_moeda_destino    = self.encontra_indice_inicial(id_moeda_destino)
        indice_final_moeda_destino       = self.url.find("&valor")
        moeda_destino = self.url[indice_inicial_moeda_destino:indice_final_moeda_destino]

        return moeda_origem, moeda_destino

    def encontra_indice_inicial(self, argumento):
        return self.url.find(argumento) + len(argumento)

    def troca_moeda_origem(self):
        self.url = self.url.replace("moedadestino", "real", 1)
        print(self.url)

    def extrai_valor(self):
        busca_valor = "valor="
        indice_inicial_valor = self.encontra_indice_inicial(busca_valor)
        valor = self.url[indice_inicial_valor:]
        return valor