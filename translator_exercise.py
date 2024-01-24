#Translator example
from translate import Translator

#help(Translator)
#this program worked only if the lines in the file are just in 1 line

translator = Translator(to_lang = 'ja', from_lang = 'en')
translation = translator.translate('I am coding today and tomorrow!')
print(translation)
try:
    with open('./sad1.txt', mode = 'r') as my_file:
        #text = my_file.readline()
        text = my_file.read()
        print(len(text))
        print(text)

        #for item in text:
        my_file_translator = Translator(to_lang = 'ja')
        my_file_translation = my_file_translator.translate(text)
        print(my_file_translation)

    with open('./sad1_ja_trans.txt', mode = 'w') as my_file1:
        my_file1.write(my_file_translation)
    with open('./sad1_ja_trans.txt', mode = 'r') as my_file2:
        txt = my_file2.read()
        print(txt)
except FileNotFoundError as err:
    print('File does not exist!')
    raise err
    
    


