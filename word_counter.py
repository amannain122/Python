words=[]
with open('file2.txt','r') as file:
    for line in file:
        for word in line.split():
            words.append(word)

words.sort()
print(words)
# print(words)
# a=0
# for item in words:
#     for i in range(len(words)):
#         if item==words[i]:
#             a+=1
#     print(item,"=",a)

word_count={}
for word in words:
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

print(word_count)

keywords=list(word_count.keys())
occur=list(word_count.values())

for item,count in zip(keywords,occur):
    print(item,"=",count)
        