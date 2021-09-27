#!/usr/bin/python3
"""
queries the Reddit API and returns the number of subscribers
(not active users, total subscribers) for a given subreddit
"""
import requests


def top_ten(subreddit):
    """return the number of suscribers fro a given subreddit,
    otherwise, return 0"""
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    headers = {'user-agent': "Mozilla/5.0 (X11; Linux x86_64)\
        AppleWebKit/537.36 (KHTML, like Gecko)\
            Chrome/51.0.2704.103 Safari/537.36"}
    response = requests.get(url, headers=headers, allow_redirects=False)
    if str(response) != "<Response [200]>":
        print(None)
        return
    response_json = response.json()
    posts = response_json.get('data').get('children')
    top = ""
    for post in posts:
        top += post.get("data").get('title') + "\n"
    print(top, end="")
