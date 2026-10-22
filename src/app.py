import tkinter as tk
from tkinter import ttk

import matplotlib.pyplot as plt

from main import generate_analysis
from charts import show_occurrences_chart

root = tk.Tk()

root.title('Big Data Log Analyzer')
root.geometry("1100x600")

def analyze_logs():
    ranking = generate_analysis()

    for item in table.get_children():
        table.delete(item)

    for index, row in ranking.iterrows():
        table.insert(
            "",
            "end",
            values=(
                row["EventId"],
                row["Level"],
                row["EventTemplate"],
                row["Occurrences"],
                row["Priority"]
            )
        )

button = tk.Button(
    root,
    text="Analisar Logs",
    command=analyze_logs
)

button.pack(pady=20)

columns = (
    "EventId",
    "Level",
    "EventTemplate",
    "Occurrences",
    "Priority"
)

table = ttk.Treeview(
    root,
    columns=columns,
    show="headings"
)

for column in columns:
    table.heading(column, text=column)

table.column("EventId", width=80, anchor="center")
table.column("Level", width=80, anchor="center")
table.column("EventTemplate", width=500)
table.column("Occurrences", width=100, anchor="center")
table.column("Priority", width=120, anchor="center")

table.pack(
    fill="both",
    expand=True,
    padx=20,
    pady=20
)

def show_chart():
    ranking = generate_analysis()
    show_occurrences_chart(ranking)

chart_button = tk.Button(
    root,
    text="Ver gráfico",
    command=show_chart
)

chart_button.pack(pady=10)

root.mainloop()