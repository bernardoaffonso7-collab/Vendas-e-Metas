import pandas as pd

df = pd.read_excel('Vendas_empresas.xlsx')

#Mostra todas as colunas
pd.set_option('display.max_columns', None)

#Mostra todas as linhas
pd.set_option('display.max_rows', None)

Qualitativas = df[["Nome", "Cargo","Departamento","Meta_Alcancada"]]

QuantitativasDiscretas = df[["ID_Funcionario", "Idade", "Vendas_Mes", "Idade", "Data_Admissao","Salario", "Horas_Extras"]]

QuantitativaContinua = df[[]]
# Sumo_vendas_Meta_Alcancada = df[df["Meta_Alcancada"] == "Sim"]["Vendas_Mes"].sum()

# Media_Vendas_meta_Alcancada = df[(df["Meta_Alcancada"]] == "Sim") & (df["Salario"]>5000)]["Vendas_Mes"].sum()

Media_Vendas_meta_Alcancada = df[(df["Meta_Alcancada"] == "Sim") & (df["Salario"] > 5000)]["Vendas_Mes"].sum()

Funcionarios_Meta_Alcancada = df[df["Meta_Alcancada"]] == "Sim"["Nome"]


print(df)
# print(Sumo_vendas_Meta_Alcancada)
print(Media_Vendas_meta_Alcancada)

# print(Qualitativas)
# print(QuantitativasDiscretas)
# print(QuantitativaContinua)