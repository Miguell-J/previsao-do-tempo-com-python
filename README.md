# Previsão do tempo python

<img src="https://images.app.goo.gl/BBjpsPqAeWgSH6td8"/>

Este é um exemplo de código Python que utiliza a biblioteca requests para fazer uma requisição à API do OpenWeatherMap e a biblioteca tkinter para criar uma interface gráfica simples. A aplicação permite obter a previsão do tempo para a cidade do Rio de Janeiro.

## Como Funciona
O código possui uma função previsao_tempo que realiza o seguinte:

- Define uma chave de API API_KEY do OpenWeatherMap e a cidade como "rio de janeiro".
- Monta a URL da API com a chave de API e cidade.
- Realiza uma requisição GET para a URL da API.
- Converte a resposta da requisição em um dicionário usando o método json().
- Extrai informações relevantes da resposta, como descrição do clima, temperatura e sensação térmica.
- Formata essas informações em um texto e atualiza um rótulo na interface gráfica com esses dados.

## Interface Gráfica
<img src="./Captura de tela 2023-10-10 191824.png"/>

A aplicação possui uma janela criada com o tkinter:

- Dimensões da janela: 600x600 pixels.
- Título da janela: "Previsão do tempo"

A janela contém três elementos:

- texto_inicial (rótulo): Exibe o texto "Previsão do tempo".
- botao (botão): Quando clicado, aciona a função previsao_tempo para obter a previsão do tempo e atualizar a interface com os dados.
- dados_finais (rótulo): Inicialmente vazio, este rótulo será preenchido com os dados da previsão do tempo após o clique no botão.

## Utilização
Para utilizar o código, siga os passos abaixo:

Certifique-se de ter a biblioteca requests instalada. Caso não a tenha, você pode instalá-la usando pip:

```bash
pip install requests

```

- Substitua a chave da API API_KEY e a cidade desejada na variável cidade de acordo com suas preferências.

- Execute o código. A janela será exibida.

- Clique no botão "Clique para vizualizar os dados sobre o clima no RJ" para obter a previsão do tempo.

- A previsão do tempo atualizada para a cidade do Rio de Janeiro será exibida no rótulo dados_finais.

- Lembre-se de que a chave de API utilizada neste exemplo é para fins de demonstração. Em um ambiente de produção, é importante proteger e gerenciar adequadamente suas chaves de API.

- Certifique-se também de estar conectado à internet para que a aplicação possa fazer a requisição à API do OpenWeatherMap com sucesso.

Este é um exemplo simples de como criar uma aplicação que faz uso de APIs e de uma interface gráfica para exibir informações relevantes. Você pode personalizar e expandir esse código para atender às suas necessidades específicas.
