
#Asks the user how the are and if the answe is not "stop copying me" it will just copy what they input.
response = input ("Hey, how are you? ")
while response != "stop copying me":
    print(response)
    response = input()
#if the response is "stop copying me" it will print "oh ok then!" and end the loop        
if  response == "stop copying me":
    print("Oh ok then!")