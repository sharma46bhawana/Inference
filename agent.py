#!/usr/bin/python 
__author__ = 'Bhawana'

import re

# AI HW 3
new_statements = []
goal = ''
goalFunction = None
statement_count = 0
facts = []
clauses = []

def replaceX(premise,constant):
    if premise.find(',') > 0:
        if premise.find('(x,')>0:
            return premise.replace('(x','('+constant)
        elif premise.find(',x')>0:
            return premise.replace('x)',constant+')')
    elif premise.find('(x')>0:
        return premise.replace('(x','('+constant)


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
    filePtr.close()


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
    #print premises
    arrayOfPremises = premises.split('&')
    newClauses = []
    for premise in arrayOfPremises:
        newClauses.append(replaceX(premise,resultArgument))
    return newClauses

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

def getAtomicPremisesWithoutValue(clause):
    premises = clause.split('=>')[0]
    arrayOfPremises = premises.split('&')
    return arrayOfPremises


def sameConclusion(result,conclusionFunction):
    resultArgCount, resArg1, resArg2 = getArguments(result)
    conclusionArgCount, conclusionArg1, conclusionArg2 = getArguments(conclusionFunction)
    if resultArgCount == conclusionArgCount:
        if resultArgCount == 1:
            if resArg1 == conclusionArg1:
                return True
            else:
                return False
        elif resultArgCount == 2:
            if resArg1 == conclusionArg1 and resArg2 == conclusionArg2:
                return True
            else:
                return False

def checkInFacts(premise):
    values = []
    #print premise
    premiseArgCount, premiseArg1, premiseArg2 = getArguments(premise)
    premiseFunctionName = premise.split('(')[0]
    for fact in facts:
        factArgCount,factArg1,factArg2 = getArguments(fact)
        factFunctionName = fact.split('(')[0]
        if premise != fact:
            #print fact
            if premiseFunctionName == factFunctionName:
                #print fact
                if checkForConclusion(fact,premise):
                    if premiseArgCount == 1:
                        values.append((fact.split('(')[1]).split(')')[0])
                    else:
                        if premiseArg1 == factArg1 and premiseArg2 != factArg2:
                            values.append((fact.split(',')[1]).split(')')[0])
                        elif premiseArg2 == factArg2 and premiseArg1 != factArg1:
                            values.append((fact.split(',')[0]).split('(')[1])

    return values




def bcAlgoWithoutSubstitution(premise):

    values = []
    factValues = []
    flagForConstant = 0
    factValues = checkInFacts(premise)
    for value in factValues:
        values.append(value)
    for clause in clauses:
        conclusionFunction = clause.split('=>')[1]
        if conclusionFunction == premise:
            premises = getAtomicPremisesWithoutValue(clause)
            if clause.split('=>')[0].find('(x') or clause.split('=>')[0].find('x)'):
                flag,constants = bcAlgoWithoutSubstitution(premiseWithX(premises))
                if flag == 1:
                    for constant in constants:
                        for eachPremise in premises:
                            if eachPremise.find('(x') or eachPremise.find('x)'):
                                #print eachPremise," ",constant," ",premise, " ",premises
                                temp = replaceX(eachPremise,constant)
                                if bcAlgorithm(temp) == False:
                                    flagForConstant = 0
                                    break
                                else:
                                    flagForConstant = 1

                        if flagForConstant == 1:
                            flagForConstant = 0
                            values.append(constant)
        elif ((premise.find('(x')>0 or premise.find('x)')>0)) and conclusionFunction.split('(')[0] == premise.split('(')[0]:
            if premise.find(',') >0 and conclusionFunction.find(','):
                if premise.find('(x') and (premise.split(',')[1]).split(')')[0] == (conclusionFunction.split(',')[1]).split(')')[0]:
                    values.append((conclusionFunction.split(',')[0]).split('(')[1])
            elif conclusionFunction.find(',')>0 and premise.find(',')>0:
                if premise.find('(x'):
                    values.append((conclusionFunction.split('(')[1]).split(')')[0])

    if values != []:
        return 1,values
    else:
        return 0,values

def premiseWithX(premisesWithoutConstantValue):
    for premise in premisesWithoutConstantValue:
        if premise.find('(x') or premise.find('x)'):
            function = premise
            break
    return function

def bcAlgorithm(result):
    flag = False
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
                            arrayOfPremises = getAtomicPremises(constant,clause)
                            for premise in arrayOfPremises:
                                if bcAlgorithm(premise) == False:
                                    flag = False
                                    break
                                else:
                                    flag = True
                            if flag == True:
                                return True
                        else:
                            if sameConclusion(result,conclusionFunction):
                                flagS = 0
                                premisesWithoutConstantValue = getAtomicPremisesWithoutValue(clause)
                                flagFound,values = bcAlgoWithoutSubstitution(premiseWithX(premisesWithoutConstantValue))
                                if flagFound == 1:
                                    for value in values:
                                        for eachPremise in premisesWithoutConstantValue:
                                            if eachPremise.find('(x') or eachPremise('x)'):
                                                temp = replaceX(eachPremise,value)
                                                if bcAlgorithm(temp) == False:
                                                    flagS = 0;
                                                    break
                                                else:
                                                    flagS = 1
                                            else:
                                                if bcAlgorithm(eachPremise) == False:
                                                    flagS = 0;
                                                    break
                                                else:
                                                    flagS = 1
                                        if flagS == 1:
                                            flag = True
                                            break


            if flag == False:
                return False
            else:
                return True
        else:
            return False

def writeFile(result):
    try:
        filePtr = open('output.txt','w+')
    except:
        print "File Write Error!"
        exit()
    if result == True:
        filePtr.write('TRUE')
    else:
        filePtr.write('FALSE')
    filePtr.close()

if __name__ == '__main__':
    x = 'HasSymptom(x,Fever)'
    a = 'Alpha'
    readFile()
    getClausesAndFacts()
    result = bcAlgorithm(goal)
    #print x.replace('(x',a)
    writeFile(result)
