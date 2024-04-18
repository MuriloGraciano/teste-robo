import re
from datetime import datetime

def formataData(texto):
    padroes = {
        r'\b\d{2}/\d{2}/\d{4}\b': '%d/%m/%Y',   # dd/mm/yyyy
        r'\b\d{2}/\d{2}/\d{2}\b': '%d/%m/%y',   # dd/mm/yy
        r'\b\d{2}/\d{4}\b': '%m/%Y',            # mm/yyyy
        r'\b\d{4}-\d{2}-\d{2}\b': '%Y-%m-%d',   # yyyy-mm-dd
        r'\b\d{4}-\d{2}\b': '%Y-%m'             # yyyy-mm
    }
    
    for regex, date_format in padroes.items():
        match = re.search(regex, texto)
        if match:
            datetime_obj = datetime.strptime(match.group(), date_format)
            return datetime_obj.date()

def formataValor(texto):
    texto = str(texto)
    numero = texto.replace(',', '.')

    contadorDePonto = numero.count('.')
    if contadorDePonto > 1:
        parteDecimal = numero[numero.rfind('.') + 1:]
        parteInteira = numero[:numero.rfind('.')]
        parteInteira = parteInteira.replace('.', '')
        numero = parteInteira + '.' + parteDecimal

    return numero

def removeEspacos(texto):
    texto = re.sub('\s', '', texto)
    return texto

def normalizaCampos(dataframe):
    
    arquivo = dataframe['arquivo'][0]
    unidade = dataframe['unidade'][0]
    mesRef = formataData(dataframe['mesRef'][0])
    dadosFiscais = dataframe['dadosFiscais'][0]
    itensFatura = dataframe['itensFatura'][0]
    dadosEndereco = dataframe['dadosEndereco'][0]
    contaContrato = dataframe['contaContrato'][0]
    codigoDeBarras = dataframe['codigoDeBarras'][0]
    medidor = dataframe['medidor'][0]
    leituraAnterior = formataValor(dataframe['leituraAnterior'][0])
    leituraAtual = formataValor(dataframe['leituraAtual'][0])
    constante = formataValor(dataframe['constante'][0])
    consumoFaturado = formataValor(dataframe['consumoFaturado'][0])
    totalFatura = formataValor(dataframe['totalFatura'][0])
    tributos1 = formataValor(dataframe['tributos1'][0])
    tributos2 = formataValor(dataframe['tributos2'][0])
    tributos3 = formataValor(dataframe['tributos3'][0])
    tipoFornecimento = dataframe['tipoFornecimento'][0]
    dataLeituraAnterior = formataData(dataframe['dataLeituraAnterior'][0])
    dataLeituraAtual = formataData(dataframe['dataLeituraAtual'][0])
    diasFatura = dataframe['diasFatura'][0]
    proximaLeitura = formataData(dataframe['proximaLeitura'][0])
    dataVencimento = formataData(dataframe['dataVencimento'][0])

    return {
        'arquivo': arquivo,
        'unidade': unidade,
        'mesRef': mesRef,
        'dadosFiscais': dadosFiscais,
        'itensFatura': itensFatura,
        'dadosEndereco': dadosEndereco,
        'contaContrato': contaContrato,
        'codigoDeBarras': codigoDeBarras,
        'medidor': medidor,
        'leituraAnterior': leituraAnterior,
        'leituraAtual': leituraAtual,
        'constante': constante,
        'consumoFaturado': consumoFaturado,
        'totalFatura': totalFatura,
        'tributos1': tributos1,
        'tributos2': tributos2,
        'tributos3': tributos3,
        'tipoFornecimento': tipoFornecimento,
        'dataLeituraAnterior': dataLeituraAnterior,
        'dataLeituraAtual': dataLeituraAtual,
        'diasFatura': diasFatura,
        'proximaLeitura': proximaLeitura,
        'dataVencimento': dataVencimento
    }