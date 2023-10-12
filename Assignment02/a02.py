# **String Multimatching**
#Example input:
#      2          <-- Number of search terms
#      p          <-- First search term
#      pup        <-- Second search term
#      popup      <-- Line to search in

#For each test case, output n lines, where the _i_’th line contains the positions of all the occurrences of the _i_’th pattern in text, from first to last, separated by a single space.

#Example output (0 based array):
#      2 4        <-- Index positions for the first search term "p", separated with space
#      2          <-- Index position for the second search term "pup"
#The problem is to find the index positions of the search terms in the input text and print a line for each search term.

#The first line of the input contains an integer _n_, the number of search terms. The next _n_ lines contain the search terms, one per line. The last line contains the text to search in.
# read the input file stringmultimatching.in and parse the input

file = open("Assignment02/stringmultimatching.in", "r")
read_file = file.readlines()
strip_file = [x.strip() for x in read_file]
print("strip_file: ", strip_file)

line_number = 0
ns = []
all_search_terms = []
texts = []
while line_number < len(strip_file):
    #print("line_number: ", line_number)
    n = int(strip_file[line_number]) # number of search terms
    ns.append(n)
    #print("n: ", n)
    search_terms = strip_file[line_number+1:line_number+1+n]
    all_search_terms.append(search_terms)
    #print("search_terms: ", search_terms)
    text = strip_file[line_number+n+1]  # text to search in
    texts.append(text)
    #print("text: ", text)
    line_number += n + 2

full_list_of_dicts = []
for j in range(len(texts)):
    print("j: ", j)
    text = texts[j]
    # create a list that contains the index positions of the search terms in the input text
    list_of_dicts = []
    for search_term in all_search_terms[j]:
        #print("search_term: ", search_term)
        index_positions = []
        for i in range(len(text)):
            if text[i:i+len(search_term)] == search_term:
                index_positions.append(i)
        list_of_dicts.append({search_term: index_positions})
        #print(" ".join(str(x) for x in index_positions))
    full_list_of_dicts.append(list_of_dicts)
    #print("list_of_dicts: ", list_of_dicts)

print("full_list_of_dicts: ", full_list_of_dicts)

with open('Assignment02/my_stringmultimatching.ans', 'w') as f:
    for i in range(len(full_list_of_dicts)):
        for j in full_list_of_dicts[i]:
            for key, value in j.items():
                f.write(" ".join(str(x) for x in value))
                f.write('\n')
