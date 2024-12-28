import feedparser
import requests

# arXivのRSSフィードURL
RSS_FEED_URL = "https://export.arxiv.org/rss/nucl-th"

# Discord Webhook URL (GitHub Actionsのシークレットで設定する)
DISCORD_WEBHOOK_URL = None

def fetch_latest_post():
    """arXivのRSSフィードから最新の投稿を取得"""
    feed = feedparser.parse(RSS_FEED_URL)
    if feed.entries:
        return feed.entries[0]
    return None

def send_notification(post):
    """Discordに通知を送信"""
    if DISCORD_WEBHOOK_URL is None:
        print("Webhook URLが設定されていません。")
        return

    content = f"**New arXiv Post**\n**Title:** {post.title}\n**Link:** {post.link}\n**Abstract:** {post.summary}"
    response = requests.post(DISCORD_WEBHOOK_URL, json={"content": content})
    
    if response.status_code == 204:
        print("Notification sent successfully.")
    else:
        print(f"Failed to send notification: {response.status_code}")

def main():
    post = fetch_latest_post()
    if post:
        send_notification(post)

if __name__ == "__main__":
    main()