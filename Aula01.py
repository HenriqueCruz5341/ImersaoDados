import pandas as pd
import matplotlib.pyplot as plt

fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

dados = pd.read_csv(fonte)

# ======| Basics |======
# qtd_inscritos = len(dados)

# head = dados.head()

# column_names = dados.columns.values

# ufs = dados["SG_UF_RESIDENCIA"]
# ufs_unique = ufs.unique()

# qtd_alun_ufs = ufs.value_counts()

# ======| Ploting a graph |======
# qtd_alun_idade = dados["NU_IDADE"].value_counts().sort_index()

# hist_idade = dados["NU_IDADE"].hist(bins=30)

# plt.suptitle("Quantidade de pessoas por idade")
# plt.ylabel("Quantidade")
# plt.xlabel("Idades")
# plt.show()

# ======| Querys |======
# query_idade_treineiro = dados.query("IN_TREINEIRO == 1")["NU_IDADE"]
# query_n_idade_treinieiro = dados.query("IN_TREINEIRO != 1")["NU_IDADE"]

# mais_treineiros_idade = (
#     dados.query("IN_TREINEIRO == 1")["NU_IDADE"].value_counts().sort_index()
# )


# hist_idade = dados["NU_IDADE"].hist(bins=30)
# hist_query_i_t = dados.query("IN_TREINEIRO == 1")["NU_IDADE"].hist(bins=30)

# plt.suptitle("Quantidade de pessoas por idade")
# plt.ylabel("Quantidade")
# plt.xlabel("Idades")
# plt.show()

# ======| Statistics |======
nota_redacao = dados["NU_NOTA_REDACAO"]

media_redacao = nota_redacao.mean()
desvio_redacao = nota_redacao.std()

print(f"Media: {media_redacao:.3f}.")
print(f"Desvio Padrao: {desvio_redacao:.3f}.")

provas = [
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_MT",
    "NU_NOTA_LC",
    "NU_NOTA_REDACAO",
]

describe = dados[provas].describe()

dados[provas].plot.box(grid=True)
plt.show()

print(describe)
