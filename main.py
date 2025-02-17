def main():  
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  character_set = count_characters(text)  
  print_report(book_path, num_words, character_set)

def print_report(path, count, character_set):  
  print(f"--- Begin report of {path} ---")
  print(f"{count} words found in the document\n")
  for char in character_set:
    if char.isalpha():      
      print(f"The '{char}' character was found {character_set[char]} times")  
  print("--- End report ---")

def count_characters(text):
  character_set = {}
  text = text.lower()  
  for c in text:    
    if c not in character_set:
      character_set[c] = 1
    else:
      character_set[c] += 1
  return character_set

def get_num_words(text):
  return len(text.split())

def get_book_text(path):
  with open(path) as f:
    return f.read()

main()
