import requests
import json
import PySimpleGUI as sg
#documentacao para consultas : http://apiadvisor.climatempo.com.br/doc/index.html
#API FREE - o codigo para esse token é o de salvador 7564, caso queira usar outro id precisa de outra token.


## CONTROLE MANUAL DO PROGRAMA ##

token = "2d3962cf2472db7aa9a69880d1781e84" #informe seu token - Atrelado ao ID.
city_id = 0
type_search = 2           #informe o codigo da consulta


class TelaPython:
    def __init__(self):
        self.frase1 = "Digite o nome da cidade para buscar o ID "
        self.frase2 = "Digite o ID da cidade que você quer saber a Previsão do tempo:"

    def Iniciar(self):

        #Layout
        layout = [
            [sg.Text(" ## Clima tempo API ## ", size=(20,0))],
            [[sg.Output(size=(30,15))]],
            [sg.Input(size=(30, 0), key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Responder')],

        ]

        #JANELA
        self.janela = sg.Window('Weather API!', layout=layout)


        while True:

            #Ler dados
            self.LerValores()

            #Fazer Algo


            # 1 - Buscar o id da cidade digitada

            if type_search == 1 and self.eventos == 'Iniciar':
                print(self.frase1)
                self.LerValores()
                city_search = self.valores['escolha']
                url = "http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=" + str(
                    city_search) + "&token=" + str(token)
                reposicao = requests.get(url)
                retorno_reposicao = json.loads(reposicao.text)
                for chave in retorno_reposicao:
                    ID = chave['id']
                    name = chave['name']
                    state = chave['state']
                    country = chave['country']
                    print("id : " + str(ID) + " name : " + str(name) + " state: " + str(state) + " Country:" + str(
                        country))
                    print(" ")

            #2 - Previsão do tempo na cidade

            if type_search == 2 and self.eventos == 'Iniciar':
                print(self.frase2)
                self.LerValores()

                try:
                    city_id = self.valores['escolha']   ##Só vai funcionar um ID, porque a API é free(7564)
                    url = "http://apiadvisor.climatempo.com.br/api/v1/weather/locale/" + str(
                        city_id) + "/current?token=" + str(
                        token)
                    reposicao = requests.get(url)
                    retorno_reposicao = json.loads(reposicao.text)

                    print("\n")
                    print("Cidade:", retorno_reposicao['name'])
                    print("Temperatura:", retorno_reposicao['data']['temperature'], "Graus")
                    print("Umidade :", retorno_reposicao['data']['humidity'])
                    print("Condição :", retorno_reposicao['data']['condition'])
                    print("Sensação termica :", retorno_reposicao['data']['sensation'])
                    print("Data e horario :", retorno_reposicao['data']['date'])

                except:
                    print("Codigo digitado errado!")


            # 3 Previsão proximas 72 horas

            if type_search == 3 and self.eventos == 'Iniciar':

                city_id = self.valores['escolha']
                url = "http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/" + str(
                    city_id) + "/hours/72?token=" + token
                reposicao = requests.get(url)
                retorno_reposicao = json.loads(reposicao.text)
                # print(retorno_reposicao)

                for chave in retorno_reposicao['data']:
                    data = chave.get('date_br')
                    temperatura = chave['temperature']['temperature']
                    print("data:" + str(data) + " " + str(chave) + "º" + "\n")


    def LerValores(self): #Modulo para ler os dados da janela
        self.eventos, self.valores = self.janela.Read()


weather = TelaPython()
weather.Iniciar()


























