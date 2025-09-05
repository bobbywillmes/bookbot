from stats import get_num_words, get_char_count, sort_char_count
import sys

def get_book(filepath):
  print(f'Analyzing book found at {filepath}...')
  with open(filepath, 'r') as file:
    book = file.read()
  return book

def main():
  print('============ BOOKBOT ============')
  if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  book_path = sys.argv[1]
  book = get_book(book_path)
  get_num_words(book)
  char_count = get_char_count(book)
  sorted_char_count = sort_char_count(char_count)
  print("--------- Character Count -------")
  for entry in sorted_char_count:
    print(f"{entry['char']}: {entry['num']}")
  print('============= END ===============')

main()
