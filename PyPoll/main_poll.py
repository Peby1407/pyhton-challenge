#falta hacer camino cvspath y convertir en texto
#Creating PyPoll code
#importing module os and csv

import csv
with open("text_file.txt", "a") as f:
    #csvpath = os.path.join('Resources','election_data.csv')
    #opening file
    with open('election_data.csv', encoding='UTF-8') as csvfile:
        csvreader=csv.reader(csvfile,delimiter=',')
        #skipping first row
        next(csvfile)
        votes_per_candidate = []
        total_votes=0
        for v in csvreader:
            votes=v[0]
            percandidate=v[2]
            #Counting the amount of votes
            total_votes+= 1
            #Creating votes list divided by each candidate
            votes_per_candidate.append(percandidate)
            #counting votes per candidate
            votes_Charles = votes_per_candidate.count('Charles Casper Stockham')
            votes_DeGette = votes_per_candidate.count('Diana DeGette')
            votes_Raymond = votes_per_candidate.count('Raymon Anthony Doane')
            #calculating percentages per candidate
            percent_Charles = votes_Charles/total_votes
            percent_DeGette = votes_DeGette/total_votes
            percent_Raymond = votes_Raymond/total_votes

    print("Election Results", file=f)
    print("--------------------------------", file=f)
    print("Total Votes: " , total_votes, file=f)
    print("--------------------------------", file=f)
    print("Charles Casper Stockham:",percent_Charles, "% (", votes_Charles,")", file=f)
    print("Diana DeGette: " ,percent_DeGette, "% (", votes_DeGette,")", file=f)
    print("Raymon Anthony Doane: " , percent_Raymond, "% (", votes_Raymond,")", file=f)
    print("--------------------------------", file=f)
    print("--------------------------------", file=f)
    #Creating list for results, to pick the highest amount of votes
    results=[votes_Charles,votes_DeGette,votes_Raymond]
    winner=max(results)
    #Creating conditionals to announce winner in a message
    if votes_Charles>votes_Raymond and votes_Charles>votes_DeGette:
        print("Winner : Charles Casper Stockham", file=f)
    if votes_DeGette>votes_Raymond and votes_DeGette>votes_Charles:
        print("Winner : Diana DeGette", file=f)
    if votes_Raymond>votes_DeGette and votes_Raymond>votes_Charles:
        print("Winner : Raymon Anthony Doane", file=f)
