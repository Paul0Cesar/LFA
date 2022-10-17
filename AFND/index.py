
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
        if str(way) not in self.vertices[str(u)]:
            self.vertices[str(u)][str(way)] = []
        self.vertices[str(u)][str(way)].append(v)
        if not self.orientated:
            self.vertices[str(v)][str(way)].append(u)

    def get_destiny_vertices_with(self, u, way):
        try:
            result = self.vertices.get(str(u)).get(str(way))
            return result if result is not None else []
        except KeyError:
            return []

    def __len__(self):
        return len(self.vertices)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.vertices))

    def __getitem__(self, v):
        return self.vertices[v]


def verify_word(afdn, word, start_state, end_state_set):
    characters = list(word.strip())
    current_state = start_state
    stack = [start_state]
    depth = 0
    visited = {}
    while len(stack) > 0:
        tmp_characters = characters[depth:]
        actual_word = str(''.join(tmp_characters))
        if actual_word not in visited:
            visited[actual_word] = []
        actual_state = stack.pop()
        if len(tmp_characters) > 0:
            vertices = afdn.get_destiny_vertices_with(
                actual_state, tmp_characters[0])
            if len(vertices) > 0:
                new = [x for x in vertices if x not in visited[actual_word]]
                if len(new) > 0:
                    depth = depth+1
                    stack.append(actual_state)
                    stack.append(new[0])
                else:
                    depth = depth-1
                    if len(tmp_characters) == len(characters):
                        visited = {}
                    else:
                        tmp_characters = characters[depth:]
                        actual_word = str(''.join(tmp_characters))
                        visited[actual_word].append(actual_state)
            else:
                current_state = None
                depth = depth-1
                tmp_characters = characters[depth:]
                actual_word = str(''.join(tmp_characters))
                if actual_word not in visited:
                    visited[actual_word] = []
                visited[actual_word].append(actual_state)
        else:
            if actual_state in end_state_set:
                current_state = actual_state
                break
            else:
                current_state = None
                depth = depth-1
                tmp_characters = characters[depth:]
                actual_word = str(''.join(tmp_characters))
                visited[actual_word].append(actual_state)
    return "S" if current_state in end_state_set else "N"


def start(states, alphabet, edges, start_state, end_state_List, words):
    graph = Graph(states)
    graph.set_edges(edges)
    result = []
    for word in words:
        result.append(verify_word(
            graph, word, start_state, set(end_state_List)))
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
