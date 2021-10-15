# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 16:14:08 2021

@author: Dell inspiron
"""

class Solution:
     def calculateArea(i, j, height_i, height_j):
        if height_i<height_j:
            return height_i*(j-i)
        else:
            return height_j*(j-i)
            
    def maxArea(self, height: List[int]) -> int:
        i=0;
        j=len(height)-1
        m=0
        area=calculateArea(i,j,height[i], height[j])
        if area>m:
            m=area
        return m;
            

            