import Reactions
import Stargazers
import Watchers
import Releases
import Taggers
import Issues
import PullRequests
def sorting(connection, userid):

    finalDataList = [] # Contains all actions with data of a user inside

    # The format of returns is a tuple(name of action(str), list of tuples with data)
    stargazers = Stargazers.starredUser(connection, userid)  # Return only one data to sort
    releases = Releases.releaseUser(connection, userid)
    taggers = Taggers.tagger(connection, userid)
    reactions = Reactions.reactedUser(connection, userid)

    # The return is a tuple(name of action(str), boolean)
    watchers = Watchers.watching(connection, userid)

    # For issues and pull request the format of return is unique for being a joined tuples
    issues = Issues.issues(connection, userid)
    pullRequests = PullRequests.pullRequests(connection, userid)

    # Now get all data returned and join them in a list to obtain all actions in same format
    # Only return one data, but to prevent any issues uses same format of the rest
    for tuples in stargazers[1:]:
        if tuples is None:
            finalDataList.append(tuple((stargazers[0], None)))
        else:
            finalDataList.append(tuple((stargazers[0], tuples[0].isoformat())))

    for tuples in releases[1:]:
        if tuples is None:
            finalDataList.append(tuple((releases[0], None)))
        else:
            finalDataList.append(tuple((releases[0], tuples[0].isoformat())))

    # Already have the iso format so convert is not necessary
    for tuples in taggers[1:]:
        if tuples is None:
            finalDataList.append(tuple((taggers[0], None)))
        else:
            finalDataList.append(tuple((taggers[0], tuples[0])))

    for tuples in reactions[1:]:
        if tuples is None:
            finalDataList.append(tuple((reactions[0], None)))
        else:
            finalDataList.append(tuple((reactions[0], tuples[0].isoformat())))

    # Issues
    if issues[3] is None:
        finalDataList.append(tuple((issues[2], None)))
    else:
        for tuples in issues[3]:
            finalDataList.append(tuple((issues[2], tuples.isoformat())))

    if issues[5] is None:
        finalDataList.append(tuple((issues[4], None)))
    else:
        for tuples in issues[5]:
            finalDataList.append(tuple((issues[4], tuples.isoformat())))

    # Pull Requests
    if pullRequests[3] is None:
        finalDataList.append(tuple((pullRequests[2], None)))
    else:
        for tuples in pullRequests[3]:
            finalDataList.append(tuple((pullRequests[2], tuples.isoformat())))

    if pullRequests[5] is None:
        finalDataList.append(tuple((pullRequests[4], None)))
    else:
        for tuples in pullRequests[5]:
            finalDataList.append(tuple((pullRequests[4], tuples.isoformat())))

    if pullRequests[9] is None:
        finalDataList.append(tuple((pullRequests[8], None)))
    else:
        for tuples in pullRequests[9]:
            finalDataList.append(tuple((pullRequests[8], tuples.isoformat())))

    # Sorting the data before insert the bools
    finalDataList.sort(key=lambda x: (x[1] is None, x[1]), reverse=False)

    # Append in the end of list all boolean values
    finalDataList.append(tuple((watchers[0], watchers[1])))
    finalDataList.append(tuple((issues[0], issues[1])))
    finalDataList.append(tuple((issues[6], issues[7])))
    finalDataList.append(tuple((pullRequests[0], pullRequests[1])))
    finalDataList.append(tuple((pullRequests[6], pullRequests[7])))
    finalDataList.append(tuple((pullRequests[10], pullRequests[11])))

    return finalDataList



