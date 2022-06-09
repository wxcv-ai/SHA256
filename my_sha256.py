import pprint



def show_binary_representation(message) :
    # this function shows the binary 
    # it shows each 8 bit seperated by spaces

    for i in range(0,binary_length(message),8) :
            
        #print(message[i:i+8])
        continue
    return  0

def convertToBites(my_string):
    # not a part of the hashing algorithm but we will store and use bite string for explanation ease. 
    # so here to convert the strings into bitearray
    # note: we may use a function but i need every step shown on the output here...

    if not type(my_string) == str :
        print('error type of input is not string ')


    arr=[]
    data = ''
    #print(data)
    for letter in my_string:
            
        # convert a string which is ascii value  to hex
        hex_letter = hex(ord(letter))

        # convert the hex to binary
        bin_letter = bin(int( str(hex_letter),16 ))
        '''
        in the conversion to binary the first zeros are not 
        reperesented which leaves varriable length between each elements
        '''
        # this code is to add the missing 0 in the binary representation
           
        final_bin = ''
        diffrence = 8 - len(bin_letter[2:])

        if diffrence != 0 :
            diffrence = 8- len(bin_letter[2:]) -1
            for i in range(0,(diffrence)+1) :
                final_bin += "0"
        final_bin+=bin_letter[2:]
        #final_bin = bin_letter
        arr.append(final_bin)


 
        data+=final_bin
    #print(show_binary_representation(data[0:len(data)-1]))
    
        
    return data


def fill_diffrence_of_bits(message) :      

    diffrence = 8 - len(message)
    final_bin = ''
    if diffrence != 0 :
        diffrence = 8- len(message)-1
        for i in range(0,(diffrence)+1) :
            final_bin += "0"
    final_bin += message
    return final_bin


def preporocessing(message) :
    original_msg_length = int (len(message))
    length_binary = str(bin(original_msg_length)[2:])
    message = message +"1"

    #print(original_msg_length)
    while (len(message))%512 !=448:
        message+="0"

    length_in_binary = str( bin(  original_msg_length ))[2:]
    last_64_bits = ""
    for i in range(0,64-len(length_in_binary)):
        last_64_bits += "0"

    last_64_bits = last_64_bits + length_in_binary
    message = message + last_64_bits

    return message


def SFTR( interger):
    # this function is to binary shift to the right one shift step the bits of type string
    first_zero = '0'
    last_value = interger[len(interger)-1]
    new_integer = ''
    new_integer += first_zero
    for i in range(0,len(interger)-1):
        new_integer+= interger[i]

    final_integer = new_integer
    

    return final_integer ;




def rigthShift(interger,rotate):
    # this function is to right rotate any binary to a how much steps
    for i in range(rotate):
        interger = SFTR(interger)
    return interger


def XOR(var1,var2):



    if len(var1) != len(var2) :
        print(len(var1))
        print(len(var2))
        raise ValueError("Error  : unmatched length")
    final_var = ''  

    for i in range(0,len(var1)):
        if (var1[i]== var2[i]) :
            final_var+="0"
        if (var1[i]!= var2[i]):
            final_var+="1"

    
    

    return final_var

def RTOR( interger):
    

    # this function is to binary rotate one rotate step the bits of type string
    first_value = (interger[len(interger)-1])
    new_integer = ''
    for i in range(0,len(interger)-1):
        new_integer+= interger[i]

    final_integer = ''
    final_integer+=first_value
    for k in (range(0,len(new_integer))):
        final_integer+= new_integer[k]

    
    return final_integer ;

def rightRotate(interger,rotate):
    # this function is to right rotate any binary to a how much steps
    new_integer = ''
    
    for i in range(rotate):
        interger = RTOR(interger)
    new_integer = interger
    return new_integer


