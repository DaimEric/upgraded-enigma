def sort(list_to_sort, items_to_sort):
    for i in range(len(list_to_sort) - 1):
        swap_index = find_smallest(list_to_sort, i)
        if swap_index != i:
            swap(list_to_sort, swap_index, i, items_to_sort)
    return list_to_sort
    
def find_smallest(in_list, start):
    smallest_pos = start
    for i in range(start + 1, len(in_list)):
        if in_list[i] < in_list[smallest_pos]:
            smallest_pos = i
    return smallest_pos

def swap(swap_in_list, from_index, to_index, items_to_sort):
    temp = swap_in_list[from_index]
    temp2 = items_to_sort[from_index]
    swap_in_list[from_index] = swap_in_list[to_index]
    swap_in_list[to_index] = temp
    items_to_sort[from_index] = items_to_sort[to_index]
    items_to_sort[to_index] = temp2;
    return swap_in_list

price = []
items = []
for i in range(5):
    items += [str(input("Enter item: "))]
    price += [int(input("Enter price: "))]
sort(price, items)
for i in range(5, 0, -1):
    print("Item:" + str(items[i-1]) + " Price:" + str(price[i-1]))
