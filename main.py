# ENUM
import sys

# number of letters in alphabet
numAlphabet = 26
# the offset needed to bring the letter a from 97 to 0th Index for the list of lastname buckets
asciiOffset = 97

class Buckets:
    def __init__(self):
        self.list = []

    def getList(self):
        return self.list.copy()

    '''
    This function takes the new name to be inserted and a name in the list
    it iterates through the new name and compares the ascii ordering of them.
    In the case of the new name being longer than the listName, the shorter name will go first
    '''
    def compareNames(self, newName, listName):
        for i in range(len(newName)):
            # if the listName has fewer words in it up to this point, it goes first
            if i > len(listName):
                return False
            # compare the new word to the word in listName, if it is smaller than it goes first
            if newName[i] < listName[i]:
                #print("Name {} is before {} ".format(newName[i], listName[i]))
                return True
            else:
                return False

        # all other cases fail, they must be identical. Either way it doesn't matter
        return True

    # inserting a list (lastname, first names) into the buckets
    def insertInto(self, newName):
        # if the bucket is empty, just add it to the front of the list
        if (len(self.list)) == 0:
            self.list.insert(0, newName)
            print("First word insert")
        # there are other names. Do insertion sort
        else:
            # insert into correct position by looping through until it is found
            for i in range(len(self.list) + 1):
                print(i)
                # if it has already gone through the entire list, just add it to the end
                if i == len(self.list):
                    self.list.append(newName)
                    print("this one")
                else:
                    listName = self.list[i]
                    # check names recursively, if true insert at this position
                    if self.compareNames(newName, listName):
                        print("Inserting {} before {}".format(newName, listName))
                        self.list.insert(i, newName)
                        break

    def printy(self):
        if (len(self.list) > 0):
            print(self.list)


class Names:
    def __init__(self):
        self.namesList = []
        for i in range(numAlphabet):
            bucket = Buckets()
            self.namesList.append(bucket)

    def insertNameIntoList(self, index, name):
        self.namesList[index].insertInto(name)
        print("Inserting {} into {}".format(name[0], index))
        #self.namesList[index].printy()

    def printOrderedNames(self):
        for i in range(len(self.namesList)):
            self.namesList[i].printy()

    def sortThroughNames(self):
        # set of alpha values used in names
        chars = set('abcdefghijklmnopqrstuvwxyz-\n ')

        # read file
        with open(sys.argv[1], 'r') as my_file:
            lines = my_file.readlines()
            for line in lines:
                line = line.lower()
                # check that line only contains alphanumeric characters
                # any((c in chars) for c in s)
                if all((c in chars) for c in line):
                    # Find individual words within the name
                    words = line.split()
                    # check that we have at least 1 word/name
                    if len(words) > 0:
                        lastName = words[-1]

                        # find the index of the last name in the alphabet
                        firstLetterIndex = ord(lastName[0]) - asciiOffset

                        # rearrange to have lastname first
                        words.insert(0, lastName)
                        # remove the lastname at the end of the list
                        words.pop()

                        # insert that name into the bucket
                        self.insertNameIntoList(firstLetterIndex, words)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create class of sorter
    names = Names()

    names.sortThroughNames()


    names.printOrderedNames()