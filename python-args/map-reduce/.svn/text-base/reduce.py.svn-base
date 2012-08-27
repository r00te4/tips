from operator import itemgetter
import sys

word2count = {}

for line in sys.stdin:
    line = line.strip()
    word, count = line.split('t', 1)
    try:
        count = int(count)
        word2count[word] = word2count.get(word, 0) + count
        print word2count[word] 
    except ValueError:
        pass

print word2count

sorted_word2count = sorted(word2count.items(), key=itemgetter(0))

for word, count in sorted_word2count:
    print ("%st%s" % (word, count))
