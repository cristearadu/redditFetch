import os
import praw
import prawcore.exceptions
from dotenv import load_dotenv


load_dotenv()
REDDIT_CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')
REDDIT_USERNAME = os.getenv('REDDIT_USERNAME')
REDDIT_PASSWORD = os.getenv('REDDIT_PASSWORD')
USER_AGENT = f"MyRedditBot/1.0 by {REDDIT_USERNAME}"


def fetch_latest_posts(subreddit_name):
    try:
        reddit = praw.Reddit(
            client_id=REDDIT_CLIENT_ID,
            client_secret=REDDIT_CLIENT_SECRET,
            user_agent=USER_AGENT,
            username=REDDIT_USERNAME,
            password=REDDIT_PASSWORD
        )

        user = reddit.user.me()
        if not user:
            raise Exception("❌ Authentication failed: Invalid credentials.")
        print(f"\n✅ Successfully authenticated as: {user}\n")

        print(f"\nFetching latest 5 posts from r/{subreddit_name}...\n")
        subreddit = reddit.subreddit(subreddit_name)
        for post in subreddit.new(limit=5):
            print(f"🔹 **Title:** {post.title}")
            print("{:>3}{:<10} {}".format("", "✏️  Author:", post.author))
            print("{:>3}{:<10} {}".format("", "👍  Upvotes:", post.score))

    except praw.exceptions.MissingRequiredAttributeException as e:
        print(f"❌ Required configuration failed. Please check initialization: {e}")

    except prawcore.exceptions.OAuthException:
        print("❌ Authentication failed: Invalid Client ID, Secret, Username, or Password.")

    except prawcore.exceptions.ResponseException as e:
        if e.response.status_code == 404:
            print("❌ Error: Subreddit not found. Please check the subreddit name.")
        elif e.response.status_code == 401:
            print("❌ Error: Invalid credentials or unauthorized access.")
        else:
            print(f"❌ API Error: {e}. Possible rate limit or Reddit API issue.")

    except prawcore.exceptions.RequestException:
        print("❌ Network Error: Unable to connect to Reddit API. Check your internet connection.")

    except Exception as e:
        print(f"❌ Unexpected/Unhandled Error: {e}")


if __name__ == "__main__":
    fetch_latest_posts('romania')
