#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the CSV format.
"""
import csv
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

    lista = []
    for dates in employee:
        for key, value in dates.items():
            if key == "completed":
                task = value
                for key, value in dates.items():
                    if key == "title":
                        lista.append([argv[1], username, task, value])

    with open('{}.csv'.format(argv[1]), 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(lista)
