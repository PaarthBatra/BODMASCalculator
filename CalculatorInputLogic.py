from __future__ import division

# Class Named CalculatorInputLogic to put all Input logic related function in this module
#Version 1.0
#Last update 23rd August 2013
# Adding SimulateBackspace function

#Version 2_1
#put C-Clear All , CE-Clear Entry , <-- Backspace and other logics to CalculatorInputLogic
#Version 2.1 finish on 26th AUg 2013

#Version 2_2
#Changes - make under-root ,1/x,% ,+- sign usable

#Version 2_3
#Changes - Make multiply /Division Work Done
#  Negate done

#Version2_4 will be on implementing Reciprocate 1/x and Percentage
#Versio 2_5 will be putting try catch for math errors
#This was once the current prod version

#Version 2_7
#support for ( at any other place then starting 
# if operator is pressed and ( is equal to ) , value should be computed
# Addition of a number after something ( in lineE and some expression in lineEU ex :lineE :(  ,LineEU:(3+6)+3+( , done in elif6.1
#included 7.1 for a entry of operator when ( != )
#included 7.2 for a entry of operator when ( matches ) and setlineE != "" . Still wondering why we use elif7
#Added elif 5 for brackets when ( is greater than )+1
#Operator Enter after ) when no. of ( > ) - included in elif 4.1

#Version 2_8
# Fixing of Negate function on () support
#Addition of SE i.e. Show Expression , this function will put complete expression till now on lineEU and result in lineE

#version 2_9 resolve bug while solving ((90+4)/2-6*7/2+((7+4)*10)+8*9-5)*10+8 , bug in brackets ( for elif 2
import math



