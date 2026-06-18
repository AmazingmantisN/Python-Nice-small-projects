#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp



with open("Input/Names/invited_names.txt", "r") as name_file:
  names = name_file.readlines()
  

  
for i in names:
    with open("Input/Letters/starting_letter.txt", "r") as file:
        letterbase = file.read()
    
    clean_name = i.strip()
    
    lettercontent = letterbase.replace("[name]", clean_name)
    
    file_name = f"Output/ReadyToSend/{clean_name}_output_letter.txt"
    
    with open(file_name, "w") as crazy:
       crazy.write(lettercontent)
    



