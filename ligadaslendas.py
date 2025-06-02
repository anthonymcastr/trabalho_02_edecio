
from collections import defaultdict
import csv

campeoes = []

with open("personagens.csv", mode="r") as arq:
  dados_csv = csv.DictReader(arq)
  for linha in dados_csv:
    campeoes.append(linha)



## essa collection dafaultdict me ajuda nas funções de agrupamento quando uma das chaves tá vazia, ela cria uma lista vazia p/ não dar erro

def titulo(texto):
  print()
  print(texto)
  print("-"*40)

## primeira função realiza a busca de perconagem por preço, jogamos pra um array encontrado caso a resposta seja o mesmo valor da chave preço
## organizamos posteriormente com o dict(sorted, defiindo que vamos organizar pelo item [0], que no caso é o nome do personagem, ou seja, ordem alfabética


def preco_personagem():
    titulo("Busca de campeões por preço")

    pergunta = int(input("Digite o valor do campeão: "))
    grupos = {}
    encontrado = False

    for campeao in campeoes:
        preco = campeao['Blue Essence']
        nome = campeao['Name']

        if preco == "":
            continue

        if int(preco) == pergunta:
            encontrado = True
            grupos[nome] = int(preco)

    if encontrado:
        organizados = dict(sorted(grupos.items(), key=lambda grupo: grupo[0]))
        print("-"*40)
        quantidade = len(organizados) 
        print(f"Temos no total {quantidade} campeões de custo BE: {pergunta}")
        for num, (nome, preco) in enumerate(organizados.items(), start=1):
         print(f"{num:2d} {nome:25s}  {preco}")

         
    else:
        print("\nNão foram lançados campeões nesse ano.")
        

## pra data de lançamento, basicamente fazemos a mesma coisa porém precisamos apenas dos 4 digitos referentes ao ano, por isso o [:4]
## coloquei um continue, caso por algum motivo não contenha o ano do personagem, assim ele contia agrupando nome e ano dos demais
## depois realizo uma repetição pra fazer a organização da resposta

  
def data_lancamento_personagem():
    titulo("Busca de personagem por data de lançamento")

    pergunta = int(input("Digite o ano que o personagem foi lançado: "))
    grupos = {}
    encontrado = False

    for campeao in campeoes:
        data = campeao['Release Date']
        ano = data[:4]
        nome = campeao['Name']

        if ano == "":
            continue

        if int(ano) == pergunta:
            encontrado = True
            grupos[nome] = int(ano)

    if encontrado:
        organizados = dict(sorted(grupos.items(), key=lambda grupo: grupo[0]))
        print("-"*40)
        quantidade = len(organizados) 
        print(f"Temos no total {quantidade} personagens lançados no ano de {pergunta}")
        for num, (nome, ano) in enumerate(organizados.items(), start=1):
         
         
         print(f"{num:2d} {nome:25s} Ano: {data[:4]}")

         
    else:
        print("\nNão foram lançados personagens nesse ano.")
  

def todos_personagens_por_ano():
    titulo("Todos os personagens agrupados por ano de lançamento")

    
    grupos = defaultdict(list)

    for campeao in campeoes:
        data = campeao['Release Date']
        if not data:
            continue

        ano = data[:4]
        nome = campeao['Name']
        grupos[ano].append(nome)

    
    anos_ordenados = sorted(grupos.items(), key=lambda item: item[0])

    for ano, personagens in anos_ordenados:
        print("-" * 50)
        print(f"Ano: {ano} - Total: {len(personagens)} personagem(ns)")
        print("-" * 50)
        for i, nome in enumerate(sorted(personagens), start=1):
            print(f"{i:2d} {nome}")
        print()  




## para o somatório de personagens em cada classe, transformamos o grupos em uma lista, nessa lista percorremos cada personagem buscando a classe e o valor
## depois de realizar a busca, em caso de sucesso, importamos o nome do personagem e selecionamos as classes dele (caso tenha mais de uma, o split divide em um array de duas classes)

