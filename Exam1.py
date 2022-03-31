sentence = input()

command = input()

while command != "Finish":

    if command == "Finish":
        break

    command = input().split()
    command_name = command[0]

    if command[0] == "Replace":
        current_chr = command[1]
        new_chr = command[2]
        sentence = sentence.replace("e", "a")
        print(sentence)

    elif command[0] == "Cut":
        start = int(command[1])
        end = int(command[2])
        if start and end:
            new_sentence = sentence.remove[int(command[1]):int(command[2])]
            print(" ".join(new_sentence))
        else:
            print("Invalid indexes!")

    elif command[0] == "Make":
        if command[1] == "Upper":
            sentence.upper()
        elif command == "Lower":
            sentence.lower()



