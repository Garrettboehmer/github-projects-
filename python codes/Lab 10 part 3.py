#Garrett Boehmer
#File Encryption and Decryption
#This program reads in a txt file and converts it using a Ceasar Cipher

def encrypt(encrypter, file):
    #i needed to add this opening and the immedietely closing of file since once the file name is changed it changes everywhere
    code_file = open(file, 'r')
    file_decry_name = code_file.read()
    code_file.close
    #user input changing the file name then opening it as a wriiten object
    file_name = input('what should be the file be called?: ')
    file_name = file_name + '.txt'
    code_write = open(file_name, 'w')
    #for loop that goes chracter by character and makes them all upper case before encrypting it
    for characters in file_decry_name:
        characters = characters.upper()
        code_write.write(encrypter.get(characters))
    code_write.close

    return file_name

#i print the result to the screen and i also write it to the file in case the code is double or more encrypted
def decrypt(decrypter, file_name):
    file = open(file_name, 'r')
    file_read = file.read()
    file.close
    on_screen = ''

    decry_file_name = input('what should the decrypted file name be?: ')
    decry_file_name = decry_file_name+'.txt'
    decry_write = open(decry_file_name, 'w')

    for characters in file_read:
        characters = characters.upper()
        decry_write.write(decrypter.get(characters))
        on_screen += decrypter.get(characters)
    print(on_screen)
    decry_write.close

    return decry_file_name

def main():
    #empty ditionary for encryption
    code_encry = {}
    #empty dictionary for decreiption
    code_decry = {}
    #file that is going to turn into a user input
    file = ''
    #user input for the menu
    user_input = 0
    #simple list used to control the while loop
    access = []
    #dictionary encryption dictionary
    code_encry = {'A':'M', 'B':'N', 'C':'O', 'D':'P', 'E':'Q' ,'F':'R' ,'G':'S', 'H':'T', 'I':'U', 'J':'V', 'K':'W', 'L':'X', 'M':'Y', 'N':'Z', 
    'O':'A', 'P':'B', 'Q':'C', 'R':'D', 'S':'E' ,'T':'F', 'U':'G', 'V':'H' ,'W':'I' ,'X':'J', 'Y':'K', 'Z':'L', ' ': ' '}

    #i didnt want to retype all that so i made a loop that auto made my decryption dictionary
    for key in code_encry:
        code_decry[code_encry.get(key)] = key

    #since the name is being changed and its being called and read then closed in each function i just set the file name to the initial document to be encrypted
    file = 'texttoencrypt.txt'
    #setting to 1 so it hits the while loop
    user_input = 'Enter loop'
    access = [1,2,'Enter loop']
    while user_input in access or user_input <= 1 or user_input > 3:

        try:
            print('Enter a 1 to encrypt the file')
            print('Enter a 2 to decrypt the file')
            user_input = int(input('Enter a 3 to exit: '))
        except ValueError:
            print('********************************')
            print('Please enter an integer')

        if user_input == 1:
                file = encrypt(code_encry, file)
        elif user_input == 2:
                file = decrypt(code_decry, file)
        elif user_input == 3:
            print('Thank you for using the encryption and decryption program. Goodbye!')
        else:
            print('Please enter either a 1, 2 or 3')
            print('********************************')

main()