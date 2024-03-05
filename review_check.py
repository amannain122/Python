reviews= ["very purple and good", "very extremely bad and one of the worst", "terrible but exceptional",""] 

def review_score(review):
    positive=["good","nice","excellent","exceptional","great","well"]   
    negative=["bad","worse","worst","terrible"]
    intensifiers=["very","extremely"]
    result=[]
    try:
        for i in review:
            score=0
            intens_score=0
            for j in i.split(" "):
                if j in positive:
                    score=score+intens_score+1
                    intens_score=0
                elif j in intensifiers:
                    intens_score+=1
                elif j in negative:
                    score+=score-intens_score-1
                    intens_score=0
            print(score)
            if score>0:
                result.append("positive")
            elif score<0:
                result.append("negative")
            else:
                result.append("neutral")
    except Exception:
        pass
    return result

answer=review_score(reviews)

    
                
            