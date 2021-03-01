# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 10:04:12 2020

@author: Shortest Path
"""

from collections import defaultdict;

class Graph:
    def __init__(self):
        self.graph=defaultdict(list)
    
    def AddEdgeToGraph(self, u, v):
        return self.graph[u].append(v);
    
    def bfs(self, startNode):
        visited=set();
        queue=[]
        queue.append(startNode)
        visited.add(startNode)
        previous=defaultdict(list)
        while queue:
            node=queue.pop(0)
            for neighbour in self.graph[node]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    visited.add(neighbour)
                    previous[neighbour]=node
        return previous;
        
    def reconstructPath(self, s, e, path):
        reconstructedPath=[]
        at=e;
        while at!=None:
            reconstructedPath.append(at)
            print(path)
            at=path.get(at) 
        reconstructedPath.reverse();
        if reconstructedPath[0] == s:
            return reconstructedPath;
        return []
        
    
    
g=Graph();

g.AddEdgeToGraph(1,2)
g.AddEdgeToGraph(1,0)
g.AddEdgeToGraph(0,3)
g.AddEdgeToGraph(3,7)
g.AddEdgeToGraph(3,4)
g.AddEdgeToGraph(7,6)
g.AddEdgeToGraph(4,6)
g.AddEdgeToGraph(4,5)

path=g.bfs(0)
#path=g.reconstructPath(0, 7, path)
#print('Shortent Path Length is ', len(path)-1)
#print('Path is::\n')
#print(path);

        
path=g.reconstructPath(2, 6, path)
print('Shortent Path Length is ', len(path)-1)
print('Path is::\n')
print(path);
        
        
        
                    
            

