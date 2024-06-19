import time

sentence = "welcometoourgame"


now = time.time() 
sentence = list(sentence)

count = 0

while True:
    try:
        if (time.time() - now) >= 0.5:
            print(sentence[count])
            count += 1
            now = time.time() 
    except:
        exit
    print("hello")
    time.sleep(0.1)

