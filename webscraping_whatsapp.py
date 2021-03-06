import requests
import pandas as pd
from bs4 import BeautifulSoup
from random import randrange, uniform

# Listas de dados a serem extraidos
nome_list = []
telefone_list = []
whatsapp_list = []

for p in range(0, 535):
  url = 'https://corretoresdeplanosdesaude.com.br/simulador-de-planos-de-saude/?u='+str(p)

  # Requisição GET
  data = requests.get(url)

  # Testando objeto Response
  if data.status_code == 200:
    # print('Requisição bem sucedida!')
    print(str(p + 1))

  # Criação de objeto para salvar documento html
  soup = BeautifulSoup(data.text, 'html.parser')
 
  # Utilizando o método find_all para acessar o objeto 
  anuncios = soup.find_all(class_="bloco-2")

  for value in anuncios[0:]:
    if value.a:
      if value.span:
        nome = "Não informado"
        nome = value.span.b.string
        nome_list.append(nome)
        print("Nome: " + str(nome))
      else:
        nome_list.append("")

      contatos1 = soup.find_all(class_="telefone-fixo")

      if contatos1:
        for value in contatos1[0:1]:
          print("telefone fixo: " + str(value.string))
          telefone = "Não informado"
          telefone = value.string
          telefone_list.append(telefone)
      else:
        telefone_list.append("")
      
      contatos2 = soup.find_all(class_="whatsapp")

      if contatos2:
        for value in contatos2[0:]:
          print("Whatsapp: " + str(value.string))
          whatsapp = "Não informado"
          whatsapp = value.string
          whatsapp_list.append(whatsapp)
      else:
        whatsapp_list.append("")

print(len(nome_list))
print(len(telefone_list))
print(len(whatsapp_list))

# Carregando os dados em um Data Frame
df = pd.DataFrame.from_dict({
  'Nome': nome_list,
  'Telefone Fixo': telefone_list,
  'Whatsapp': whatsapp_list
})

# salvando planilha para excel
df.to_excel('Corretores.xlsx', encoding='utf-8', index=False)

# salvando planilha para csv
df.to_csv('Corretores.csv', encoding='utf-8', index=False)
