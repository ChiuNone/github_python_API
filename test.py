import unittest

from test_python_repos_3 import get_status_code

class StatusCodeTestCase(unittest.TestCase):

    def test_first_url(self):
        url_1 = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        formatted_status_code = get_status_code(url_1)
        self.assertEqual(formatted_status_code, 200)

unittest.main()

