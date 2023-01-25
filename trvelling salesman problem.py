import Model, xsum, minimize, BINARY
def TSP_ILP(G):
    start = time()
    V1 =  range(len(G))
    n, V = len(G), set(V1)
    model = Model()
    x = [[model.add_var(var_type=BINARY) for j in V] for i in V]
    y = [model.add_var() for i in V]
    model.objective = minimize(xsum(G[i][j]*x[i][j] \
                                    for i in V for j in V))
    for i in V:
        model += xsum(x[i][j] for j in V - {i}) == 1
        for i in V:
            model += xsum(x[j][i] for j in V - {i}) == 1
            for (i, j) in product(V - {0}, V - {0}):
                if i != j:
                     model += y[i] - (n+1)*x[i][j] >= y[j]-n
                     model.optimize()
                     if model.num_solutions:
                         print('Total distance {}'.format(model.objective_value))
                         nc = 0
                         cycle = [nc]
                         while True:
                             nc = [i for i in V if x[nc][i].x >= 0.99][0]
                             cycle.append(nc)
                             if nc == 0:
                                 break
                             return (model.objective_value, cycle)

