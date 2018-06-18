# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 19:33:06 2018

@author: aksha
"""

from collections import deque
queue = deque(["Ram", "Tarun", "Asif", "John"])
print(queue)
queue.append("Akbar")
print(queue)
queue.append("Birbal")
print(queue)
print(queue.popleft())                 
print(queue.popleft())                 
print(queue)
