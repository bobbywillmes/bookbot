def get_num_words(text):
  num_words = len(text.split())
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")

def get_char_count(text):
  char_count = {}
  for char in text:
    if char.isalpha():  # Consider only alphabetic characters
      char = char.lower()  # Normalize to lowercase
      if char in char_count:
        char_count[char] += 1
      else:
        char_count[char] = 1
  return char_count

def sort_on(items):
  return items['num']

def sort_char_count(char_count_dict):
  sorted_chars = []
  for entry in char_count_dict:
    new_entry = {"char": entry, "num": char_count_dict[entry]}
    sorted_chars.append(new_entry)
  sorted_chars.sort(key=sort_on, reverse=True)
  return sorted_chars