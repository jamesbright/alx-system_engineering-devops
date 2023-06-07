#!/usr/bin/python3
"""Module that queries the Reddit API and return the number of 
subscribers a given subreddit has."""
import requests
def number_of_subscribers(subreddit):
    """Function that sends a request to the Reddit API and takes a 
    subreddit as parameter, then displays the number of subscribers 
    of the subreddit. subreddit: the subredit to query"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit) 
    response = requests.get(url, headers={'user-agent': 'request'},
                            allow_redirects=False) 
    if response.status_code != requests.codes.ok:
	return 0
    rdict = response.json()
    sub_num = rdict.get('data').get('subscribers')
    return sub_num
