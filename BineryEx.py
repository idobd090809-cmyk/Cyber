def GetBinary(num,memory):
    #convert to binery and removes the first 2 letters
    binary=bin(num)
    binary=binary[2:]
    binary=binary.zfill(memory)
    return binary
def GetNegativeBinary(binery_num,memory):
     negative_binary=''.join('1' if bit=='0' else '0' for bit in binery_num)
     decimal_number=int(negative_binary,2)+1
     negative_binary=GetBinary(decimal_number,memory)
     return negative_binary
     




def main():
        try:
            #getting decimal number 
            number=int(input("enter positive and decimal number"))
            #getting bit size
            bit_size=int(input("enter memory size"))
            #converting the decimal number to binary
            binary=GetBinary(number,bit_size)
            #converting the binary number to negative binary
            negative_binery=GetNegativeBinary(binary)

        except:
             
             print("wrong parameter")



    


    