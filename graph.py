import networkx as nx
from pyvis.network import Network



# definimos el grafo
def graph():
    G = nx.Graph()

    # agregar vertices/aristas
    G.add_edge('Salones posgrado', 'Cancha posgrados', weight=2)
    G.add_edge('Salones posgrado', 'Parqueadero posgrados', weight=1)
    G.add_edge('Parqueadero posgrados', 'Planta de lacteos', weight=3)
    G.add_edge('Planta de lacteos', 'Parqueadero ing1', weight=1)
    G.add_edge('Parqueadero ing1', 'Administrativo', weight=1)
    G.add_edge('Parqueadero ing1', 'Lab quimica', weight=3)
    G.add_edge('Parqueadero ing1', 'Lab sistemas', weight=1)
    G.add_edge('Administrativo', 'Parqueadero principal', weight=3)
    G.add_edge('Biblioteca', 'Parqueadero principal', weight=2)
    G.add_edge('Lab quimica', 'Parqueadero principal', weight=3)
    G.add_edge('Parqueadero principal', 'Preu', weight=3)
    G.add_edge('Parqueadero principal', 'Counillanos', weight=2)
    G.add_edge('Lab sistemas', 'Parqueadero ing2', weight=3)
    G.add_edge('Lab quimica', 'Parqueadero ing2', weight=2)
    G.add_edge('Einstein', 'Parqueadero ing2', weight=1)
    G.add_edge('Lab biotec', 'Parqueadero ing2', weight=3)
    G.add_edge('Fcbi', 'Parqueadero ing2', weight=2)
    G.add_edge('Comedor', 'Fcbi', weight=3)
    G.add_edge('Preu', 'Comedor', weight=1)
    G.add_edge('Lab biotec', 'Lab anatomia', weight=2)
    G.add_edge('Lab anatomia', 'Agronomia', weight=1)
    G.add_edge('Counillanos', 'Lab clinico', weight=1)
    G.add_edge('Lab clinico', 'Entrada 2', weight=2)
    G.add_edge('Lab electronica', 'Entrada 2', weight=1)
    G.add_edge('Licenciatura', 'Lab electronica', weight=1)
    G.add_edge('Licenciatura', 'Almacen', weight=1)
    G.add_edge('Licenciatura', 'Paradero de bus', weight=3)
    G.add_edge('Lab fisiologia', 'Almacen', weight=1)
    G.add_edge('Lab fisiologia', 'Entrada 2', weight=3)
    G.add_edge('Clinica veterinaria', 'Lab fisiologia', weight=1)
    G.add_edge('Piscina', 'Almacen', weight=1)
    G.add_edge('Counillanos', 'Audiovisuales 1', weight=1)
    G.add_edge('Audiovisuales 1', 'Lab biologia', weight=1)
    G.add_edge('Lab biologia', 'Paradero de bus', weight=4)
    G.add_edge('Lab biologia', 'Comedor', weight=1)
    G.add_edge('Piscina', 'Paradero de bus', weight=2)
    G.add_edge('Alm bienestar', 'Paradero de bus', weight=3)
    G.add_edge('Alm bienestar', 'Coliseo', weight=2)
    G.add_edge('Coliseo', 'Cancha', weight=1)
    G.add_edge('Lab biotec', 'Cancha', weight=3)
    G.add_edge('Cultivos', 'Cancha', weight=2)
    G.add_edge('Cultivos', 'Vivero', weight=2)
    G.add_edge('Criaderos', 'Cultivos', weight=1)
    
    return G


def showGraph(G):
    #Dibujando el grafo en base a la lista de posiciones y asignando a los atributos a las aristas
    nt = Network('500px','500px')
    nt.from_nx(G)
    #nt.show('grafo.html')
 

    
def shortestPath(G, u):
    #Lista con los puntos de encuentro
    listControlPoint = ['Cancha posgrados', 'Parqueadero posgrados', 
                        'Parqueadero ing1', 'Parqueadero principal', 'Parqueadero ing2',
                        'Lab anatomia', 'Entrada 2', 'Almacen', 'Paradero de bus', 'Cancha', 'Vivero']
    listweightPath = list()
    
    #Obteniendo el "peso" de cada punto de control desde el punto de inicio y guardandolo en una lita
    for x in listControlPoint:
        aux = nx.dijkstra_path_length(G, source=u, target=x, weight='weight')
        listweightPath.append(aux)
    
    #Retornando el camino mas corto teniendo en cuenta cual fue el de menor 
    pos = listweightPath.index(min(listweightPath))
    print("El camino mas corto es: ", nx.dijkstra_path(G, u, listControlPoint[pos] , True) )
    print("El costo del cammino es: ", min(listweightPath))
   

    