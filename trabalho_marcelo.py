investimento = float(input("Quanto você quer investir? "))
tempo_investimento = int(input("Quantos dias você quer deixar investindo? "))

taxa_diaria = 0.000388
rendimento_bruto = investimento * taxa_diaria * tempo_investimento

tabela_iof = {
    1: 96, 2: 93, 3: 90, 4: 86, 5: 83,
    6: 80, 7: 76, 8: 73, 9: 70, 10: 66,
    11: 63, 12: 60, 13: 56, 14: 53, 15: 50,
    16: 46, 17: 43, 18: 40, 19: 36, 20: 33,
    21: 30, 22: 26, 23: 23, 24: 20, 25: 16,
    26: 13, 27: 10, 28: 6, 29: 3, 30: 0
}

if 1 <= tempo_investimento <= 30:
    iof = tabela_iof[tempo_investimento]
else:
    iof = 0
    
valor_iof = rendimento_bruto * (iof / 100)
apos_iof = rendimento_bruto - valor_iof

if tempo_investimento <= 180:
    ir = 22.5
elif tempo_investimento <= 360:
    ir = 20
elif tempo_investimento <= 720:
    ir = 17.5
else:
    ir = 15

valor_ir = apos_iof * (ir / 100)
rendimento_liquido = apos_iof - valor_ir

valor_final = investimento + rendimento_liquido
print(f"Valor liquido final: R$ {valor_final:.2f}")