#!/usr/bin/python3
""" Returns an employees todo
    list using the employee ID
"""
import requests
import sys
import csv


def main():
    """Show employee todo according to ID
    """

    user_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
        .format(user_id)
    user_name = requests.get(user).json().get('name')
    todo_request = requests.get(todos).json()

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
