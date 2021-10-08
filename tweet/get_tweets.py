from datetime import timedelta
import pandas as pd
import tweepy
import random

class Tweets:
	def __init__(self, api):
		self.api = api
		
	def get_search(self, environment_name, q, start_date, end_date):

		query = f"{q}"

		tweets = self.api.search_full_archive(
			environment_name,
			query = query,
			fromDate = start_date,
			toDate = end_date,
			maxResults = 500
		)

		df = pd.DataFrame(
			columns=[
				"tweet_id",
				"tweet_full_text",
				"tweet_favorite_count",
				"tweet_created_at",
			]
		)

		for tweet in tweets:
			df = df.append(
				{
					"tweet_id": tweet.id,
					"tweet_full_text": tweet.text,
					"tweet_favorite_count": tweet.favorite_count,
					"tweet_created_at": tweet.created_at + timedelta(hours=+9),
				},
				
				ignore_index=True,
			)
			
		return df

	def implement(self, month, end_day):
		for day in range(1, int(end_day)+1):
			time = random.randrange(0, 23, 1)

			if 0<= time <= 9:
				s_time = '0' + str(time)
			else:
				s_time = str(time)

			if 1<= day <= 9:
				s_day = '0' + str(day)
			else:
				s_day = str(day)

			search = self.get_search('takakidev', q='就活', start_date=f"2021{month}{s_day}{s_time}00", end_date=f"2021{month}{s_day}2359")
			search.to_csv(f'data/tweets_data_{month}_{s_day}.csv')