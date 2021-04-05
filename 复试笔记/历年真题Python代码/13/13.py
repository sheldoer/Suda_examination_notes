def _2013():
    """
    `2013`年复试上机题
    **要求：**
    * **Introduction**
      The project will read flight data from an input file and flight path requests from another input file
      and output the required information.
    * **Your Task**
      Your program should determine ***if a particular destination airport can be reached from
      a particular originating airport within a particular number of hops.
    ***
      A hop (leg of a flight) is a flight from one airport to another on the path between
      an originating and destination airports.
      For example, the flight plan from `PVG` to `PEK` might be `PVG -> CAN -> PEK`.
      So `PVG -> CAN` would be a hop and `CAN -> PEK` would be a hop.
    * **Input Data Files**
      * Path Input File(`PathInput.txt`)

        This input file will consist of a number of single origination/destination airport pairs
         (direct flights).The first line of the file will contain an integer representing the total
         number of pairs in the rest of the file.
        ```
        6
        [PVG, CAN]
        [CAN, PEK]
        [PVG, CTU]
        [CTU, DLC]
        [DLC, HAK]
        [HAK, LXA]
        ```
      * Path Request File(`PathRequest.txt`)
        This input file will contain a sequence of pairs of origination/destination airports and
        a max number of hops. The first line of the file will contain an integer representing the
        number of pairs in the file.
        ```
        2
        [PVG, DLC, 2]
        [PVG, LXA, 2]
        ```
      * Output File(`Output.txt`)
        For each pair in the Path Request File, your program should output
        the pair followed by `YES` or `NO` indicating that it is possible
        to get from the origination to destination airports within the max number
        of hops or it is not possible, respectively.
        ```
        [PVG, DLC, YES]
        [PVG, LXA, NO]
        ```
      * **Assumptions you can make:**
      You may make the following simplifying assumptions in your project:
      * `C/C++` is allowed to be used.
      * All airport codes will be `3` letters and will be in all caps
      * Origination/destination pairs are unidirectional. To indicate that both directions
      of flight are possible, two entries would appear in the file. For example,
      `[PVG, PEK]` and `[PEK, PVG]` would have to be present in the file to indicate
      that one could fly from `Shanghai` to `Beijing` and from `Beijing` to `Shanghai`.
      **程序：**
    """

    def read_file():
        with open('PathInput.txt') as file:
            content = file.read().split('\n')
        with open('PathRequest.txt') as file:
            request = file.read().split('\n')
        path, req = [], []
        for i in content[1:]:
            if i:
                a, b = list(map(lambda x: x.strip(), i.strip(' []').split(',')))
                path.append((a, b))
        for i in request[1:]:
            if i:
                a, b, c = list(map(lambda x: x.strip(), i.strip(' []').split(',')))
                req.append((a, b, int(c)))
        return path, req

    def create_map(data: list):
        dic = {}
        for a, b in data:
            dic[a] = dic.get(a, [])
            dic.get(a).append((b))
        return dic

    def init_visit(data: list):
        visit = {}
        for a, b in data:
            visit[a] = 0
            visit[b] = 0
        return visit

    def dfs(visit: dict, graph: dict, start: str, end: str, deep: int):
        if deep == 0:
            return False
        if start == end:
            return True
        ls = graph.get(start)
        print(start, deep)
        visit[start] = 1
        if ls:
            for item in ls:
                if visit[item] == 0 and dfs(visit, graph, item, end, deep - 1):
                    return True
        return False

    def write_to_file(ls):
        with open('Output.txt', 'w') as file:
            file.write('\n'.join(ls))

    city_sites, require_path = read_file()
    map_c = create_map(city_sites)
    answer = []
    for start, end, hops in require_path:
        visited = init_visit(city_sites)
        flag = dfs(visited, map_c, start, end, hops + 1)
        result = '[{}, {}, {}]'.format(start, end, 'Yes' if flag else 'No')
        answer.append(result)
    write_to_file(answer)
