from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd


def obter_caminhos() -> Dict[str, Path]:
    """
    Retorna os caminhos padrão de entrada e saída do projeto.

    A ideia é centralizar os caminhos em um único lugar para evitar
    strings espalhadas pelo código.
    """
    pasta_raiz = Path(__file__).resolve().parent.parent
    pasta_dados = pasta_raiz / "dados"
    pasta_saida = pasta_raiz / "saida"

    return {
        "campanha": pasta_dados / "Campanha Distribuidores Vinho.xlsx",
        "configuracao": pasta_dados / "Configuração Campanha Distribuidores Vinho.xlsx",
        "bruto": pasta_dados / "Dados Brutos Fevereiro.csv",
        "indicadores": pasta_dados / "Indicadores.xlsx",
        "saida": pasta_saida / "Indicadores.xlsx",
    }


def carregar_bases() -> Dict[str, pd.DataFrame]:
    """
    Lê todos os arquivos necessários para a auditoria.

    Retorna um dicionário com os DataFrames já carregados.
    """
    caminhos = obter_caminhos()

    return {
        "relatorio_campanha_premiacao": pd.read_excel(
            caminhos["campanha"],
            sheet_name="Premiação Distribuidores",
        ),
        "relatorio_campanha_detalhe": pd.read_excel(
            caminhos["campanha"],
            sheet_name="Detalhamento Mês Apurado",
        ),
        "configuracao_campanha_cliente": pd.read_excel(
            caminhos["configuracao"],
            sheet_name="Cliente",
        ),
        "configuracao_campanha_produto": pd.read_excel(
            caminhos["configuracao"],
            sheet_name="Produto",
        ),
        "relatorio_bruto": pd.read_csv(
            caminhos["bruto"],
            sep=";",
        ),
    }


def preparar_base_bruta(
    relatorio_bruto: pd.DataFrame,
    configuracao_campanha_cliente: pd.DataFrame,
    configuracao_campanha_produto: pd.DataFrame,
) -> pd.DataFrame:
    """
    Prepara a base bruta para comparação com a campanha.

    Etapas:
    1. mantém apenas clientes da configuração
    2. mantém apenas produtos da configuração
    3. filtra apenas CFOPs válidos para a regra
    4. renomeia a coluna de volume para deixar claro que vem do bruto
    """
    cfops_validos = [5102, 5106, 5110, 6102, 6106, 6110, 5160, 6160, 6910, 5910]

    dados_bruto = pd.merge(
        relatorio_bruto,
        configuracao_campanha_cliente[["CODIGOCLIENTE"]],
        how="inner",
        on="CODIGOCLIENTE",
    )

    dados_bruto = pd.merge(
        dados_bruto,
        configuracao_campanha_produto[["CODIGOPRODUTO"]],
        how="inner",
        on="CODIGOPRODUTO",
    )

    dados_bruto = dados_bruto[dados_bruto["CFOP"].isin(cfops_validos)].copy()
    dados_bruto = dados_bruto.rename(columns={"VOLUME": "VOLUME BRUTO"})

    return dados_bruto


def contagem_validacao(validacao: pd.DataFrame) -> Tuple[int, int]:
    """
    Conta quantos registros estão corretos e quantos estão divergentes.
    """
    contagem = validacao["Validação"].value_counts()
    valores_corretos = ["Correto", "Ok", "OK", "TRUE"]
    qtde_correta = contagem.loc[contagem.index.isin(valores_corretos)].sum()
    qtde_divergente = len(validacao) - qtde_correta

    return int(qtde_correta), int(qtde_divergente)


def observacao_validacao(
    validacao: pd.DataFrame,
    qtde_correto: int,
    qtde_divergente: int,
) -> pd.DataFrame:
    """
    Adiciona uma observação no primeiro registro do DataFrame
    resumindo o resultado da validação.
    """
    resultado = validacao.copy()
    resultado.loc[0, "Observação"] = (
        f"Existem {qtde_correto} corretos e {qtde_divergente} divergentes"
    )
    return resultado


def validar_multiplas_regras(
    dataframe: pd.DataFrame,
    regras,
    separador: str = " | ",
):
    """
    Aplica múltiplas regras vetorizadas e devolve uma coluna de status.

    Se nenhuma regra falhar, devolve 'Correto'.
    Se uma ou mais regras falharem, devolve a descrição das divergências.
    """
    mensagens = np.full(len(dataframe), "", dtype=object)

    for mascara, texto in regras:
        mensagens = np.where(
            mascara,
            np.where(mensagens == "", texto, mensagens + separador + texto),
            mensagens,
        )

    return np.where(mensagens == "", "Correto", mensagens)


def exportar_resultados(resultados: Dict[str, pd.DataFrame]) -> Path:
    """
    Exporta todas as validações para um único arquivo Excel.
    """
    caminhos = obter_caminhos()
    caminho_saida = caminhos["saida"]
    caminho_saida.parent.mkdir(parents=True, exist_ok=True)

    with pd.ExcelWriter(caminho_saida, engine="xlsxwriter") as writer:
        for nome_aba, dataframe in resultados.items():
            dataframe.to_excel(writer, sheet_name=nome_aba, index=False)

    return caminho_saida
