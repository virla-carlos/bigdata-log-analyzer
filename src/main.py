import pandas as pd

#! Registros das primeiras cinco linhas
# bgl.head(5)
#! Quantidade de linhas e colunas
# print(bgl.shape)
#! Nome das colunas
# print(bgl.columns)
#! Informações do dataset
# bgl.info()
#! Colunas linhas que possuem valor
# print(bgl.isna())
#? Exibe todas as linhas de um dataframe
pd.set_option("display.max_rows", None)

bgl = pd.read_csv("./data/raw/BGL_2k.log_structured.csv")  


def normal_events():

    noAlert = bgl.loc[
        bgl["Label"] == "-",
        ["Label", "EventId", "EventTemplate", "Level"]
    ].copy()

    eventIdNoAlert = noAlert["EventId"].value_counts()
    print(eventIdNoAlert)

def alert_events():
    alert = bgl.loc[
        bgl["Label"] != "-",
        ["Label", "EventId"]
    ]

    print(alert.value_counts())
    
# alert_events()

if __name__ == "__main__":
    normal_events()
    alert_events()