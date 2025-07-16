from queue import Queue

class BFD:
    def BFDsearch(self, adjacency_matrix, v):
        q = Queue()
        visited = {i: False for i in range(len(adjacency_matrix))}
        q.put(v)
        print(v)
        while(not q.empty()):
            temp=q.get()
            visited[temp]=True
            for ele in range(len(adjacency_matrix)):
                if((not visited[ele]) and (adjacency_matrix[temp][ele]==1)):
                    visited[ele]=True
                    q.put(ele)
                    print(ele)



matrix = [
    [0, 1, 1, 1, 0],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 0, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 1, 0, 0]
]

initv=0

B = BFD()
B.BFDsearch(matrix,initv)