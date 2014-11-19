__author__ = 'Bhawana'

new_statements = []
goal = None
statement_count = None
facts = []
clauses = []

def readFile():
    try:
        filePtr = open('input.txt')
    except:
        print "File Read Error!"
        exit()
    file_input =  filePtr.readlines()
    goal = file_input[0]
    statement_count = file_input[1]
    statements = file_input[2:]

    for statement in statements:
        new_statements.append(statement.strip('\n'))


def getClauses():
    for new_statement in new_statements:
        if new_statement.find('=>')>0 :
            clauses.append(new_statement)
        else:
            facts.append(new_statement)
    print facts, clauses



if __name__ == '__main__':
    readFile()
    getClauses()

