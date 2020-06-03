# Create your tests here.
import unittest

from requests import get


class TestAPI(unittest.TestCase):
    def test_top_post(self):
        """
        Test that get the top 10 posts order by comments count
        """
        result = get("http://127.0.0.1:8000/api/toppost").json()

        self.assertEqual(result['posts'][0]['total_number_of_comments'], 5)

    def test_search_comments(self):
        """
        Test search comments
        """
        field, value = 'id', 6
        result = get("http://127.0.0.1:8000/api/comments?field={}&value={}".format(field, value)).json()

        self.assertNotEqual(result['comments'][0]['postId'], 6)


if __name__ == '__main__':
    unittest.main()
