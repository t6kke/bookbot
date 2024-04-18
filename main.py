book_path = "books/frankenstein.txt"



def main(book_path):
    content = book_text(book_path)
    #print(content)

    word_count = count_words(content)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words counted in the book")
    print("")

    letter_dict = count_letters(content)
    #print(letter_dict)
    
    #report_letters(letter_dict)

    letter_data_list = sort_dictionary(letter_dict)
    letter_data_list.sort(reverse=True, key=sort_on)
    report_letters2(letter_data_list)

    print("--- End report ---")




def book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def count_letters(text):
    result_dict = {}
    for letter in text:
        lowercase_letter = letter.lower()
        if result_dict.get(lowercase_letter) != None:
            nbr = result_dict[lowercase_letter]
            result_dict.update({lowercase_letter:nbr+1})
        else:
            result_dict[lowercase_letter] = 1
    return result_dict


def sort_dictionary(input_dictionary):
    result_list = []
    for item in input_dictionary:
        temp_dict = {}
        temp_dict["letter"] = item
        temp_dict["count"] = input_dictionary[item]
        result_list.append(temp_dict)

    return result_list

def sort_on(dict):
    return dict["count"]


def report_letters(letter_dict):
    for item in letter_dict:
        letter = item
        count = letter_dict[item]
        print(f"Letter {letter} was counted {count} times")

def report_letters2(list_of_dict):
    for item in list_of_dict:
        letter = item["letter"]
        count = item["count"]
        if letter.isalpha():
            print(f"The \'{letter}\' character was found {count} times")


main(book_path)