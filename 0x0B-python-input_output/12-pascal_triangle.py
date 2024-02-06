#!/usr/bin/python3
"""define a pascal triangle func"""


def pascal_triangle(n):
    """represent pascal triangle by size n"""
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        temp = [1]
        for x in range(len(tri) - 1):
            temp.append(tri[x] + tri[x + 1])
        temp.append(1)
        triangles.append(temp)
    return triangles
