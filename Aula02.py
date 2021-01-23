import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def grafico_boxplot_renda(coluna, dados, titulo):
    renda_ordenada = dados["Q006"].unique()
    renda_ordenada.sort()
    sns.boxplot(
        x="Q006", y=coluna, data=dados, order=renda_ordenada, hue="IN_TREINEIRO"
    )
    plt.title(titulo)

    plt.show()


fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

dados = pd.read_csv(fonte)

proporcao_idade = dados.query("NU_IDADE <= 14")["SG_UF_RESIDENCIA"].value_counts(
    normalize=True
)

# ======| Multiple graphs |======

# alunos_menor_quatorze = dados.query("NU_IDADE <= 14")
# graf_pizza = alunos_menor_quatorze["SG_UF_RESIDENCIA"].value_counts()

# fig, axes = plt.subplots(ncols=2)

# fig.suptitle("Alunos menor de quatorze anos por estado")
# graf_pizza.plot.pie(ax=axes[0])
# graf_pizza.plot.bar(ax=axes[1])

# plt.show()

# ======| Working with Seaborn |======

# renda_ordenada = dados["Q006"].unique()
# renda_ordenada.sort()
# sns.boxplot(x="Q006", y="NU_NOTA_MT", data=dados, order=renda_ordenada)
# plt.title("Boxplot das notas de matemática pela renda")

# plt.show()

# ======| Sum all tests |======

provas = [
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_MT",
    "NU_NOTA_LC",
    "NU_NOTA_REDACAO",
]

notas_totais_participantes = dados[provas].sum(axis=1)
dados["NU_NOTA_TOTAL"] = notas_totais_participantes

# grafico_boxplot_renda(
#     coluna="NU_NOTA_TOTAL", dados=dados, titulo="Boxplot das notas totais pela renda"
# )

# ======| Filter at least 1 test |======

dados_sem_notas_zero = dados.query("NU_NOTA_TOTAL != 0")

grafico_boxplot_renda(
    coluna="NU_NOTA_TOTAL",
    dados=dados_sem_notas_zero,
    titulo="Boxplot das notas totais pela renda",
)
