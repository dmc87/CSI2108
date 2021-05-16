# Darcy McIntyre, 10522336
# Linear feedback shift register

# Need random to create a seed number for my 8 flip flops
# 8 bit range is 00000000 to 11111111 (0 to 255) = 256 bits
import random

message_x="Meet Alice next to the fridge in Building 18 at ECU."
X=0
for c in message_x:
    X=X+(ord(c))


def simple_lfsr(x):                                 # Need a random number and a number of rounds 
    seed=random.randint(0,255)
    seed_bin=(format('{:08b}'.format(seed)))        # Turn the decimal number into an 8 bit binary number
    seed=[]
    check=[]
    count=0
    count2=1
    for i in seed_bin:                              # Put each bit of the binary into a list
        seed.append(i)
    for i in range(x):                              # Perform a binary XOR at position 0 and the switch location
        seed[0]=(str((int(seed[7])+int(seed[6]))%2))
        seed = (seed[-1:] + seed[:-1])              # Shift all bits right so you can perform the xor on each bit
        check.append(''.join(map(str, seed)))
#        print(i,check[count])                      # Test period length
        count=count+1
    for i in check:
        if i==check[0]:                             # Check period length
            print("Repeating value:",count2)
            count2=count2+1
        else:
            count2=count2+1
    session_key = ''.join(map(str, seed))           # Join all the bits together to create the session key
    return session_key

while True:
    quit=input("create new sesison key? y/n > ")
    if quit=="y":
        clock=input("How many clock cycles would you like? > ")
        sesh=(simple_lfsr(int(clock)))
        x=int(sesh,2)
        print("Binary session key:", sesh, " Decimal session key:", x)
        choice2=input("\nHi Alice. Would you like to encrypt the session key\nfor bob using his public key 562013? y/n > ")
        if choice2=="y":
            print("\nencrypting plaintext x:",x)
            print(x,"**2557 mod 562013 = y (ciphertext). Result:")
            y=(x**2557%562013)
            print(y)
            choice3=input("\nWould you like to decrypt the message? y/n > ")
            if choice3=="y":
                print("Decrypting ciphertext y:",y)
                print(y,"**558037 mod 562013 = x (plaintext). Result:")
                plaintext=(y**558037%562013)
                print(plaintext)
            else:
                break
        else:
            break
    else:
        break


    

