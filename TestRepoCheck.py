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
import json

from unittest.mock import MagicMock as Mock
from unittest.mock import patch

from RepoCheck import check_repos

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestRepoCheck(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    @patch('requests.get')
    def testOctocat(self, injectedMock): 
        results = [Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock(), Mock()]
        results[0].json.return_value = json.loads('[{"name": "boysenberry-repo-1"}, {"name": "git-consortium"}, {"name": "hello-worId"}, {"name": "Hello-World"}, {"name": "linguist"}, {"name": "octocat.github.io"}, {"name": "Spoon-Knife"}, {"name": "test-repo1"}]')
        results[1].json.return_value = json.loads('[{"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}]')
        results[2].json.return_value = json.loads('[{"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}]')
        results[3].json.return_value = json.loads('[{"commit": "a"}]')
        results[4].json.return_value = json.loads('[{"commit": "a"}, {"commit": "a"}, {"commit": "a"}]')
        results[5].json.return_value = json.loads('[{"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}]')
        results[6].json.return_value = json.loads('[{"commit": "a"}, {"commit": "a"}, {"commit": "a"}, {"commit": "a"}]')
        results[7].json.return_value = json.loads('[{"commit": "a"}, {"commit": "a"}, {"commit": "a"}]')
        results[8].json.return_value = json.loads('[{"commit": "a"}]')
        results[0].status_code = 200
        results[1].status_code = 200
        results[2].status_code = 200
        results[3].status_code = 200
        results[4].status_code = 200
        results[5].status_code = 200
        results[6].status_code = 200
        results[7].status_code = 200
        results[8].status_code = 200
        injectedMock.side_effect = results
        self.assertEqual(check_repos('octocat'), {'boysenberry-repo-1': 4, 'git-consortium': 6, 'hello-worId': 1, 'Hello-World': 3, 'linguist': 30, 'octocat.github.io': 4, 'Spoon-Knife': 3, 'test-repo1': 1}, '\'octocat\' should return a full list of repos.')

    @patch('requests.get')
    def testJunk(self, injectedMock): 
        injectedMock.return_value.status_code = 404
        self.assertEqual(check_repos('{{*JUNK*}}'), {'User query {{*JUNK*}} failed; code 404': -1}, '\'{{*JUNK*}}\' should fail to connect with code 404.')
    
    @patch('requests.get')
    def testBlank(self, injectedMock): 
        injectedMock.return_value.status_code = 404
        self.assertEqual(check_repos(''), {'User query  failed; code 404': -1}, '<Blank> should fail to connect with code 404.')
    
    def testTwo(self): 
        self.assertEqual(check_repos(2), {'Input is not a string': -1}, '2 is not a valid input.')
    
    def testDict(self): 
        self.assertEqual(check_repos({'Apple': 1}), {'Input is not a string': -1}, '{\'Apple\': 1} is not a valid input.')
    
    @patch('requests.get')
    def testEmpty(self, injectedMock):
        injectedMock.return_value.json.return_value = json.loads('{}')
        injectedMock.return_value.status_code = 200
        self.assertEqual(check_repos('Jordan884'), {}, '\'Jordan884\' should return an empty dictionary.')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()