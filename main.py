import pandas as pd
import os, shutil
from funcoes import formataData, formataValor, normalizaCampos

def main():
    diretorioBase = os.path.abspath('.')
    criaDiretoriosEssenciais(diretorioBase)
    diretorioCsv = os.path.join(diretorioBase, 'faturasCsv')
    arquivosCsv = [arq for arq in os.listdir(diretorioCsv) if arq.endswith('.csv')]

    dataframe = {}
    for arquivo in arquivosCsv:
        caminhoCompleto = os.path.join(diretorioCsv, arquivo)
        nomeArquivo = arquivo.replace('.csv', '')

        dataframe = pd.read_csv(caminhoCompleto, sep=',', encoding="ISO-8859-1")
        
        dataframe = normalizaCampos(dataframe)

        dataframe = pd.json_normalize(dataframe)
        print(dataframe)

        dataframe.to_json(
            f'{diretorioBase}/faturasJson/{nomeArquivo}.json', orient='records', 
            lines=False, 
            force_ascii=False,
            indent=4
        )

def criaDiretoriosEssenciais(diretorioBase):
    diretoriosEssenciais = [
        'faturas',
        'faturasCsv',
        'faturasJson'
    ]

    for diretorio in diretoriosEssenciais:
        os.makedirs(f'{diretorioBase}/{diretorio}', exist_ok=True)

if __name__ == "__main__":
    main()