import requests
import json
#documentacao para consultas : http://apiadvisor.climatempo.com.br/doc/index.html
#é preciso fazer algumas alterações por causa da API free.

token = "" #informe seu token
city_id = 7564   #informe o id da sua cidade que esta relacionado com o token
type_search = 3             #informe o codigo da consulta


#1 - Buscar o id da cidade digitada

if type_search == 1:
    city_search  = input("Digite o nome da cidade : ")
    url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name="+str(city_search)+"&token=" + str(token)
    reposicao = requests.get(url)
    retorno_reposicao = json.loads(reposicao.text)
    for chave in retorno_reposicao:
        ID = chave['id']
        name = chave['name']
        state = chave['state']
        country = chave['country']
        print("id : " + str(ID) + " name : " + str(name) + " state: " + str(state) + " Country:" + str(country))

    new_city = input("informe o ID da cidade : ")
    url = "http://apiadvisor.climatempo.com.br/api-manager/user-token/"+str(token)+"/locales"
    payload = "localeId[]=" + str(new_city)
    headers = {"Content-Type": 'application/x-www-form-urlencoded'}
    reposicao = requests.put(url, headers=headers, data=payload)
    print(reposicao)

#2 - Previsão do tempo na cidade
if type_search == 2:
    url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/"+str(city_id)+"/current?token=" + str(token)
    reposicao = requests.get(url)
    retorno_reposicao = json.loads(reposicao.text)

    print("Cidade:" , retorno_reposicao['name'])
    print("Temperatura:", retorno_reposicao['data']['temperature'], "Graus")
    print("Umidade :", retorno_reposicao['data']['humidity'])
    print("Condição :", retorno_reposicao['data']['condition'])
    print("Sensação termica :", retorno_reposicao['data']['sensation'])
    print("Data e horario :", retorno_reposicao['data']['date'])

#3 Previsão proximas 72 horas
if type_search == 3:
    url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/"+str(city_id)+"/hours/72?token="+token
    reposicao = requests.get(url)
    retorno_reposicao = json.loads(reposicao.text)
    #print(retorno_reposicao)

    for chave in retorno_reposicao['data']:
        data = chave.get('date_br')
        temperatura = chave['temperature']['temperature']
        print("data:" + str(data) + " " + str(chave) + "º" + "\n")


















