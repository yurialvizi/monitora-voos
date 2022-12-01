# MonitoraVoos

O seguinte projeto diz respeito ao desenvolvimento de um sistema de monitoramento de voos de aviões.

## Grupo 6

Nome      | NUSP
--------- | ------
Dênio Araujo de Almeida   | 10309013
Vinícius Barros Alvarenga | 11257564
Yuri de Sene Alvizi       | 11260398

### Pré-requisitos

* Python 3.6+

## Passo a passo da instalação

1. Abra um terminal powershell (instruções para Windows).

2. Clone o repositório do grupo. No terminal, digite o comando:

```
  git clone https://github.com/vinibalvarenga/MonitoraVoos.git
```

3. Crie um ambiente virtual chamado **env** usando:

```
  python -m venv env
```

4. Ative o ambiente usando o comando:

```
  .\env\scripts\Activate.ps1
```

5. De acordo com o seu diretório, vá até a pasta **MonitoraVoos**:

```
  cd MonitoraVoos
```

6. Instale as dependências:

```
pip install -r requirements.txt
```

### Executar o projeto

1. Ainda no mesmo terminal, volte para a pasta raiz:

```
  cd ..
```

2. Escreva o seguinte comando para a realização dos testes:

```
  python manage.py test
```

3. Agora digite o comando para rodar o projeto:

```
  python manage.py runserver
```

4. Abra um navegador web e abra a seguinte página: <http://127.0.0.1:8000/>.

### Mapeamento O-R

O projeto do monitoramento dos voos se baseia no seguinte mapeamento:

![Mapeamento O-R](/docs/img/ModeloOR.png "Mapeamento O-R")

### Modelo de Interface

As telas do projeto seguem o seguinte esquema:

![Modelo de Interface](/docs/img/ModeloDeInterface.png "Modelo de Interface")

#### Login

Atenção! É permitido que o usuário erre até três vezes o login. Se não, após essas tentativas ele deve esperar por três minutos para fazer novas tentativas.