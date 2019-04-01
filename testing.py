# import os
# import numpy as np
# from collections import Counter
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.svm import LinearSVC
# from sklearn.metrics import confusion_matrix
# import pickle
#
#
# def make_Dictionary(email_received):
#
#     all_words = []
#     for email_line in email_received.splitlines(True):
#         words = email_line.split(" ")
#         all_words += words
#
#     dictionary = Counter(all_words)
#
#     list_to_remove = dictionary.keys()
#     for item in list(list_to_remove):
#         if item.isalpha() == False:
#             del dictionary[item]
#         elif len(item) == 1:
#             del dictionary[item]
#     dictionary = dictionary.most_common(3000)
#     # print('dict  ')
#     # print(dictionary)
#     return dictionary
#
#
# def extract_features(email_received):
#
#     features_matrix = np.zeros((1,3000))
#     for email_line in email_received.splitlines(True):
#         words = email_line.split(" ")
#         for word in words:
#             wordID = 0
#             for i,d in enumerate(dictionary):
#                 if d[0] == word:
#                     wordID = i
#                     features_matrix[0, wordID] = words.count(word)
#     return features_matrix
#
#
# # Create a dictionary of words with its frequency
# email = """Hey amrita. Hope you are doing fine. How are things going around"""
# # email = str(input("Enter your email "))
# dictionary = make_Dictionary(email)
#
# test_labels = np.zeros(1)
# test_labels[0:1] = 0
# test_matrix = extract_features(email)
#
# filename = 'amrita_test_mail.sav'
# # load the model from disk
# loaded_model = pickle.load(open(filename, 'rb'))
#
# result2 = loaded_model.predict(test_matrix)
# # print(result2)
# print(confusion_matrix(test_labels, result2))


import os
import numpy as np
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.svm import LinearSVC
from sklearn.metrics import confusion_matrix
import pickle


def make_Dictionary(train_dir):
    emails = [os.path.join(train_dir,f) for f in os.listdir(train_dir)]
    all_words = []
    for mail in emails:
        with open(mail) as m:
            for i,line in enumerate(m):
                if i == 2:
                    words = line.split()
                    all_words += words

    dictionary = Counter(all_words)

    list_to_remove = dictionary.keys()
    for item in list(list_to_remove):
        if item.isalpha() == False:
            del dictionary[item]
        elif len(item) == 1:
            del dictionary[item]
    dictionary = dictionary.most_common(3000)
    return dictionary


def extract_features(test_email):
    feature_matrix = np.zeros((1,3000))
    for email_line in test_email.splitlines():
        words = email_line.split(" ")
        for word in words:
            word_id = 0
            for i, d in enumerate(dictionary):
                if d[0] == word:
                    word_id = i
                    feature_matrix[0,word_id] = words.count(word)

    return feature_matrix

while True:
    train_dir = 'ling-spam/train-mails'
    dictionary = make_Dictionary(train_dir)
    test_email = raw_input("Enter email: \n")
    if test_email == "exit":
        break

    test_matrix = extract_features(test_email)
    # print(test_matrix)
    file_name = 'amrita_test_mail.sav'
    loaded_model = pickle.load(open(file_name, 'rb'))
    result = loaded_model.predict(test_matrix)
    # print(result)

    if result == 1:
        print ("SPAM \n \n")
    else:
        print ("NOT SPAM \n \n")