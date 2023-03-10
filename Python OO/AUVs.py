from tabulate import tabulate
class AUVs():
    lista_auvs = []
    def __init__(self, nome, numero_thursters, ano_construção, numero_cameras, sensores):
        self.nome = nome
        self.numero_cameras = numero_cameras
        self.numero_thursters = numero_thursters
        self.lista_sensores = sensores
        self.ano_construção = ano_construção
        

    def exibir_individualmente(self):
        print(f'Nome do AUV: {self.nome}, possui thursters: {self.numero_thursters} e foi construído em {self.ano_construção}. Atualmente possui {self.numero_cameras} câmeras.')
        print(f'Possui os seguintes sensores: {self.lista_sensores}')
        
    def catalogar_auv(*auvs):
        AUVs.lista_auvs.extend(auvs)

    def listar_tabela_auvs():
        lista = []
        for auv in AUVs.lista_auvs:
            lista.append([auv.nome, auv.numero_thursters, auv.ano_construção, auv.numero_cameras, auv.lista_sensores])
        print(tabulate(lista, headers=['Nome', 'Thursters', 'Ano de construção', 'Câmeras', 'Sensores']))
        
    def definir_antiguidade():
        idadeMaior = 0
        lista = []
        for auv in AUVs.lista_auvs:
            if auv.ano_construção > idadeMaior:
                lista.insert(0, auv.nome)
                idadeMaior = auv.ano_construção
            else:
                lista.append(auv.nome)
        print(f'Rank de AUVs a partir do mais antigo: {lista}')

    def maior_angulo():
        numeroCamera = 0
        nome_auv = ''
        for auv in AUVs.lista_auvs:
            if auv.numero_cameras > numeroCamera:
                nome_auv = auv.nome
                numeroCamera = auv.numero_cameras
        print(f'O AUV com maior numero de cameras é o {nome_auv}')


#Exemplos aleatórios                   
auv1 = AUVs('Lua', 1, 2, 4, ['Oi', 'eu'])
auv2 = AUVs('HueBr', 2, 1, 3, ['h', 'l'])

# AUVs.catalogar_auv(auv1, auv2)
# AUVs.definir_antiguidade()
# AUVs.maior_angulo()
# AUVs.listar_tabela_auvs()
#auv1.exibir_individualmente()

