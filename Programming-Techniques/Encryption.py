def encrypt():
    new_message = ""
    x = 0
    for enc in range(0,len(message)):
        new = chr(message[enc] + key[x])
        new_message += new
        x += 1
        if x == i:
            x = 0           
    print(new_message)
    print("Copy and paste this message to keep it ")
#endfunction

def decrypt():
    org_message = ""
    x = 0
    for dec in range(0,len(message)):
        org = chr(message[dec] - key[x])
        org_message += org
        x += 1
        if x == i:
            x = 0        
    print(org_message)

key = input("Input the key phrase ")
key = [ord(c) for c in key]
message = input("Input the message ")
message = [ord(c) for c in message]
i = len(key) - 1
choice = input("Do you want to encrypt or decrypt a message? E = encrypt D = decrypt ")
choice = choice.lower()

while choice != "e" or choice != "d":
    choice = "Input a valid choice: " ### SRC - this line doesn't look right?
    
if choice == "e":
    encrypt()
else:
    decrypt()
end = input() ### SRC - What's happening here?
