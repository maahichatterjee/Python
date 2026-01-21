"""
Problem: Type Hints
URL: https://neetcode.io/problems/python-type-hints/question
Language: python

Solution by NeetCode GitHub Pusher
"""

# def greet(name: str) -> str:# def greet(name: str) -> str:
#     # print("Hello, " + name)#     # print("Hello, " + name)
#     return "Hello, "+name#     return "Hello, "+name
def greet(name:str)->None:def greet(name:str)->None:
    print("Hello, "+name)    print("Hello, "+name)
value= greet("NeetCode")value= greet("NeetCode")
print(type(value))print(type(value))