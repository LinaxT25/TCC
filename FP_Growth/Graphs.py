import plotly.express as px
import pandas as pd


def graphs(patterns, rules):
    df = pd.DataFrame({"Activities": patterns.keys(), "Frequency": patterns.values()})
    df.loc[df['Frequency'] < 20, 'Activities'] = 'Minor Activities'

    fig = px.pie(df, values="Frequency", names="Activities", title="Github user activity")
    fig.show()
