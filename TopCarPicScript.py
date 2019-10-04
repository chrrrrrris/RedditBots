#required libraries
import praw
import urllib.request
import datetime
#PR - 2
#gets the date in order to add it to the submission
todayDate = datetime.date.today()
user_agent = ("Top Daily Car Pic 1.2 by /u/CodeTestAccount")
#change log: updated subreddits and url generation
r = praw.Reddit(user_agent=user_agent)

r.login(*accountnamehere*, *passwordhere*)

#takes the top submission from a number of car related subreddits
submissions = r.get_subreddit('miata+RX7+mustang+subaru').get_top(limit=1)
submission = next(submissions)
saveUrl = submission.url
print("Submitting picture")
r.submit('TopCarPic', todayDate, url=saveUrl)
submissions2 = r.get_subreddit('TopCarPic').get_new(limit=1)
submission2 = next(submissions2)
#Adds the source to the post
print("Adding source to post")
#Adds a comment that constructs the source by making a new string out of the various
#parts needed
submission2.add_comment('Source: ' + "www.reddit.com/r/"+str(submission.subreddit)+"/comments/"+submission.id+"/")
print("Finished")
