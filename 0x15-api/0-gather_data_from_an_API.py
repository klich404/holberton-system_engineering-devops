#!/usr/bin/python3
"""
"""
from requests import get
from sys import argv


if __name__ == "__main__":
    employee = get(
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            argv[1])).json()

    users = get('https://jsonplaceholder.typicode.com/users?id={}'.format(
        argv[1])).json()
    for user in users:
        for key, value in user.items():
            if key == "name":
                name = value

    complete_task = 0
    tasks = 0
    for dates in employee:
        for key, value in dates.items():
            if key == "completed":
                tasks = tasks + 1
                if value is True:
                    complete_task = complete_task + 1

    print('Employee {} is done with tasks({}/{}):'.format(
        name, complete_task, tasks))
    for dates in employee:
        for key, value in dates.items():
            if key == "completed":
                if value is True:
                    for key, value in dates.items():
                        if key == "title":
                            print('\t {}'.format(value))
