import csv

CONTRATO = 2000

print("===== GERADOR DE ORÇAMENTO =====")

tipo = input("Tipo do imóvel (apartamento/casa/estudio): ").lower()

if tipo not in ["apartamento", "casa", "estudio"]:
    print("Tipo de imóvel inválido!")
    exit()

valor = 0

# APARTAMENTO
if tipo == "apartamento":
    valor = 700

    quartos = int(input("Quantidade de quartos 1 ou 2: "))

    if quartos < 1 or quartos > 2:
        print("Quantidade de quartos inválida!")
        exit()

    if quartos == 2:
        valor += 200

    garagem = input("Deseja garagem? (s/n): ").lower()

    if garagem == "s":
        valor += 300

    criancas = input("Possui crianças? (s/n): ").lower()

    if criancas == "n":
        valor *= 0.95

# CASA
elif tipo == "casa":
    valor = 900

    quartos = int(input("Quantidade de quartos: "))

    if quartos < 1 or quartos > 2:
        print("Quantidade de quartos inválida!")
        exit()

    if quartos == 2:
        valor += 250

    garagem = input("Deseja garagem? (s/n): ").lower()

    if garagem == "s":
        valor += 300

# ESTUDIO
elif tipo == "estudio":
    valor = 1200

    vagas = int(input("Quantidade de vagas: "))

    if vagas >= 2:
        valor += 250

    if vagas > 2:
        extras = vagas - 2
        valor += extras * 60

# PARCELAMENTO
parcelas = int(input("Quantidade de parcelas do contrato (1 a 5): "))

if parcelas < 1 or parcelas > 5:
    print("Quantidade de parcelas inválida!")
    exit()

valor_parcela = CONTRATO / parcelas

print("\n===== ORÇAMENTO =====")
print(f"Aluguel mensal: R$ {valor:.2f}")
print(f"Contrato: R$ {CONTRATO:.2f}")
print(f"{parcelas} parcelas de R$ {valor_parcela:.2f}")

# GERAR CSV
gerar = input("Deseja gerar arquivo CSV? (s/n): ").lower()

if gerar == "s":

    with open("orcamento.csv", mode="w", newline="", encoding="utf-8") as arquivo:

        escritor = csv.writer(arquivo)

        escritor.writerow([
            "Parcela",
            "Valor Aluguel",
            "Parcela Contrato"
        ])

        for i in range(1, 13):

            contrato_mes = valor_parcela if i <= parcelas else 0

            escritor.writerow([
                i,
                f"R$ {valor:.2f}",
                f"R$ {contrato_mes:.2f}"
            ])

    print("Arquivo orcamento.csv gerado com sucesso!")