#!/usr/bin/python3

import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    posts = response.json()

    for post in posts[:5]:
        print(f"Post ID: {post['id']}")
        print(f"Title: {post['title']}")
        print(f"Body: {post['body']}\n")

else:
    print(f"Failed to fetch posts. Status code: {respones.status_code}")
