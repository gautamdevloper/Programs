def aStar(start,stop):
    open_set=set(start)
    closed_set=set()
    p={}
    g={}
    p[start]=start
    g[start]=0

    while len(open_set)>0:
        n=None
        for v in open_set:
            if n==None or g[n]+heuristic(n)>g[v]+heuristic(v):
                n=v
        if n==stop or Graph_nodes[n]==None:
            pass
        else:
            for(m,weight) in get_neighbours(n):
                if m not in open_set and m not in closed_set:
                    open_set.add(m)
                    g[m]=g[n]+weight
                    p[m]=n
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        p[m]=n
                        if m in closed_set:
                            closed_set.remove(m)
                            open_set.add(m)
        if n==None:
            print("Path does not exist!")
            return None
        if n==stop:
            path=[]
            while p[n]!=n:
                path.append(n)
                n=p[n]
            path.append(start)
            path.reverse()
            print("Path found :",path)
            return path
        open_set.remove(n)
        closed_set.add(n)
    
    print("Path does not exist!")
    return None
def get_neighbours(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
def heuristic(v):
    H_dist={
        'A': 11,
        'B': 6,
        'C': 99,
        'D': 1,
        'E': 7,
        'G': 0,

    }
    return H_dist[v]
Graph_nodes={
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1),('G', 9)],
    'C': None,
    'E': [('D', 6)],
    'D': [('G', 1)],

}
aStar('A', 'G')