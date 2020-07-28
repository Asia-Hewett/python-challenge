import os
import csv

election_data = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('Analysis', 'election_analysis.txt')

analysis = ""
winner = 0
voter_count = 0
candidates = []
total_votes = []
perc_vote_rec = []

with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    # check and make sure the delimter is a comma
    # print(csv_header)

    for vote_cast in csvreader:
        # this looks through the 0th column and adds 1 each time a vote is cast
        # used this to check how many total votes were cast
    # print(voter_count)
        if (vote_cast[0]) != "csv_header":
            voter_count += 1
            # this adds candidates not already in the array "candidates"
            # not in function looks to see if unique variables are not already
            #            in the array "candidates"
            if (vote_cast[2] not in candidates):
                total_votes.append(1)
                candidates.append(vote_cast[2])
            else:
                total_votes[candidates.index(vote_cast[2])] += 1
                
    for unique_total in total_votes:
        percentage = 0
        percentage = '{:.1%}'.format(round((unique_total / voter_count) ,2))
        perc_vote_rec.append(percentage)
    
    winner = max(perc_vote_rec)

    winner_index = perc_vote_rec.index(winner)

    for index, redbull in enumerate(candidates):
        analysis += f"{redbull}: {perc_vote_rec[index]} ({total_votes[index]})\n"
    # print(analysis)
    output = (
    f"Election Results\n"
    f"-------------------------\n"
    f"Total Votes: {voter_count}\n"
    f"-------------------------\n"
    f"{analysis}"
    f"-------------------------\n"
    f"Winner: {candidates[winner_index]}\n"
    f"-------------------------\n")

    print(output)
    with open(output_path, 'w') as txtfile:
        txtfile.write(output)




        
    