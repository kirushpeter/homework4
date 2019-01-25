myUniqueList = []

myLeftovers = []

def addItemToList(item):

    ''' object.__contains__ is Called to implement membership test operators.
      Should return true if item is in self, false otherwise.
      For mapping objects, this should consider the keys of the
      mapping rather than the values or the key-item pairs.'''

    if(myUniqueList. __contains__(item)):

         myLeftovers.append(item)

         return False
         
    else:

        myUniqueList.append(item)

        return True

addItemToList('CLASS ONE')
addItemToList(2)
addItemToList('CLASS 3')
addItemToList(4)
addItemToList('CLASS 5')
addItemToList('6')

print(myUniqueList)

print(myLeftovers)

addItemToList('CLASS ONE')
addItemToList('CLASS 8')
addItemToList('6')
addItemToList('CLASS 5')
addItemToList('CLASS 7')
addItemToList('4')

print(myUniqueList)

print(myLeftovers)
