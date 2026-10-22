import matplotlib.pyplot as plt

def show_occurrences_chart(ranking):
    plt.figure(figsize=(10, 6))

    plt.barh(
        ranking["EventId"],
        ranking["Occurrences"]
    )

    plt.xlabel("Quantidade de ocorrências")
    plt.ylabel("EventId")
    plt.title("Alertas mais recorrentes")

    plt.gca().invert_yaxis()

    plt.tight_layout()
    plt.show()