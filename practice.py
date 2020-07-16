def test_thing(N, trust):
    town = {}

    for i in range(1, N + 1):
        town[i] = {"you": i}
    print(town)

    for item in trust:
        if item[0] in town.keys():
            # print(f"{item[0]} trusts {item[1]}")
            town.pop(item[0], None)
        elif item[1] in town.keys():
            # print(f"{item[1]} is trusted by {item[0]}")
            obj = town[item[1]]
            obj[item[0]] = [item[0]]

    for item in town.values():
        print(item)
        print(len(item))
        if len(item) == N:
            return item["you"]

    # return - 1


print(test_thing(2, [[1, 2]]))
