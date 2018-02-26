#author: Luca Rospocher
class Object1:
    def __init__(self):
        self.field1 = 0
        self.field2 = ""
        pass

class Object2:
    def __init__(self):
        self.field1 = 0
        self.field2 = False
        self.field3 = []
        self.field4 = []
        pass
    
list1 = []
list2 = []
    
def main():
    
    ############### READ FILE ###############

    # read all file
    print("reading file...")
    fileLines = open('input.in', 'r').readlines()

    # usually first line is distinct integer variables
    splittedFirstLine = fileLines[0].split(' ')
    var1 = int(splittedFirstLine[0])
    var2 = int(splittedFirstLine[1])
    var3 = int(splittedFirstLine[2])
    
    # prepare a list of object, as big as specified in one of the previous variables
    for i in range(var1):
        list1.append(Object1()) #fill with empty
    
    # read integers from second line and save in a list
    splittedSecondLine = fileLines[1].split(' ')
    for i in range(var1):
        list1.append(int(splittedSecondLine[i]))
    
    # read all the lines, number of lines and elements per line are already known
    lineCounter = 2
    for i in range(var2):
        splittedLine = fileLines[lineCounter].split(' ')
        lineCounter += 1

        # DO STUFF
        
        for k in range(len(splittedLine)):
            list2.append(int(splittedLine[k]))
            # DO STUFF

    ############### MAIN ALGORITHM ###############    
    countResults = 10
    someRowHeader = 'ROW'

    ############### PRINT FILE ###############
    print("writing file...")
    fileOutput = open('output.out', 'w')
    fileOutput.write(str(countResults) + '\n')
    for b in range(countResults):
        fileOutput.write(someRowHeader + str(b) + ' ')
        for t in range(len(list2)):
            fileOutput.write(str(list2[t]) + ' ')
        fileOutput.write('\n')
        
if  __name__ =='__main__':
    main()