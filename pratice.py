# # import mysql.connector
# # connection= mysql.connector.connect(host='localhost',user='root',password='2324',database='practise')
# # # print(connection)

# # cursor = connection.cursor()

# # # cursor.execute("CREATE DATABASE practise ")
# # # cursor.execute("CREATE TABLE emptable(ID int,name varchar(225),address varchar(225))")
# # # cursor.execute("SHOW TABLES")
# # # for x in cursor:
# # #     print(x)

# # sql ="INSERT INTO emptable(ID,name,address)VALUES(%s,%s,%s)"
# # val=[(1,"sai","hyd"),(2,"teja","gdv"),(3,"rakesh","vjy")]
# # cursor.executemany(sql,val)
# # connection.commit()
# # print("insert records")
# # cursor.close()


# #anagram :
# def are_anagrams(str1, str2):
    
#     return sorted(str1.replace(" ", "").lower()) == sorted(str2.replace(" ", "").lower())


# pairs = [
#     ("Dog", "god"),
#     ("Cat", "tac"),
#     ("Cat", "act"),
#     ("angle", "glean"),
#     ("tar", "rat"),
#     ("car", "rac")
# ]

# for str1, str2 in pairs:
#     print(f"'{str1}' and '{str2}' are anagrams: {are_anagrams(str1, str2)}")


# #panagram
# import string

# def findMissingLetters(sentence):
    
#     alphabet = set(string.ascii_lowercase)
    
#     sentence_letters = set(filter(str.isalpha, sentence.lower()))
    
#     missing = alphabet - sentence_letters
#     return "".join(sorted(missing))


# sentence = "The quick brown fox jumps over the lazy dog"
# missing_letters = findMissingLetters(sentence)

# if not missing_letters:
#     print("The sentence is a pangram.")
# else:
#     print("The sentence is not a pangram. Missing letters:", missing_letters)


# # #3. remove dulipcates
# # def remove_duplicates(sentence):
# #     words = sentence.split()  
# #     unique_words = []
# #     for word in words:
# #         if word not in unique_words:
# #             unique_words.append(word)  
# #     return " ".join(unique_words)  


# # input1 = "Good day day bye bye"
# # input2 = "greet the day user greet good day"

# # print(remove_duplicates(input1))  
# # print(remove_duplicates(input2))  

#4 weight of a string
def calculate_weight(string):
    weight = 0
    for char in string.lower(): 
        if char.isalpha(): 
            weight += ord(char) - ord('a') + 1 
    return weight


input_string = "Apple"
output = calculate_weight(input_string)
print(f"Weight of '{input_string}' is: {output}")

# #5
# def starts_with_s(strings):
   
#     return [string for string in strings if string.lower().startswith('s')]

# def has_unique_characters(string):
   
#     return len(set(string)) == len(string)


# input_strings = ["apple", "sample", "search", "cat"]


# result_a = starts_with_s(input_strings)
# print("Strings starting with 'S':", result_a)

 
# result_b = {string: has_unique_characters(string) for string in input_strings}
# print("Unique character status:", result_b)

def cal_weight(string):
    weight = 0
    for char in string.lower():
        if char.isalpha():
            weight += ord(char) - ord('a')+1
    return weight

input_string = ("Teja")
output = cal_weight(input_string)
print(f"cal_weight'{input_string}' is : {output}")



