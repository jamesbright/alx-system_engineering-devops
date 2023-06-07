#!/usr/bin/python3
"""Module with top_ten function"""
import requests
import sys


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    parameters = {'limit': 10}
    json_obj = requests.get(url, headers={'User-Agent': 'My User Agent 1.0'},
                            params=parameters)
    if json_obj.status_code != 404:
        dict_obj = json_obj.json().get('data').get('children')
        for each in dict_obj:
            print(each.get('data').get('title'))
    else:
        print(None)
