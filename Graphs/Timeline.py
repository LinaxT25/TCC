import plotly.graph_objects as go
import plotly_express as px
import pandas as pd
import psycopg2

from DB import Connect


def timeline():
    activity_data = []  # Global list to store all activities made by users

    try:
        connection = Connect.connect()
        cursor = connection.cursor()

        # Get all activities
        query = 'SELECT activity, activity_date from "dv8fromtheworld/jda".standard;'
        cursor.execute(query)
        activity_data.append(cursor.fetchall())

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

    # Convert the tuples to DataFrame
    for i in range(len(activity_data)):
        main_table = pd.DataFrame(activity_data[i], columns=['Activity', 'Date'])

    # Sorting activities by date
    main_table.sort_values(by=['Date'], inplace=True)

    # Creating a table for each activity to put in graphic
    authorpr_table = main_table[main_table['Activity'] == "AuthorPullRequest"]
    authorpr_table.insert(0, "Sum", range(1, 1 + len(authorpr_table)))

    starred_table = main_table[main_table['Activity'] == "Starred"]
    starred_table.insert(0, "Sum", range(1, 1 + len(starred_table)))

    releases_table = main_table[main_table['Activity'] == "Releases"]
    releases_table.insert(0, "Sum", range(1, 1 + len(releases_table)))

    editorpr_table = main_table[main_table['Activity'] == "EditorPullRequest"]
    editorpr_table.insert(0, "Sum", range(1, 1 + len(editorpr_table)))

    reactions_table = main_table[main_table['Activity'] == "Reaction"]
    reactions_table.insert(0, "Sum", range(1, 1 + len(reactions_table)))

    taggers_table = main_table[main_table['Activity'] == "Taggers"]
    taggers_table.insert(0, "Sum", range(1, 1 + len(taggers_table)))

    merged_table = main_table[main_table['Activity'] == "Merged"]
    merged_table.insert(0, "Sum", range(1, 1 + len(merged_table)))

    authorissue_table = main_table[main_table['Activity'] == "AuthorIssue"]
    authorissue_table.insert(0, "Sum", range(1, 1 + len(authorissue_table)))

    editorissue_table = main_table[main_table['Activity'] == "EditorIssue"]
    editorissue_table.insert(0, "Sum", range(1, 1 + len(editorissue_table)))

    # Creating a trace for each activity in graph
    trace1 = go.Scatter(x=authorpr_table['Date'],
                        y=authorpr_table['Sum'],
                        mode='lines',
                        zorder=1,
                        name="AuthorPullRequest",
                        line=dict(width=3)
                        )

    trace2 = go.Scatter(x=starred_table['Date'],
                        y=starred_table['Sum'],
                        mode='lines',
                        zorder=2,
                        name="Starred",
                        line=dict(width=3)
                        )

    trace3 = go.Scatter(x=releases_table['Date'],
                        y=releases_table['Sum'],
                        mode='lines',
                        zorder=3,
                        name="Releases",
                        line=dict(width=3)
                        )

    trace4 = go.Scatter(x=editorpr_table['Date'],
                        y=editorpr_table['Sum'],
                        mode='lines',
                        zorder=4,
                        name="EditorPullRequest",
                        line=dict(width=3)
                        )

    trace5 = go.Scatter(x=reactions_table['Date'],
                        y=reactions_table['Sum'],
                        mode='lines',
                        zorder=5,
                        name="Reactions",
                        line=dict(width=3)
                        )

    trace6 = go.Scatter(x=taggers_table['Date'],
                        y=taggers_table['Sum'],
                        mode='lines',
                        zorder=6,
                        name="Taggers",
                        line=dict(width=3)
                        )

    trace7 = go.Scatter(x=merged_table['Date'],
                        y=merged_table['Sum'],
                        mode='lines',
                        zorder=7,
                        name="Merged",
                        line=dict(width=3)
                        )

    trace8 = go.Scatter(x=authorissue_table['Date'],
                        y=authorissue_table['Sum'],
                        mode='lines',
                        zorder=8,
                        name="AuthorIssue",
                        line=dict(width=3)
                        )

    trace9 = go.Scatter(x=editorissue_table['Date'],
                        y=editorissue_table['Sum'],
                        mode='lines',
                        zorder=9,
                        name="EditorIssue",
                        line=dict(width=3)
                        )

    layout = go.Layout(title="Linha do Tempo das Atividades")

    fig = go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9], layout=layout)
    fig.show()

