class AUVs():
    def __init__(self, nome, numero_thursters, ano_construção, numero_cameras):
        self.nome = nome
        self.numero_cameras = numero_cameras
        self.numero_thursters = numero_thursters
        # self.lista_sensores = [sensores]
        self.ano_construção = ano_construção
        self.auvs = []

    def exibir(self):
        return f'Meu nome é {self.nome}'
        
    def catalogar_auv(self, *auvs):
        self.auvs.extend(auvs)

    def listar_auvs(self):
        print()
        for auv in self.auvs:
            print(auv.nome)
        print()

# from dataclasses import dataclass
# from typing import List

# @dataclass
# class AUVs():
#     nome: str
#     numero_thursters: int
#     ano_construção: int
#     numero_cameras: int
#     lista_auvs : List[AUVs]
#     lista_sensores: List[str]

#     def exibir(self):
#         return f'Meu nome é {self.nome}'
        
# auv1 = AUVs('Gustavo', 1, 2, 3)
# print(auv1.numero_cameras)
# AUVs.catalogar_auv(auv1)
# AUVs.listar_auvs

