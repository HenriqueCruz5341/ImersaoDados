import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import LinearSVR
from sklearn.dummy import DummyRegressor
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold


def calcula_mse(resultados):
    media = resultados["test_score"].mean()
    desvio_padrao = resultados["test_score"].std()
    lim_inferior = media - (2 * desvio_padrao)
    lim_superior = media + (2 * desvio_padrao)

    print(f"Media: {media:.3f}.")
    print(f"Desvio Padrao: {desvio_padrao:.3f}.")
    print(f"Limite Inf: {lim_inferior:.3f}.")
    print(f"Limite Sup: {lim_superior:.3f}.")
    print(f"Intervalo Confiança: {lim_inferior:.3f} - {lim_superior:.3f}.")


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


# ======| Decision Tree Regressor |======

# modelo_arvore = DecisionTreeRegressor(max_depth=3)
# modelo_arvore.fit(x_treino, y_treino)
# predicoes_matematica_arvore = modelo_arvore.predict(x_teste)

# print(mean_squared_error(y_teste, predicoes_matematica_arvore))

# ======| Using Cross Validate and understand Overfit|======


def regressor_arvore(nivel):
    SEED = 1232
    np.random.seed(SEED)

    partes = KFold(n_splits=10, shuffle=True)

    modelo_arvore = DecisionTreeRegressor(max_depth=nivel)
    resultados = cross_validate(
        modelo_arvore,
        x,
        y,
        cv=partes,
        scoring="neg_mean_squared_error",
        return_train_score=True,
    )
    resultados["test_score"] = resultados["test_score"] * -1

    print(
        f"Treino = {(resultados['train_score']*-1).mean():.3f} | Teste = {resultados['test_score'].mean():.3f}"
    )


for i in range(1, 21):
    regressor_arvore(i)

# calcula_mse(resultados)
