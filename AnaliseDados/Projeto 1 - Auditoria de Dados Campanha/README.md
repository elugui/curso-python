# Projeto 1 - Auditoria de Dados de Campanha

## Objetivo
Comparar os dados da campanha de distribuidores de vinho com os dados brutos e com a configuração da campanha, gerando validações que indiquem se os números apurados estão corretos ou divergentes.

## Estrutura do projeto

```text
projeto_validacao_vinhos/
├── dados/
│   ├── Campanha Distribuidores Vinho.xlsx
│   ├── Configuração Campanha Distribuidores Vinho.xlsx
│   ├── Dados Brutos Fevereiro.csv
│   └── Indicadores.xlsx
├── saida/
├── funcoes/
│   └── funcoes_gerais.py
├── validacoes/
│   └── regras_validacao.py
├── notebooks/
│   └── 01_exploracao_auditoria.ipynb
├── main.py
├── requirements.txt
└── README.md
```

## O que cada parte faz

### `dados/`
É a entrada do projeto. Aqui ficam os arquivos originais que serão lidos pelo código.

### `funcoes/funcoes_gerais.py`
Aqui ficam as funções reutilizáveis do projeto:
- leitura dos arquivos
- tratamento inicial dos dados
- contagem dos resultados das validações
- geração de observação
- exportação para Excel

### `validacoes/regras_validacao.py`
Aqui ficam as regras de negócio da campanha:
- filtro dos dados válidos da base bruta
- validação do volume apurado x volume bruto
- validação da premiação

### `main.py`
É o orquestrador. Ele coordena o fluxo completo:
1. carrega os dados
2. trata a base bruta
3. executa as validações
4. exporta os resultados

### `notebooks/01_exploracao_auditoria.ipynb`
É o ambiente de estudo. Serve para o aluno enxergar o dado, executar etapas aos poucos e entender o que o pipeline está fazendo.

## Fluxo do projeto

1. Ler os arquivos da campanha, configuração e dados brutos
2. Filtrar apenas clientes e produtos válidos para a campanha
3. Filtrar apenas CFOPs aceitos
4. Comparar o volume da apuração com o volume da base bruta
5. Recalcular a premiação
6. Comparar o cálculo com o relatório da campanha
7. Exportar os resultados para um arquivo Excel

## Como executar

No terminal, dentro da pasta do projeto:

```bash
python main.py
```

## Como ensinar isso para o aluno
A lógica que o aluno precisa entender não é “decorar pandas”. É entender a sequência:

- **entrada**: de onde os dados vêm
- **tratamento**: o que precisa ser limpo ou filtrado
- **regra**: o que será comparado
- **resultado**: como saber se está certo ou divergente
- **saída**: onde o relatório final será salvo

Esse projeto já foi separado pensando nisso.
