candidats = ['albert','emilie','oscar','marine','max']
 
vote = [
   {'nb':3273,'rang':[1,5,4,2,3]},
   {'nb':2182,'rang':[5,1,4,3,2]},
   {'nb':1818,'rang':[5,2,1,4,3]},
   {'nb':1636,'rang':[5,4,2,1,3]},
   {'nb':727,'rang':[5,2,4,3,1]},
   {'nb':364,'rang':[5,4,2,3,1]}
 ]

 
def un_tour(votes):
   scores = [0,0,0,0,0] #initialise les scores des candidats a 0
   for vote in votes:
      nb= vote['nb'] #nombre de votes pour le candidat
      r= vote ['rang'] #classement des votes 
      for i in range ( len ( candidats)): 
         if r[i]==1: # si en parcourant le tableau 
            scores[i]=scores[i]+ nb
   maxi=scores[0]
   ind_gagnant = 0
   for i in range (1,len(scores)):
      if scores [i]>maxi:
         maxi=scores[i]
         ind_gagnant=i
   print("un tour-->gagnant:",candidats[ind_gagnant],"scores:",scores)
   return ind_gagnant, scores 

un_tour(vote)




def deux_tours(votes):
  scores = [0] * len(candidats)   # start scores for each candidate at 0

    # For each vote profile
    for vote in votes:
        nb = vote['nb']      # number of voters in this group
        r = vote['rang']     # their ranking

        # Find the candidate ranked 1st
        i = r.index(1)       # index = candidate number
        scores[i] += nb      # add votes to that candidate

    # Find top 2 candidates 
    premier = max(range(len(scores)), key=lambda i: scores[i])   # index of the top candidate
    # For the second: take the max among the others
    deuxieme = max(
        (i for i in range(len(scores)) if i != premier),
        key=lambda i: scores[i]
    )

    #  SECOND ROUND

    scores2 = [0] * len(candidats)   # reset scores for the final

    for vote in votes:
        nb = vote['nb']
        r = vote['rang']

        # Compare ranks of the 2 finalists: smaller rank = better
        if r[premier] < r[deuxieme]:
            scores2[premier] += nb
        else:
            scores2[deuxieme] += nb

    #  Decide winner 
    if scores2[premier] > scores2[deuxieme]:
        winner = premier
    else:
        winner = deuxieme


    # 3. RETURN RESULTS

    return {
        "scores_first_round": dict(zip(candidats, scores)),
        "first_round_top2": (candidats[premier], candidats[deuxieme]),
        "scores_second_round": {candidats[premier]: scores2[premier],
                                candidats[deuxieme]: scores2[deuxieme]},
        "winner": candidats[winner]
    }


# Run the election
result = deux_tours(vote)
print(result)



   
   


def lastman_standing():




def condorcet():
   return "candidats gagnant" 



def borda():
   return "candidats gagnant" 

