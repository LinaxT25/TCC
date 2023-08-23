import plotly.express as px
import plotly.graph_objects as go
import pandas as pd


def graph_pattern(patterns, frequency):
    # Patterns graph
    df = pd.DataFrame({"Activities": patterns.keys(), "Frequency": patterns.values()})
    df.loc[df["Frequency"] < frequency * 3, 'Activities'] = 'Minor Activities'

    fig = px.pie(df, values="Frequency", names="Activities", title="Github user activity")
    fig.show()


def graph_rule(rules):
    # Rules graph
    activity_chance = []
    probability = []
    rules_values = rules.values()

    for x in rules_values:
        activity_chance.append(x[0])
        probability.append(x[1])

    df = pd.DataFrame({"Activities": rules.keys(), "Activity_chance": activity_chance, "Probability": probability})
    fig = px.scatter(df, x="Probability", hover_data="Activity_chance", color="Activities", size="Probability")
    fig.show()
