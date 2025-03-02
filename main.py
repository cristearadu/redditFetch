import os
import praw
import prawcore.exceptions

from dotenv import load_dotenv

load_dotenv()
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
USER_AGENT = "interview challenge"

# REDDIT_CLIENT_ID = "1"
# REDDIT_CLIENT_SECRET = "1"


def fetch_latest_posts(subreddit_name):
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=USER_AGENT
        )

        assert reddit.user.me(), "❌ Authentication failed: Invalid Client ID or Secret. Please check your credentials."
        print("Successfully authenticated! Fetching latest 5 posts from r/{subreddit_name}...\n")

        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.new(limit=5):
            print(f"🔹 **Title:** {post.title}")
            print(f"   ✏️  Author: {post.author}")
            print(f"   👍  Upvotes: {post.score}\n")

    except praw.exceptions.MissingRequiredAttributeException as e:
        print(f"❌ Required configuration failed. Please check initialization: {e}")

    except prawcore.exceptions.OAuthException:
        print("❌ Authentication failed: Invalid Client ID or Secret. Please check your credentials.")

    except prawcore.exceptions.ResponseException as e:
        print(f"❌ API Error: {e}. Possible rate limit or Reddit API issue.")

    except prawcore.exceptions.NotFound:
        print("❌ Error: Subreddit not found. Please check the subreddit name.")

    except prawcore.exceptions.RequestException:
        print("❌ Network Error: Unable to connect to Reddit API. Check your internet connection.")



if __name__ == "__main__":
    fetch_latest_posts('romania')
