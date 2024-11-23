from collections import permutations
def cal_route_cost(route):
    cost=0
    for i in range(len(route)):
        cost+=dm[i][i+1]
    cost+=dm[route[i]][route[0]]
    return cost
def tsp(s_n):
    route=(i for i in range(len(dm)))
    min_cost=inf
    path=()
    for p in permutations(route):
        cost=cal_route_cost(p)
        if cost<min_cost:
            min_cost=cost
            path=p
    return min_cost,path
dm=[[0, 10, 15, 20],[10, 0, 35, 25],[15, 35, 0, 30],[20, 25, 30, 0]]
min_cost,path=tsp(0)
print(f'Min_Cost={min__cost}\nPath={pth}')
