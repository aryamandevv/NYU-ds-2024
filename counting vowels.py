def count_vowels(word):
  vowels = 'aeiouAEIOU'
  count = 0

  for char in word:
    if char in vowels:
      count += 1

  return count

while True:
  word = input("Enter a word (or type 'exit' to quit): ")
  if word.lower() == 'exit':
    print("goodbye za")
    break
  else:
    print(f"The word {word} has {count_vowels(word)} vowels.")
