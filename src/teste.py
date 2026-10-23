import pandas as pd

pd.set_option("display.max_rows", None) #? Máximo de linhas
# pd.set_option("display.max.columns", None) #? Máximo de colunas

bgl = pd.read_csv("./data/raw/BGL_2k.log_structured.csv")

def alert_components():
    
    alert = bgl.loc[
        (bgl["Label"] != "-"),
        ["Component"]
    ]

    alert = (
        alert.groupby(
            [
                "Component"
            ]
        )
        .size()
        .reset_index(name="Occurrences")
        .sort_values(by="Occurrences",ascending=False)
    )

    alert = alert.reset_index(drop=True)
    
    print(alert)

alert_components()