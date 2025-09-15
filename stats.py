import string

def get_book_text(a):
    with open(a) as f:
        file_content=f.read()
    return file_content

def word_count(a):
     for symbol in string.punctuation:
         text=a.replace(symbol," ")
     number_of_words=len(text.split())
     return number_of_words

def count_characters(a):
    content=get_book_text(a)
    word_symbol_list=content.split()
    character_list=[]
    for x in word_symbol_list:
        for ch in x:
            character_list.append(ch)
    d={}
    for ch in character_list:
        d[ch.lower()]=0
    for ch in character_list:
        d[ch.lower()]=d[ch.lower()]+1
    return d

def report(d):
    result_list=[]
    for key in d.keys():
        temp={"char":key,"num":d[key]}
        result_list.append(temp)
    def helper_function(d):
        #this function will extract the numerical value from the dictionary inside the list
        return d["num"]
    result_list.sort(key=helper_function,reverse=True)

    return result_list

