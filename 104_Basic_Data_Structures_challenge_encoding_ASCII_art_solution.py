# Python code​​​​​​‌‌​​‌​​‌‌​‌‌​‌‌‌​‌​‌​‌‌‌​ below
class Answer:
    def encodeString(stringVal):
        encodedList = [] # create a list
        prevChar = stringVal[0] # set prevChar as first char
        count = 0
        for char in stringVal:
            if prevChar != char:
                encodedList.append((prevChar, count))
                count = 0
            prevChar = char
            count = count + 1

        encodedList.append((prevChar, count))
        return encodedList
    
    def decodeString(encodedList):
        decodeStr = ''
        for item in encodedList:
            decodeStr = decodeStr + item[0] * item[1]
        return decodeStr


# This is an example of how your code will be called.
# Your function should return the factorial of the number.
# You can edit this code to try different testing cases, which
# will run before the challenge test cases.
art = '''

                                                                                
                                                                                
                               %%%%%%%%%%%%%%%%%%%                              
                        %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%                       
                    %%%%%%%%                         %%%%%%%%                   
                %%%%%%%                                   %%%%%%                
              %%%%%%                                         %%%%%%             
           %%%%%%                                               %%%%%           
          %%%%%                                                   %%%%%         
        %%%%%                                                       %%%%%       
       %%%%                 %%%%%              %%%%%                  %%%%      
      %%%%                 %%%%%%%            %%%%%%%                  %%%%     
     %%%%                  %%%%%%%            %%%%%%%                   %%%%    
    %%%%                   %%%%%%%            %%%%%%%                    %%%%   
    %%%%                    %%%%%              %%%%%                     %%%%   
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                                   %%%%  
   %%%%                                                      %%%%        %%%%   
    %%%%       %%%%%%                                        %%%%%       %%%%   
    %%%%         %%%%                                       %%%%        %%%%    
     %%%%         %%%%                                     %%%%         %%%%    
      %%%%         %%%%%                                  %%%%         %%%%     
       %%%%%         %%%%%                             %%%%%         %%%%%      
        %%%%%          %%%%%%                        %%%%%          %%%%        
          %%%%%           %%%%%%%               %%%%%%%           %%%%%         
            %%%%%             %%%%%%%%%%%%%%%%%%%%%             %%%%%           
              %%%%%%%                                        %%%%%              
                 %%%%%%%                                 %%%%%%%                
                     %%%%%%%%%                     %%%%%%%%%                    
                          %%%%%%%%%%%%%%%%%%%%%%%%%%%%%                         
                                   %%%%%%%%%%%%                                 
                                                                                
                                                                                 

'''
encoded = Answer.encodeString(art)
decoded = Answer.decodeString(encoded)

print (encoded)
print ('')
print ('------------------------------------')
print ('')
print (decoded)
