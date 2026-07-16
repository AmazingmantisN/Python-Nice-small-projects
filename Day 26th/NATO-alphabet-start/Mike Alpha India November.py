import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
phonetic_dict = {row['letter']:row['code'] for index,row in df.iterrows()}

user_word = input("Enter your word: ")
uesrwordlist = list(user_word.upper())
user_code_word = [phonetic_dict[value] for value in uesrwordlist]

for i in user_code_word:
  print(i, end=" ")
