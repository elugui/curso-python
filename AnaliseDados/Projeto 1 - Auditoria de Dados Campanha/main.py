from funcoes.funcoes_gerais import (
    carregar_bases,
    preparar_base_bruta,
    exportar_resultados,
)
from validacoes.regras_validacao import (
    validar_volume_apurado_x_bruto,
    validar_premiacao,
)


def main():
    """
    Orquestra o pipeline completo de auditoria.
    """
    bases = carregar_bases()

    dados_bruto = preparar_base_bruta(
        relatorio_bruto=bases["relatorio_bruto"],
        configuracao_campanha_cliente=bases["configuracao_campanha_cliente"],
        configuracao_campanha_produto=bases["configuracao_campanha_produto"],
    )

    resultado_volume = validar_volume_apurado_x_bruto(
        relatorio_campanha_detalhe=bases["relatorio_campanha_detalhe"],
        dados_bruto=dados_bruto,
    )

    resultado_premiacao = validar_premiacao(
        relatorio_campanha_premiacao=bases["relatorio_campanha_premiacao"],
        relatorio_campanha_detalhe=bases["relatorio_campanha_detalhe"],
    )

    caminho_saida = exportar_resultados(
        {
            "Dados Apuração x Bruto": resultado_volume,
            "Premiação": resultado_premiacao,
        }
    )

    print(f"Arquivo gerado com sucesso em: {caminho_saida}")


if __name__ == "__main__":
    main()
