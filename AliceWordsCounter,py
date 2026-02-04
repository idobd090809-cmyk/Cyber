def word_frequency_counter(file_name):
    with open(file_name,'r') as file:
        text=file.read()
    mydict={}
    words=text.split()
    for word in words:
        word=word.lower()
        if word in mydict:   
            mydict[word]+=1
        else:
            mydict[word]=1
    sorted_dict=sorted(mydict.items(),key=lambda item:item[1], reverse=True)
    five_most_common=dict(sorted_dict[:5])
    result=[]
    for word, count in five_most_common.items():
        result.append(word)
    return result
most_words=word_frequency_counter("alice.txt")
print(most_words)
    
    

    
    


    
        

    
    

    