import urllib.request

#String data.
url="http://google.com"
html_data=urllib.request.urlopen(url).read().decode('utf-8')

#data
list_word=[]
freq_word=[]

#check with older string.if not found add it in word_list otherwise increment the freq.
def match_string(value):
    for i in range(len(list_word)):
        if list_word[i]==value :
            freq_word[i]+=1
            return 
    list_word.append(value)
    freq_word.append(1)

def match_seperator(value):
    if((value<='Z' and value>='A') or (value <='z' and value>='a') or (value<='9' and value>='0') or value=='@'):
        return False
    return True


def differtiate_word():
    last=""
    keep=False
    for x in html_data:
        if(keep):
            if x=='>': 
                keep= False
        else:
            if x=='<':
                keep=True 
            else:
                if match_seperator(x):
                    if len(last)>1 :
                        match_string(last)
                    last=""
                else:
                    last+=x
    if(len(last)):
        match_string(last)

def print_output():
    print("Total Different Text Founds : ",len(list_word))
    for i in range(len(list_word)):
        space=""
        for j in range(len(list_word[i]),25):
            space+=" "
        print(list_word[i],space,freq_word[i])

differtiate_word()
print_output()
