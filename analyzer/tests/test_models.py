import unittest
from app.models import Analytics 

class TestAnalytics(unittest.TestCase):
    def setUp(self):
        # Create a sample instance for testing
        self.analytics_instance = Analytics(
            name="John Doe",
            leaderboardPosition=1,
            language_scores={"python": 90, "javascript": 80},
            topLanguage="python"
        )

    def test_to_dict(self):
        expected_dict = {
            'name': "John Doe",
            'leaderboardPosition': 1,
            'language_scores': {"python": 90, "javascript": 80},
            'topLanguage': "python"
        }

        # Call the to_dict method and compare the result with the expected dictionary
        result_dict = self.analytics_instance.to_dict()
        self.assertDictEqual(result_dict, expected_dict)

    def test_to_dict_empty_instance(self):
        # Test with an instance where all attributes are None or empty
        empty_instance = Analytics(name=None, leaderboardPosition=None, language_scores={}, topLanguage=None)
        expected_dict = {
            'name': None,
            'leaderboardPosition': None,
            'language_scores': {},
            'topLanguage': None
        }

        result_dict = empty_instance.to_dict()
        self.assertDictEqual(result_dict, expected_dict)

if __name__ == '__main__':
    unittest.main()
