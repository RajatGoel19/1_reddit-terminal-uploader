import praw
import sys

# Simplified logic for Reddit API Access Request demonstration
def upload_to_reddit(file_path, subreddit_name, title):
    reddit = praw.Reddit(
        client_id="YOUR_CLIENT_ID",
        client_secret="YOUR_CLIENT_SECRET",
        password="YOUR_PASSWORD",
        user_agent="terminal_uploader_v1.0",
        username="YOUR_USERNAME",
    )

    subreddit = reddit.subreddit(subreddit_name)
    
    # Logic for handling video vs image
    if file_path.endswith(('.mp4', '.mov')):
        print(f"Uploading video: {file_path} to r/{subreddit_name}...")
        subreddit.submit_video(title, file_path)
    else:
        print(f"Uploading image: {file_path} to r/{subreddit_name}...")
        subreddit.submit_image(title, file_path)

if __name__ == "__main__":
    # Usage: python uploader.py path/to/media.mp4 "SubredditName" "My Post Title"
    upload_to_reddit(sys.argv[1], sys.argv[2], sys.argv[3])