# Crawler de Exploração HTTP

Este projeto consiste em um crawler desenvolvido em Python utilizando a biblioteca padrão `socket` para comunicação HTTP de baixo nível e `BeautifulSoup` para a extração de links. O objetivo é mapear as páginas de um ambiente de laboratório local.

## Pré-requisitos e Instalação

Siga os passos abaixo para extrair o projeto, configurar o ambiente virtual e instalar as dependências necessárias.

### 1. Criar e Ativar o Ambiente Virtual (`.venv`)
O uso de um ambiente virtual isola as dependências do projeto:

```bash
python3 -m venv .venv

```

Ative o ambiente de acordo com o seu sistema operacional:

* **Linux/macOS:**
```bash
source .venv/bin/activate
```

```
* **Windows (Prompt de Comando):**
  ```cmd
  .venv\Scripts\activate.bat
```

### 2. Instalar as Dependências (`requirements.txt`)

Com o ambiente virtual ativo, instale os pacotes necessários:

```bash
pip install -r requirements.txt

```

### 4. Inicializar o Servidor (Imagem Docker)

O crawler realiza as requisições contra um ambiente de laboratório que roda localmente. Certifique-se de que o Docker está ativo em sua máquina e execute o contêiner na porta `8080`:

```bash
docker run -p 80:80 robertovrf/http-crawler-lab:latest
```

---

## Como Executar o Projeto

Após ativar o `.venv` e garantir que o contêiner Docker está em execução, inicie o script principal do crawler:

```bash
python main.py
```

### Arquivos de Saída Gerados

Ao finalizar a execução, o script criará automaticamente dois arquivos na raiz do projeto:

1. `relatorio.txt`: Lista detalhada contendo cada URL acessada, o código de status retornado pelo servidor e a descrição do seu significado.
2. `grafo.md`: Mapa visual de conexões entre as páginas gerado automaticamente utilizando a sintaxe do **Mermaid**.
