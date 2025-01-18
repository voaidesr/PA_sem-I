def liste_adiacenta(orientare, lista_muchii, n):
    lista = {i: [] for i in range(1, n + 1)}
    if orientare == "orientat":
        for muchie in lista_muchii:
            lista[muchie[0]].append(muchie[1])
    elif orientare == "neorientat":
        for muchie in lista_muchii:
            lista[muchie[0]].append(muchie[1])
            lista[muchie[1]].append(muchie[0])
    return lista

def matrice_adiacenta(orientare, lista_muchii, n):
    matrice = [[0 for _ in range(n)] for _ in range(n)]
    if orientare == "orientat":
        for muchie in lista_muchii:
            matrice[muchie[0]-1][muchie[1]-1] = 1
    elif orientare == "neorientat":
        for muchie in lista_muchii:
            matrice[muchie[0]-1][muchie[1]-1] = 1
            matrice[muchie[1]-1][muchie[0]-1] = 1
    return matrice

def bfs(lista_adiacenta, s):
    bf = []  # se comporta ca queue, tine tupluri (child, parent)
    # nu se sterg elemente
    # mentinem poizita primului
    # nodurile din bf sunt deja vizitate
    st = dr = 0
    bf.append((s, -1))
    visited = set([s])
    while st <= dr:  # cat timp coada nu este vida
        node, _ = bf[st] # parintele actual
        st += 1
        for child in lista_adiacenta[node]:
            if child not in visited:
                bf.append((child, node))
                visited.add(child)
                dr += 1
    return bf

def dfs(lista_adiacenta, s):
    df = []  # Stack to manage DFS traversal
    vizitat = []  # List of visited nodes
    df.append(s)
    vizitat.append(s)
    
    while df:
        parent = df[-1]  # Peek at the top of the stack
        for child in lista_adiacenta[parent]:
            if child not in vizitat:
                df.append(child)  # Push to stack
                vizitat.append(child)  # Mark as visited
                break  # Explore this child
        else:
            # If no unvisited children are found, backtrack
            df.pop(-1)
    
    return vizitat

def minimal_len(s, f, lista_adiacenta):
    bf = bfs(lista_adiacenta, f)
    path = []
    for i in bf:
        path += [i]
        node, parent = i
        if node == s:
            break
    return path[-1::-1]
    
      

def main():
    file = "graf_in.txt"
    try:
        with open(file) as f:
            cuv = f.readline().strip()
            n = int(f.readline().strip())
            m = int(f.readline().strip())
            lista_muchii = []
            for _ in range(m):
                x, y = f.readline().split()
                lista_muchii.append((int(x), int(y)))
            s = int(f.readline().strip())
            f = int(f.readline().strip())

            g = open("graf_out.txt", 'w')
            for muchie in lista_muchii:
                g.write(f"({muchie[0]}, {muchie[1]}) ")
            g.write("\n")

            list_adiac = liste_adiacenta(cuv, lista_muchii, n)
            for key, value in list_adiac.items():
                g.write(f"{key}: {value}\n")

            g.write("\n")
            matrice = matrice_adiacenta(cuv, lista_muchii, n)

            for line in matrice:
                g.write(" ".join(str(x) for x in line))
                g.write("\n")

            bfs_result = [str(node) for (node, _) in bfs(list_adiac, s)]
            g.write(f"BFS result: {' '.join(bfs_result)}\n")

            dfs_result = dfs(list_adiac, s)
            g.write(f"DFS result: {' '.join(map(str, dfs_result))}\n")

            print(minimal_len(s, f, list_adiac))


    except FileNotFoundError:
        print(f"Fisierul {file} nu exista!")
if __name__ == "__main__":
    main()