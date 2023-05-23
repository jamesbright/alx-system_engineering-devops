#!/usr/bin/python3
""" Returns an employees todo
    list using the employee ID
"""
import requests
import sys


def main():
    """Show employee todo according to ID
    """

    user_id = sys.argv[1]
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todos = 'https://jsonplaceholder.typicode.com/todos/?userId={}'.
    format(user_id)
    name_request = requests.get(user).json().get('name')
    todo_request = requests.get(todos).json()
    tasks = [task.get('title')for task in todo_request
             if task.get('completed') is True]
    print('Employee {} is done with tasks({}/{}):'.
          format(name_request, len(tasks),
                 len(todo_request)))
    print('\n'.join('\t {}'.format(task)
          for task in tasks))


if __name__ == "__main__":
    if len(sys.argv) == 2:
        main()
