__author__ = 'Bhawana'

new_statements = []
goal = ''
goalFunction = None
statement_count = 0
facts = []
clauses = []

def readFile():
    try:
        filePtr = open('input.txt')
    except:
        print "File Read Error!"
        exit()
    file_input =  filePtr.readlines()
    global goal, statement_count
    goal = file_input[0]
    statement_count = file_input[1]
    statements = file_input[2:]

    for statement in statements:
        new_statements.append(statement.strip('\n'))


def getClausesAndFacts():
    for new_statement in new_statements:
        if new_statement.find('=>')>0 :
            clauses.append(new_statement)
        else:
            facts.append(new_statement)
    #print facts, clauses

def getFunctionName(function):
    goalFunctionName = function.split('(')[0]
    return goalFunctionName

def getArguments(function):
    argument1 = ((function.split('(')[1]).split(')')[0]).split(',')[0]
    argument2 = ((function.split('(')[1]).split(')')[0]).split(',')[1]
    return argument1,argument2

def checkFacts(input):
    for fact in facts:
        if input == fact:
            return True
    return False

def conclusionMatch(input):
    flag = 0
    inputFunctionName = input.split('(')[0]
    for clause in clauses:
        tempFunctionName = (clause.split('=>')[1]).split('(')[0]
        if inputFunctionName == tempFunctionName:
            flag = 1
    if flag == 1:
        return True
    else:
        return False


def bcAlgorithm(result):
    print result
    if checkFacts(result):
        return True
    else:
        if conclusionMatch(result):
            return True

if __name__ == '__main__':
    readFile()
    #print goal, statement_count, new_statements
    getClausesAndFacts()
    print bcAlgorithm(goal)

