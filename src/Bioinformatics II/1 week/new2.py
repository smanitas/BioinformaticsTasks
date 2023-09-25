class AdjNode:
    def __init__(self, value):
        self.vertex = value
        self.next = None


class Graph:
    def __init__(self, num):
        self.V = num
        self.graph = [None] * self.V

    # Add edges
    def add_edge(self, s, d):
        node = AdjNode(d)
        node.next = self.graph[s]
        self.graph[s] = node

        node = AdjNode(s)
        node.next = self.graph[d]
        self.graph[d] = node

    def is_valid(self, v, pos, path):
        # Проверяем, можно ли добавить вершину v в путь
        if not self.graph[path[pos - 1]]:
            return False

        # Проверяем, была ли вершина v уже посещена
        if v in path[:pos]:
            return False

        return True

    def hamiltonian_cycle_util(self, pos, path):
        if pos == self.V:
            # Проверяем, соединена ли последняя вершина с начальной
            if self.graph[path[pos - 1]]:
                # Выводим гамильтонов цикл
                cycle = '>'.join(map(str, path + [path[0]]))
                return cycle
            else:
                return None

        # Пробуем все вершины в качестве следующей вершины
        for v in range(1, self.V):
            if self.is_valid(v, pos, path):
                path[pos] = v

                # Рекурсивно ищем гамильтонов цикл
                cycle = self.hamiltonian_cycle_util(pos + 1, path)
                if cycle:
                    return cycle

                # Откатываемся, если текущая вершина не ведет к решению
                path[pos] = -1

        return None

    def find_hamiltonian_cycles(self):
        # Создаем массив для хранения пути
        path = [-1] * self.V

        # Начинаем с вершины 1
        path[0] = 1

        # Находим все гамильтоновы циклы, начинающиеся с вершины 1
        cycles = []
        while True:
            cycle = self.hamiltonian_cycle_util(1, path)
            if cycle:
                cycles.append(cycle)
            else:
                break
        return cycles


if __name__ == "__main__":
    V = 5

    # Create graph and edges
    graph = Graph(V)
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 5)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 1)
    graph.add_edge(3, 2)
    graph.add_edge(3, 5)
    graph.add_edge(4, 1)
    graph.add_edge(4, 3)
    graph.add_edge(5, 2)
    graph.add_edge(5, 4)

    # Находим и выводим все гамильтоновы циклы
    cycles = graph.find
