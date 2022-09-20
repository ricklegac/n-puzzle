'''
Grupo 4
Ricardo Leguizamon
Diego Seo
Lorenzo Cabrera
Soledad Decoud
'''

import queue as Q
from time import time
from math import sqrt

class Nodo:
    
    def __init__(self, nodo, step, GraphNode, Link):
        self.UID = ""
        self.step = step
        self.nodo = nodo
        self.distance_top = 0
        self.distance = 0
        self.GraphNode = GraphNode
        self.Link = Link
        for i in range(len(nodo)):
            GraphNode.append([])
            for j in range(len(nodo[i])):
                GraphNode[i].append(nodo[i][j])
                self.UID += str(nodo[i][j])

    def isEqual(self, node2):
        return self.UID == node2.UID
    
    def DeepCopy(self):
        nodo = []
        for i in range(len(self.GraphNode)):
            nodo.append([])
            for j in range(len(self.GraphNode[i])):
                nodo[i].append(self.GraphNode[i][j])
        return nodo

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
    
    def __init__(self, size):
        self.size = size
        
    def isVisited(nodo, visit):
        for i in range(len(visit)):
            if nodo.isEqual(visit[i]):
                return True
        return False

    def BuscarMovimientosCero(NodeArg):
        for i in range(len(NodeArg.GraphNode)):
            for j in range(len(NodeArg.GraphNode[i])):
                if ( NodeArg.GraphNode[i][j] == 0 ):
                    return [i, j]
        print(-1, -1)
        return [-1, -1]    

    def BuscarNodos(nodo):
        nodo_hijo = []
        temp = Graph.BuscarMovimientosCero(nodo)
        x = temp[0]
        y = temp[1]
        nodo_temporal = nodo.DeepCopy()

        if ( x == 0 and y == 0 ):
            nodo_temporal[x][y] = nodo_temporal[x+1][y]
            nodo_temporal[x+1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x+1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x][y+1]
            nodo_temporal[x][y+1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y+1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

        elif ( x == 0 and y == (len(nodo.GraphNode[x])-1) ):
            nodo_temporal[x][y] = nodo_temporal[x+1][y]
            nodo_temporal[x+1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x+1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x][y-1]
            nodo_temporal[x][y-1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y-1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

        elif ( x == (len(nodo.GraphNode[y])-1) and y == 0 ):
            nodo_temporal[x][y] = nodo_temporal[x][y+1]
            nodo_temporal[x][y+1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y+1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x-1][y]
            nodo_temporal[x-1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x-1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

        elif ( x == (len(nodo.GraphNode[y])-1) and y == (len(nodo.GraphNode[x])-1) ):
            nodo_temporal[x][y] = nodo_temporal[x-1][y]
            nodo_temporal[x-1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x-1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x][y-1]
            nodo_temporal[x][y-1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y-1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0
            
        elif ( x > 0 and x < len(nodo.GraphNode[y]) and y == 0 ):
            nodo_temporal[x][y] = nodo_temporal[x+1][y]
            nodo_temporal[x+1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x+1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x-1][y]
            nodo_temporal[x-1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x-1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x][y+1]
            nodo_temporal[x][y+1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y+1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

        elif ( x == 0 and y > 0 and y < len(nodo.GraphNode[x]) ):
            nodo_temporal[x][y] = nodo_temporal[x+1][y]
            nodo_temporal[x+1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x+1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x][y+1]
            nodo_temporal[x][y+1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y+1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x][y-1]
            nodo_temporal[x][y-1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y-1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

        elif ( x > 0 and x < len(nodo.GraphNode[y]) and y == (len(nodo.GraphNode[x])-1) ):
            nodo_temporal[x][y] = nodo_temporal[x+1][y]
            nodo_temporal[x+1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x+1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x-1][y]
            nodo_temporal[x-1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x-1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0
            
            nodo_temporal[x][y] = nodo_temporal[x][y-1]
            nodo_temporal[x][y-1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y-1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0
            
        elif ( x == (len(nodo.GraphNode[y])-1) and y > 0 and y < len(nodo.GraphNode[x]) ):
            nodo_temporal[x][y] = nodo_temporal[x-1][y]
            nodo_temporal[x-1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x-1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0 
            
            nodo_temporal[x][y] = nodo_temporal[x][y-1]
            nodo_temporal[x][y-1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y-1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x][y+1]
            nodo_temporal[x][y+1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y+1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

        else:
            nodo_temporal[x][y] = nodo_temporal[x-1][y]
            nodo_temporal[x-1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x-1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0 
            
            nodo_temporal[x][y] = nodo_temporal[x][y-1]
            nodo_temporal[x][y-1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y-1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x][y+1]
            nodo_temporal[x][y+1] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x][y+1] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0

            nodo_temporal[x][y] = nodo_temporal[x+1][y]
            nodo_temporal[x+1][y] = 0
            n1 = Nodo(nodo_temporal, nodo.step+1, [],None)
            nodo_hijo.append(n1)
            nodo_temporal[x+1][y] = nodo_temporal[x][y]
            nodo_temporal[x][y] = 0
        return nodo_hijo

        
    def bfs(self, root, end):
        visited = {}
        queue = []
        queue.append(root)
        visited[root.UID] = root
        Count = 0
        while ( True ):
            Count += 1
            if ( len(queue) == 0 ):
                return False
            current_Node = queue.pop(0)
            if ( current_Node.isEqual(end) ):
                print("Cantidad de nodos visitados: ", Count)
                print("Profundidad: ",current_Node.step)
                return True
            Neighbours = Graph.BuscarNodos(current_Node)
            current_Node.Link = Neighbours

            for i in range(len(Neighbours)):
                if Neighbours[i].UID not in visited:
                    Neighbours[i].step = current_Node.step + 1
                    queue.append(Neighbours[i])
                    visited[Neighbours[i].UID] = Neighbours[i]    


    def Dfs(self, root, end):
        visited = {}
        stack = []
        stack.append(root)
        Count = 0

        while ( len(stack) > 0 ):
            Count += 1
            current_Node = stack.pop()
            if ( current_Node.isEqual(end) ):
                print("Cantidad de nodos visitados: ", Count)
                print("Profundidad: ",current_Node.step)
                return True
            if ( current_Node.UID in visited ):
                continue
            visited[current_Node.UID] = current_Node
            Neighbours = Graph.BuscarNodos(current_Node)
            current_Node.Link = Neighbours

            for i in range(len(Neighbours)):
                Neighbours[i].step = current_Node.step + 1
                stack.append(Neighbours[i])
            
        return False
            
    def DfsRec(self, root, end):
        visited = {}
        return self.DfsUtil(root, end, visited)

    def DfsUtil(self, current_node, end, visited):
        visited[current_node.UID] = current_node
        if ( current_node.isEqual(end) ):
            print("Match!")
            return True

        Neighbours = Graph.BuscarNodos(current_node)
        current_node.Link = Neighbours

        for i in range(len(Neighbours)):
            if Neighbours[i].UID not in visited:
                Neighbours[i].step += current_node.step
                var = self.DfsUtil(Neighbours[i], end, visited) 
                if ( var == True ):
                    return var
    
    def CalculateManhattanDistance(self, nodo, end):
        arr = [0]*(self.size+1)
        brr = [0]*(self.size+1)
        for i in range(len(nodo.GraphNode)):
            for j in range(len(nodo.GraphNode[i])):
                arr[nodo.GraphNode[i][j]] = [i, j]

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
                print("Cantidad de nodos visitados: ", Count)
                print("Profundidad: ",current_Node.step)
                return True
            
            Neighbours = Graph.BuscarNodos(current_Node)
            current_Node.Link = Neighbours

            for i in range(len(Neighbours)):
                if Neighbours[i].UID not in visited:
                    dist = self.CalculateManhattanDistance(Neighbours[i], end)
                    Neighbours[i].distance_top = current_Node.distance_top + 1
                    Neighbours[i].distance = Neighbours[i].distance_top + dist
                    Neighbours[i].step = current_Node.step + 1
                    q.put((Neighbours[i].distance, Neighbours[i]))
                    visited[Neighbours[i].UID] = Neighbours[i]

        return False
    
    def IDAStar(self, root, end):
        dist = self.CalculateManhattanDistance(root, end)
        var = dist
        while True:
            visited = {}
            queue = Q.PriorityQueue()
            root.distance_top = 0
            root.distance = dist
            queue.put((1, root))
            visited[root.UID] = root
            print("Threshold: ",var)
            var = self.IDAStarUtil(queue, end, var, visited)
            # var = self.IDAStarUtil(queue, end, var)
            if ( isinstance(var, bool) ):
                return True
            elif( isinstance(var, int) ):
                if ( var == -1 ):
                    return False
        
    def IDAStarUtil(self, q, end, MaxDistance, visited):
    # def IDAStarUtil(self, q, end, MaxDistance):
        
        Count = 0
        CurrentDistance = -1
        while ( not q.empty() ):
            Count += 1
            current_Node = (q.get())[1]
            if ( current_Node.isEqual(end) ):
                print("Cantidad de nodos visitados: ", Count)
                print("Profundidad: ",current_Node.step)
                return True

            if ( current_Node.distance > MaxDistance ):
                if ( CurrentDistance != -1 and current_Node.distance < CurrentDistance ):
                    CurrentDistance = current_Node.distance
                elif ( CurrentDistance == -1 ):
                    CurrentDistance = current_Node.distance
                continue
            Neighbours = Graph.BuscarNodos(current_Node)
            current_Node.Link = Neighbours

            for i in range(len(Neighbours)):
                if Neighbours[i].UID not in visited:
                    dist = self.CalculateManhattanDistance(Neighbours[i], end)
                    Neighbours[i].distance_top = current_Node.distance_top + 1
                    Neighbours[i].distance = Neighbours[i].distance_top + dist
                    Neighbours[i].step = current_Node.step + 1
                    q.put((Neighbours[i].distance, Neighbours[i]))
                    visited[Neighbours[i].UID] = Neighbours[i]
    
        return CurrentDistance
    
if __name__ == "__main__":
    
    print("Ingrese N: ")
    N = int(input())
    gp = Graph(N)
    print("Ingrese estado Inicial: ")
    EstadoInicial = []
    for i in range(int(sqrt(N+1))):
        lil = list(map(int, input().split()))
        EstadoInicial.append(lil)
    print("Ingrese estado Final: ")
    EstadoFinal = []
    for i in range(int(sqrt(N+1))):
        lil = list(map(int, input().split()))
        EstadoFinal.append(lil)
    Root = Nodo(EstadoInicial, 0, [], None)
    End = Nodo(EstadoFinal, 0, [], None)
    while True:
        print("-------Menu-------")
        print("1. BFS")
        print("2. DFS")
        print("3. A*")
        print("4. IDA*")
        print("5. All")
        print("6. Salir")
        NumEnter = int(input())
        if ( NumEnter == 1 ):
            t1 = int(round(time()*1000))
            if ( gp.bfs(Root, End) ):
                print("Match!")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Tiempo: Bfs: ", t2-t1)
            print("")
        elif ( NumEnter == 2 ):
            t1 = int(round(time()*1000))
            if ( gp.Dfs(Root, End) ):
                print("Match!")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Tiempo: Dfs: ", t2-t1)
            print("")
        elif ( NumEnter == 3 ):
            t1 = int(round(time()*1000))
            if ( gp.AStarAlgorithm(Root, End) ):
                print("Match!")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Tiempo: A*: ", t2-t1)
            print("")
        elif ( NumEnter == 4 ):
            t1 = int(round(time()*1000))
            if ( gp.IDAStar(Root, End) ):
                print("Match!")
            else:
                print("No Match")
            t2 = int(round(time()*1000))
            print("Tiempo: IDA*: ", t2-t1)
            print("")
        elif( NumEnter == 5 ):
            t1 = int(round(time()*1000))
            if ( gp.bfs(Root, End) ):
                print("Match con  Bfs")
            else:
                print("Ningun Match para Bfs")
            t2 = int(round(time()*1000))
            print("Tiempo: bfs: ", t2-t1)
            print("")
            t1 = int(round(time()*1000))
            if ( gp.Dfs(Root, End) ):
                print("Match con  Dfs")
            else:
                print("Ningun Match para Dfs")
            t2 = int(round(time()*1000))
            print("Tiempo: Dfs: ", t2-t1)
            print("")
            t1 = int(round(time()*1000))
            if ( gp.AStarAlgorithm(Root, End) ):
                print("Match con  A*")
            else:
                print("Ningun Match para A*")
            t2 = int(round(time()*1000))
            print("Tiempo: A*: ", t2-t1)
            print("")
            t1 = int(round(time()*1000))
            if ( gp.IDAStar(Root, End) ):
                print("Match con  IDA*")
            else:
                print("Ningun Match para IDA*")
            t2 = int(round(time()*1000))
            print("Tiempo: IDA*: ", t2-t1)
            print("")
        elif ( NumEnter == 6 ):
            break
        else:
            print("Ingrese una opcion valida")
            

    # N = int(input())
    # # # N = 2
    # # Solucionable
    # # EstadoInicial = [[0, 2, 3], [1, 4, 5], [8, 7, 6]]
    # # EstadoFinal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]

    # # No Solucionable
    # # EstadoInicial = [[1, 2, 5], [3, 4, 6], [8, 7, 0]]
    # # EstadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # # Mejor Solucion
    # EstadoInicial = [[0, 3, 8], [4, 1, 7], [2, 6, 5]]
    # EstadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    # # casos en donde dfs corre mejor que bfs
    # # EstadoInicial = [[3, 0, 8], [4, 1, 7], [2, 6, 5]]
    # # EstadoFinal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    # # EstadoInicial = [[10, 17, 22, 11, 2], [6, 7, 20, 24, 21], [14, 12, 5, 23, 1], [16, 18, 13, 15, 9], [4, 8, 3, 19, 0]]
    # # EstadoFinal = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 0]]
    # # EstadoInicial = [[2, 1, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    # # EstadoFinal = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 0]]
    # # EstadoInicial = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 10, 12], [13, 14, 11, 15]]

    # Root = Nodo(EstadoInicial, 0, [], None)
    # End = Nodo(EstadoFinal, 0, [], None)

    # gp = Graph(N)
    # # gp.bfs(Root, End)
    # # if ( gp.bfs(Root, End) ):
    #     # print("Match!")
    # # else:
    #     # print("No Match")
    # # print(gp.Dfs(Root, End))
    # print(gp.AStarAlgorithm(Root, End))
    # print(gp.IDAStar(Root, End))
