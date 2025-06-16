#!/usr/bin/python3

import requests
import csv

def fetch_and_print_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post['title'])

def fetch_and_save_posts():
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        posts = response.json()

        filtered_posts = []
        for post in posts:
            new_post = {
                    'id': post['id'],
                    'title': post['title'],
                    'body': post['body']
            }
            filtered_posts.append(new_post)

        with open('posts.csv', 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=filtered_posts[0].keys())
            writer.writeheader()
            writer.writerows(filtered_posts)

