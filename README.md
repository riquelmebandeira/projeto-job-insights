# Projeto Jobs Insight

# Contexto
O Jobs Insight é uma simples aplicação Web que provê informações sobre empregos.

Nele pude dar meus primeiros passos na linguagem Python, tendo como base a interface feita com Flask pela Trybe. 

Implementei uma série de funções que filtram os dados que estão armazenados localmente e são exibidos na rota '/jobs'. Além de testes para algumas funções já implementadas no projeto base.

Por fim, pude eu mesmo implementar uma rota que exibe os detalhes de um determinado emprego, me baseando no código existente.

![Preview da aplicação](preview.gif)

## Tecnologias usadas

* Python
* Pytest
* Flask
* Docker

## Instalando o projeto

1. Clone o repositório:

```
git clone git@github.com:riquelmebandeira/projeto-job-insights.git
```

2. Entre na pasta do repositório clonado e instale as dependências:

```
cd projeto-job-insights
```

3. Crie um ambiente virtual:

```
python3 -m venv .venv && source .venv/bin/activate
```

4. Instale as dependências no ambiente virtual:
```
python3 -m pip install -r dev-requirements.txt
```

5. Rode a aplicação! ela ficará acessível em http://localhost:5000.
```
flask run
```

## Executando com o Docker

* Para rodar a aplicação, integrada pelo docker compose, utilize o comando:

```
docker-compose up
```

Após isso, a aplicação pode ser acessada em http://localhost:5000

## Executando os testes

Para executar os testes certifique-se de que você está com o ambiente virtual ativado e execute:
```
python3 -m pytest
```