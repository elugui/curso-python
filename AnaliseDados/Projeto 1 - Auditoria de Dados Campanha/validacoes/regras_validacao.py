import numpy as np
import pandas as pd

from funcoes.funcoes_gerais import (
    contagem_validacao,
    observacao_validacao,
    validar_multiplas_regras,
)

PERCENTUAL_CRESCIMENTO_PREMIACAO = [
    {"min": 0.20, "max": float("inf"), "percentual": 0.10},
    {"min": 0.15, "max": 0.1999, "percentual": 0.08},
    {"min": 0.10, "max": 0.1499, "percentual": 0.06},
    {"min": 0.05, "max": 0.0999, "percentual": 0.03},
    {"min": 0.00, "max": 0.0499, "percentual": 0.00},
]


def percentual_premiacao_crescimento(crescimento: float) -> float:
    """
    Converte o percentual de crescimento em percentual de premiação.
    """
    if pd.isna(crescimento):
        return 0.0

    for faixa in PERCENTUAL_CRESCIMENTO_PREMIACAO:
        if faixa["min"] <= crescimento <= faixa["max"]:
            return faixa["percentual"]

    return 0.0


def validar_volume_apurado_x_bruto(
    relatorio_campanha_detalhe: pd.DataFrame,
    dados_bruto: pd.DataFrame,
) -> pd.DataFrame:
    """
    Compara o volume da apuração com o volume da base bruta.

    Regra:
    - se VOLUME != VOLUME BRUTO, o registro é divergente
    - caso contrário, está correto
    """
    validacao = pd.merge(
        relatorio_campanha_detalhe,
        dados_bruto[["CODIGOCLIENTE", "CODIGODOCUMENTO", "CODIGOPRODUTO", "VOLUME BRUTO"]],
        how="inner",
        on=["CODIGOCLIENTE", "CODIGODOCUMENTO", "CODIGOPRODUTO"],
    )

    validacao["Validação"] = np.where(
        validacao["VOLUME"] != validacao["VOLUME BRUTO"],
        "Divergente",
        "Correto",
    )

    qtde_correto, qtde_divergente = contagem_validacao(validacao)
    return observacao_validacao(validacao, qtde_correto, qtde_divergente)


def validar_premiacao(
    relatorio_campanha_premiacao: pd.DataFrame,
    relatorio_campanha_detalhe: pd.DataFrame,
) -> pd.DataFrame:
    """
    Recalcula a premiação e compara com o relatório da campanha.

    Conceito para o aluno:
    1. agrupar a campanha por cliente e produto
    2. recalcular crescimento
    3. descobrir o percentual de premiação correto
    4. recalcular o valor da premiação
    5. comparar cálculo x relatório
    """
    campanha_detalhe = (
        relatorio_campanha_detalhe.groupby(["CODIGOCLIENTE", "CODIGOPRODUTO"])["VOLUME"]
        .sum()
        .reset_index()
    )

    validacao = pd.merge(
        relatorio_campanha_premiacao,
        campanha_detalhe,
        how="left",
        on=["CODIGOCLIENTE", "CODIGOPRODUTO"],
    )

    validacao["% Crescimento Calculado"] = (
        validacao["VOLUMEREALIZADO"] / validacao["METAVOLUMEVENDA"] - 1
    )

    validacao["% Premiação Calculado"] = validacao["% Crescimento Calculado"].apply(
        percentual_premiacao_crescimento
    )

    validacao["Valor Premiação Calculado"] = (
        validacao["VALORVENDAPREMIACAO"] * validacao["% Premiação Calculado"]
    )

    validacao["Validação"] = validar_multiplas_regras(
        validacao,
        regras=[
            (
                validacao["% Premiação Calculado"] != validacao["PORCENTAGEMPREMIACAO"],
                "Percentual Premiação divergente do cálculo",
            ),
            (
                validacao["VALORPREMIACAO"] != validacao["Valor Premiação Calculado"],
                "Valor Premiação divergente do cálculo",
            ),
        ],
    )

    qtde_correto, qtde_divergente = contagem_validacao(validacao)
    return observacao_validacao(validacao, qtde_correto, qtde_divergente)
