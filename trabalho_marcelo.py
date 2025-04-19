# Primeiro ele pergunta quanto você quer investir e por quanto tempo (em dias). Bem direto.
investimento = float(input("Quanto você quer investir? "))
tempo_investimento = int(input("Quantos dias você quer deixar investindo? "))

# Aqui ele define a taxa diária do investimento. Pegamos o 14,15% e dividimos por 365 (total de dias em um ano).
taxa_diaria = 0.000388

# E aqui é calculado quanto o cliente vai ganhar "bruto", sem descontar nada ainda.
rendimento_bruto = investimento * taxa_diaria * tempo_investimento

# Essa tabela a seguir é o IOF (Imposto sobre Operações Financeiras). Ele muda conforme os dias.
# Quanto menos tempo o dinheiro fica aplicado, mais imposto o cliente paga. Até 30 dias tem desconto, depois disso é isento.
# Usamos o modelo dicionário para melhor organizar os dados.
tabela_iof = {
    1: 96, 2: 93, 3: 90, 4: 86, 5: 83,
    6: 80, 7: 76, 8: 73, 9: 70, 10: 66,
    11: 63, 12: 60, 13: 56, 14: 53, 15: 50,
    16: 46, 17: 43, 18: 40, 19: 36, 20: 33,
    21: 30, 22: 26, 23: 23, 24: 20, 25: 16,
    26: 13, 27: 10, 28: 6, 29: 3, 30: 0
}

# Aqui ele verifica se o tempo de investimento tá dentro dos 30 dias, e aplica o IOF correspondente da tabela.
# Se passou de 30 dias, IOF é zerado.
if 1 <= tempo_investimento <= 30:
    iof = tabela_iof[tempo_investimento]
else:
    iof = 0

# Calcula o valor do IOF com base na porcentagem, tira esse valor do rendimento bruto.
valor_iof = rendimento_bruto * (iof / 100)
apos_iof = rendimento_bruto - valor_iof

# Agora entra o IR (Imposto de Renda), que depende do tempo também:
# quanto mais tempo deixar aplicado, menos imposto o cliente paga. Tem essa regrinha de faixas.
if tempo_investimento <= 180:
    ir = 22.5
elif tempo_investimento <= 360:
    ir = 20
elif tempo_investimento <= 720:
    ir = 17.5
else:
    ir = 15

# Calcula o IR em cima do valor que já tinha descontado o IOF.
valor_ir = apos_iof * (ir / 100)

# Agora sim, esse é o que sobrou de verdade no bolso: o rendimento líquido.
rendimento_liquido = apos_iof - valor_ir

# Soma o valor que o cliente investiu com o rendimento líquido e mostra o total no final.
valor_final = investimento + rendimento_liquido
print(f"Valor liquido final: R$ {valor_final:.2f}")