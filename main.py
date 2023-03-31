import Connect
import Close
import User
import Reactions
import Stargazers
import Watchers
import Releases
import Taggers
import Issues
import Pull_Requests


if __name__ == '__main__':
    userDict = {
        "user_reacted" : "",
        "user_starred" : "",
        "user_is_watching" : "",
        "user_made_releases" : "",
        "user_made_tags" : "",
        "user_is_assignee_issues" : "",
        "user_is_author_issues": "",
        "user_is_editor_issues" : "",
        "user_is_participant_issues" : "",
        "user_is_assignee_PR" : "",
        "user_is_author_PR" : "",
        "user_is_editor_PR" : "",
        "user_is_participant_PR" : "",
        "user_is_author_of_merge_PR" : "",
        "user_is_suggested_reviewer_of_PR" : ""
    }
    print("Input the user ID.")
    id = input()

    connection = Connect.connect()
    user = User.retrieveActors(connection, id)


    if user is not False:
        print("User found!\n")
        userDict.update({"user_reacted" : Reactions.reactedUser(connection, id)})
        userDict.update({"user_starred" : Stargazers.starredUser(connection, id)})
        userDict.update({"user_is_watching" : Watchers.watching(connection, id)})
        userDict.update({"user_made_releases" : Releases.releaseUser(connection, id)})
        userDict.update({"user_made_tags" : Taggers.tagger(connection, id)})

        issuesList = Issues.issues(connection, id)
        userDict.update({"user_is_assignee_issues" : issuesList[0]})
        userDict.update({"user_is_author_issues" : issuesList[1]})
        userDict.update({"user_is_editor_issues" : issuesList[2]})
        userDict.update({"user_is_participant_issues" : issuesList[3]})

        pullRequestsList = Pull_Requests.pullRequests(connection, id)
        userDict.update({"user_is_assignee_PR" : pullRequestsList[0]})
        userDict.update({"user_is_author_PR" : pullRequestsList[1]})
        userDict.update({"user_is_editor_PR" : pullRequestsList[2]})
        userDict.update({"user_is_participant_PR" : pullRequestsList[3]})
        userDict.update({"user_is_author_of_merge_PR" : pullRequestsList[4]})
        userDict.update({"user_is_suggested_reviewer_of_PR" : pullRequestsList[5]})

        #print(userDict)
    else:
        print("User not found!\n")

    Close.closeConnection(connection)
