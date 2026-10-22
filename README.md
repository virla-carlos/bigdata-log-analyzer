# Big Data Log Analyzer

Aplicação desenvolvida em **Python** para análise de grandes volumes de logs, identificação de padrões recorrentes de alertas e classificação de prioridade com base na frequência das ocorrências.

O projeto foi desenvolvido como parte da disciplina de **Tópicos de Big Data em Python**.

---

## 🎯 Objetivo

Em aplicações que geram grandes volumes de logs, a análise manual pode dificultar a identificação dos erros mais recorrentes e tornar a investigação de incidentes mais demorada.

O **Big Data Log Analyzer** busca auxiliar principalmente equipes de suporte na análise inicial desses registros, permitindo:

- identificar registros classificados como alerta;
- agrupar padrões de erro semelhantes;
- calcular a quantidade de ocorrências;
- classificar os padrões por prioridade;
- gerar um ranking dos alertas encontrados;
- apresentar os resultados por meio de interface gráfica;
- visualizar os dados através de gráficos.

A aplicação **não tem como objetivo diagnosticar automaticamente a causa raiz nem corrigir erros do sistema**.

---

## 🖥️ Funcionalidades atuais

A versão atual da aplicação permite:

- ✅ Leitura do dataset estruturado BGL;
- ✅ Processamento dos dados com Pandas;
- ✅ Separação entre eventos normais e alertas;
- ✅ Agrupamento dos alertas por padrão;
- ✅ Contagem da recorrência dos padrões;
- ✅ Classificação em níveis de prioridade;
- ✅ Ordenação dos alertas por quantidade de ocorrências;
- ✅ Exibição do ranking em uma interface desenvolvida com Tkinter;
- ✅ Gráfico dos alertas mais recorrentes;
- ✅ Gráfico da distribuição dos padrões por prioridade.

---

## 📊 Dataset

O projeto utiliza o **BGL (Blue Gene/L)**, disponibilizado pelo LogHub.

O dataset completo possui aproximadamente:

- **4,7 milhões de registros**
- cerca de **708 MiB**
- registros provenientes de um sistema de supercomputação

Durante o desenvolvimento inicial da aplicação foi utilizado o arquivo:

```text
BGL_2k.log_structured.csv
```

Essa versão contém **2.000 registros estruturados**, permitindo desenvolver e validar inicialmente o fluxo de processamento antes da aplicação sobre volumes maiores.

### Principais campos utilizados

| Campo | Descrição |
|---|---|
| `Label` | Classificação do registro. `-` representa um evento normal e outros valores representam categorias de alerta. |
| `EventId` | Identificador associado a um padrão de log. |
| `EventTemplate` | Estrutura generalizada da mensagem de log. |
| `Level` | Nível de severidade do registro. |
| `Content` | Mensagem original do log. |
| `Node` | Nó ou máquina onde o evento ocorreu. |

> **Importante:** o `EventId` não representa necessariamente um código de erro. Ele funciona como um identificador associado a determinado padrão de mensagem.

---

## 🔎 EventTemplate

Logs podem possuir mensagens semelhantes, mas conter valores variáveis, como identificadores, endereços, portas ou caminhos.

Por exemplo:

```text
socket to 10.0.0.1:5000
socket to 10.0.0.2:6000
```

Um parser pode transformar essas mensagens em um padrão semelhante a:

```text
socket to <*>
```

Esse padrão é representado pelo campo `EventTemplate`.

Na versão atual do projeto, o dataset estruturado utilizado **já fornece `EventId` e `EventTemplate` previamente processados**.

A geração desses padrões diretamente a partir do arquivo bruto do BGL poderá ser incorporada em versões futuras.

---

## 🔄 Fluxo da aplicação

```text
Dataset BGL
    ↓
Leitura com Pandas
    ↓
Filtragem dos registros de alerta
    ↓
Agrupamento por padrão
    ↓
Contagem das ocorrências
    ↓
Cálculo da prioridade
    ↓
Ordenação do ranking
    ↓
Interface Tkinter
    ↓
Tabela + gráficos Matplotlib
```

---

## 🚨 Classificação de prioridade

A prioridade atual é definida utilizando a distribuição da quantidade de ocorrências dos padrões.

São calculados:

```text
Q50 → mediana das ocorrências
Q75 → terceiro quartil
```

A classificação segue a regra:

```text
Ocorrências <= Q50
→ RISCO BAIXO

Ocorrências > Q50 e <= Q75
→ RISCO MÉDIO

Ocorrências > Q75
→ RISCO ALTO
```

No conjunto atual de alertas analisados, todos os registros possuem nível `FATAL`.

Por isso, nesta versão, a classificação consegue diferenciar os padrões principalmente pela **recorrência**.

Em uma evolução futura, datasets com diferentes níveis de severidade poderão permitir combinar:

```text
recorrência + severidade
```

na definição da prioridade.

---

## 📈 Visualizações

A aplicação atualmente possui duas visualizações utilizando **Matplotlib**.

### Alertas mais recorrentes

Gráfico de barras horizontal comparando:

```text
EventId × Quantidade de ocorrências
```

Esse gráfico permite identificar rapidamente quais padrões aparecem com maior frequência.

