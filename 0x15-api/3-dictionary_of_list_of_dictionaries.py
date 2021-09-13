#!/usr/bin/python3
"""
Using what you did in the task #0, extend your
Python script to export data in the JSON format.
"""
import json
from requests import get


if __name__ == "__main__":
    dictionary = {}
    for user_id in range(1, 11):
        employee = get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                user_id)).json()

        users = get('https://jsonplaceholder.typicode.com/users?id={}'.format(
            user_id)).json()
        for user in users:
            for key, value in user.items():
                if key == "username":
                    username = value
        inner_dictionary = {}
        lista = []
        for dates in employee:
            for key, value in dates.items():
                if key == "completed":
                    task = value
                    for key, value in dates.items():
                        if key == "title":
                            inner_dictionary = {
                                "task": value,
                                "completed": task,
                                "username": username}
                            lista.append(inner_dictionary)
        dictionary[user_id] = lista
    with open('todo_all_employees.json', 'w', encoding='utf8') as f:
        json.dump(dictionary, f)
