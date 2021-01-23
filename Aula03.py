import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

fonte = "https://github.com/alura-cursos/imersao-dados-2-2020/blob/master/MICRODADOS_ENEM_2019_SAMPLE_43278.csv?raw=true"

dados = pd.read_csv(fonte)

provas = [
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_MT",
    "NU_NOTA_LC",
    "NU_NOTA_REDACAO",
]

notas_totais_participantes = dados[provas].sum(axis=1)
dados["NU_NOTA_TOTAL"] = notas_totais_participantes
dados_sem_notas_zero = dados.query("NU_NOTA_TOTAL != 0")

provas_e_total = [
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_MT",
    "NU_NOTA_LC",
    "NU_NOTA_REDACAO",
    "NU_NOTA_TOTAL",
]

# ======| Ploting mean, median and mode lines |======

# mean = dados_sem_notas_zero["NU_NOTA_TOTAL"].mean()
# median = dados_sem_notas_zero["NU_NOTA_TOTAL"].median()
# mode = dados_sem_notas_zero["NU_NOTA_TOTAL"].mode().values[0]

# sns.histplot(dados_sem_notas_zero, x="NU_NOTA_TOTAL")

# plt.axvline(mean, color="r", linestyle="--")
# plt.axvline(median, color="g", linestyle="-")
# plt.axvline(mode, color="b", linestyle="-")

# plt.legend({"Mean": mean, "Median": median, "Mode": mode})

# plt.show()

# ======| Comparing using 'hue' |======

# sns.histplot(
#     dados_sem_notas_zero,
#     x="NU_NOTA_TOTAL",
#     kde=True,
#     hue="Q025",
#     stat="density",
#     cumulative=True,
# )

# plt.show()

# ======| Scatterplot graphic |======

# plt.figure(figsize=(10, 10))
# sns.scatterplot(
#     data=dados_sem_notas_zero,
#     x="NU_NOTA_LC",
#     y="NU_NOTA_CH",
# )
# plt.xlim((-50, 1050))
# plt.ylim((-50, 1050))

# plt.show()

# ======| Pairplot graphic |======

# sns.pairplot(
#     data=dados_sem_notas_zero[provas_e_total],
# )

# plt.show()

# ======| Correlattion and heatmap |======

correlacao = dados_sem_notas_zero[provas_e_total].corr()

mask = np.zeros_like(correlacao)

mask[np.triu_indices_from(mask)] = True

sns.heatmap(correlacao, cmap="Blues", center=0, annot=True, square=True, mask=mask)

plt.show()