### Distribuição por prioridade

Gráfico que apresenta a quantidade de padrões classificados como:

```text
RISCO BAIXO
RISCO MÉDIO
RISCO ALTO
```

Ele permite visualizar como os padrões encontrados estão distribuídos entre os níveis de prioridade.

---

## 🏗️ Estrutura do projeto

```text
bigdata-log-analyzer/
│
├── data/
│   └── raw/
│       └── BGL_2k.log_structured.csv
│
├── outputs/
│
├── src/
│   ├── main.py
│   ├── app.py
│   └── charts.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

### Responsabilidade dos arquivos

**`main.py`**

Responsável pelo processamento e análise dos dados:

- leitura do dataset;
- filtragem dos alertas;
- agrupamento;
- cálculo das ocorrências;
- classificação de prioridade;
- geração do ranking.

**`app.py`**

Responsável pela interface gráfica desenvolvida com **Tkinter**.

A interface permite:

- iniciar a análise;
- visualizar o ranking;
- acessar as visualizações gráficas.

**`charts.py`**

Responsável pelas visualizações desenvolvidas com **Matplotlib**.

---

## 🛠️ Tecnologias utilizadas

### Principais

- Python
- Pandas
- Matplotlib
- Tkinter

### Tecnologias previstas para evolução

- NumPy
- SQL
- técnicas de Inteligência Artificial / Machine Learning

---

## 🚀 Como executar

### 1. Clone o repositório

```bash
git clone https://github.com/virla-carlos/bigdata-log-analyzer.git
```

Entre na pasta:

```bash
cd bigdata-log-analyzer
```

---

### 2. Crie um ambiente virtual

No Windows:

```bash
python -m venv .venv
```

---

### 3. Ative o ambiente virtual

No Prompt de Comando:

```bash
.venv\Scripts\activate
```

Caso não queira ou não possa ativar o ambiente virtual, também é possível utilizar diretamente o Python existente dentro dele.

---

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

Ou utilizando diretamente o Python do ambiente virtual:

```bash
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

---

### 5. Adicione o dataset

Por questões de tamanho e organização, os arquivos do dataset não são versionados no Git.

Adicione:

```text
BGL_2k.log_structured.csv
```

dentro de:

```text
data/raw/
```

O caminho esperado será:

```text
data/raw/BGL_2k.log_structured.csv
```

---

### 6. Execute a aplicação

Na raiz do projeto:

```bash
python src/app.py
```

Ou utilizando diretamente o ambiente virtual:

```bash
.\.venv\Scripts\python.exe .\src\app.py
```

---

## 🖥️ Utilizando a aplicação

Após iniciar o programa:

1. Clique em **Analisar Logs**;
2. Aguarde o processamento do dataset;
3. O ranking dos padrões será exibido na tabela;
4. Utilize **Ver gráfico** para visualizar a recorrência dos alertas;
5. Utilize **Ver prioridades** para visualizar a distribuição das prioridades.

---

## 📌 Resultado atual

Nos 2.000 registros utilizados durante o desenvolvimento inicial:

```text
2.000 registros analisados
1.857 eventos normais
143 registros classificados como alerta
```

O padrão mais recorrente identificado no conjunto analisado foi:

```text
EventId: E55
Ocorrências: 59
```

seguido por:

```text
EventId: E52
Ocorrências: 30
```

Esses resultados demonstram como o agrupamento facilita a identificação dos padrões que merecem maior atenção durante a investigação de incidentes.

---

## ⚠️ Limitações da versão atual

A versão atual ainda possui algumas limitações:

- utiliza inicialmente a amostra estruturada BGL de 2.000 registros;
- `EventId` e `EventTemplate` já vêm processados pelo dataset;
- todos os alertas da amostra analisada possuem nível `FATAL`;
- a prioridade atual é baseada principalmente na recorrência;
- não realiza monitoramento em tempo real;
- não realiza diagnóstico automático de causa raiz;
- não executa correções no sistema analisado.

---

## 🗺️ Próximas etapas

Entre as evoluções previstas estão:

- processamento do dataset BGL completo;
- análise dos logs brutos;
- geração automática de templates de eventos;
- novas visualizações;
- análise temporal dos alertas;
- análise por componentes e nós;
- utilização mais ampla de NumPy;
- integração com banco de dados SQL;
- exploração de técnicas de Inteligência Artificial;
- evolução da regra de prioridade utilizando recorrência e severidade;
- melhorias visuais na interface Tkinter.

---

## 📚 Contexto acadêmico

Projeto desenvolvido para a disciplina de **Tópicos de Big Data em Python**, com foco na aplicação prática de técnicas de processamento, análise e visualização de grandes volumes de dados.

O projeto busca também aplicar conceitos próximos a um fluxo real de desenvolvimento de software, incluindo:

- definição de problema;
- Discovery;
- planejamento;
- versionamento com Git;
- organização por responsabilidades;
- desenvolvimento incremental;
- testes;
- documentação.

---

## 📄 Versão atual

```text
v0.1
```

A primeira versão funcional contém o fluxo completo entre:

```text
Dataset
→ Processamento
→ Análise
→ Priorização
→ Interface
→ Visualização
```