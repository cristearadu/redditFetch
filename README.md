# Reddit API Fetcher

A Python script that authenticates using OAuth and retrieves the latest 5 posts from a given subreddit.

## 🚀 Features
-  Connects to the Reddit API using OAuth (password grant)
-  Fetches 5 latest posts from a specified subreddit
-  Displays each post's title, author, and upvote count
-  Handles errors such as invalid credentials, API issues, and rate limits
-  Uses environment variables (.env) to store credentials securely

---

## 🛠️ Installation

### ⭐ Clone the repository
```sh
git clone https://github.com/yourusername/reddit-fetch.git
cd reddit-fetch
```

### ⚙️ Install dependencies
Ensure you have **Python 3.7+** installed, then run:
```sh
pip install -r requirements.txt
```

### 🛡️ Set up environment variables
Create a `.env` file in the root directory and add your Reddit API credentials:
```ini
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
REDDIT_USERNAME=your_reddit_username
REDDIT_PASSWORD=your_reddit_password
```

---

## 🚀 Running the Script
```sh
python main.py
```
It defaults to `r/romania`.

---

## 👤 Example Output
```
Enter a subreddit name: python

💪 Successfully authenticated as: radu07

Fetching latest 5 posts from r/python...

🔹 **Title:** Python 3.12 Released!
   ✏️  Author: some_redditor
   👍  Upvotes: 420

🔹 **Title:** What's new in PRAW?
   ✏️  Author: another_redditor
   👍  Upvotes: 127
```

---

## 🛠️ Troubleshooting

| Issue                                          | Cause | Solution |
|------------------------------------------------|---------------|-----------|
| `❌ Authentication failed`                      | Incorrect credentials in `.env` | Double-check API keys and username/password |
| `❌ API Error: NNN`                             | Exceeded Reddit rate limit | Wait and try again later |
| `❌ Error: Subreddit not found`                 | Typo or non-existent subreddit | Verify the subreddit name |
| `❌ Network Error`                              | No internet connection | Check connection and retry |
| `❌ Invalid credentials or unauthorized access` | Incorrect Client ID or Secret | Ensure credentials are correct in `.env` |


