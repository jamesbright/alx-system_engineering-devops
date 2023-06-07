#!/usr/bin/python3
"""Module with number_of_subscribers function"""
import requests
import sys


def number_of_subscribers(subreddit):
    """function that queries the Reddit API
    and returns the number of subscri    bers for a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    json_obj = requests.get(url,
                            headers={'User-Agent': 'My User Agent 1.0'})
    if json_obj.status_code != 404:
        dict_obj = json_obj.json()
        return dict_obj.get('data').get('subscribers')
    else:
        return 0
