#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
import json
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
            if key == "username":
                username = value

    dictionary = {}
    lista = []
    for dates in employee:
        for key, value in dates.items():
            if key == "completed":
                task = value
                for key, value in dates.items():
                    if key == "title":
                        lista.append(
                            {"task": value,
                             "completed": task,
                             "username": username})
    dictionary = {argv[1]: lista}
    with open('{}.json'.format(argv[1]), 'w', encoding='utf8') as f:
        json.dump(dictionary, f)
