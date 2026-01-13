def append(list1, list2):
    combined = []
    for item in list1:
        combined.append(item)
    for item in list2:
        combined.append(item)
    return combined


def concat(lists):
    combined = []
    for sublist in lists:
        for item in sublist:
            combined.append(item)
    return combined


def filter(function, list):
    filtered = []
    for item in list:
        if function(item):
            filtered.append(item)
    return filtered


def length(list):
    count = 0
    for _ in list:
        count += 1
    return count


def map(function, list):
    mapped = []
    for item in list:
        mapped.append(function(item))
    return mapped


def foldl(function, list, initial):
    acc = initial
    for item in list:
        acc = function(acc, item)
    return acc


def foldr(function, list, initial):
    acc = initial
    for item in reverse(list):
        acc = function(acc, item)
    return acc


def reverse(list):
    reversed_list = []
    index = length(list) - 1
    while index >= 0:
        reversed_list.append(list[index])
        index -= 1
    return reversed_list
