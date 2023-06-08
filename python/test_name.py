import unittest
from main import *


class TestNames(unittest.TestCase):

    '''
    testing using the example names given on the spec
    '''
    def test_names_equal(self):
        names = Names('exampleNames.txt')

        names.sortThroughNames()

        names.writeNamesToFile()

        # get the list of names the file has created
        with open('sorted-names-list.txt', 'r') as sortedNamesList:
            fileContents = sortedNamesList.read()

        # get the answers of the order of names
        with open('exampleNamesAnswer.txt', 'r') as answerToExampleNames:
            answerNames = answerToExampleNames.read()

        self.assertEqual(fileContents, answerNames)


    
    
    ''' Edgecase names uses atypical names
    '''
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




if __name__ == '__main__':
    unittest.main()
