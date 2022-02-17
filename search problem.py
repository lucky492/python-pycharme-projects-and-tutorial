"""                      Search Engine

You have a list containing some sentences.Take a query string as input from
user. You have to pull out sentence matching this query by user in decreasing
order of relevance.Relevance means that sentence which has maximum number of
matching words.

Example
 sentence =["python is good","python is not snake python","this is good"]

input -
    python is
output -
    we got 3 result

    1.python is not snake python    # 1st bcz there are 2 'python' & 1 'is'
    2.python is good                # 1st bcz there are 1 'python' & 1 'is'
    3.this is good                  # 1st bcz there are 0 'python' & 1 'is'
"""


# def searchengine(sentence1, sentence2):
#     word1 = sentence1.strip().split(" ")
#     user_word = sentence2.strip().split(" ")
#
#     no_of_search = 0
#
#     for u_words in user_word:
#         for words in word1:
#             if u_words.lower() == words.lower():
#                 # for testing purpose
#                 # print(f"{u_words} is matching with {words}")
#                 no_of_search += 1
#     return no_of_search
#
#
# if __name__ == '__main__':
#     list = ["python not snake python", "this is good", "python is is good"]
#
#     user = input("enter the word you want to search : ")
#
#     # print(searchengine("this is good ",user)) # for testing purpose
#
#     # to store no of search of sentence
#     list2 = [searchengine(sentence, user) for sentence in list]
#
#     # without suing list comprehensiom
#     # for loop is used to extract each sentence in list like
#     # for sentence in list:
#     #     # print(sentence) #testing purpose
#     #         list2.append(searchengine(sentence,user))
#     # print(list2) #testing purpose
#
#     '''arrange list2 in descending order so we will sort the list2 and reverse it'''
#     sorted_list = []
#
#     # without using list comprehension
#     for s in sorted(zip(list2,list) ,reverse=True):
#         sorted_list.append(s)
#
#     '''reverse = True ,reverse the sorted list in descending order'''
#     print(sorted_list) #testing purpose
#
#     print(f"{len(sorted_list)} search found")
#     '''now we have print only the sentences as per the question'''
#     for score, item in sorted_list:
#         print(f"{score} . {item} ")
#



'''above program without using list comprehension'''
# def search(sentence1,sentence2):
#     words1 = sentence1.split(" ")
#     words2 = sentence2.split(" ")
#     n_of_search = 0
#
#
#     for word1 in words1:
#         for word2 in words2:
#             if word1 == word2:
#                 # print(f"{word1} is marching with {word2}")
#                 n_of_search+=1
#     return n_of_search #return to search()
#
#
# if __name__ == '__main__':
#     list = ["hello world","python is is not snake","python is good"]
#
#     user = input("Enter your search\n: ")
#
#     list2=[]
#     for sentence in list:
#         list2.append(search(user,sentence))
#
#     """but we don't have to print score,we have to print words
#     in place of score"""
#
#     #print words
#
#     # list3 = [list3 for list3 in sorted(zip(list,list2) ,reverse=True)]
#
#     list3=[]
#     for sent in sorted(zip(list,list2),reverse=True):
#         list3.append(sent)
#         # print(sent)
#
#
#     '''now we have to print as per the question'''
#
#     for sentences,score in list3:
#         print(f" {sentences}.{score} .")
#




"""above program without ' if __name__ == '__main__': '"""

# list = ["hello world","python is is not snake","python is good"]
#
# user = input("Enter the search keyword - ")
#
# #match
# def search(word1,word2):
#     user_word = word1.strip().split(" ")
#     list_word = word2.split(" ")
#     score = 0
#     for w1 in user_word:
#         for w2 in list_word:
#             if w1.upper() == w2.upper():
#                 print(f"{w1} is being matched with {w2}")
#                 score +=1
#     return score
#
# # a=search(user,"hello is is")
# # print(a)
#
#
# list2=[]
# for sentences in list:
#     scores_list = search(user,sentences)
#     #now store the scores in list 2
#     list2.append(scores_list)

# print(list2)

'''we have stored the scores in list so that we can
print the string having most score in list'''

# list3 = []

# for arranged in sorted(zip(list,list2), reverse=True):
#     list3.append(arranged)

'''or'''
# a = sorted(zip(list,list2), reverse=True)
#
# for arranged in a:
#     list3.append(arranged)
#
# print(list3)
#
# #print as per question
# for score,result in list3:
#     print(f"{result} . {score}")