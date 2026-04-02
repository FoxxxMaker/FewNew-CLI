# FewNew CLI

Um projeto simples em **Python** para gerar ideias de atividades aleatórias no terminal, usando uma API externa e tradução automática para português.

## Sobre o projeto

O **FewNew CLI** foi criado como um projeto de prática para consumir uma API com Python, organizar o código em módulos e exibir o resultado em uma interface de linha de comando.

Atualmente, o programa:

* busca uma atividade aleatória pela API Bored
* traduz o texto do inglês para o português
* mostra a sugestão no terminal
* pergunta se o usuário deseja continuar

## Tecnologias utilizadas

* **Python**
* **requests**
* **translate**
* **CLI / Terminal**

## Estrutura do projeto

```text
FewNew CLI/
├── Main.py
├── Request.py
├── Tradutor.py
└── .env/
```

### Arquivos principais

* **Main.py**: controla o menu e a interação com o usuário no terminal
* **Request.py**: faz a requisição para a API e retorna uma atividade aleatória
* **Tradutor.py**: traduz o texto retornado para português

## Como funciona

1. O programa inicia no terminal.
2. O usuário pressiona **Enter** para receber uma sugestão.
3. O sistema busca uma atividade aleatória na API.
4. A atividade é traduzida para português.
5. O resultado é exibido na tela.

## Exemplo de uso

```bash
Iniciando Programa....
Olá! Bem-vindo ao FewNew!

Pressione a tecla ENTER para receber uma ideia nova ou digite sair para sair
```

Exemplo de saída:

```bash
Saiba mais sobre a Proporção Áurea
```

## Instalação

Clone o repositório:

```bash
git clone https://github.com/FoxxxMaker/FewNew-CLI.git
```

Entre na pasta do projeto:

```bash
cd FewNew-CLI
```

Crie um ambiente virtual:

```bash
python -m venv .env
```

Ative o ambiente virtual.

No **Windows (PowerShell)**:

```powershell
.\.env\Scripts\Activate
```

Instale as dependências:

```bash
pip install requests translate
```

Execute o projeto:

```bash
python Main.py
```

## Dependências

Este projeto usa as seguintes bibliotecas externas:

* `requests`
* `translate`

## Objetivo de aprendizado

Este projeto foi desenvolvido com foco em praticar:

* requisições para API em Python
* organização de código em módulos
* manipulação de strings
* interação com usuário no terminal
* tradução automática de texto

## Melhorias futuras

Algumas melhorias que podem ser adicionadas no futuro:

* melhorar a lógica do menu principal
* tratar erros de conexão com a API
* evitar repetições de código
* adicionar arquivo `requirements.txt`
* adicionar `Dockerfile`
* melhorar mensagens e validações do CLI
* permitir filtros de atividades

## Observações

O projeto está em evolução e faz parte do processo de aprendizado. A proposta é manter o código cada vez mais organizado, funcional e pronto para novas melhorias.

## Repositório

Repositório do projeto:

`https://github.com/FoxxxMaker/FewNew-CLI.git`

---

Feito com carinho para praticar Python, APIs e organização de projetos em CLI. 🐾
