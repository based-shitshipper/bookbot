import sys
book_path = sys.argv[1]
def get_book_text(book_path):
    with open(book_path) as f:
        file_contents = f.read()
    return file_contents
'''============================================'''
'''                                            '''
def word_count(book_path):
    book = get_book_text(book_path)
    count = len(book.split())
    return count 
'''============================================'''
'''                                            '''
def character_count(book_path):
    l = get_book_text(book_path)

    d = {}
    for char in l:
        if char.isalpha():
            char = char.lower()
        if char in d:
            d[char] += 1
        else:
            d[char] = 1
    return d
'''============================================'''
'''                                            '''
def sort_on(d):
    return d['num']
'''============================================'''
'''                                            '''
def sort_characters(character_count):
    chars = []
    for key, value in character_count.items():
        if key.isalpha():
            chars.append({'char': key, 'num': value})
    chars.sort(reverse=True, key=sort_on)
    return chars
'''============================================'''
'''                                            '''
def main(book_path):
    char_count = character_count(book_path)
    print("============ BOOKBOT ============")
    print("Analyzing book found at" + " " + f"{book_path}" "...")
    print("----------- Word Count ----------")
    print(f"Found {word_count(book_path)} total words")
    print("--------- Character Count -------")
    for item in sort_characters(char_count):
        print(f"{item['char']}: {item['num']}")
