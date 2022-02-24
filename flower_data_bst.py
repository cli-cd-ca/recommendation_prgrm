# Codecademy - CS102: Data Structures and Algorithms - Final Project
# Builds flower data binary search tree

from binarysearchtree import BinarySearchTree
from flower_data import *

BST = BinarySearchTree()
flower_safe = ['safe']
for flower in flower_data:
    BST.put(flower[0], flower)
    temp = "-".join(flower[1:])
    for color in flower_colors:
        if color in temp:
            BST.put(color, flower)
        for cycle in flower_cycles:
            if color in temp and cycle in temp:
                BST.put(color+cycle, flower)
            for season in flower_seasons:
                if color in temp and cycle in temp and season in temp:
                    BST.put(color+cycle+season, flower)
                for safe in flower_safe:
                    if color in temp and cycle in temp and season in temp and safe in temp:
                        BST.put(color+cycle+season+safe, flower)     
for flower in flower_data:
    temp = "-".join(flower[1:])
    for cycle in flower_cycles:
        if cycle in temp:
            BST.put(cycle, flower)
        for season in flower_seasons:
            if cycle in temp and season in temp:
                BST.put(cycle+season, flower)
            for safe in flower_safe:
                if cycle in temp and season in temp and safe in temp:
                    BST.put(cycle+season+safe, flower)
for flower in flower_data:                        
    temp = "-".join(flower[1:])
    for color in flower_colors:
        for season in flower_seasons:
            if color in temp and season in temp:
                BST.put(color+season, flower)
            for safe in flower_safe:
                if color in temp and season in temp and safe in temp:
                    BST.put(color+season+safe, flower)
for flower in flower_data:
    temp = "-".join(flower[1:])
    for color in flower_colors:
        for cycle in flower_cycles:
            for safe in flower_safe:
                if color in temp and cycle in temp and safe in temp:
                    BST.put(color+cycle+safe, flower)
for flower in flower_data:
    temp = "-".join(flower[1:])
    for season in flower_seasons:
        if season in temp:
            BST.put(season, flower) 
        for safe in flower_safe:
            if season in temp and safe in temp:
                BST.put(season+safe, flower) 
for flower in flower_data:
    temp = "-".join(flower[1:])
    for cycle in flower_cycles:
        for safe in flower_safe:
            if cycle in temp and safe in temp:
                BST.put(cycle+safe, flower)  
for flower in flower_data:
    temp = "-".join(flower[1:])
    for color in flower_colors:
        for safe in flower_safe:
            if color in temp and safe in temp:
                BST.put(color+safe, flower)
for flower in flower_data:
    temp = "-".join(flower[1:])
    for safe in flower_safe:
        if safe in temp:
            BST.put(safe, flower)
              
BST.root = BST.balanceBST(BST.root)