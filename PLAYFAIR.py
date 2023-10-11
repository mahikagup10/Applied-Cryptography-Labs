key = "WORK"
plaintext= "CRYPTOGRAPHY"

def create_matrix(key):
    
    matrix = [[0 for i in range (5)] for j in range(5)]
    added = []
    row = 0
    col = 0
    for letter in key:
        if letter not in added:
            matrix[row][col] = letter
            added.append(letter)
        else:
            continue
        if (col==4):
            col = 0
            row += 1
        else:
            col += 1
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    for letter in letters:
        if letter not in added: # Do not add repeated letters
            added.append(letter)
            

    index = 0
    for i in range(5):
        for j in range(5):
            matrix[i][j] = added[index]
            index+=1
    return matrix



def separate_same_letters(message):
    index = 0
    while (index<len(message)):
        l1 = message[index]
        if index == len(message)-1:
            message = message + 'X'
            index += 2
            continue
        l2 = message[index+1]
        if l1==l2:
            message = message[:index+1] + "X" + message[index+1:]
        index +=2   
    return message

#Return the index of a letter in the matrix
#This will be used to know what rule (1-4) to apply
def indexOf(letter,matrix):
    for i in range (5):
        try:
            index = matrix[i].index(letter)
            return (i,index)
        except:
            continue
#Implementation of the playfair cipher
#If encrypt=True the method will encrypt the message
# otherwise the method will decrypt
def playfair(key, message, encrypt=True):
    inc = 1
    if encrypt==False:
        inc = -1
    matrix = create_matrix(key)
    message = message.replace(' ','')    
    message = separate_same_letters(message)
    cipher_text=''
    for (l1, l2) in zip(message[0::2], message[1::2]):
        row1,col1 = indexOf(l1,matrix)
        row2,col2 = indexOf(l2,matrix)
        if row1==row2: 
            cipher_text += matrix[row1][(col1+inc)%5] + matrix[row2][(col2+inc)%5]
        elif col1==col2:
            cipher_text += matrix[(row1+inc)%5][col1] + matrix[(row2+inc)%5][col2]
        else: 
            cipher_text += matrix[row1][col2] + matrix[row2][col1]
    
    return cipher_text


ct = playfair(key, plaintext)
dt = playfair(key, ct, False)

print ('Encrypted text:',ct)
print ('Decrypted text:',dt)
