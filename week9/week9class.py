



def getfamily():
    name = '---'
    
    family_list =[]
    while name.lower() != 'stop':
        name = input("What is the name? type 'stop' to end: ")
        if name.lower() != 'stop':
            age = input('What is their age: ')
            family_list.append({'name':name, 'age': age})
    return family_list

def savefamily(family_list):
    with open("family.txt", 'w') as fp:
        for name in family_list:
            fp.write("%s\n" % name)


def main():
    request = 
    family = getfamily()
    savefamily(family)
    print (family)

main()