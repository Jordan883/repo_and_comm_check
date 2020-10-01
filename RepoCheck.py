'''
@author: Jordan Fernandes
I pledge my honor that I have abided by the Stevens Honor System. - Jordan Fernandes

This file contains a function that takes in a GitHub user ID and outputs the public repos
from that ID. The number of commits that the user has made to each repo is also listed. This 
output is structured as a dictionary. 
'''

# Imports
try:
    import requests
except:
    print("requests import failed")

def check_repos(userid):
    ''' Takes in a GitHub User ID as a string, then returns a dictionary containing the name 
    of each public repo that the user has and their numbers of commits. If an error occurs, this 
    function will return an "error dictionary". This dictionary has one key of an error message and 
    a value of zero. 

    Input: A GitHub User ID, as a string. 
    Output: A dictionary containing the name of each public repo that the user has and their 
    numbers of commits. This dictionary is of the form {"name1": commit #, "name2": commit #}. 
    '''
    output = {}

    user_r = requests.get('https://api.github.com/users/' + str(userid) + '/repos')
    if user_r.status_code != 200:
        return {'User query ' + userid + ' failed; code ' + str(user_r.status_code): -1}
    
    user_jsons = user_r.json()

    for user_json in user_jsons:
        repo_name = user_json['name']
        repo_r = requests.get('https://api.github.com/repos/' + userid + '/' + repo_name + '/commits')
        if repo_r.status_code != 200:
            return {'Repo query ' + repo_name + ' failed; code ' + str(repo_r.status_code): -1}
        repo_jsons = repo_r.json()
        num_commits = len(repo_jsons)
        output[repo_name] = num_commits
    
    return output
