john = open('john_text.txt', 'r')
file_contents = john.read()
words = ['Father', 'God', 'Christ', 'Spirit', 'life', 'man']

for w in words:
    print(w + ':', file_contents.count(w))



