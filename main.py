import string 
from stats import word_count
from stats import count_characters
from stats import report
import sys
def get_book_text(a):
    with open(a) as f:
        file_content=f.read()
    return file_content

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book_path=sys.argv[1]


def main(b):
    absolute_path=book_path

    result_string= get_book_text(absolute_path)
    print(result_string)


result_var=count_characters(book_path)

num_words=word_count(get_book_text(book_path))



var1=report(result_var)
print("============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ----------\nFound 75767 total words\n--------- Character Count -------")
for chinfo in var1:
    if chinfo["char"].isalpha():
        print(f"{chinfo["char"]}: {chinfo["num"]}")
    

