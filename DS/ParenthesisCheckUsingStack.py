def check(expr) :  
  
    s = [];  
  
    for i in range(len(expr)) : 
  
        if (expr[i] == '(' or 
            expr[i] == '[' or expr[i] == '{') : 
  
            # Push the element in the stack  
            s.append(expr[i]);  
            continue;  
  
        if (len(s) == 0) : 
            return False;  
  
        if expr[i] == ')' : 
  
            x = s.pop(); 
              
            if (x == '{' or x == '[') : 
                return False;  
  
        elif expr[i] == '}':  
  
            x = s.pop(); 
              
            if (x == '(' or x == '[') : 
                return False;  
          
        elif expr[i] == ']':  
  
            x = s.pop(); 
              
            if (x =='(' or x == '{') : 
                return False;  
  
    if len(s) : 
        return False
    else : 
        return True
    
if __name__ == "__main__" :  
    expr = "[{}]]";  
    if (check(expr)) : 
        print("Balanced");  
    else : 
        print("Not Balanced");  
