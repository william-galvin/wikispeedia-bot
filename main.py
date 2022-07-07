import tweepy
from wikipedia_parser import wikiCrawler as Crawler
from time import sleep

#variables for accessing twitter API
access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
bearer_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

class BotManager():
    """
    The thing that actually runs the twitter bot
    """

    def __init__(self):
        self.id = 1470907073399451650 # always the id for @wikispeedia_bot 
        self.client = tweepy.Client(
            bearer_token = bearer_token, 
            consumer_key = consumer_key, 
            consumer_secret = consumer_secret_key, 
            access_token = access_token, 
            access_token_secret = access_token_secret,
            wait_on_rate_limit = True
        )

    def run(self):
        """
        Currently just looks for mentions and replies.
        Will eventually include more behavior?
        """

        while True:
            try:
                self.mentionsAndReplies()
            except Exception as e:
                pass
            sleep(15)


    def mentionsAndReplies(self):
        """
        Looks for tweets that mention @wikispeedia_bot, replies to them
        """

        mentions = self.client.get_users_mentions(id = self.id)

        if (mentions.data == None):
            return

        for mention in mentions.data:
            likers = self.client.get_liking_users(mention.id)

            if not str(self.id) in str(likers):
                self.client.like(mention.id)

                tweet = self.client.get_tweet(id = mention.id).data
                tweetText = tweet.text.replace("@wikispeedia_bot", "").replace("&gt;", ">")

                crawler = Crawler()
                text = crawler.findPath(tweetText)

                self.client.create_tweet(text = text, in_reply_to_tweet_id = mention.id)

            sleep(15)

    
    def delete_all_tweets(self):
        """Deletes all tweets for @wikispeedia_bot"""

        tweets = self.client.get_users_tweets(id = self.id)
        while tweets.data != None:
            for tweet in tweets[0]:
                self.client.delete_tweet(id = tweet.id)
            tweets = self.client.get_users_tweets(id = self.id)


def main():
    bot = BotManager()
    bot.run()


if __name__ == "__main__":
    main()

    