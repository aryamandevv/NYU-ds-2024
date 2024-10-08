animals = ['tiger', 'elephant', 'monkey', 'zebra', 'panther']

for animal in animals:  
    print(animal.upper())  
more_animals = ['lion', 'giraffe', 'bear']
for animal in more_animals:
    print(animal.upper())

while True:
  word = input("Enter a word (or type 'exit' to quit): ")
  if word.lower() == 'exit':  
    print("Goodbye!")
    break  
  else:
    print(f"Uppercase: {word.upper()}")  
    print(f"Lowercase: {word.lower()}")
