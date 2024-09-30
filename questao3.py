import json

#função para processar o faturamento
def processar_faturamento(dados_faturamento):

    faturamento_valido = [dia['valor'] for dia in dados_faturamento if dia['valor'] > 0]
    
    menor_valor = min(faturamento_valido)
    maior_valor = max(faturamento_valido)
    
    media_mensal = sum(faturamento_valido) / len(faturamento_valido)
    
    dias_acima_da_media = len([dia['valor'] for dia in dados_faturamento if dia['valor'] > media_mensal])

    return menor_valor, maior_valor, dias_acima_da_media

with open('faturamento.json', 'r') as arquivo_json:
    dados_faturamento = json.load(arquivo_json)

#chama a função para processar os dados
menor, maior, dias_acima_media = processar_faturamento(dados_faturamento)

print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima_media}")