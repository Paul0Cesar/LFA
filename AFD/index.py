
class Graph(object):

    def __init__(self, vertices, orientated=True):
        self.vertices = {}
        for vertice in vertices:
            self.vertices[vertice] = {}
        self.orientated = orientated

    def get_vertices(self):
        return list(self.vertices.keys())

    def print_edges(self):
        for u in self.vertices.keys():
            for edge in self.vertices[u]:
                print(u, edge)

    def set_edges(self, edges):
        for u, way, v in edges:
            self.add_edge(u, way, v)

    def add_edge(self, u, way, v):
        self.vertices[str(u)][str(way)] = v
        if not self.orientated:
            self.vertices[str(v)][str(way)] = u

    def get_destiny_vertice_with(self, u, way):
        try:
            return self.vertices[str(u)][str(way)]
        except KeyError:
            return None

    def __len__(self):
        return len(self.vertices)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.vertices))

    def __getitem__(self, v):
        return self.vertices[v]


def verify_word(afd, word, start_state, end_state_list):
    characters = list(word.strip())
    current_state = start_state
    for char in characters:
        vertice = afd.get_destiny_vertice_with(current_state, char)
        if (vertice is not None):
            current_state = vertice
        else:
            current_state = None
            break
    try:
        end_state_list.index(current_state)
        return "S"
    except ValueError:
        return "N"


def start(states, alphabet, edges, start_state, end_state_list, words):
    graph = Graph(states)
    graph.set_edges(edges)
    result = []
    for word in words:
        result.append(verify_word(graph, word, start_state, end_state_list))
    return result


if __name__ == "__main__":
    states = input().split(" ")
    alphabet = input().split(" ")
    states_number = int(input())
    edges = []
    for i in range(states_number):
        edge = input().split(" ")
        edges.append((edge[0], edge[1], edge[2]))
    start_state = input()
    end_state_list = input().split(" ")
    words = input().split(" ")
    for result in start(states, alphabet, edges, start_state, end_state_list, words):
        print(result)
