from DB import Issues, PullRequests, Reactions, Releases, Stargazers, Taggers, Watchers


def sorting(connection, userid):
    final_data_list = []  # Contains all actions with data of a user inside

    # The format of returns is a tuple(name of action(str), list of tuples with data)
    stargazers = Stargazers.starred_user(connection, userid)  # Return only one data to sort
    releases = Releases.release_user(connection, userid)
    taggers = Taggers.tagger(connection, userid)
    reactions = Reactions.reacted_user(connection, userid)

    # The return is a tuple(name of action(str), boolean)
    watchers = Watchers.watching(connection, userid)

    # For issues and pull request the format of return is unique for being a joined tuples
    issues = Issues.issues(connection, userid)
    pull_requests = PullRequests.pull_requests(connection, userid)

    # Now get all data returned and join them in a list to obtain all actions in same format
    # Only return one data, but to prevent any issues uses same format of the rest
    for tuples in stargazers[1:]:
        if tuples is None:
            final_data_list.append(tuple((str(stargazers[0]), None)))
        else:
            final_data_list.append(tuple((str(stargazers[0]), tuples[0].isoformat())))

    for tuples in releases[1:]:
        if tuples is None:
            final_data_list.append(tuple((releases[0], None)))
        else:
            final_data_list.append(tuple((releases[0], tuples[0].isoformat())))

    # Already have the iso format so convert is not necessary
    for tuples in taggers[1:]:
        if tuples is None:
            final_data_list.append(tuple((taggers[0], None)))
        else:
            final_data_list.append(tuple((taggers[0], tuples[0])))

    for tuples in reactions[1:]:
        if tuples is None:
            final_data_list.append(tuple((reactions[0], None)))
        else:
            final_data_list.append(tuple((reactions[0], tuples[0].isoformat())))

    # Issues
    if issues[3] is None:
        final_data_list.append(tuple((issues[2], None)))
    else:
        for tuples in issues[3]:
            final_data_list.append(tuple((issues[2], tuples.isoformat())))

    if issues[5] is None:
        final_data_list.append(tuple((issues[4], None)))
    else:
        for tuples in issues[5]:
            final_data_list.append(tuple((issues[4], tuples.isoformat())))

    # Pull Requests
    if pull_requests[3] is None:
        final_data_list.append(tuple((pull_requests[2], None)))
    else:
        for tuples in pull_requests[3]:
            final_data_list.append(tuple((pull_requests[2], tuples.isoformat())))

    if pull_requests[5] is None:
        final_data_list.append(tuple((pull_requests[4], None)))
    else:
        for tuples in pull_requests[5]:
            final_data_list.append(tuple((pull_requests[4], tuples.isoformat())))

    if pull_requests[9] is None:
        final_data_list.append(tuple((pull_requests[8], None)))
    else:
        for tuples in pull_requests[9]:
            final_data_list.append(tuple((pull_requests[8], tuples.isoformat())))

    # Sorting the data before insert the bools
    final_data_list.sort(key=lambda x: (x[1] is None, x[1]), reverse=False)

    # Append in the end of list all boolean values
    final_data_list.append(tuple((watchers[0], watchers[1])))
    final_data_list.append(tuple((issues[0], issues[1])))
    final_data_list.append(tuple((issues[6], issues[7])))
    final_data_list.append(tuple((pull_requests[0], pull_requests[1])))
    final_data_list.append(tuple((pull_requests[6], pull_requests[7])))
    final_data_list.append(tuple((pull_requests[10], pull_requests[11])))

    return final_data_list
