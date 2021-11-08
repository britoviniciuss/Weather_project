import requests
import json
import PySimpleGUI as sg
#documentation: http://apiadvisor.climatempo.com.br/doc/index.html
#API FREE - for this reason option #2 only works with code (7564 - Salvador)


## Manual program control ##
token = " " #inform your token - Attached in ID.
city_id = 0


class WeatherAPI:
    def __init__(self):
        self.frase1 = "Nome da cidade para buscar o ID: "
        self.frase2 = "ID da cidade que você quer saber a Previsão do tempo:"

    def Start(self):


        #Layout
        sg.theme('DarkAmber') #theme
        layout = [
            [sg.Text(" ## Clima tempo API ## ", size=(20,0))],
            [sg.Text("Oque você deseja fazer?")],
            [sg.Checkbox("Cons. ID",key='id'), sg.Checkbox('Cons. Previsao',key="previsao")],
            [[sg.Output(size=(30,15))]],
            [sg.Input(size=(30, 0), key='escolha')],
            [sg.Button('Iniciar'),sg.Button('Consultar')],

        ]

        #Window
        self.janela = sg.Window('Weather API', layout=layout)


        while True:

            #Data read;
            self.ReadValues()


            #Caso selecione as duas opções

            if self.eventos == 'Iniciar' and self.valores['previsao'] and self.valores['id']:
                print("Selicione apenas uma opção")
                self.ReadValues()


            # 1 - Buscar o id da cidade digitada


            if self.eventos == 'Iniciar' and self.valores['id'] and not self.valores['previsao'] :
                print(self.frase1)
                self.ReadValues()
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
                    break

            #2 - Previsão do tempo na cidade

            if self.eventos == 'Iniciar' and self.valores['previsao'] and not self.valores['id']:
                print(self.frase2)
                self.ReadValues()

                try:
                    city_id = self.valores['escolha']  ##Here only one ID works 7564 because API it's free.
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




    def ReadValues(self): #module to read values.
        self.eventos, self.valores = self.janela.Read()


weather = WeatherAPI()
weather.Start()


























