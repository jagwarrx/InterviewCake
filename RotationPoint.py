#Modified version of binary search 
# each iteration halves the search space - it's either in this side or that


def find_rotation_point(words):

    # Find the rotation point in the list
    end = len(words) - 1
    start = 0
    left_pointer = 0
    while(start < end):
        middle = (start + end)/2
        if(start + 1 == end):
            return end
        else:
            if(words[middle] < words[left_pointer]):
                end = middle
            else:
                start = middle
        
        
        
