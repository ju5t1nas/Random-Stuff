#A function for Finding Max Value Indexes in a Matrix

#What to import from numpy
from numpy import array
from numpy import max
from numpy import where
from numpy import asarray
from numpy import transpose


#This function takes in either a Matrix in a form of List of Lists or Numpy array.
#It returns a list of indexes in form of list of lists.
def maxIndexes(Matrix):
    #We either turn a list in to an array or just make sure it is an array.
    Matrix = array(Matrix)
    #We obtain an array of indexes. We don't like it's format, so we will transform it into a list.
    #If we just wanted an answer in the form of an array, then we could simply return indexArray.
    indexArray = asarray(where(Matrix == Matrix.max())).T
    #We create the list of indexes that we will later return
    indexes = []
    for i in range(len(indexArray)):
        indexes.append([indexArray[i][0], indexArray[i][1]])
    #We return the list of indexes.
    #Ex: [[0,1], [4, 3], [7, 4]]
    return indexes

