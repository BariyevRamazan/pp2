def unique_elements(list):
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

list = list(map(int,input().split()))
result = unique_elements(list)
print(result)
