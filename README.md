# MLFlow

1. [Setup](#setup)

## Setup

### Pre-reqs

* Python 3 (I specifically use 3.9.12, but should work in other versions)
* Git
* Knowledge about Machine Learning Models

### Setting up your working environment
Este projeto analisa um vídeo para extrair áudio e detectar emoções faciais. Além disso, ele inclui exemplos de arquivos para uso em Jupyter Notebooks ou no Power BI.

## Pré-requisitos
- Certifique-se de que você tem um arquivo de vídeo chamado `entrevista.mp4` dentro da pasta `videos`.
- Para análises com Power BI ou Jupyter Notebook, utilize os arquivos de exemplo na pasta `power-bi`.

### Arquivos para Análise em Power BI ou Jupyter Notebook
- A pasta `power-bi` contém exemplos para análises adicionais:
- Arquivos Power BI (`.pbix`) para você explorar e criar visualizações.
- Arquivos Excel (`.xlsx`) para usar como fonte de dados para análises no Jupyter Notebook ou Power BI.

- Se estiver usando o Power BI, abra os arquivos `.pbix` na pasta `power-bi` para visualizar ou personalizar gráficos e relatórios.
- Se estiver usando Jupyter Notebook, os arquivos Excel podem ser carregados para análise adicional.

### Instruções para Execução do Projeto
1. Coloque o arquivo `entrevista.mp4` na pasta `videos`.
2. Se quiser analisar dados no Power BI ou Jupyter Notebook, use os arquivos na pasta `power-bi`.
3. Execute o script a partir da pasta `src` para a análise de vídeo.

### Problemas Comuns
- Se você encontrar erros de arquivo não encontrado, confirme que o arquivo `entrevista.mp4` está na pasta `videos`.

1. Clone this repo

```console
git clone git@github.com:Dev-Senior-Sciencies/nlp-tutorial.git
```

2. Create a Python venv

    There are many ways to do that. I'll use the simple one, but you can use your preferable.

    Inside of the clonned path run:

```console
python -m venv .env
```

3. Activate venv

> For Linux:
```console
source .env/bin/activate
```

> For Windows:

```console
.env/Scripts/Activate
```



3. Install requirements.txt

```console
pip install -r requirements.txt
```
4. execute o programs

```console
py .\src\nlp.py  
```

5. Dados Tratados no Google Colab
Para visualizar dados tratados em um ambiente Google Colab, use o seguinte link:

```console
https://colab.research.google.com/drive/1lfofBx9eWHcesSGwCA2F46xdmwp37ipg#scrollTo=bRjUmdXm697m
```
