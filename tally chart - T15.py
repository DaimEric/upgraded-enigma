def sort(list_to_sort, candidates_to_sort):
    for i in range(len(list_to_sort) - 1):
        swap_index = find_smallest(list_to_sort, i)
        if swap_index != i:
            swap(list_to_sort, swap_index, i, candidates_to_sort)
    return list_to_sort
def find_smallest(in_list, start):
    smallest_pos = start
    for i in range(start + 1, len(in_list)):
        if in_list[i] < in_list[smallest_pos]:
            smallest_pos = i
    return smallest_pos
def swap(swap_in_list, from_index, to_index, candidates_to_sort):
    temp = swap_in_list[from_index]
    temp2 = candidates_to_sort[from_index]
    swap_in_list[from_index] = swap_in_list[to_index]
    swap_in_list[to_index] = temp
    candidates_to_sort[from_index] = candidates_to_sort[to_index]
    candidates_to_sort[to_index] = temp2;
    return swap_in_list
candidates = []
tally = []
for i in range (5):
    candidates += [(str[a, b ,c , d, e])]
    tally += [int(input("Enter nubmer of votes for: "))]
sort(tally, cndidates)
for i in range (5, 0, -1):
    print ("Candidate:" + str(candidates[i-1]) + "Votes:" + str(tally[i-1]))
