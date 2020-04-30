# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()

def censor_string(string, email):
  censor_string = "#" * len(string)
  new_email = email.replace(string, censor_string)
  return new_email

# print(censor_string("learning algorithms", email_one))

def censor_list(lst, email):
  full_text = email
  for phrase in lst:
    full_text = censor_string(phrase, full_text)
  return full_text

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"] 

# print(censor_list(proprietary_terms, email_two))

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

def censor_plus_negative_words(negatives, lst, email):
  full_text = email.split()
  bad_word_counter = 0
  for i in range(len(full_text)):
    if full_text[i] != "." or full_text[i] != "?" or full_text[i] != "!":
      for negs in negative_words:
        if full_text[i] == negs:
          ++bad_word_counter
          if bad_word_counter > 1:
            full_text[i] = "#" * len(negs)
    else:
      bad_word_counter = 0
  full_text = " ".join(full_text)
  new_full_text = censor_list(lst, full_text)
  return new_full_text

# print(censor_plus_negative_words(negative_words, proprietary_terms, email_three))

def censor_negatives(negatives, email):
  full_text = email
  for neg in negatives:
    full_text = censor_string(neg, full_text)
  return full_text

def censor_it_all(negatives, lst, email):
  print(email)
  new_text = censor_list(lst, email)
  new_text = censor_negatives(negatives, new_text)
  newer_text = new_text.split()
  for i in range(len(newer_text)):
    if "#" in newer_text[i]:
      newer_text[i-1] = "#" * len(newer_text[i-1])
      if len(newer_text) > i+1:
        newer_text[i+1] = "#" * len(newer_text[i+1])
  final_text = " ".join(newer_text)
  return final_text

print(censor_it_all(negative_words, proprietary_terms, email_four))