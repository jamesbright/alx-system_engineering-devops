#!/usr/bin/python3
""" Returns an employees todo
    list using the employee ID
"""
import json
import requests


def main():
    """Show all employee todos
    """


    # GET all the users
    users = requests.get('https://jsonplaceholder.typicode.com/users')
    users = json.loads(users.text)
    dict_ = {}
    for user in users:
        task_list = []
        dict_[user.get('id')] = task_list
        # GET tasks for specific user
        todos = requests.get('https://jsonplaceholder.typicode.com/todos?userId={}'
            .format(user.get('id')))
        todos = json.loads(todos.text)
       
        for task in todos:
            task_d = {}
            task_d['task'] = task.get('title')
            task_d['completed'] = task.get('completed')
            task_d['username'] = task.get('username')
            task_list.append(task_d)

    with open("{}.json".format('all_employees'), 'w', encoding='utf-8') as fp:
        json.dump(dict_, fp)


if __name__ == "__main__":
    main()
