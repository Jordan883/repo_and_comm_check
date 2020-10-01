'''
@author: Jordan Fernandes
I pledge my honor that I have abided by the Stevens Honor System. - Jordan Fernandes

This file contains a function that takes in a GitHub user ID and outputs a dictionary containing 
that user's public repos and the number of commits made to each. 
'''

# Imports. Note: I did not need to use the json module in my implementation. 
try:
    import requests
except:
    print("requests import failed")

def check_repos(userid):
    ''' Takes in a GitHub User ID as a string, then returns a dictionary containing the name 
    of each public repo that the user has and their numbers of commits. If an error occurs, this 
    function will return an "error dictionary". This dictionary has one entry: an error message key 
    with a value of -1. 

    Input: A GitHub User ID, as a string. 
    Output: A dictionary containing the name of each public repo that the user has and their 
    numbers of commits. This dictionary is of the form {"name1": commit #, "name2": commit #}. 
    Alternatively, an error dictionary returns with an error message key and a value of -1. 
    '''
    output = {}

    if not isinstance(userid, str):
        return {'Input is not a string': -1}

    repo_r = requests.get('https://api.github.com/users/' + userid + '/repos')
    if repo_r.status_code != 200:
        return {'User query ' + userid + ' failed; code ' + str(repo_r.status_code): -1}
    
    repos = repo_r.json()

    for repo in repos:
        repo_name = repo['name']
        comm_r = requests.get('https://api.github.com/repos/' + userid + '/' + repo_name + '/commits')
        if comm_r.status_code != 200:
            return {'Repo query ' + repo_name + ' failed; code ' + str(comm_r.status_code): -1}
        commits = comm_r.json()
        num_commits = len(commits)
        output[repo_name] = num_commits
    
    return output
