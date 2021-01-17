class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def formatada(self):
        if self.dia and self.mes and self.ano:
            print(f"{self.dia}/{self.mes}/{self.ano}")
        else:
            print("Informações estão faltando.")