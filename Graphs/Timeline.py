import plotly.graph_objects as go
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

    reactions_table = main_table[main_table['Activity'] == "Reactions"]
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

    layout = go.Layout(xaxis=dict(title='Data'), yaxis=dict(title='Soma das Atividades'),
                       title="Linha do Tempo das Atividades")

    fig = go.Figure(data=[trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8, trace9], layout=layout)
    fig.show()


def timeline_user(userid):
    activity_data = []  # Global list to store all activities made by users

    try:
        connection = Connect.connect()
        cursor = connection.cursor()

        # Get all activities
        query = 'SELECT activity, activity_date from "dv8fromtheworld/jda".standard WHERE "user_id" = %s;'
        cursor.execute(query, (userid,))
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

    reactions_table = main_table[main_table['Activity'] == "Reactions"]
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
    # fig0 = go.Figure(data=go.Scatter(
    #     x=starred_table['Date'],
    #     y=starred_table['Sum'],
    #     mode="markers",
    #     marker=dict(size=15, color="BlueViolet")
    # ))
    # fig0.show()

    # fig1 = go.Figure(data=go.Scatter(
    #         x=authorpr_table['Date'],
    #         y=authorpr_table['Sum'],
    #         mode='lines',
    #         name="AuthorPullRequest",
    # ), layout=go.Layout(
    #     title="AuthorPullRequest", xaxis=dict(title='Data'), yaxis=dict(title='Soma das Atividades')))
    # fig1.show()

    # fig2 = go.Figure(data=go.Scatter(
    #     x=editorpr_table['Date'],
    #     y=editorpr_table['Sum'],
    #     mode='lines',
    #     name="EditorPullRequest",
    #     line=dict(width=3, color='Orangered')
    # ), layout=go.Layout(
    #     title="EditorPullRequest", xaxis=dict(title='Data'), yaxis=dict(title='Soma das Atividades')))
    # fig2.show()

    # fig3 = go.Figure(data=go.Scatter(
    #     x=merged_table['Date'],
    #     y=merged_table['Sum'],
    #     mode='lines',
    #     name="Merged",
    #     line=dict(width=3, color="lime")
    # ), layout=go.Layout(
    #     title="Merged", xaxis=dict(title='Data'), yaxis=dict(title='Soma das Atividades')))
    # fig3.show()

    # fig4 = go.Figure(data=go.Scatter(
    #     x=reactions_table['Date'],
    #     y=reactions_table['Sum'],
    #     mode='lines',
    #     name="Reactions",
    #     line=dict(width=3, color="Gold")
    # ), layout=go.Layout(
    #     title="Reactions", xaxis=dict(title='Data'), yaxis=dict(title='Soma das Atividades')))
    # fig4.show()

    # fig5 = go.Figure(data=go.Scatter(
    #     x=authorissue_table['Date'],
    #     y=authorissue_table['Sum'],
    #     mode='lines',
    #     name="AuthorIssue",
    #     line=dict(width=3, color="Darkcyan")
    # ), layout=go.Layout(
    #     title="AuthorIssue", xaxis=dict(title='Data'), yaxis=dict(title='Soma das Atividades')))
    # fig5.show()

    # fig6 = go.Figure(data=go.Scatter(
    #     x=editorissue_table['Date'],
    #     y=editorissue_table['Sum'],
    #     mode='lines',
    #     name="EditorIssue",
    #     line=dict(width=3, color="Dodgerblue")
    #     ), layout=go.Layout(
    #     title="EditorIssue", xaxis=dict(title='Data'), yaxis=dict(title='Soma das Atividades')))
    # fig6.show()

    # fig7 = go.Figure(data=go.Scatter(
    #     x=releases_table['Date'],
    #     y=releases_table['Sum'],
    #     mode='lines',
    #     name="Releases",
    #     line=dict(width=3, color="Fuchsia")
    # ), layout=go.Layout(
    #     title="Releases", xaxis=dict(title='Data'), yaxis=dict(title='Soma das Atividades')))
    # fig7.show()

    fig8 = go.Figure(data=go.Scatter(
        x=taggers_table['Date'],
        y=taggers_table['Sum'],
        mode='lines',
        name="Taggers",
        line=dict(width=3, color="Deeppink")
    ), layout=go.Layout(
        title="Taggers", xaxis=dict(title='Data'), yaxis=dict(title='Soma das Atividades')))
    fig8.show()

