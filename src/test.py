import pandas as pd
from main import alert_events 

bgl = pd.read_csv("./data/raw/BGL_2k.log_structured.csv")

# bgl.info()

def functionAlertTest():
    alert = bgl.loc[
        (bgl["Label"] != "-") & (bgl["EventId"] == "E55"), 
        ["EventId", "Content", "LineId", "Level"]
    ]

    alert.drop_duplicates()

    
    print(alert)

functionAlertTest()
# alert_events()