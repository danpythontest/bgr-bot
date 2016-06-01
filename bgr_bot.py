import praw
import os
import smtplib



r = praw.Reddit(user_agent = "BGR Notifier")
r.login("bgr_bot","watson", disable_warning=True)
server = smtplib.SMTP("smtp.gmail.com",587)
server.starttls()
server.login('danpythontest@gmail.com','password69!')

if not os.path.isfile("old_posts.txt"):
    old_posts = []
else:
    with open("old_posts.txt","r") as f:
        old_posts = f.read()
        old_posts = old_posts.split("\n")
        old_posts = filter(None,old_posts)
        old_posts = list(old_posts)

        
def find_new():
    subreddit = r.get_subreddit('bgr')
    for submission in subreddit.get_hot(limit=25):
        if submission.id not in old_posts:
            old_posts.append(submission.id)
            server.sendmail("danpythontest@gmail.com",["4016448858@vtext.com","4016490455@vtext.com","4019351574@txt.att.net"],"You've been visited by the spooky BGR Bot! Updoot in 4.20 seconds or lose all your calcium")
    with open("old_posts.txt","w") as f:
        for post_id in old_posts:
            f.write(post_id + "\n")

find_new()
