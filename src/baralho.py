from carta_normal import CartaNormal
from carta_especial import CartaEspecial
import json


class Baralho():
    
    def __init__(self) -> None:
        self.__cartas = []
        self.criar_baralho()

    @property
    def cartas(self):
        return self.__cartas
    
    @cartas.setter
    def ultima_carta(self, cartas):
        self.__cartas = cartas


    def to_json(self) -> dict:
        a =  json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json_acceptable_string = a.replace("'", "\"")
        json_ = json.loads(json_acceptable_string)
        return json_

    def darCarta(self):
        return self.__cartas.pop(0)
    
    def get_cartas(self):
        return self.__cartas
    
    
    def criar_baralho(self):
        cores_primaria = ["vermelho", "laranja", "amarelo", "verde", "azul", "anil", "roxo"]
        cores_secundaria = ["roxo",  "anil", "azul", "verde", "amarelo", "laranja", "vermelho"]
        lista_cartas_comuns = []
        lista_cartas_especiais = []

        for cor_primaria in cores_primaria:
            for cor_secundaria in cores_secundaria:
                for numero in range(1, 4):
                    if cor_primaria != cor_secundaria:
                        lista_cartas_comuns.append(CartaNormal(cor_primaria, cor_secundaria, numero))
                        #print("carta criada: ", cor_primaria, cor_secundaria, numero)
        for numero in range(7):
            lista_cartas_especiais.append(CartaEspecial('preto', 'mais-um'))
            lista_cartas_especiais.append(CartaEspecial('preto', 'block'))
        
        self.__cartas.extend(lista_cartas_comuns)
        self.__cartas.extend(lista_cartas_especiais)

