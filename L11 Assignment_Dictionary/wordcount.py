# 읽어 들여오는 텍스트 파일명("Les_Miserables-Victor_Hugo.txt")
# 구두점을 없애주기 위함 ("import string")
import string

f = open("Les_Miserables-Victor_Hugo.txt","r")


text = f.read()
text = text.translate(str.maketrans('', '', string.punctuation))

text = text.split()


wordCount = {}

for w in text:
    if w not in wordCount:
        wordCount[w] = 1
    else:
        wordCount[w] += 1

# value값을 기준으로 내림차순 정렬
a = sorted(wordCount.items(), key=lambda x : x[1], reverse = True)

f = open("result.txt", "w")
for _ in range(1000):
    b = a[_]
    word_name = b[0]
    word_count = str(b[1])
    f.write(word_name+"\t"+word_count+"\n\n")

f.close()