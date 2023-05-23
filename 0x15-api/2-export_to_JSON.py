#!/usr/bin/python3
""" Returns an employees todo
    list using the employee ID
"""
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

    dict_ = {}
    task_list = []
    dict_[user_id] = task_list
    for task in todo_request:
        task_d = {}
        task_d['task'] = task.get('title')
        task_d['completed'] = task.get('completed')
        task_d['username'] = user_name
        task_list.append(task_d)

    with open("{}.json".format(user_id), 'w', encoding='utf-8') as fp:
        json.dump(dict_, fp)


if __name__ == "__main__":
    main()
