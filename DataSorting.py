import Reactions
import Stargazers
import Watchers
import Releases
import Taggers
import Issues
import PullRequests
def sorting(connection, userid):

    # Possible optimization: Search if some function only can return one data then sorting is not necessary
    stargazers = Stargazers.starredUser(connection, userid)  # Return data to sort
    releases = Releases.releaseUser(connection, userid)  # Return data to sort
    taggers = Taggers.tagger(connection, userid)  # Return data to sort
    reactions = Reactions.reactedUser(connection, userid)  # Return data to sort

    watchers = Watchers.watching(connection, userid)  # Only return true or false

    issues = Issues.issues(connection, userid)  # Diverse tuple return
    pullRequests = PullRequests.pullRequests(connection, userid)  # Diverse tuple return

    # Splitting the unordered tuple in str and data, then sorting the data and joining again
    stargazers =  tuple((stargazers[0], None if stargazers[1] is None else sorted(stargazers[1])))
    releases = tuple((releases[0], None if releases[1] is None else sorted(releases[1])))
    taggers = tuple((taggers[0], None if taggers[1] is None else sorted(taggers[1])))
    reactions = tuple((reactions[0], None if reactions[1] is None else sorted(reactions[1])))

    # For the giant tuples in issues and pull request, split then in minor tuples
    assigneeIssues = tuple((issues[0], issues[1]))
    authorIssue = tuple((issues[2], None if issues[3] is None else sorted(issues[3])))
    editorIssue = tuple((issues[4], None if issues[5] is None else sorted(issues[5])))
    participantIssue = tuple((issues[6], issues[7]))

    assigneePullRequest = tuple((pullRequests[0], pullRequests[1]))
    authorPullRequest = tuple((pullRequests[2], None if pullRequests[3] is None else sorted(pullRequests[3])))
    editorPullRequest = tuple((pullRequests[4], None if pullRequests[5] is None else sorted(pullRequests[5])))
    participantPullRequest = tuple((pullRequests[6], pullRequests[7]))
    mergedPullRequest = tuple((pullRequests[8], None if pullRequests[9] is None else sorted(pullRequests[9])))
    suggestedReviewerPullRequest = tuple((pullRequests[10], pullRequests[11]))

    finalTuple = tuple((
        stargazers, releases, taggers, reactions, watchers, assigneeIssues, authorIssue, editorIssue, participantIssue,
        assigneePullRequest, authorPullRequest, editorPullRequest, participantPullRequest, mergedPullRequest,
        suggestedReviewerPullRequest ))

    print(finalTuple)



