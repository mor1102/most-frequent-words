#Import moudle string and sys
import string
import sys

#קורא את התוכן של הקובץ והופך את המילים בקובץ לרשימה
def file_content_to_list(file_name):
    with open(file_name,'r') as file:
        text=file.read()
    for p in string.punctuation:
         text=text.replace(p,"")
    content_list=text.split()
    return content_list

#יוצר מילון שמכיל עבור כל מילה בקובץ כמה פעמים היא הופיעה
def count_word_dictionary(list_content):
      word_count=dict()
      for word in list_content:
           if word in word_count:
                word_count[word]+=1
           else:
                word_count[word]=1
      return word_count

#יוצר רשימה שממוינת מהמילה שהופיעה הכי הרבה פעמים להכי פחות
def ordered_list(count_word):
     ordered_list=sorted(count_word.items(), key=lambda x: x[1], reverse=True)
     return ordered_list

#מדפיס את N המילים הראשונות (מספר שהמשתמש נותן) מתוך הרשימה הממוינת 
def Prints_n_words(file_name,commonN):
     list_content=file_content_to_list(file_name)
     count_word=count_word_dictionary(list_content)
     orderd_lst=ordered_list(count_word)
     for item in range(commonN):
        word, count = orderd_lst[item]
        print(f"word {word} {count} times")

#main function
def main(file_name,commonN):
    Prints_n_words(file_name,commonN)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_name = sys.argv[1]
        print(sys.argv)
        try:
            commonN = int(sys.argv[2]) 
            if commonN > 0:
                main(file_name,commonN)
            else:
                print("commonN must be higher than 0. ")
        except  ValueError:
            print("Error commonN must be an interger. ")
    else:
        print("Error, enter 2 arguments in the command line.")