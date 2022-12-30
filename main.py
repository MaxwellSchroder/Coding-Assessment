# ENUM
import sys

# number of letters in alphabet
numAlphabet = 26
# the offset needed to bring the letter a from 97 to 0th Index for the list of lastname buckets
asciiOffset = 97


class Buckets:
    def __init__(self):
        self.list = []

    # inserting a list (lastname, first names) into the buckets
    def insertInto(self, newName):
        # if the bucket is empty, just add it to the front of the list
        if (len(self.list)) == 0:
            self.list.insert(0, newName)
        # there are other names. Do insertion sort

    def printy(self):
        print(self.list)


class Names:
    def __init__(self):
        self.namesList = []
        for i in range(numAlphabet):
            bucket = Buckets()
            self.namesList.append(bucket)

        #self.namesList = [Buckets] * numAlphabet
        #print(self.namesList)

    def insertNameIntoList(self, index, name):
        self.namesList[index].insertInto(name)
        self.namesList[index].printy()
        print("Inserting %s into %i", name[0], index)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # create class of sorter
    names = Names()
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
                lastName = words[-1]

                # find the index of the last name in the alphabet
                firstLetterIndex = ord(lastName[0]) - asciiOffset

                # rearrange to have lastname first
                words.insert(0, lastName)
                # remove the lastname at the end of the list
                words.pop()

                # insert that name into the bucket
                names.insertNameIntoList(firstLetterIndex, words)
                #print(words)
    #print(names)