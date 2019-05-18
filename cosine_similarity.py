# The function cosine similarity takes two arguments (a,b) where a and b either a single word or word phrases(Collection of words).

def cosine(a,b):
    
    #creating a set of words from the word phrase
    set1=set(a.split())
    set2=set(b.split())
    
    # Finding the dissimilar words in both the sets
    diff_LR=list(set1-set2)
    diff_RL=list(set2-set1)
    
    # Calculating Similarity Score
    similar_score=(len(set1)-len(diff_LR))/len(set1)
    return(similar_score)
