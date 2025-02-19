#!/usr/bin/python3

import urllib.parse

def get_input():
    prompt = input("Enter the input type (file/text): ").strip().lower()
    if prompt == "file":
        file_path = input("Enter the file path: ").strip()
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError:
            print("File not found")
    elif prompt == "text":
        content = input("Enter the text: ")
        return content
    else:
        print("Invalid input type!")

user_input = get_input()

def encode(content):
    return urllib.parse.quote(content, safe=':/?=&')

if user_input is not None:
    result =  encode(user_input)
    print("Result: \n", result)
else:
    print("Invalid input!")
