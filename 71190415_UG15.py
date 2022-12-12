class Graph:
    def __init__(self):
        #constructor
        self._data = {}

    def addVertex(self, key):
        #menambah vertex
        if key not in self._data:
            self._data[key] = set()

    def vertex(self): #mencetak seluruh vertex
        print("\nSeluruh Node = ", end = "")
        for key, value in self._data.items():
            print(key, ';', value)
        print()
    
    def edge(self): #mencetak seluruh edge
        print("Seluruh Edge = ", end = "")
        listEdge = set()
        for key, value in self._data.items():
            for item in self._data[key]:
                if key+item not in listEdge and item+key not in listEdge:
                    listEdge.add(key+item)
        print()

    def addEdge(self, x, y):
        #menambah edge antara vertex x dan y
        if x in self._data and y in self._data:
            self._data[x].add(y)
            self._data[y].add(x) #hanya digunakan jika graph tidak berarah

    # untuk pembacaan traversing bfs graph
    def bfs(self, node, graph , visited):
        visited = [] 
        queue = [] 
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0) 
            print (s, end = " ") 

        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)

# silahkan buat graph seperti pada soal
graph = Graph()

graph.addVertex('a')
graph.addVertex('b')
graph.addVertex('c')
graph.addVertex('d')
graph.addVertex('g')
graph.addVertex('f')
graph.addVertex('e')

graph.addEdge('a', 'b')
graph.addEdge('b','d')
graph.addEdge('b', 'c')
graph.addEdge('g', 'c')
graph.addEdge('d', 'e')
graph.addEdge('c', 'e')
graph.addEdge('e', 'f')

# jangan ubah bagian di bawah 
graph.vertex()
graph.edge()
graph.bfs(visited, graph, "a")