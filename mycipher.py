import sys

sft = int(sys.argv[1])
message = ""
output = ""

for line in sys.stdin:

    line = line.upper()

    for word in line.split():

        for punc in '!,.?;"-':
            word = word.replace(punc, "")

        for letter in word:

            char = ord(letter)

            if 65 <= char <= 90:
                char += sft

                if char > 90:
                    char -= 26

            message += chr(char)


wc = 0

for i in range(0, len(message), 5):
    output += message[i:i+5] + " "
    wc += 1

    if wc == 10:
        output += "\n"
        wc = 0

print(output)

