import pandas as pd

#? Exibe todas as linhas de um dataframe
# pd.set_option("display.max_rows", None)

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
        (bgl["Label"] != "-"),
        [
            "EventId", 
            "Level", 
            "EventTemplate"
        ]
    ]

    alert = (
        alert.groupby([
            "EventId",
            "Level",
            "EventTemplate",
        ])
        .size()
        .reset_index(name="Occurrences")
    )
    
    return alert

alert_data = alert_events()

def calc_limit(alert_data):

    q50 = alert_data["Occurrences"].quantile(0.50)
    q75 = alert_data["Occurrences"].quantile(0.75)
    
    return q50, q75

q50, q75 = calc_limit(alert_data)

def define_priority(occurrences, q50, q75):

    if occurrences <= q50:
        return "RISCO BAIXO"
    elif occurrences  <= q75:
        return "RISCO MÉDIO"
    else:
        return "RISCO ALTO"

def apply_priority(alert_data, q50, q75):
    alert_data["Priority"] = alert_data["Occurrences"].apply(
        lambda occurrence: define_priority(occurrence, q50, q75)
    )

    return alert_data

alert_data = apply_priority(alert_data, q50, q75)

print(alert_data)