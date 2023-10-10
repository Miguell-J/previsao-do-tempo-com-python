import requests
from tkinter import *

def previsao_tempo():
    API_KEY = '8a20a2b6fdb834daaee3a1c7bc841a2d'

    cidade = 'rio de janeiro'

    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(link)

    requisicao_dict = requisicao.json()

    descricao = requisicao_dict['weather'][0]['description']
    temperatura = requisicao_dict['main']['temp'] - 273.15
    sensacao_termica = requisicao_dict['main']['feels_like'] - 273.15

    texto = '''
        O clima hoje está {}
        A temperatura de hoje foi {:.2f} graus celcius
        A sensação térmica de hoje foi {:.2f} graus celcius
        '''.format(descricao, temperatura, sensacao_termica)
        
    dados_finais["text"] = texto
    
janela = Tk()
janela.geometry("600x600")
janela.title("Previsão do tempo")

texto_inicial = Label(janela, text="Previsão do tempo")
texto_inicial.grid(column=0, row=0, padx=170, pady=30)

botao = Button(janela, text="Clique para vizualizar os dados sobre o clima no RJ", command=previsao_tempo)
botao.grid(column=0, row=1, padx=170, pady=30)

dados_finais = Label(janela, text="")
dados_finais.grid(column=0, row=2, padx=170, pady=30)

janela.mainloop()