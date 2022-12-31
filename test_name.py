import unittest
from main import *


class TestNames(unittest.TestCase):

    def test_names_equal(self):
        names = Names('names.txt')

        names.sortThroughNames()

        names.writeNamesToFile()

        # get the list of names the file has created
        with open('sorted-names-list.txt', 'r') as sortedNamesList:
            fileContents = sortedNamesList.read()

        # get the answers of the order of names
        with open('exampleAnswerNames.txt', 'r') as answerToExampleNames:
            answerNames = answerToExampleNames.read()

        self.assertEqual(fileContents, answerNames)


    
    

    def test_edgecase_names(self):
        names = Names('edgecaseNames.txt')

        names.sortThroughNames()

        names.writeNamesToFile()

        # get the list of names the file has created
        with open('sorted-names-list.txt', 'r') as sortedNamesList:
            fileContents = sortedNamesList.read()

        # get the answers of the order of names
        with open('edgecaseNamesAnswer.txt', 'r') as answerToExampleNames:
            answerNames = answerToExampleNames.read()

        self.assertEqual(fileContents, answerNames)


    '''
    
    
    def test_large_number_of_names(self):
        names = Names('largeNumberOfNames.txt')

        names.sortThroughNames()

        names.writeNamesToFile()

        
        
        # get the list of names the file has created
        with open('sorted-names-list.txt', 'r') as sortedNamesList:
            fileContents = sortedNamesList.read()

        # get the answers of the order of names
        with open('largeNumberOfNamesAnswer.txt', 'r') as answerToExampleNames:
            answerNames = answerToExampleNames.read()

        self.assertEqual(fileContents, answerNames)
    '''


if __name__ == '__main__':
    unittest.main()
