#!/usr/bin/python3
"""Module with top_ten function"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=""):
    """Queries the Reddit API and returns a
    list containing the titles of all hot
    articles for a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot.json{}".format(subreddit,
                                                          after)
    json_obj = requests.get(url,
                            headers={'User-Agent': 'My User Agent 1.0'})
    if json_obj.status_code != 404:
        dict_obj = json_obj.json()
        list_obj = dict_obj.get('data').get('children')
        for each in list_obj:
            hot_list.append(each.get('data').get('title'))
        next_fullname = dict_obj.get('data').get('after')
        after = "?after={}".format(next_fullname)
        if next_fullname is not None:
            hot_list.append(recurse(subreddit, hot_list, after))
        return hot_list
    else:
        return None
