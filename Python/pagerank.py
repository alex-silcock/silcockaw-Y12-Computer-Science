#PR(A) = 0.15 + 0.85*(PR(Ti)/C(Ti) + ... + PR(Tn)/C(Tn))

# pageNameList holds the name of each page
pageNameList = [1, 2, 3]
# numberLinksOutbound list holds the number of links going into each page first page = index 0
numberLinksOutbound = [2, 1, 1]
# pageLinksList is a dictionary of pages that link to each other, the first page links to the second and third pages
pageLinksList = {1:[2, 3], 2:[1], 3:[2]}
# inital page rank value
pageRank = [1, 1, 1]
# updated page rank value
ranks = [1, 1, 1]
# number of iterations
iterations = 5
# damping factor
d = 0.85

# first for loop handles the number of iterations  
for a in range(iterations):
    # loops through each page
    for x in range(len(pageNameList)):
        sum = 0
        # loops through each page inside the dictionary
        for y in range(len(pageNameList)):
            # if the value is in the dictionary then the calculation takes place
            if x+1 in pageLinksList[y+1]:
                sum = sum + (0.85 * pageRank[y]/numberLinksOutbound[y])

        # calculates the page rank of the page
        ranks[x] = round(0.15 + sum, 2)
        
    # updates the page rank so they can be used for the next iteration
    for n in range(len(pageRank)):
        pageRank[n] = ranks[n]
    
# prints the page rank after 'a' number of iterations
print(ranks)