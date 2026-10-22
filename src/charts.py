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

def show_priority_chart(ranking):
    priority_count = ranking["Priority"].value_counts()

    plt.figure(figsize=(8, 5))
    
    plt.bar(
        priority_count.index,
        priority_count.values
    )

    plt.xlabel("Prioridade")
    plt.ylabel("Quantidade de padrões")
    plt.title("Distribuição dos alertas por prioridade")

    plt.tight_layout()
    plt.show()