def Add (bin1,bin2,bin3,bin4) :

    if len(bin1) != len(bin2) :
        if len(bin1) < len(bin2) :
           diff=  len(bin2)-len(bin1)
           elem = "0"
           total_elem = diff*elem
           bin1 =total_elem+bin1
           #print(bin1)

        if len(bin2) < len(bin1) :
           diff=  len(bin1)-len(bin2)
           elem = "0"
           total_elem = diff*elem
           bin2 =total_elem+bin2

        #print(bin2)           
        #raise ValueError("Error the two binaries does not have the same length")

    bin_arr = []

    for i in  reversed(range(0,len(bin1))):

        bin_arr.append(str(bin1[i:i+1]) + str(bin2[i:i+1]))




    summ = str( bin(  int(bin1, 2) + int(bin2, 2)+int(bin3, 2) + int(bin4, 2)   )     )[2:]  
    if len(summ ) == 32:
        final = summ
        #print("perfect")
       # print('\n')

    elif len(summ ) > 32 :
        diffrence = len(summ) -32 
        final = summ[diffrence:len(summ)]
        #print(len(summ))
        #print('larger')
        #print('\n')
    elif len(summ) < 32 :
        diffrence = 32 - len(summ)
        zeros = "0"*diffrence
        final = zeros+summ

        #print(diffrence)
        #print("inferior")
        #print('\n')
    return(final)        



def AND(bin1,bin2) :

    and_bin=""
    if len(bin1) == len(bin2):

        for i in range(0,len(bin1)):

            if bin1[i] == "1" and bin2[i] =="1" :
                and_bin+="1"
            elif( bin1[i] =="0" and bin2[i] =="0") or (bin1[i] =="1" and bin2[i] =="0") or (bin1[i] =="0" and bin2[i] =="1"):
                and_bin+="0"
            else :
                print("error bit invalide")
                print(bin1[i])
    else :
        print('erreur pas de meme longeur') 
    return and_bin


def NOT(bin1):
    nouveau_bin1 = ""
    for i in range(0,len(bin1)):
        if bin1[i]=="0":
            nouveau_bin1 += "1"
        elif bin1[i]=="1":
            nouveau_bin1 += "0"
        else :
            print("erreur pas de 1 ou 0")
    return nouveau_bin1
    

def hex_editing(table) :
    new_tab = []
    for i in range(0,len(table)) :
        elem = table[i]
        hexadeciaml = str(hex(elem))[2:]
        hexadeciaml = hexadeciaml[0:8]
        elem = bin(int(hexadeciaml,16))[2:]
        if len(elem)< 32 :
            diffrence = 32 - len(elem)
            zeros = "0"*diffrence
            final = zeros+elem
        else :
            final = elem
        new_tab.append(final)
    return new_tab



