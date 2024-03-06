if __name__ == '__main__':
    # Lists in python
    thislist = [3,4,6,8,'abc', 'def','ghi']

    # Append
    thislist.append(4)

    # Extend
    thislist.extend([5,6,7])
    print(thislist)

    # add items using append for loop
    for x in range(7,15):
        thislist.append(x)
    print(thislist)

    # insert items
    thislist.insert(1,'inserted')
    print(thislist)

    # Remove item
    thislist.remove('inserted')
    print(thislist)

    # pop items
    thislist.pop(1)
    print(thislist)

    # Slice
    print(thislist[1:4])

    # Print length
    print(len(thislist))

    # count
    print(thislist.count(5))

    # concatenate join
    thislist1 = [1,2,3]
    thislist2 = [4,5,6]
    print(thislist1+thislist2)

    # Multiply
    print(thislist1*2)

    # print the
    print(thislist.index('item1'))

    # sort or
    thislist1 = [5,3,2,0,1]
    thislist1.sort()
    print(thislist1)
