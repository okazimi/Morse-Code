import time

# DICTIONARY REPRESENTING MORSE CODE
MORSE_CODE_DICT = {'A': '.-', 'B': '-...',
                   'C': '-.-.', 'D': '-..', 'E': '.',
                   'F': '..-.', 'G': '--.', 'H': '....',
                   'I': '..', 'J': '.---', 'K': '-.-',
                   'L': '.-..', 'M': '--', 'N': '-.',
                   'O': '---', 'P': '.--.', 'Q': '--.-',
                   'R': '.-.', 'S': '...', 'T': '-',
                   'U': '..-', 'V': '...-', 'W': '.--',
                   'X': '-..-', 'Y': '-.--', 'Z': '--..',
                   '1': '.----', '2': '..---', '3': '...--',
                   '4': '....-', '5': '.....', '6': '-....',
                   '7': '--...', '8': '---..', '9': '----.',
                   '0': '-----', ', ': '--..--', '.': '.-.-.-',
                   '?': '..--..', '/': '-..-.', '-': '-....-',
                   '(': '-.--.', ')': '-.--.-'}


# ENCODING FUNCTION
def encrypt(message):
    # INITIALIZE EMPTY STRING
    cipher = ""
    # LOOP THROUGH EACH CHARACTER
    for char in message:
        # IF CHARACTER IS NOT A SPACE
        if char != " ":
            # ADD MORSE CODE VALUE OF CHARACTER TO CIPHER STRING
            cipher += MORSE_CODE_DICT[char] + " "
        # IF CHARACTER IS A SPACE
        else:
            cipher += " "
    # RETURN COMPLETED CIPHER
    return cipher


# DECODING FUNCTION
def decrypt(message):
    # CREATE EMPTY STRING
    decipher = ""
    # CREATE WORD VARIABLE
    word = ""
    # LOOP THROUGH EACH CHARACTER
    for char in message:
        # IF CHAR IS NOT EQUAL TO SPACE
        if char != " ":
            # KEEP TRACK OF SPACES
            space = 0
            # ADD CHARACTER TO WORD
            word += char
        # IF CHAR IS EQUAL TO SPACE
        else:
            # KEEP TRACK OF SPACES
            space += 1
            # IF SPACES == 2, ADD SPACE FOR NEW WORD
            if space == 2:
                # ADD SPACE
                decipher += " "
            else:
                # DECIPHER WORD
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT.values()).index(word)]
                # RESET WORD TO EMPTY STRING
                word = ""
    return decipher


# MAIN FUNCTION
def main():
    # WELCOME STATEMENT
    print("Hi🖐")
    # SLEEP
    time.sleep(2)
    # WELCOME STATEMENT
    print("Welcome to Morse Coder")
    # SLEEP
    time.sleep(2)
    # OBTAIN USER INPUT AND CAPITALIZE ALL CHARACTERS
    user_input = input("Please enter the text that you'd like to be encoded: ").upper()
    # FORMAT USER'S INPUT TO REMOVE DUPLICATE WHITESPACES AND NEWLINE CHARACTERS
    formatted_user_input = " ".join(user_input.split())
    # ERROR HANDLING
    # TRY TO ENCODE/DECODE TEXT
    try:
        # PASS USER INPUT TO ENCODER FUNCTION
        encoded_text = encrypt(formatted_user_input)
        # PASS ENCODED TEXT TO DECODER AND VERIFY RESULTS
        decoded_text = decrypt(encoded_text)
    # CATCH KEY ERROR
    except KeyError:
        # INFORM USER OF ERROR
        print("You entered a character that does not have a corresponding morse code value. Please try again.\n")
        # RERUN MAIN
        main()
    # IF NO ERRORS EXIST, PRINT RESULTS
    else:
        # PRINT STATEMENTS
        print(f"The Encoded Text is {encoded_text}")
        print(f"The Decoded Text is {decoded_text}")


# RUN MAIN
main()



