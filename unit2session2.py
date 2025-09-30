def cast_vote(votes, candidate):
    if candidate in votes:
        votes[candidate] += 1
    else:
        votes[candidate] = 1
votes = {"Alice": 5, "Bob": 3}
cast_vote(votes, "Alice")
print(votes)
cast_vote(votes, "Gina")
print(votes)

def common_keys(dict1, dict2):
    common = []
    for i in dict1:
        for j in dict2:
            if i == j:
                common.append(i)
    return common
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 4, "c": 5, "d": 6}
common_list = common_keys(dict1, dict2)
print(common_list)

def count_occurrences(nums):
    pass

def contains_duplicate(nums):
    d = {}
    for item in nums:
        d[item] = 0
    for key in d: 
        d[key] += 1
    return d
print(contains_duplicate([1, 2, 3, 4, 1]))

#method in uploaded screenshot doesnt work as expected (more questions were done in breakout rooms)