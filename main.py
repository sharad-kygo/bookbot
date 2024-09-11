def main():
    print("--- Begin report of books/frankenstein.txt ---")  
    print(f"{countwords()} words found in the document")
    return sorto(countofletters())
    
        

def countwords():
    file_contents = ""
    file_spl = ""
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        file_spl = file_contents.split()
    return len(file_spl)


def countofletters():
    dicto = {}
    file_contents = ""
    low_case = ""
    uniquechar = []
    sumun = 0
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        low_case = file_contents.lower()
    for char in low_case:
        if char not in uniquechar:
            uniquechar.append(char)
    for charw in uniquechar:
        dicto[charw] = 0
    for charx in low_case:
        for chary in uniquechar:
            if charx == chary:
                dicto[chary] += 1
    return dicto

def sorto(dict):
    listo = []
    listo = sorted(dict.items(),key=lambda x:x[1], reverse=True)
    for i in listo:
        if i[0].isalpha():
            print(f"The {i[0]} character was found {i[1]} times")
    print("--- End report ---")
        
             



main()







    
