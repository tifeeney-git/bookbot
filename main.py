def main():
    with open('books/frankenstein.txt') as f:
        file_contents = f.read()
   # noWords = calculateNoWords(file_contents)
    #print(f'Number words  {noWords}')
    dict = numberChars(file_contents)
    list =[]
    list = dictToList(dict, list)
    list.sort(reverse=True, key=sort_on)
    printReport(list)

def calculateNoWords(words):
    splitWords = words.split()
    return len(splitWords)

def numberChars(words):
    lowered_string = words.lower()
    dict = {}
    for i in range(len(lowered_string)):
        char = lowered_string[i]
        count = dict.get(char)
        if count is None:
            count=0
        count+=1
        new_dict = {char: count}
        dict.update(new_dict)
    return dict

def dictToList(dict, list):
    for key in dict:
        char = key
        if(char.isalpha()):
            list.append({'char':char, 'num': dict[char]})
    return list

def printReport(list):
    for i in list:
        char = i['char']
        number = i['num']
        print(f"The '{char}' character was found '{number}' times")
    
def sort_on(dict):
    return dict['num']

main()
