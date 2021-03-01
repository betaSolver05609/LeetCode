# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 13:04:47 2020

@author: Someindra Kumar Singh
"""

from collections import defaultdict;

class Graph:
    
    def __init__(self):
        self.graph=defaultdict(list)
    
    def AddEdgeToGraph(self, u, v):
        self.graph[u].append(v)
    
    def 

