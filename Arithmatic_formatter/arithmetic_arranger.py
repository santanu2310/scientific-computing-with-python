import operator
ops = { "+": operator.add, "-": operator.sub }

def arithmetic_arranger(problems, solution = False):

    #checking for no. of problems
    if len(problems) > 5:
        return 'Error:Too many problems.'
    
    operand1 = [x.split()[0] for x in problems]
    operand2 = [x.split()[2] for x in problems]
    operators = [x.split()[1] for x in problems]


    #Checking operator
    for oper in operators:
        if oper not in "+-":
            return "Error: Operator must be '+' or '-'."
    
    #checking for digit
    for i in range(0,len(operand1)):
        if not operand1[i].isdigit() or not operand2[i].isdigit():
            return "Error: Numbers must only contain digits."
        
        elif len(operand1[i])>4 or len(operand2[i])>4:
            print(len(operand1[i]))
            return "Error: Numbers cannot be more than four digits."
        
    #Arrenging in string
    
    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""

    for i in range(0,len(operators)):
        oper_1 = operand1[i]
        oper_2 = operand2[i]
        
        if len(oper_1) > len(oper_2):
            line1 += " "*2 + str(oper_1) + " "*4
            line2 += operators[i] + " "+" "*int(len(oper_1)-len(oper_2))+oper_2+" "*4
            line3 += "-"*(2+len(oper_1))+" "*4
            value = ops[operators[i]](int(oper_1),int(oper_2))
            line4 += " "*(2+len(oper_1)-len(str(value)))+str(value)+" "*4

        else:
            line1 += " "*2 +" "*int(len(oper_2)-len(oper_1))+ str(oper_1) + " "*4
            line2 += operators[i] + " "+oper_2+" "*4
            line3 += "-"*(2+len(oper_2))+" "*4
            value = ops[operators[i]](int(oper_1),int(oper_2))
            line4 += " "*(2+len(oper_2)-len(str(value)))+str(value)+" "*4
        
    
    answer = line1.rstrip() + '\n' +line2.rstrip() + '\n' + line3.rstrip()
    if solution:
        answer += '\n' + line4.rstrip()

    return answer
