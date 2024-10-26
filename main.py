def sort_on(dict):
    return dict["num"]

def count_words(string):
  return len(string.split())

def letter_count(string):
  counter = {}
  words = string.split()
  for word in words:
    lower_word = word.lower()
    for letter in lower_word:
      if letter in counter:
        counter[letter] += 1
      else:
        counter[letter] = 1
  letter_dict_list = []
  for char in counter:
    letter_dict_list.append({
      "char": char,
      "num": counter[char]
    })
  return sorted(letter_dict_list, key=sort_on, reverse=True)


def main():
  with open("books/frankenstein.txt") as f:
    text = f.read()
    word_count = count_words(text)
    letter_dict = letter_count(text)
    print('--- Begin report of books/frankenstein.txt ---')
    print(f"{word_count} words found in the document")
    for char_dict in letter_dict:
      print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print('--- End report ---')


main()