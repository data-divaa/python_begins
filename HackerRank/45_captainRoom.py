'''
Date - 03 - September- 2024
Aurthur - Data-Divaa
Question -
One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of k members per group where k ≠1

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists.
The room numbers will appear k times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of k and the room number list
'''


#defining the function
def captainRoom_dict(k,lst):
    dict = {}
    for i in lst:
        #if i not in dict as key add it and value will be 1 as its count of occurence
        if i not in dict:
            dict[i] = 1
        else:
        #else if already present add 1 to value of that key
            dict[i] += 1

    for room,count in dict.items():
        if count != k:
            print(room)


#taking inputs
k = int(input("enter the number of people in the group :"))
lst = list(map(int,input("enter the list of room number of all member:").split()))


#calling function
captainRoom_dict(k,lst)



#-------------in a different but lenghty way----------


# def captainRoom(k,room_lst):
#     room_set = set(room_lst)
#     for i in room_set:
#         if not((room_lst.count(i) == k)):
#             return i

# k = int(input())
# room_lst = list(map(int,input().split()))

#print(captainRoom(k,room_lst))
