def removedup(str2):
    counter = 0; 
  
    i = 0; 
    size = len(str2); 
    str1 = list(str2); 
    x = 0; 
    length = 0; 
  
    while (i < size): 
        x = ord(str1[i]) - 97; 
        if ((counter & (1 << x)) == 0): 
            str1[length] = chr(97 + x); 
            counter = counter | (1 << x); 
            length += 1; 
        i += 1; 
          
    str2=''.join(str1); 
    return str2[0:length]; 
    
    
str1="heyyyyyyyyyyyyyyyyyyyyyyyyyyy"
print(removedup(str1))

