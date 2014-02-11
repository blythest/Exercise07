import operator
f = open("scores.txt")

whole_file = f.read()

lines = whole_file.split("\n")


scores = dict()

for line in lines:
    line = line.split(":")
    # key = line[0]
    # value = line[1]
    # scores[key] = value
    if len(line) == 2:
        scores[line[0]] = line[1]

#in descending order by value
sorted_values = sorted(scores.iteritems(), key=operator.itemgetter(1), reverse=True)
print sorted_values

#alphabetically by key
for key in sorted(scores.iterkeys()):
    print "%s: %s" % (key, scores[key])

