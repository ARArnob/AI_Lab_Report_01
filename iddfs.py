class Node:
    def __init__(self, x, y, level, path_history = None):
        self.x, self.y, self.level = x, y, level
        self.path_history = path_history if path_history is not None else []
    
class IDDFS:
    def __init__(self):
        self.found = False
        self.directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.winning_Path = []
    
    def init(self):
        graph = []
        self.grid_x, self.grid_y = map(int, input().split())
        for i in range(self.grid_x):
            row = list(map(int, input().split()))
            graph.append(row)
        
        sx, sy = map(int, input("Start: ").split())
        gx, gy = map(int, input("Target: ").split())

        self.source = Node(sx, sy, 0, [(sx, sy)])
        self.goal = Node(gx, gy, float('inf'))

        for limit in range(self.grid_x * self.grid_y):
            if self.st_iddfs(graph, limit):
                break
        if self.found:
            print(f"Path found at depth {self.goal.level} using IDDFS")
            print(f"Traversal Order: {self.winning_Path}")
        else:
            print(f"Path not found at max depth {self.grid_x * self.grid_y} using IDDFS")
    
    def st_iddfs(self, graph, limit):
        stack = [self.source]
        visited = {(self.source.x, self.source.y):0}

        while stack:
            u = stack.pop()
            if u.x == self.goal.x and u.y == self.goal.y:
                self.found = True
                self.goal.level = u.level
                self.winning_Path = u.path_history
                return True
            if u.level < limit:
                for dx, dy in self.directions:
                    v_x, v_y = u.x + dx, u.y + dy
                    v_level = u.level + 1
                    if 0 <= v_x < self.grid_x and 0 <= v_y < self.grid_y and graph[v_x][v_y] == 0:
                        if (v_x, v_y) not in visited or v_level < visited[(v_x, v_y)]:
                            visited[(v_x, v_y)] = v_level
                            new_Path = u.path_history + [(v_x, v_y)]
                            child = Node(v_x, v_y, v_level, new_Path)
                            stack.append(child)
        return False

if __name__ == "__main__":
    iddfs = IDDFS()
    iddfs.init()