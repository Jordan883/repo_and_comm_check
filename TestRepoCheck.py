# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk

@author: Jordan Fernandes
I pledge my honor that I have abided by the Stevens Honor System. - Jordan Fernandes
"""

import unittest

from RepoCheck import check_repos

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestRepoCheck(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin
    def testOctocat(self): 
        self.assertEqual(check_repos('octocat'), {'boysenberry-repo-1': 4, 'git-consortium': 6, 'hello-worId': 1, 'Hello-World': 3, 'linguist': 30, 'octocat.github.io': 4, 'Spoon-Knife': 3, 'test-repo1': 1}, '\'octocat\' should return a full list of repos.')

    def testJunk(self): 
        self.assertEqual(check_repos('{{*JUNK*}}'), {'User query {{*JUNK*}} failed; code 404': -1}, '\'{{*JUNK*}}\' should fail to connect with code 404.')
    
    def testBlank(self): 
        self.assertEqual(check_repos(''), {'User query  failed; code 404': -1}, '<Blank> should fail to connect with code 404.')
    
    def testTwo(self): 
        self.assertEqual(check_repos(2), {'Input is not a string': -1}, '2 is not a valid input.')
    
    def testDict(self): 
        self.assertEqual(check_repos({'Apple': 1}), {'Input is not a string': -1}, '{\'Apple\': 1} is not a valid input.')
    
    def testEmpty(self):
        self.assertEqual(check_repos('Jordan884'), {}, '\'Jordan884\' should return an empty dictionary.')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()