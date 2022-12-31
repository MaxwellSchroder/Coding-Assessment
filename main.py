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
                return True
            else:
                # if the last names are the same, continue to the next loop
                if newName[i] != listName[i]:
                    return False
        # all other cases fail, they must be identical. Either way it doesn't matter
        return True

    # inserting a list (lastname, first names) into the buckets
    def insertInto(self, newName):
        # if the bucket is empty, just add it to the front of the list
        if (len(self.list)) == 0:
            self.list.insert(0, newName)
        # there are other names. Do insertion sort
        else:
            # insert into correct position by looping through until it is found
            for i in range(len(self.list) + 1):
                # if it has already gone through the entire list, just add it to the end
                if i == len(self.list):
                    self.list.append(newName)
                else:
                    listName = self.list[i]
                    # check names recursively, if true insert at this position
                    if self.compareNames(newName, listName):
                        self.list.insert(i, newName)
                        break

    ''' This functions job is to take a list of an individuals name, which goes surname, then firstnames, and 
    return a string which is the correct way of reading that name. That being firstname, then surname
    '''

    def getNameInOrder(self, nameList):
        nameString = ''
        if len(nameList) > 1:
            # need to add multiple names. Therefore, must correct the order. Do this by indexing from the 2nd Index up
            # until the end of the list. Then add the lastname last
            for i in range(len(nameList) - 1):
                # go through each name, and change order of the first word to the last
                nameString = nameString + nameList[i + 1] + ' '
            nameString = nameString + nameList[0]
        else:
            # just one name to add
            nameString = nameList[0]
        return nameString

    def getBucketNames(self):
        # check if bucket has any names in the first place
        if len(self.list) == 0:
            return ''
        else:
            # there are one or more names to add to our string
            bucketString = ''
            for i in range(len(self.list)):
                singleNameString = self.getNameInOrder(self.list[i])
                bucketString = bucketString + singleNameString + '\n'
            return bucketString


class Names:
    def __init__(self, filePath = None):
        self.namesList = []
        for i in range(numAlphabet):
            bucket = Buckets()
            self.namesList.append(bucket)
        # add a file path for testing
        if filePath is not None:
            self.filePath = filePath
        else:
            self.filePath = ''

    def insertNameIntoList(self, index, name):
        self.namesList[index].insertInto(name)

    def sortThroughNames(self):
        # set of alpha values used in names
        chars = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ-\n ')

        # This block of code is to allow for testing with a given filePath
        if len(self.filePath) > 0:
            nameOfFile = self.filePath
        else:
            nameOfFile = sys.argv[1]

        # read file
        with open(nameOfFile, 'r') as my_file:
            lines = my_file.readlines()
            for line in lines:
                # line = line.lower()
                # check that line only contains alphanumeric characters
                # any((c in chars) for c in s)
                if all((c in chars) for c in line):
                    # Find individual words within the name
                    words = line.split()
                    # check that we have at least 1 word/name
                    if len(words) > 0:
                        lastName = words[-1]

                        # find the index of the last name in the alphabet
                        lowercaseLastname = lastName.lower()
                        firstLetterIndex = ord(lowercaseLastname[0]) - asciiOffset

                        # rearrange to have lastname first
                        words.insert(0, lastName)
                        # remove the lastname at the end of the list
                        words.pop()

                        # insert that name into the bucket
                        self.insertNameIntoList(firstLetterIndex, words)

    '''This function will go through the namesList and write each name correctly to file.
    This involves changing the order of individual names to put the last name back in its correct position
    '''

    def writeNamesToFile(self):
        entireListString = ''
        for bucket in self.namesList:
            # return the string of all names in that bucket, in the correct order
            bucketString = bucket.getBucketNames()
            if len(bucketString) > 0:
                entireListString = entireListString + bucketString
        # remove final \n from string

        with open('sorted-names-list.txt', 'w') as f:
            f.write(entireListString[:-1])
        print(entireListString)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create class of sorter
    names = Names()

    names.sortThroughNames()

    names.writeNamesToFile()

    # TESTING
