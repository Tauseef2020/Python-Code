Stack = []
while True:
    value = input("Please enter postfix expression : ")
    List = list(value)
    
    for i in range(len(List)):
        
        if (List[i].isdigit() == True):
            Stack.append(int(List[i]))
        
        elif (List[i] == "+"):
            x = Stack.pop()
            y = Stack.pop()
            res = x+y
            Stack.append(res)
            
        elif (List[i] == "*"):
            x = Stack.pop()
            y = Stack.pop()
            res = x*y
            Stack.append(res)
        
        elif (List[i] == "-"):
            x = Stack.pop()
            y = Stack.pop()
            res = x-y
            Stack.append(res)
            
        elif (List[i] == "/"):
            x = Stack.pop()
            y = Stack.pop()
            res = x/y
            Stack.append(res)
            
            
    print("The Answer from given equation is : ", Stack[0])
    Stack.clear()

