import random

#Method to increment global counter

#Node Functions
class Node(object):
    # Constructor
    def __init__(self, item, next=None):  
        self.item = item
        self.next = next 
        
#List Functions
class List(object):   
    # Constructor
    def __init__(self): 
        self.head = None
        self.tail = None
        
def IsEmpty(L):  
    return L.head == None     
        
def Append(L,x): 
    # Inserts x at end of list L
    if IsEmpty(L):
        L.head = Node(x)
        L.tail = L.head
    else:
        L.tail.next = Node(x)
        L.tail = L.tail.next
        
def Print(L):
    # Prints list L's items in order using a loop
    temp = L.head
    while temp is not None:
        print(temp.item, end=' ')
        temp = temp.next
    print()  # New line 
    
def ElementAt(L,i):
    #Finds the element stored at index i in list L
     if IsEmpty(L):
         return None
     else:
         temp = L.head
         count = 0
         while count < i:
             temp = temp.next
             count+= 1
         return temp.item

def GetLength(L):
    #Returns the length of list L
    temp = L.head
    count = 0
    while temp is not None:
        count+= 1
        temp = temp.next
    return count

def RandomList(i):
    #Creates a list of random int values from 1-100 with length i
    L = List()
    for n in range(i):
        Append(L,random.randint(1,101))
    return L

def Copy(L):
    #Creates a copy of list L
    C = List()
    temp = L.head
    while temp is not None:
        Append(C, temp.item)
        temp = temp.next
    return C
        
def ListMerge(L1, L2):
    #Merges lists L1 and L2 into a single linked list in ascending order
    if L1 is None:
        return L2
    if L2 is None:
        return L1
    if(L1.item<L2.item):
        L1.next = ListMerge(L1.next,L2)
        increment()
        return L1
    else:
        L2.next = ListMerge(L1,L2.next)
        increment()
        return L2

def Concate(L1,L2):
    #Attaches the head of list L2 to the end of list L1
    if L1.head is None:
        return L2
    if L2.head is None:
        return L1
    temp = L1.head
    while temp.next is not None:
        temp = temp.next
    temp.next = L2.head
    return L1

def BubbleSortMedian(L):
    #Method that returns the median value of a list sorted using bubble sort
    C = Copy(L)
    BubbleSort(C)
    return ElementAt(C,GetLength(C)//2)

def BubbleSort(L):
    #Sorts linked list L using bubble sort algorithm
    if IsEmpty(L):
        return
    sortDone = False
    while sortDone is False:
        sortDone = True
        temp = L.head
        while temp.next is not None:
            if temp.next.item<temp.item:
                #Swaps values in a list if one value is greater than the value
                #in front of it
                swap = temp.item
                temp.item = temp.next.item
                temp.next.item = swap
                sortDone = False
            temp = temp.next
            increment()

#Method that returns the median value of a list sorted using merge sort
def MergeSortMedian(L):
    C = Copy(L)
    MergeSort(C)
    return ElementAt(C,GetLength(C)//2)

def MergeSort(L):
    #Sorts linked list L using merge sort algorithm
    if IsEmpty(L):
        return
    temp = L.head
    if GetLength(L)>1:
        L1 = List()
        L2 = List()
        for i in range(GetLength(L)//2):
            #Creates a new list with first half of list L
            Append(L1,temp.item)
            temp = temp.next
        for i in range(GetLength(L)-GetLength(L)//2):
            #Creates a new list with second half of list L
            Append(L2,temp.item)
            temp = temp.next
        #Recursive calls of method "MergeSort" using newly created lists
        MergeSort(L1)
        MergeSort(L2)
        #Stores new list created from "ListMerge" method
        L.head = ListMerge(L1.head,L2.head)

#Method that returns the median value of a list sorted using quicksort
def QuicksortMedian1(L):
    C = Copy(L)
    Quicksort1(C)
    return ElementAt(C,GetLength(C)//2)

#Sorts linked list L using quicksort algorithm
def Quicksort1(L):
    if IsEmpty(L):
        return
    if GetLength(L)>1:
        L1 = List()
        L2 = List()
        pivot = L.head.item
        L.head = L.head.next
        while L.head is not None:
            #Creates new lists by comparing values in L.head to value in pivot
            if L.head.item<pivot:
                Append(L1,L.head.item)
                increment()
            elif L.head.item>=pivot:
                Append(L2,L.head.item)
                increment()
            L.head = L.head.next
        Append(L1,pivot)
        increment()
        #Recursive calls of method "Quicksort1" using newly created lists
        Quicksort1(L1)
        Quicksort1(L2)
        #Combines lists L1 and L2 using method "Concate"
        Concate(L1,L2)
        L.head = L1.head

#Method that returns the median value of a list sorted using alternate
#quicksort
def QuicksortMedian2(L):
    C = Copy(L)
    Quicksort2(C)
    return ElementAt(C,GetLength(C)//2)

#Sorts list L using alternate quicksort
def Quicksort2(L):
    if IsEmpty(L):
        return
    if GetLength(L)>1:
        L1 = List()
        L2 = List()
        pivot = L.head.item
        L.head = L.head.next
        while L.head is not None:
            #Creates new lists by comparing values in L.head to value in pivot
            if L.head.item<pivot:
                increment()
                Append(L1,L.head.item)
            elif L.head.item>=pivot:
                increment()
                Append(L2,L.head.item)
            L.head = L.head.next
        Append(L1,pivot)
        increment()
        #Recursive calls for "Quicksort2" based on if else conditions
        if GetLength(L1)>=GetLength(L2):
            Quicksort2(L1)
        else:
            Quicksort2(L2)
        #Combines lists L1 and L2 using method "Concate"
        Concate(L1,L2)
        L.head = L1.head

#Global counter
count = 0

#Increments global counter by 1
def increment():
    global count
    count = count+1

#Resets global counter    
def reset():
    global count
    count = 0

#Main Method
L = List()
L = RandomList(1000)
print('Random List:')
Print(L)
print()

print('Initial count: ',count)
print('Bubble Sort Median: ',BubbleSortMedian(L))
print('Final counter: ',count)
reset()
print()

print('Initial count: ',count)
print('Merge Sort Median: ',MergeSortMedian(L))
print('Final counter: ',count)
reset()
print()

print('Initial count: ',count)
print('Quicksort 1 Median: ',QuicksortMedian1(L))
print('Final counter: ',count)
reset()
print()

print('Initial count: ',count)
print('Quicksort 2 Median: ',QuicksortMedian2(L))
print('Final counter: ',count)
reset()
print()
