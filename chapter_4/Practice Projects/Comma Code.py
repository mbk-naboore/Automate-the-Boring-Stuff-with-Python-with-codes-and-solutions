spam = ['apples', 'bananas', 'tofu', 'cats']


def comma_code(the_list):
    the_full_sentence = str()
    for i in the_list:
        if i == the_list[-1]:
            the_full_sentence += f"and {i}"
            return the_full_sentence
        else:
            the_full_sentence += f"{i}, "
    return the_full_sentence


print(comma_code(spam))

