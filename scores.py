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
# print sorted_values

# alphabetically by key
# for key in sorted(scores.iterkeys()):
    # print "%s: %s" % (key, scores[key])

# collect the keys that have the same value and sort alphabetically
new_scores = {}
for key, value in scores.iteritems():
    new_key = value
    new_value = key
    if new_scores.get(new_key):
        # print new_scores[new_key]
        new_scores[new_key].append(new_value)
    else:
        new_scores[new_key] = [new_value]

for key, value in new_scores.iteritems():
    new_scores[key] = sorted(new_scores[key])

# print new_scores

# ask for user input to search through restaurant listings
while True:
    print "We have a list of restaurants with their ratings.  Please choose from the following options."
    user_input = raw_input("Type 1 to search by rating, type 2 to search for a particular restaurant." )

    if int(user_input) == 1:
        print 'Search by rating. Enter a numerical value between 1 and 5.'
        rating_input = raw_input()

    elif int(user_input) == 2:
        print "Search by restaurant. To view directory, type 'directory.' If you know the name of the restaurant"
        + "you're searching for, enter a name."
    else:
        print 'Invalid input.'