class CalculatorInputLogic():

    def findLastNumber(self,inputLineE):
        print "original inputLineE is ",inputLineE
        inputLineE = inputLineE.replace("(","")
        print "( is replced now str is ", inputLineE
        inputLineE = inputLineE.replace(")","")
        print ") is replced now str is ", inputLineE
        while True:
            try:
                print "Trying on"+inputLineE
                result = float(inputLineE) + 0
                return result
            except :

                inputLineE = inputLineE[:-1]
                print "In Exception block inputLineE changed to",inputLineE

    def showExpression(self,classobj):
        print "\n\n\n\nWelcome to Show Expression function. I will put full expression in lineEU and if its valid ,result in lineE"
        print "Current line EU is ",classobj.lineEU
        print "Current line E is ",classobj.lineE

        if classobj.lineE == classobj.lineEU or classobj.lineEU == "":
            print "values are same so setting classobj.setlineE = lineEU and classobj.setlineEU = lineEU"

            try:
                eval(classobj.lineE)
                classobj.setlineE = self.calculateStrVal(classobj.lineE)
            except:
                classobj.setlineE = classobj.lineE
            classobj.setlineEU =classobj.lineE

        elif classobj.lineEU[-1:] == ")":
            classobj.setlineEU =classobj.lineEU
            try:
                eval(classobj.lineEU)
                classobj.setlineE = self.calculateStrVal(classobj.lineEU)
            except:
                classobj.setlineE = classobj.lineE
        else:
            #find char extra in lineEU

            operator = self.findOperator(classobj.lineEU)
            print "Operator in lineEU is ", operator
            posOfLineETxtinLineEU = classobj.lineEU.rfind(operator + classobj.lineE )
            print "Position is ", posOfLineETxtinLineEU
            #find string in lineEU before position found above
            inititalStrEU = classobj.lineEU[:posOfLineETxtinLineEU]
            print "Initial String in lineEU is ",inititalStrEU
            finalStringToShow = inititalStrEU + operator + classobj.lineE
            print "Final String to Show is ",finalStringToShow
            try:
                eval(finalStringToShow)
                finalStringToShowLineE = self.calculateStrVal(finalStringToShow)
            except:
                finalStringToShowLineE = classobj.lineE
            print "Final String to show in lineE is ",finalStringToShowLineE
            classobj.setlineE = finalStringToShowLineE
            classobj.setlineEU = finalStringToShow

        classobj.lineEdit.setText(classobj.setlineE)
        classobj.lineEditu.setText(classobj.setlineEU)

    def findOperator(self,input):

        # This Function is created to find the Last operator present in the total string passed.
        #   This will be further called by calculateStrVal function to do the calculations

        # Introduced in CalculatorQt 2.0 on 18th August 2013
        # Author - Paarth

    # Version 2.0
    #Changes
    #Moved to CalculatorInput Logic Module
    #Last update date 23rd Aug 2013

        plus = input.rfind("+")
        minus = input.rfind("-")
        multiply = input.rfind("*")
        divide = input.rfind("/")
        listOperator = [plus,minus,multiply,divide]
        maxi = max(listOperator)
        if maxi > -1:
            print "Maximum is", maxi
            operator = input[maxi]
            print "operator is ", input[maxi]
        else:
            operator="-1"
        return operator

    def calculateStrVal (self,inputVal):
        #Calculate string value by using math operators
        print "from calculateStr_val : Value Passed to me is ",inputVal
        try :
            result = eval(inputVal)
            print "Result is ",result
        except Exception as Messages:
            return str(Messages)
        return str(result)


    def calculateStrVal_old(self,inputVal):
    # This function will take the string anything example 2+3+5-45 , calculate the result and /
    # retrun result back to addTxt function

    # Introduced in CalculatorQt 2.0 on 18th August 2013
    # Author - Paarth

    # Version 2.0
    # Changes
    # Moved to CalculatorInput Logic Module
    # Last update date 23rd Aug 2013

        #This will find the last operator in the string passed
        operator = self.findOperator(inputVal)
        print " Operator is ", operator

        if operator == "-1":
            a=inputVal
            b="0"
        else:

            #variable to find the last position of operator in the string passed
            temp = inputVal.rfind(operator)

            #finding a as the value of last operator example a in 2+3+4-5 is -5
            a = inputVal[temp:]
            print "A is ", a
            #finding b as the value of last operator example b in 2+3+4-5 is 2+3+4
            b = inputVal[:temp]
            print "B is ", b

        # if b d ont have any operators in it,  b will be final b i.e. if string /
        # was 2+3 then b is 2 this
        # otherwise we calculate b by if condition example if string was 2+3+1 where b is 2+3 we go to if
            if b.find("+") != -1 or b.find("-") != -1 or b.find("*") != -1 or b.find("/") != -1:
                print "As b contains operators passing b to calculateStrVal as ", b
                #Find b by passing b to same function . This is use of recursive function
                b = self.calculateStrVal(b)

        print "A and B are :", a, "  ", b
        #creating variable result which gives result of a and b , so if we had 3-4 , a = -4 , b =3 then /
        # result is -4+3 i.e. -1.0
        result = str(float(a)+float(b))

        print "from CalculateStrVal : Result is ", result

        #Check if result will contain decimal points or not

        # dot will find the position of . in the result , so in -1.0 it will be 2
        dot = result.find(".")
        print "position  dot is ", dot
        #this will keep string after . so in -1.0 this will be 0
        strAfterDot=result[dot+1:]
        print "Value after dot is ", strAfterDot

        #Check if result have anything more than 0 then send result else send value before .
        if int(strAfterDot) > 0:
            return result
        else:
            return result[:dot]

    def addTxt(self,classobj,inputVal):
    # This function will take :
    # 1. Input from Calculator GUI  example 2,+,-,.  /
    # 2. Check what should be done with this input and perform action

    # Introduced in CalculatorQt 2.0 on 18th August 2013
    # Author - Paarth

    # Version 2.0
    # Changes
    # Moved to CalculatorInput Logic Module
    # Last update date 23rd Aug 2013

        print "New Cycle : \n\n\n\n\n\n\n\n\n\n\n\n\nValue entered is ", inputVal
        print "From add Txt before setting anything : lineE and lineEu are ", classobj.lineE, classobj.lineEU
        #if We are entering anything very first time , i.e. when lineE is 0 and lineEU is empty
        if classobj.lineE == "0" and classobj.lineEU == "" and str(inputVal) in ("1", "2", "3", "4", "5", "6", "7",\
                "8", "9"):

            classobj.lineE = inputVal
            classobj.lineEU = inputVal
            classobj.setlineE = inputVal
            classobj.setlineEU = ""
            print "from if of addTxt : value entered is ", inputVal

        #elif 0.01 for "("
        elif str(inputVal) in ("("):
            self.brackets("(", classobj)
        #elif 0.01 for ")"
        elif str(inputVal) in (")"):
            self.brackets(")", classobj)
        #elif o.1 for backspace
        elif str(inputVal) == "backspace":
            text=classobj.lineEdit.text()
            if len(text) == 1:
                print "from backspace if and len(text) == 1 if"
                classobj.lineE="0"
                classobj.lineEU=""
                classobj.setlineE=classobj.lineE
                classobj.setlineEU=""
            else:
                print "from backspace if and len(text) > 1 "
                classobj.lineE=str(text[:len(text)-1])
                classobj.lineEU=str(classobj.lineEU[:len(classobj.lineEU)-1])
                classobj.setlineE=classobj.lineE
            print "from elif 0.1 of addTxt : Value entered is Backspace"

        #elif 0.2 for CE
        elif str(inputVal) == "CE":
            if classobj.setlineEU[-1:] in ("+","-","*","/"):
                classobj.lineE="0"
                classobj.lineEU=str(classobj.lineEditu.text())
                classobj.setlineE=classobj.lineE
                classobj.setlineEU=classobj.setlineEU
            else:
                classobj.lineE="0"
                classobj.lineEU=""
                classobj.setlineE=classobj.lineE
                classobj.setlineEU=classobj.lineEU
            print "from elif 0.2 of addTxt : Value entered is CE"

        #elif 0.3 for C - Clear All
        elif str(inputVal) == "C" :
            classobj.lineE="0"
            classobj.lineEU=""
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.lineEU
            print "from elif 0.3 of addTxt . Value entered is : ",inputVal

        #elif 0.4 for under-root / square root
        elif str(inputVal) == "sqrt" :
            #as per windows calculator it always compute squareroot for variable in lineE . and put the sqrt(lineE) to \
            # LineEU , which means we need to change compute string function for sqrt strings .


            txtUpperLabel=str(classobj.lineEditu.text())
            if  txtUpperLabel == "" :
                classobj.lineEU="sqrt("+classobj.lineE+")"
            elif  txtUpperLabel.find("sqrt") > -1 :
                classobj.lineEU=classobj.lineEditu.text() + " --> sqrt("+classobj.lineE+")"
            elif txtUpperLabel.find("sqrt") == -1 :
                classobj.lineEU=classobj.lineEditu.text() + " sqrt("+classobj.lineE+")"
            try:
                classobj.lineE=str(math.sqrt(float(classobj.lineE)))
            except Exception as Messages:
                classobj.lineE = str(Messages)
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.lineEU
            print "from elif 0.4 of addTxt for square root. Value entered is : ",inputVal
        # For input value Negate
        elif str(inputVal) == "+-":
            bracketCountLeft = classobj.lineEU.count("(")
            bracketCountRight = classobj.lineEU.count(")")
            operator = self.findOperator(classobj.lineEU)
            print "from elif 0.5 of addTxt , operator in ",classobj.lineEU," is ",operator
            posOfOperator=classobj.lineEU.rfind(operator)
            print "from elif 0.5 of addTxt , position of operator in ",classobj.lineEU," is ",posOfOperator
            if bracketCountLeft == 0 and bracketCountRight == 0:
                if classobj.lineE.find(".") == -1:
                    classobj.lineE=str(int(classobj.lineE) * -1)
                    if operator == "-1":
                        if classobj.lineEU <> "":
                            classobj.lineEU=str(int(classobj.lineEU) * -1)
                            print "lineU is ",classobj.lineEU
                    else:
                        newStr=classobj.lineEU[:posOfOperator] + operator + str(int(classobj.lineEU[posOfOperator+1:]) * -1)
                        classobj.lineEU = newStr
                    print "from elif 0.5 of addTxt , lineEU becomes",classobj.lineEU
                else:
                    classobj.lineE=str(float(classobj.lineE) * -1)
                    if posOfOperator == "-1":
                        classobj.lineEU=str(float(classobj.lineEU) * -1)
                    else:
                        newStr=classobj.lineEU[:posOfOperator] + operator + str(float(classobj.lineEU[posOfOperator+1:]) * -1)
                        classobj.lineEU = newStr
                    print "from elif 0.5 of addTxt , lineEU becomes",classobj.lineEU
            else:
                print "Brackets and negate logic"
                print "Find digit in the last which should be negated"
                #if last of lineEU is operator and ( in lineE <> )
                #classobj.lineEU[-1:] in ("+","-","*","/") and
                if classobj.lineE.count("(") != classobj.lineE.count(")"):
                    ##find last digit and negate it
                    lastDigit = int(self.findLastNumber(classobj.lineE))
                    print 'negating, last digit is ',lastDigit
                    classobj.lineE = classobj.lineE.replace(str(lastDigit),str(int(lastDigit)*-1))
                    classobj.lineEU = classobj.lineEU.replace(str(lastDigit),str(int(lastDigit)*-1))
                elif  classobj.lineE.count("(") == classobj.lineE.count(")"):
                    #find last ( and replace it with -(

                    classobj.lineE= classobj.lineE.replace("(","-(")
                    classobj.lineEU = classobj.lineEU.replace("(,","-(")
            classobj.setlineE=classobj.lineE
            print "from elif 0.5 when input is +- . lineE is ",classobj.lineE," LineEU is ",classobj.lineEU
        # elif 0.6 for a 1/x
        elif str(inputVal) == "Reci" :
            #as per windows calculator it always compute squareroot for variable in lineE . and put the sqrt(lineE) to \
            # LineEU , which means we need to change compute string function for sqrt strings .


            txtUpperLabel=str(classobj.lineEditu.text())
            if  txtUpperLabel == "" :
                classobj.lineEU="Reci("+classobj.lineE+")"
            elif  txtUpperLabel.find("Reci") > -1 :
                classobj.lineEU=classobj.lineEditu.text() + " --> Reci("+classobj.lineE+")"
            elif txtUpperLabel.find("Reci") == -1 :
                classobj.lineEU=classobj.lineEditu.text() + " Reci("+classobj.lineE+")"
            a = '1/'
            classobj.lineE=str(float(eval(a + classobj.lineE)))
            print "Calculated value for ", a + classobj.lineE
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.lineEU
            print "from elif 0.6 of addTxt for Reciprocate. Value entered is : ",inputVal
        #elif 0.7 fir percentage
        elif str(inputVal) == "%":
            txtUpperLabel=str(classobj.lineEditu.text())
            txtLowerLabel=str(classobj.lineEdit.text())
            if  txtUpperLabel == "" :
                classobj.lineEU="0"
                classobj.lineE="0"
            else :
                operator = self.findFirstOperator(txtUpperLabel)
                posOfOperator = txtUpperLabel.find(operator)
                StrBeforeOperator = txtUpperLabel[:posOfOperator]
                percentage = str(float(StrBeforeOperator) * float(txtLowerLabel) / 100)
                classobj.lineE=percentage
                classobj.lineEU=percentage
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.lineEU
            print "from elif 0.7 of addTxt for Percentage. Value entered is : ",inputVal


        # elif 1 for a wrong input at the very first input
        elif classobj.lineE == 0 and classobj.lineEU == "" and str(inputVal) in ("+", "-", "*", "/", ".", "0"):

            print "from elif 1:Wrong input dear , Nothing changes"
    #Elif 2 for entering . twice , its sequence of elif is 2nd because we need to check second entry of dot before \
    # any second level entry could be made
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and classobj.lineEU[-1:]   \
            in ("1","2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and str(inputVal) == "." and \
            classobj.lineE.find(".") != -1:

            print "from elif 2:Wrong input dear , Nothing changes : Value entered is . and . is already present "

    #Elif 3 for a second level entry for inputs except operators
        elif classobj.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0",".","(") and classobj.lineEU[-1:] in ("1",   \
                "2", "3", "4", "5", "6", "7", "8", "9", "0", ".","(") and str(inputVal) in ("1", "2", "3", "4", "5", "6",  \
                "7", "8", "9", "0", ".") and classobj.setlineEU[-1:] == "":

            classobj.lineE=classobj.lineE+inputVal
            classobj.lineEU=classobj.lineEU+inputVal
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=""
            print "from elif 3 of addTxt : This was a second level entry for any digits and . "

    #Elif 4 for a operator entry when num of ( match number of )
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ")") and classobj.lineEU[-1:] in \
                ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ")") and str(inputVal) in ("+", "-", "*", "/") and     \
                classobj.setlineEU[-1:] == "" and classobj.lineE.count("(") == classobj.lineE.count(")"):

            #classobj.lineE=classobj.lineE
            #classobj.lineEU=classobj.lineEU+inputVal
            #classobj.setlineE=classobj.lineE
            #classobj.setlineEU=classobj.lineEU
            print "from elif 4 when input is operator and ( matches ) "

            print " Value which will be calculated for lineE is ", classobj.lineEU
            StrToPass = classobj.lineEU
            print " Passing string to calculateStrVal", StrToPass
            resultCalculateStr = self.calculateStrVal(StrToPass)

            classobj.lineE = resultCalculateStr
            classobj.lineEU = classobj.lineEU+inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.lineEU


    #Elif 4.1 for a operator entry when ( dosent match )
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".",")") and classobj.lineEU[-1:] in \
                ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".",")") and str(inputVal) in ("+", "-", "*", "/") and     \
                classobj.setlineEU[-1:] == "" and classobj.lineE.count("(") > classobj.lineE.count(")"):

            classobj.lineE=classobj.lineE+inputVal
            classobj.lineEU=classobj.lineEU+inputVal
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.setlineEU
            print "from elif 4 when input is operator and ( dosent match )"

    #Elif 4.101 for a operator entry when ( dosent match ) and setlineEU != ""
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".",")") and classobj.lineEU[-1:] in \
                ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".",")") and str(inputVal) in ("+", "-", "*", "/") and     \
                classobj.setlineEU[-1:] != "" and classobj.lineE.count("(") > classobj.lineE.count(")"):

            classobj.lineE=classobj.lineE+inputVal
            classobj.lineEU=classobj.lineEU+inputVal
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.setlineEU
            print "Elif 4.101 for a operator entry when ( dosent match ) and setlineEU != null"

    #Elif 4.2 for digit entry when last lineEU is operator
        elif classobj.lineE[-1:] in ("+", "-", "*", "/") and str(inputVal) in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0")\
            and classobj.lineE.count("(") > classobj.lineE.count(")"):

            classobj.lineE=classobj.lineE+str(inputVal)
            classobj.lineEU=classobj.lineEU+str(inputVal)
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.setlineEU
            print "from elif 4.2 when input is digit after + due to ( inside lineE  "

    #Elif 5 for digit entry when last lineEU is operator
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ")") and classobj.lineEU[-1:] in \
                ("+", "-", "*", "/") and str(inputVal) in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):

            classobj.lineE=inputVal
            classobj.lineEU=classobj.lineEU+inputVal
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.setlineEU
            print "from elif 5 when input is digit  "
    
    #Elif 6 Digit entry when last in setLineEU in operator and last in lineEU is not operator and entry is digit
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and classobj.lineEU[-1:] \
            in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and  str(inputVal) in \
            ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and classobj.setlineEU[-1:] in ("+", "-", "*", "/"):

            classobj.lineE=classobj.setlineE+inputVal
            classobj.lineEU=classobj.lineEU+inputVal
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.setlineEU
            print "from elif 6 when input is digit , last entry in setLineEU is operator and last in lineEU is digit  "


    #Elif 6.1 Digit entry when last in LineE is ( and last in lineEU is ( and entry is digit
        elif classobj.lineE[-1:] in ( "(" ) and classobj.lineEU[-1:] \
            in ("(") and  str(inputVal) in \
            ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0") :

            classobj.lineE=classobj.setlineE+inputVal
            classobj.lineEU=classobj.lineEU+inputVal
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.setlineEU
            print "from elif 6.1 when input is digit , last entry in LineEU  and lineE is (  "

     #Elif 6.101 Digit entry when last in setLineEU in anything and last in lineEU is not operator
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and classobj.lineEU[-1:] \
            in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and  str(inputVal) in \
            ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and classobj.setlineEU[-1:] in ("+", "-", "*", "/","1", "2", "3", "4", "5", "6", "7", "8", "9", "0"):

            classobj.lineE=classobj.setlineE+inputVal
            classobj.lineEU=classobj.lineEU+inputVal
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.setlineEU
            print "6.101 Digit entry when last in setLineEU in anything and last in lineEU is not operator . this is to support SE s "

    #Elif 7 when entry is operator,last in setLineEU is operator and last in lineEU is not operator and
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and classobj.lineEU[-1:] \
            in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and str(inputVal) in ("+", "-","*","/") \
            and classobj.setlineEU[-1:] in ("+", "-", "*", "/") and classobj.lineEU.count("(") == classobj.lineEU.count(")"):

            print " Value which will be calculated for lineE is ", classobj.lineEU
            StrToPass = classobj.lineEU
            print " Passing string to calculateStrVal", StrToPass
            resultCalculateStr = self.calculateStrVal(StrToPass)

            classobj.lineE = resultCalculateStr
            classobj.lineEU = classobj.lineEU+inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.lineEU
            print "from elif 7 when last in setLineEU = operator, last in lineEU != operator and entry is operator and ( == )"

        #Elif 7.1 when entry is operator,last in setLineEU is operator and last in lineEU is not operator and
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and classobj.lineEU[-1:] \
            in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and str(inputVal) in ("+", "-","*","/") \
            and classobj.setlineEU[-1:] in ("+", "-", "*", "/") and classobj.lineEU.count("(") != classobj.lineEU.count(")"):

            classobj.lineE = classobj.lineE + inputVal
            classobj.lineEU = classobj.lineEU+inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.lineEU
            print "from elif 7.1 when last in setLineEU = operator, last in lineEU != operator and entry is operator and ( != )"

        #Elif 7.101 when entry Operator last in setLineEU is anything and last in lineEU is not operator .This case will support SE s
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and classobj.lineEU[-1:] \
            in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".") and str(inputVal) in ("+", "-","*","/") \
            and classobj.setlineEU[-1:] in ("+", "-", "*", "/","1", "2", "3", "4", "5", "6", "7", "8", "9", "0") and classobj.lineEU.count("(") != classobj.lineEU.count(")"):

            classobj.lineE = classobj.lineE + inputVal
            classobj.lineEU = classobj.lineEU+inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.lineEU
            print "from elif 7.101 when entry Operator last in setLineEU is anything and last in lineEU is not operator .This case will support SE s, last in lineEU != operator and entry is operator and ( != )"
        #Elif 7.2 for a operator entry when num of ( match number of ) and setlineEU is not ""
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ")") and classobj.lineEU[-1:] in \
                ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ".", ")") and str(inputVal) in ("+", "-", "*", "/") and     \
                classobj.lineE.count("(") == classobj.lineE.count(")"):

            #classobj.lineE=classobj.lineE
            #classobj.lineEU=classobj.lineEU+inputVal
            #classobj.setlineE=classobj.lineE
            #classobj.setlineEU=classobj.lineEU
            print "from elif 7.2 when input is operator and ( matches ) "

            print " Value which will be calculated for lineE is ", classobj.lineEU
            StrToPass = classobj.lineEU
            print " Passing string to calculateStrVal", StrToPass
            resultCalculateStr = self.calculateStrVal(StrToPass)

            classobj.lineE = resultCalculateStr
            classobj.lineEU = classobj.lineEU+inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.lineEU
            
    #Elif 8 when operator entered is =
        elif str(inputVal) == "=":
            print "classobj.lineEU[:1] is :", classobj.lineEU[:-1]
            if classobj.lineEU.count("(") == classobj.lineEU.count(")"):
                if classobj.lineEU == "":
                    StrToPass = str(classobj.lineE)
            #StrToPass = classobj.setlineEU+classobj.setlineE
                elif classobj.lineEU[-1:] in ("+", "-", "*", "/"):
                    StrToPass = str(classobj.lineEU + classobj.lineE)
                else:
                    StrToPass = str(classobj.lineEU)

                print " Passing string to calculateStrVal",StrToPass
                resultCalculateStr = self.calculateStrVal(StrToPass)


                classobj.lineE = resultCalculateStr
                classobj.lineEU = ""
                classobj.setlineE = classobj.lineE
                classobj.setlineEU = classobj.lineEU
            else:
                print "Do nothing"
            print "from elif 8 where passed input is ="

    #Elif 9 , anything after = was pressed , almost same as first time entry
        elif classobj.lineE[-1:] in ("1","2","3","4","5","6","7","8","9","0",".") and classobj.lineEU == "" and str(inputVal) in \
                ("1","2","3","4","5","6","7","8","9","."):
            classobj.lineEU=classobj.lineE+"+"+inputVal
            classobj.lineE=inputVal
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=""
            print "from elif 9: value entered is ",input
        
        #Elif 10 , anything after = was pressed , almost same as first time entry
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0") and classobj.lineEU == "" and  str(inputVal) in \
                ("+", "-", "*", "/") :#and classobj.setlineEU[-1:] == "" :

            classobj.lineE=classobj.lineE
            classobj.lineEU=classobj.lineE+inputVal
            classobj.setlineE=classobj.lineE
            classobj.setlineEU=classobj.lineEU
            print "from elif 10 when input is operator: anything after =",inputVal

        else:
            print "From Else: value entered is", inputVal

        print "CalculatorInputLogic from add Txt of after setting : lineE :",classobj.lineE,"lineEu : ",classobj.lineEU, \
        "setLine : ",classobj.setlineE,"setlineEU : ",classobj.setlineEU
        classobj.lineEdit.setText(classobj.setlineE)
        classobj.lineEditu.setText(classobj.setlineEU)

    def findFirstOperator(self, inputVal):
        #Returns the first operator in the string where operators are in +,-,*,/
        # if none is found -1 is returned
        for i in inputVal:
            if i in ("+", "-", "*", "/"):
                print "First Operator found : ", i
                return i
        print "No Operator present in string"
        return -1

    def brackets(self,inputVal,classobj):
        if classobj.lineE == "0" and classobj.lineEU == "" and str(inputVal) in ("("):
            classobj.lineE = inputVal
            classobj.lineEU = inputVal
            classobj.setlineE = inputVal
            classobj.setlineEU = ""
            print "from if of brackets : value entered is ", inputVal
        #Elif 1 ( operator entry when ( is already present
        elif classobj.lineEU[-1:] in ("+","-","*","/","(") and classobj.lineE[-1:] == "(" and str(inputVal) in ("("):
            classobj.lineE = classobj.lineE + inputVal
            classobj.lineEU = classobj.lineEU + inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.setlineEU
            print "from elif 1 of brackets when ( is entered for non starting point having ( as last in lineE: value entered is ", inputVal
        #Elif 2 ( left bracket entry when ( is already present and lineE last is a digit
        elif classobj.lineEU[-1:] in ("+","-","*","/","(") and classobj.lineE[-1:] not in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0","(") and str(inputVal) in ("("):
            classobj.lineE = classobj.lineE + inputVal
            classobj.lineEU = classobj.lineEU + inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.setlineEU
            print "from elif 2 of brackets when ( is entered for non starting point having digit as last in lineE: value entered is ", inputVal

        #Elif 2.1 ( left bracket entry when lineE last is a digit
        elif classobj.lineEU[-1:] in ("+","-","*","/","(") and classobj.lineE[-1:]  in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0") and str(inputVal) in ("("):
            classobj.lineE = inputVal
            classobj.lineEU = classobj.lineEU + inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.setlineEU
            print "from elif 2.1 ( left bracket entry when lineE last is a digit ", inputVal
        #Elif 3 ) operator entry when ( is not present
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0") and  str(inputVal) in \
                (")") and classobj.lineE.count("(") == classobj.lineE.count(")") :
            print "from elif3 of brackets when ) can not be entered as ( and ) are same "
        #Elif 4 ) entry when ( is present
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0",")") and  str(inputVal) in \
                (")") and str(int(classobj.lineE.count("("))) == str(int(classobj.lineE.count(")")) + 1) :
            classobj.lineE = classobj.lineE+inputVal
            classobj.lineEU = classobj.lineEU+inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.setlineEU
            print "from elif4 of brackets when ) can be entered as ( and )+1 are same "

        #Elif 5 Entry of ) i.e. right bracket when count of ( is greater than )
        elif classobj.lineE[-1:] in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0",")") and  str(inputVal) in \
                (")") and str(int(classobj.lineE.count("("))) > str(int(classobj.lineE.count(")")) + 1) :
            classobj.lineE = classobj.lineE+inputVal
            classobj.lineEU = classobj.lineEU+inputVal
            classobj.setlineE = classobj.lineE
            classobj.setlineEU = classobj.setlineEU
            print "from elif5 of brackets when ) can be entered as ( > )  are same "
        else :
            print "Else of brackets"
            print "counts are "+str(int(classobj.lineE.count("(")))+" == "+str(int(classobj.lineE.count(")")) + 1)
            print "Last of lineE is ",classobj.lineE[-1:]
            print "Last of lineEU is ",classobj.lineEU[-1:]
            print "value entered is ",str(inputVal)