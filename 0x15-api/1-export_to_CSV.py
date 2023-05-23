#!/usr/bin/python3
""" Returns an employees todo
    list using the employee ID
"""
import csv
import json
import requests
import sys


def main():
    """Show employee todo according to ID
    """

    user_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
        .format(user_id)
    user_request = requests.get(user)
    user = json.loads(user_request.text)
    user_name = user.get('username')
    todo_request = requests.get(todos)
    todo_request = json.loads(todo_request.text)

    with open('{}.csv'.format(user_id),
              'w', newline='', encoding='utf-8') as fp:
        taskwriter = csv.writer(fp, quoting=csv.QUOTE_ALL)
        for task in todo_request:
            taskwriter.writerow(["{}".format(user_id),
                                 "{}".format(user_name),
                                 "{}".format(task.get('completed')),
                                 "{}".format(task.get('title'))])


if __name__ == "__main__":
    main()
