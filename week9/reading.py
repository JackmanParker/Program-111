


def main():
    print("test")
    provinces = read_list("/Users/parker/Desktop/Class Codes/Program 111/week9/provinces.txt")
    print(provinces)
    provinces.pop(0)
    print(provinces)
    provinces.pop(len(provinces) - 1)
    print(provinces)
    for idx, item in enumerate(provinces):
        if item == "AB":
            provinces[idx] = "Alberta"
    print(provinces)
    print(f"The province Alberta appears {provinces.count('Alberta')}") 


def read_list(filename):
    #Reading the file
    listname = []
    with open(filename, "rt") as text_file:
        for line in text_file:
            clean_line = line.strip()
            listname.append(clean_line)

    return listname

main()