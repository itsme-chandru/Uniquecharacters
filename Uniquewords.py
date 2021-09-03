with open("abc.txt","r") as f:
    f_contents = f.read()
    list_words = f_contents.split()
    list_words=set(list_words)
    list_words = list(list_words)
    len_list_words=[]
    for i in range(len(list_words)):
        len_list_words.append(len(list_words[i]))
    list_dictionary = dict(zip(list_words, len_list_words))
    sort_dict = dict(sorted(list_dictionary.items(), key=lambda kv: kv[1]))
    with open("output1.txt", mode="w") as op:
        for k, v in sort_dict.items():
            op.write(str(k) + ' ' + str(v) + '\n')
    f.close()