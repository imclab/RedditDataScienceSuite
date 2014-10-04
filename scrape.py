import praw


r = praw.Reddit(user_agent='my_cool_application')
submissions = r.get_subreddit('fitness').get_hot(limit=1000)
throwaway = next(submissions)

for sub in submissions:
	try:
		print u'time={time}\ttext="{text}"'.format(time=sub.created, text=sub.selftext.replace('"',''))
		
	except:
		pass


