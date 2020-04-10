import re
import actions as ac

def search(querry,list):
    regex = '(^.*' + re.escape(querry) + '.*$)'
    matches=[]
    for element in list:
        z=re.match(regex, element, re.IGNORECASE)
        if z:
            matches.append(z.groups()[0])
    if len(matches)>0:
        return matches
    if len(matches)==0:
        failure_statement="no contacts" #return won't print on shell if given variable
        return failure_statement
