look_up = str((input("What acronym are you looking for?\n"))).upper()

found = False

with open('software_acronyms.txt') as file:
    for line in file:
        if look_up in line:
            print(line)
            found = True
            break

if not found:
    print('The string was not found')