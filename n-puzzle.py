#!/usr/bin/python
# Kaustav Vats (2016048)

import queue as Q
from time import time
from math import sqrt

class Node:
    
    def __init__(self, node, step, GraphNode, Link):
        self.UID = ""
        self.step = step
        self.node = node
        self.distance_top = 0
        self.distance = 0
        self.GraphNode = GraphNode
        self.Link = Link
        for i in range(len(node)):
            GraphNode.append([])
            for j in range(len(node[i])):
                GraphNode[i].append(node[i][j])
                self.UID += str(node[i][j])

    def isEqual(self, node2):
        return self.UID == node2.UID
    
    def DeepCopy(self):
        node = []
        for i in range(len(self.GraphNode)):
            node.append([])
            for j in range(len(self.GraphNode[i])):
                node[i].append(self.GraphNode[i][j])
        return node

    def __str__(self):
        ans = ""
        for i in range(len(self.GraphNode)):
            ans += self.GraphNode[i] + "\n"
        return ans

    def __cmp__(self, other):
        return cmp(self.distance, other.distance)

    def __lt__(self, other):
        return self.distance_top < other.distance_top

    def __eq__(self, other):
        return self.distance_top == other.distance_top

class Graph:
    
    '''
    Constructor donde recibimos N 
    '''
    def __init__(self, size): 
        self.size = size
        
    def isVisited(node, visit):
        for i in range(len(visit)):
            if node.isEqual(visit[i]):
                return True
        return False
    '''
    Buscamos el cero por donde moverse el puzzle 
    '''
    def Salida(NodeArg):
        for i in range(len(NodeArg.GraphNode)):
            for j in range(len(NodeArg.GraphNode[i])):
                if ( NodeArg.GraphNode[i][j] == 0 ): 
                    return [i, j]
        print(-1, -1) 
        return [-1, -1]    
    '''
        buscamos todos los nodos
    '''
    def Buscar_Nodo(node):
        nodo_hijo = []
        temp = Graph.Salida(node)
        x = temp[0]
        y = temp[1]
        temp_node = node.DeepCopy()

        if ( x == 0 and y == 0 ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x == 0 and y == (len(node.GraphNode[x])-1) ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x == (len(node.GraphNode[y])-1) and y == 0 ):
            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x == (len(node.GraphNode[y])-1) and y == (len(node.GraphNode[x])-1) ):
            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0
            
        elif ( x > 0 and x < len(node.GraphNode[y]) and y == 0 ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x == 0 and y > 0 and y < len(node.GraphNode[x]) ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0

        elif ( x > 0 and x < len(node.GraphNode[y]) and y == (len(node.GraphNode[x])-1) ):
            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0
            
            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0
            
        elif ( x == (len(node.GraphNode[y])-1) and y > 0 and y < len(node.GraphNode[x]) ):
            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0 
            
            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

        else:
            temp_node[x][y] = temp_node[x-1][y]
            temp_node[x-1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x-1][y] = temp_node[x][y]
            temp_node[x][y] = 0 
            
            temp_node[x][y] = temp_node[x][y-1]
            temp_node[x][y-1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y-1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x][y+1]
            temp_node[x][y+1] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x][y+1] = temp_node[x][y]
            temp_node[x][y] = 0

            temp_node[x][y] = temp_node[x+1][y]
            temp_node[x+1][y] = 0
            n1 = Node(temp_node, node.step+1, [],None)
            nodo_hijo.append(n1)
            temp_node[x+1][y] = temp_node[x][y]
            temp_node[x][y] = 0
        return nodo_hijo

    
    
    def CalculateManhattanDistance(self, node, end):
        arr = [0]*(self.size+1)
        brr = [0]*(self.size+1)
        for i in range(len(node.GraphNode)):
            for j in range(len(node.GraphNode[i])):
                arr[node.GraphNode[i][j]] = [i, j]

        for i in range(len(end.GraphNode)):
            for j in range(len(end.GraphNode[i])):
                brr[end.GraphNode[i][j]] = [i, j]
        dist = 0
        for i in range(1, len(arr)):
            dist += abs(arr[i][0]-brr[i][0]) + abs(arr[i][1]-brr[i][1])
        return dist
    
    def AStarAlgorithm(self, root, end):
        visited = {}
        q = Q.PriorityQueue()
        dist = self.CalculateManhattanDistance(root, end)
        root.distance = dist
        q.put((1, root))
        visited[root.UID] = root
        Count = 0

        while ( not q.empty() ):
            Count += 1
            current_Node = (q.get())[1]
            if ( current_Node.isEqual(end) ):
                print("Nodos visitados: ", Count)
                print("Produndidad: ",current_Node.step)
                return True
            
            nodo_vecino = Graph.Buscar_Nodo(current_Node)
            current_Node.Link = nodo_vecino

            for i in range(len(nodo_vecino)):
                if nodo_vecino[i].UID not in visited:
                    dist = self.CalculateManhattanDistance(nodo_vecino[i], end)
                    nodo_vecino[i].distance_top = current_Node.distance_top + 1
                    nodo_vecino[i].distance = nodo_vecino[i].distance_top + dist
                    nodo_vecino[i].step = current_Node.step + 1
                    q.put((nodo_vecino[i].distance, nodo_vecino[i]))
                    visited[nodo_vecino[i].UID] = nodo_vecino[i]
        return False
    
    
if __name__ == "__main__":
    
    print("Ingresar N de la matriz: ")
    N = int(input())
    gp = Graph(N)
    print("Ingresar Estado Incial: ")
    Estado_Inicial = []
    for i in range(int(sqrt(N+1))):
        lil = list(map(int, input().split()))
        Estado_Inicial.append(lil)
    print("Ingresar Estado Final: ")
    Estado_Final = []
    for i in range(int(sqrt(N+1))): 
        lil = list(map(int, input().split()))
        Estado_Final.append(lil)
    Root = Node(Estado_Inicial, 0, [], None)
    End = Node(Estado_Final, 0, [], None)
    t1 = int(round(time()*1000))
    try:
        if ( gp.AStarAlgorithm(Root, End) ):
            print("match! ")
        else:
            print("no encontro match ")
    except Exception as e:
        print(e)
        print("mismo numero en la misma matriz")
    t2 = int(round(time()*1000))
    print("Tiempo  A*: ", t2-t1)
    print("")
    # N = int(input())
    # # # N = 2
    # # Estado_Inicial = [[0, 2, 3], [1, 4, 5], [8, 7, 6]]
    # # Estado_Final = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    # # Prueba no resuelve
    # # Estado_Inicial = [[1, 2, 5], [3, 4, 6], [8, 7, 0]]
    # # Estado_Final = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # # Solucionable
    # Estado_Inicial = [[0, 3, 8], [4, 1, 7], [2, 6, 5]]
    # Estado_Final = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

  

    
