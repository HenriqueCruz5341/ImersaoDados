import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVR
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error

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
dados_sem_notas_zero = dados_sem_notas_zero[provas].dropna()

provas_e_total = [
    "NU_NOTA_CN",
    "NU_NOTA_CH",
    "NU_NOTA_MT",
    "NU_NOTA_LC",
    "NU_NOTA_REDACAO",
    "NU_NOTA_TOTAL",
]

# ======| Introducing to machine learning |======
provas_entra = ["NU_NOTA_CH", "NU_NOTA_LC", "NU_NOTA_CN", "NU_NOTA_REDACAO"]
provas_saida = "NU_NOTA_MT"

notas_entra = dados_sem_notas_zero[provas_entra]
notas_saida = dados_sem_notas_zero[provas_saida]

x = notas_entra
y = notas_saida

SEED = 4321

x_treino, x_teste, y_treino, y_teste = train_test_split(
    x, y, test_size=0.25, random_state=SEED
)

modelo = LinearSVR(random_state=SEED)
modelo.fit(x_treino, y_treino)

predicoes_matematica = modelo.predict(x_teste)

# ======| Comparing results graphically |======

# sns.scatterplot(x=predicoes_matematica, y=y_teste)
# plt.xlim((-50, 1050))
# plt.ylim((-50, 1050))

# plt.show()

# ======| Other analyzes |======

# resultados = pd.DataFrame()
# resultados["Real"] = y_teste
# resultados["Previsao"] = predicoes_matematica
# resultados["Diferenca"] = resultados["Real"] - resultados["Previsao"]
# resultados["Quadrado_Diferenca"] = (resultados["Real"] - resultados["Previsao"]) ** 2

# media_erro = resultados["Quadrado_Diferenca"].mean() ** (1 / 2)

# print(media_erro)

# ======| Using DummyRegressor |======

modelo_dummy = DummyRegressor()
modelo_dummy.fit(x_treino, y_treino)
dummy_predicoes = modelo_dummy.predict(y_teste)

media_erro = mean_squared_error(y_teste, dummy_predicoes)

print(media_erro)