

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
        for u, char, stack_output, v, stack_input in edges:
            self.add_edge(u, char, stack_output, v, stack_input)

    def add_edge(self, u, char, stack_output, v, stack_input):
        stack = str(stack_output+","+stack_input)
        if str(char) not in self.vertices[str(u)]:
            self.vertices[str(u)][str(char)] = {}
        if str(stack) not in self.vertices[str(u)][str(char)]:
            self.vertices[str(u)][str(char)][str(stack)] = []
        self.vertices[str(u)][str(char)][str(stack)].append(v)
        if not self.orientated:
            if str(stack) not in self.vertices[str(v)][str(char)]:
                self.vertices[str(v)][str(char)][stack] = []
            self.vertices[str(v)][str(char)][stack].append(u)

    def get_destiny_vertices_with(self, u, char):
        try:
            result = self.vertices.get(str(u)).get(str(char))
            return result if result is not None else {}
        except KeyError:
            return {}

    def __len__(self):
        return len(self.vertices)

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self.vertices))

    def __getitem__(self, v):
        return self.vertices[v]


def verify_lambda_ways(afdn, actual_state, end_state_set):
    vertices_lambda = afdn.get_destiny_vertices_with(actual_state, "*")
    for key in vertices_lambda.keys():
        stack_output, stack_input = str(key).split(",")
        if stack_output == "*" and stack_input == "*":
            states = vertices_lambda[key]
            for state in states:
                if state in end_state_set:
                    return "S"


def process(afdn, stack_output, stack_input, tmp_stack, tmp_characters, processing_stack, end_state_set, states):
    valid_way = True
    if stack_output != "*":
        if len(tmp_stack) > 0:
            top = tmp_stack.pop()
            if top != stack_output:
                tmp_stack.append(top)
                valid_way = False
        else:
            valid_way = False
    if valid_way and stack_input != "*":
        tmp_stack_input = [*stack_input]
        for to_add in tmp_stack_input:
            tmp_stack.append(to_add)
    if valid_way and len(tmp_stack) == 0 and len(tmp_characters) == 0:
        for state in states:
            if state in end_state_set:
                return "S"
            if verify_lambda_ways(afdn, state, end_state_set) == "S":
                return "S"
        return "N"
    elif valid_way:
        for state in states:
            new_process = (state, tmp_characters, tmp_stack)
            processing_stack.append(new_process)
    return None


def verify_word(afdn, word, start_state, end_state_set):
    processing_stack = [(start_state, list(word.strip()), [])]
    while processing_stack:
        actual_process = processing_stack.pop()
        actual_state = actual_process[0]
        characters = actual_process[1]
        stack = actual_process[2]
        actual_char = "*" if len(characters) == 0 else characters[0]
        vertices = afdn.get_destiny_vertices_with(actual_state, actual_char)
        for key in vertices.keys():
            tmp_stack = stack.copy()
            stack_output, stack_input = str(key).split(",")
            states = vertices[key]
            tmp_characters = characters[1:]
            result = process(afdn, stack_output, stack_input, tmp_stack,
                             tmp_characters, processing_stack, end_state_set, states)
            if result == "S":
                return result

        vertices = afdn.get_destiny_vertices_with(actual_state, "*")
        for key in vertices.keys():
            tmp_stack = stack.copy()
            stack_output, stack_input = str(key).split(",")
            states = vertices[key]
            tmp_characters = characters.copy()
            result = process(afdn, stack_output, stack_input, tmp_stack,
                             tmp_characters, processing_stack, end_state_set, states)
            if result is not None:
                return result
    return "N"


def start(states, alphabet, stack_alphabet, edges, start_state, end_state_List, words):
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
    stack_alphabet = input().split(" ")
    states_number = int(input())
    edges = []
    for i in range(states_number):
        edge = input().split(" ")
        edges.append((edge[0], edge[1], edge[2], edge[3], edge[4]))
    start_state = input()
    end_state_list = input().split(" ")
    words = input().split(" ")
    for result in start(states, alphabet, stack_alphabet, edges, start_state, end_state_list, words):
        print(result)
