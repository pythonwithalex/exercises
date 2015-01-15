# write a function that takes two sorted lists and merges them into a single sorted list

def merge(list_a,list_b):

    merged_list = []
    
    # reversed the lists so i can use the pop value
    a_index, b_index = len(list_a)-1,len(list_b)-1

    while True:
        if not list_a:
        
            # remembering to reverse the list back to correct order
            merged_list.extend([i for i in list_b][::-1])
            break

        if not list_b:
            # remembering to reverse the list back to correct order
            merged_list.extend([i for i in list_a][::-1])
            break

        elif list_a[a_index] > list_b[b_index]:
            merged_list.append(list_a.pop())
            a_index -= 1

        elif list_b[b_index] > list_a[a_index]:
            merged_list.append(list_b.pop())
            b_index -= 1

        elif list_a[a_index] == list_b[b_index]:
            merged_list.append(list_a[a_index])
            merged_list.append(list_b[b_index])
            a_index -= 1
            b_index -= 1

    return merged_list


def get_lists():
    lists = []
    a_raw = raw_input("please enter the first comma-separated list of numbers")
    b_raw = raw_input("please enter the second comma-separated list of numbers")

    for l in [a_raw,b_raw]:
        processed_list = [ int(n.strip()) for n in l.split(',')]
        processed_list.sort(reverse=True)
        # so i can use the pop value 
        processed_list.reverse()
        lists.append(processed_list)

    return lists

l,m = get_lists()
print l,m
print merge(l,m)
