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
n = int(strip_file[0]) # number of search terms
print("n: ", n)
search_terms = strip_file[1:n+1]
print("search_terms: ", search_terms)
text = strip_file[n+1]  # text to search in
print("text: ", text)

# create a list with the index positions of each of the search terms found in the text:




