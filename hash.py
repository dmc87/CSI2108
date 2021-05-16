# Darcy McIntyre
# 10522336

message_x="Meet Alice next to the fridge in Building 18 at ECU."
message_y="Greet Alice next to the fridge in Building 18 at ECU."

def ascii_x(plaintext):             # This function converts text to binary via decimal
    value = ''                      # and spits it out in one whole string 
    for character in plaintext:
        binary = ("{0:08b}".format(ord(character)))
        value = value + binary 
    return value

def group32(value):                  # This function groups strings together by 7 to make ascii bits
    n = 32
    lst = [value[index : index + n] for index in range(0, len(value), n)]
    return lst

while True:
    choice=input("Use message x, y, make your own or quit? x/y/o/q > ")
    if choice=="x":
        b=(group32(ascii_x(message_x))) # Turn message X into grouped 32 bit binary strings
    elif choice=="y":
        b=(group32(ascii_x(message_y))) # Turn message y into grouped 32 bit binary strings
    elif choice=="o":
        b=(group32(ascii_x(input("enter a message: > "))))
    else:
        break
    cnt=0                               # Counter
    clk=1                               # Counter for pretty output
    c=0                                 # empty integer value for later 'calculation'
     # Turn message X into grouped 32 bit binary strings

    for i in b:                         # Then, pad the values out to 48 bit
        if len(i)<48:
            s=48-len(i)                 # s=sum, figure out the difference then;
            b[cnt]=b[cnt]+"0"*s         # add 0's to the string until it equals 48 bits
        cnt=cnt+1                       # cnt=count, keeps count of the items in the list

    for i in b:                         # This part prints neat values for you to see
        print("48-bit block",clk,"of X:",i, "Decimal value:",(int(i, 2)))
        c=c+int(i,2)                    # Convert each block to integers and add together
        clk=clk+1
        cnt=cnt+1
    print("Sum of decmal values:",c)    # display sum of blocks
    h=c*2557%65535                    # The calculation
    print("Sum of decimal values x 2557 mod 65535:", h)
    end=input("End program? y/n > ")
    if end=="y":
        break