def valor_por_classe():
    titulo("Todas as classes e a soma total de personagens presentes nelas.")

    grupos = defaultdict(list)

    for campeao in campeoes:
        classes = campeao['Classes']
        preco = campeao['Blue Essence']

        if not classes:
            continue

        nome = campeao['Name']
        lista_classes = classes.split()

        for classe in lista_classes:
            grupos[classe].append((nome, preco))

    

    ## aqui ordenamos as classes, onde selecionamos que precisamos apenas do valor, ignoramos o primeiro atributo com o _
    classes_ordenadas = sorted(
    grupos.items(),
    key=lambda item: sum(int(preco) for _, preco in item[1]),
    reverse=True
)

    for classe, lista in classes_ordenadas:
        print("-" * 50)
        print(f"Classe: {classe} - Total: {len(lista)} personagem(ns)")
        soma_valores = sum(int(preco) for _, preco in lista)
        print(f"Soma total de Blue Essence: {soma_valores}")
        print("-" * 50)
        for i, (nome, preco) in enumerate(sorted(lista), start=1):
            print(f"{i:2d}. {nome} ({preco} BE)")
        print()


## fazemos duas perguntas iniciais, qual classe deseja buscar e qual atributo ela não deve ter
## 



def analise_por_classe_sem_atributo():
    titulo("Análise de personagem por classe escolhida, que NÃO contém determinado atributo")

    classe_busca = input("Qual a classe do personagem? ").strip().lower()
    atributo_excluido = input("Qual o atributo que NÃO deve estar presente? Ex: mana, energy... ").strip().lower()

    encontrados = []

    for campeao in campeoes:
        classes = campeao['Classes']
        atributos = campeao['Resourse type']
        preco = campeao['Blue Essence']
        nome = campeao['Name']

        if not classes or not preco:
            continue

        lista_classes = str(classes).lower().split() ## transformamos todas as classes em strings, e retiramos os espaços vazios com split
        atributo_formatado = str(atributos).lower().strip() if atributos else "" ## caso tenha atributos, formatamos ele com lower e o strip vai tirar os espaços vazios

        # Se a classe bate e o atributo não é exatamente o que deve ser excluído
        if classe_busca in lista_classes and atributo_excluido not in atributo_formatado:
            encontrados.append((nome, preco))

    if not encontrados:
        print("\nNenhum personagem encontrado com os critérios fornecidos.")
        return

    print(f"\nPersonagens da classe {classe_busca} que NÃO POSSUEM o atributo {atributo_excluido}:")
    print("-" * 60)
    for i, (nome, preco) in enumerate(sorted(encontrados), start=1):
        print(f"{i:2d}. {nome} ({preco} BE)")
    print("-" * 60)
    soma_total = sum(int(preco) for _, preco in encontrados)
    media = soma_total / len(encontrados)
    print(f"Total de personagens: {len(encontrados)}")
    print(f"Soma total de BE: {soma_total}")
    print(f"Média de BE: {media:.2f}")
    print()


## busca de personagens que estão presentes em duas classes
## abrimos um array p personagens encontrados
## percorremos a lista de personagens, importando classe, preco e nome. 
## lista as classes com lower e split, depois faz um if com duas condições onde ambas as classes precisam estar presentes nessa lista
## se estiverem, o array encontrados vai receber o nome e o preco do personagem

def personagens_duas_classes():
    titulo("Campeões que pertencem a DUAS classes específicas")
    classe1 = input("Digite a 1ª classe: ").strip().lower()
    classe2 = input("Digite a 2ª classe: ").strip().lower()

    encontrados = []
    for campeao in campeoes:
        classes = campeao['Classes']
        preco = campeao['Blue Essence']
        nome = campeao['Name']

        if not classes or not preco:
            continue

        lista_classes = classes.lower().split()
        if classe1 in lista_classes and classe2 in lista_classes:
            encontrados.append((nome, int(preco)))

    if encontrados:
        print(f"\Personagens das classes {classe1} E {classe2}:")
        for i, (nome, preco) in enumerate(sorted(encontrados), start=1):
            print(f"{i:2d}. {nome} ({preco} BE)")
        print(f"Total: {len(encontrados)} campeões")
    else:
        print("Nenhum personagem encontrado nas duas classes.")


while True:
  titulo("League of Legends até 2024")
  print("1. Busca de personagens por Preço")
  print("2. Busca de personagens por Ano de Lançamento")
  print("3. Lista todos os personagens agrupando por Ano de Lançamento")
  print("4. Lista de classes e valor total de BE")
  print("5. Análise de personagem sem determinado atributo")
  print("6. Personagens que pertencem a duas classes")
  print("7. Finalizar")  
  opcao = int(input("Opção: "))
  if opcao == 1:
    preco_personagem()
  
  elif opcao == 2:
     data_lancamento_personagem()

  elif opcao == 3:
    todos_personagens_por_ano()

  elif opcao ==4:
     valor_por_classe()

  elif opcao == 5:
     analise_por_classe_sem_atributo()

  elif opcao == 6:
     personagens_duas_classes()

  else:
    break
