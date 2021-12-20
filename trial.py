def quick_sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()
    print(pivot)
    lis1 = [1,2,3,4,5]
    lis2 = lis1.pop()
    print(lis2)
    print(lis1)

quick_sort([2,1,0,8,7,10])
