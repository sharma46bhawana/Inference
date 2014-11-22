__author__ = 'Bhawana'

# AI HW 3
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

def getArguments(function):
    if function.find(',') > 0:
        argumentCount = 2
        argument1 = ((function.split('(')[1]).split(')')[0]).split(',')[0]
        argument2 = ((function.split('(')[1]).split(')')[0]).split(',')[1]
    else:
        argument1 = (function.split('(')[1]).split(')')[0]
        argument2 = None
        argumentCount = 1
    return argumentCount, argument1,argument2

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

def getAtomicPremises(resultArgument,clause):
    premises = clause.split('=>')[0]
    arrayOfPremises = premises.split('&')
    for premise in arrayOfPremises:
        substitu
    return arrayOfPremises

def checkForConclusion(result,conclusionFunction):
    resultArgCount, resArg1, resArg2 = getArguments(result)
    conclusionArgCount, conclusionArg1, conclusionArg2 = getArguments(conclusionFunction)

    if resultArgCount == conclusionArgCount:
        if resultArgCount == 1:
            if resArg1 == conclusionArg1:
                return True
            elif conclusionArg1 == 'x':
                return True
            else:
                return False
        elif resultArgCount == 2:
            if resArg1 == conclusionArg1 and resArg2 == conclusionArg2:
                return True
            elif resArg1 == conclusionArg1 and conclusionArg2 == 'x':
                return True
            elif resArg2 == conclusionArg2 and conclusionArg1 == 'x':
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def findSubstitution(result,conclusionFunction):
    resultArgCount, resArg1, resArg2 = getArguments(result)
    conclusionArgCount, conclusionArg1, conclusionArg2 = getArguments(conclusionFunction)

    if resultArgCount == 1:
        if resArg1 == conclusionArg1:
            return None
        elif conclusionArg1 == 'x':
            return resArg1
    elif resultArgCount == 2:
        if resArg1 == conclusionArg1 and resArg2 == conclusionArg2:
            return None
        elif resArg1 == conclusionArg1 and conclusionArg2 == 'x':
            return resArg2
        elif resArg2 == conclusionArg2 and conclusionArg1 == 'x':
            return resArg1




def bcAlgorithm(result):
    print result
    if checkFacts(result):
        return True
    else:
        if conclusionMatch(result):
            resultFunctionName = result.split('(')[0]
            for clause in clauses:
                conclusionFunctionName = (clause.split('=>')[1]).split('(')[0]
                conclusionFunction = clause.split('=>')[1]
                if resultFunctionName == conclusionFunctionName:
                    if checkForConclusion(result,conclusionFunction):
                        constant = findSubstitution(result,conclusionFunction)
                        if constant != None:



        else:
            return False

if __name__ == '__main__':
    readFile()
    #print goal, statement_count, new_statements
    getClausesAndFacts()
    print bcAlgorithm(goal)