def chunk_hash(preporocessing_msg) :
    # this function do hashing for only one chunck of 512 bits
    #if the message is larger than 512 bits than use this function in a loop


    initial_Hash_Values = [0x6a09e667, 0xbb67ae85, 0x3c6ef372, 0xa54ff53a,
                        0x510e527f, 0x9b05688c, 0x1f83d9ab, 0x5be0cd19]
   
    
    initial_Hash_binary_Values = [] 
    initial_Hash_binary_Values = hex_editing(initial_Hash_Values)  




    k = [0x428a2f98, 0x71374491, 0xb5c0fbcf, 0xe9b5dba5,
        0x3956c25b, 0x59f111f1, 0x923f82a4, 0xab1c5ed5,
        0xd807aa98, 0x12835b01, 0x243185be, 0x550c7dc3,
        0x72be5d74, 0x80deb1fe, 0x9bdc06a7, 0xc19bf174,
        0xe49b69c1, 0xefbe4786, 0x0fc19dc6, 0x240ca1cc,
        0x2de92c6f, 0x4a7484aa, 0x5cb0a9dc, 0x76f988da,
        0x983e5152, 0xa831c66d, 0xb00327c8, 0xbf597fc7,
        0xc6e00bf3, 0xd5a79147, 0x06ca6351, 0x14292967,
        0x27b70a85, 0x2e1b2138, 0x4d2c6dfc, 0x53380d13,
        0x650a7354, 0x766a0abb, 0x81c2c92e, 0x92722c85,
        0xa2bfe8a1, 0xa81a664b, 0xc24b8b70, 0xc76c51a3,
        0xd192e819, 0xd6990624, 0xf40e3585, 0x106aa070,
        0x19a4c116, 0x1e376c08, 0x2748774c, 0x34b0bcb5,
        0x391c0cb3, 0x4ed8aa4a, 0x5b9cca4f, 0x682e6ff3,
        0x748f82ee, 0x78a5636f, 0x84c87814, 0x8cc70208,
        0x90befffa, 0xa4506ceb, 0xbef9a3f7, 0xc67178f2]

    K = (hex_editing(k))


    # this code is to put our data into an array as each element in the array is 32 bit long
    W =[]
    msg_length =len(preporocessing_msg)+1

    unit_size = 32
    for i in range(0,msg_length-unit_size,unit_size):
        bit_32_chunck= preporocessing_msg[i:i+32]
        W.append(bit_32_chunck)

    #print(len(preporocessing_msg)/512)
    #print(len(W))
    # this code is to add 48 more block in the array with 32 bit zero elements
    # check if the W table is a multiple of 64
    tab_of_chunks = []
    for j in range(0,len(W),16) :
        
        new_W = []
        zero = "0"
        block_zero = 32* zero
        for k in range(j,j+16):
            new_W.append(W[k])
        for k in range(16,64):
            new_W.append(block_zero)


        for i in range(16,64) :
            
              
            S0 = XOR(    XOR(  rightRotate(new_W[i-15],7) , rightRotate(new_W[i-15],18)  )  ,  rigthShift(new_W[i-15],3) )
            S1 = XOR(    XOR(  rightRotate(new_W[i-2],17) , rightRotate(new_W[i-2],19)  )   ,   rigthShift(new_W[i-2],10) )
            #print(S1)
            #print(  len(  rightRotate(W[i-2],19)  )  )

            W_prep0= Add(  new_W[i-16] ,S0,   new_W[i-7] ,S1)
            new_W[i] = W_prep0

        tab_of_chunks.append(new_W)






    h0 = initial_Hash_binary_Values[0]
    h1 = initial_Hash_binary_Values[1]
    h2 = initial_Hash_binary_Values[2]
    h3 = initial_Hash_binary_Values[3]
    h4= initial_Hash_binary_Values[4]
    h5 = initial_Hash_binary_Values[5]
    h6 = initial_Hash_binary_Values[6]
    h7 =  initial_Hash_binary_Values[7]


    for num in range(0,len(tab_of_chunks)) :

        a = h0
        b = h1
        c = h2
        d = h3
        e= h4
        f = h5
        g = h6
        h =  h7

        new_tab = tab_of_chunks[num]
        for i in range(0,64) :
            S1 = XOR (  XOR(rightRotate(e,6) ,rightRotate(e,11))  , rightRotate(e,25) ) 
            ch = XOR(AND(e,f) ,AND(NOT(e),g))

            S0 = XOR (XOR(rightRotate(a,2) ,  rightRotate(a , 13)) , rightRotate(a , 22))

            maj = XOR(XOR(AND(a , b) , AND(a , c)) , AND(b , c))
            temp2 = Add(S0 , maj ,32*"0",32*"0")
            temp1 = Add(Add(h, S1, ch ,(K[i])),(new_tab[i]),32*"0",32*"0") 

            #temp1_x = Add(h, S1, ch ,(K[i])) 
            #temp1 = Add(temp1_x,(new_tab[i]),32*"0",32*"0") 
            h = g
            g = f
            f = e
            e = Add(d ,temp1,32*"0",32*"0")
            d = c
            c = b
            b = a
            a = Add(temp1 ,temp2,32*"0",32*"0")


        h0 = Add(h0 ,a ,32*"0",32*"0")
        h1 = Add(h1 ,b ,32*"0",32*"0")
        h2 = Add(h2, c ,32*"0",32*"0")
        h3 = Add(h3, d ,32*"0",32*"0")
        h4 = Add(h4 ,e ,32*"0",32*"0")
        h5 = Add(h5 ,f ,32*"0",32*"0")
        h6 = Add(h6 ,g ,32*"0",32*"0")
        h7 = Add(h7, h ,32*"0",32*"0")

    hash_value_binary = h0+h1+h2+h3+h4+h5+h6+h7
    hash_int = int(hash_value_binary,2)
    hash_hex = hex(hash_int)[2:]
    hash_string = str(hash_hex)
    if len(hash_string) ==  65 :

        hash_string = hash_string[0:64]

    hash_value =   hash_string.upper()
    
    
    if len(hash_value) < 64 :
        diffrence = 64- len(hash_value)
        zeros= diffrence * "0"
        hash_value = zeros + hash_value
    if len(hash_value) >  64 :
        print("erreur longueur de hash est superieur a 64 ")
    return hash_value

mystring = 100*"hgf"
#mystring = "hello world"
converted = convertToBites(mystring)
preporocessing_msg = preporocessing(converted)
hash_value =chunk_hash(preporocessing_msg)

print(hash_value)
#print(mystring)
