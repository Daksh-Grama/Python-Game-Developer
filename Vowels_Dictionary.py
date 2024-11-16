#step 1 get user to input a statement
#step 2 convert input to lower or uppercase
#step 3 create dictionary with vowels as keys and count as value
#step 4 write a loop to itrate the user statement and update vowel counts

vc = input("enter a sentence please : ").lower()
Vowel_Count = {"a": 0, "e": 0 , "i": 0, "o": 0, "u": 0}

for x in vc:
    if x in Vowel_Count:
        Vowel_Count[x] += 1

print(Vowel_Count)