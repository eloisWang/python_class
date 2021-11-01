"""
paragraph=
   Growing up, they remember a home filled with state-of-the-art technology — like an early digital clock and some of the first home computers.
   They came to StoryCorps to reflect on their unforgettable childhood and their father’s colossal personality.
"""
"""
1) How many words in the paragraph : example count of the words
2) How many unique words:
3) How many characters:
4) Need count of characters
5) I need count of special characters
6) Print all the special characters
"""

paragraph="""
   Growing up, they remember a home filled with state-of-the-art technology — like an early digital clock and some of the first home computers.
   They came to StoryCorps to reflect on their unforgettable childhood and their father’s colossal personality.
"""

split_paragraph = paragraph.split()
print(f"Number of words: {len(split_paragraph)}")
print(f"Number of unique words: {len(set(split_paragraph))}")
print(f"Number of characters: {len(paragraph)}")
print(f"umber of unique characters: {len(set(paragraph))}")
special_char_defined = "!\"#$%&'()*+,-./:;<=>?@[\]^_`{|}~—’"
special_char_included = set(special_char_defined).intersection(set(paragraph))
print(f"Number of special characters: {len(special_char_included)}")
print("Special characters: " + " ".join(special_char_included))
