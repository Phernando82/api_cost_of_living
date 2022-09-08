## Título 

<h1 align="center"> Unofficial Numbeo API </h1>

## Índice 

* [Título](#título)
* [Índice](#índice)
* [Descrição do Projeto](#descrição-do-projeto)
* [Status do Projeto](#status-do-projeto)
* [Funcionalidades do Projeto](#funcionalidades-do-projeto)
* [Acesso ao Projeto](#acesso-ao-projeto)
* [Tecnologias utilizadas](#tecnologias-utilizadas)
* [Pessoas Desenvolvedoras do Projeto](#pessoas-desenvolvedoras-do-projeto)

## Descrição do Projeto

API não oficial Numbeo para acessar informações do custo de vida nas cidades disponíveis nesta página

## Status do Projeto
![Badge em Desenvolvimento](http://img.shields.io/static/v1?label=STATUS&message=EM%20DESENVOLVIMENTO&color=GREEN&style=for-the-badge)

## Funcionalidades do Projeto

- `Web Scraping`: varre as informações de custos da cidade pesquisada
- `Armazenamento`: salva as informações em banco de dados
- `Flask API`: disponibiliza as informações em arquivo JSON

## Acesso ao Projeto

- `Github`: faça um fork do projeto
- `Dependências`: instale as dependências do arquivo requirements.txt
- `Banco de dados`: execute o script db_script.py para gerar o banco de dados
- `Varrer a página`: set o valor da variável city e execute o comando scrapy crawl numbeo
- `API em serviço`: execute o arquivo api_numbeo.py para deixar em serviço 
- `Autorização`: por meio da URL padrão primeiro gere o token url_padrão/login e set a variável x-access-token
- `Obter dados`: por meio da URL padrão primeiro selecione o endpoint: /city e então o verbo http GET

## Tecnologias utilizadas


  <img align="center" alt="Fer-Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">- `Python`
  
  <img align="center" alt="Fer-Pyc" height="30" width="40"   src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pycharm/pycharm-original.svg" /> - `Pycharm`
  
  <img align="center" alt="Fer-Her" height="30" width="40"   src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/heroku/heroku-original.svg" /> - `Heroku` 
  
  <img align="center" alt="Fer-Flas" height="30" width="40"  src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/flask/flask-original.svg" /> - `Flask`
  
  <img align="center" alt="Fer-Vsc" height="30" width="40"   src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original-wordmark.svg" /> - `VS Code`
  
  <img align="center" alt="Fer-Sql" height="30" width="40"   src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/sqlite/sqlite-original.svg" /> - `SQLite`

## Pessoas desenvolvedoras do Projeto
[<img src="https://github.com/Phernando82.png?size=460" width=115><br><sub>Phernando82</sub>](https://https://github.com/Phernando82) 
##
![Github Issues:](https://img.shields.io/github/issues/Phernando82/api_cost_of_living)
![Github Forks:](https://img.shields.io/github/forks/Phernando82/api_cost_of_living)
![GitHub Org's stars](https://img.shields.io/github/stars/Phernando82/api_cost_of_living)
![Github License:](https://img.shields.io/github/license/Phernando82/api_cost_of_living)

