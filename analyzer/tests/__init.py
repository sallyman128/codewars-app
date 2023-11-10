import unittest
from unittest.mock import patch, MagicMock
from app import app, publishEvent, fetch_data_from_codewars, Analytics

class TestFlaskApp(unittest.TestCase):
    def setUp(self):
        app.testing = True
        self.app = app.test_client()

    @patch('app.publishEvent.apply_async')
    @patch('app.fetch_data_from_codewars')
    def test_fetch_codewars_valid_username(self, mock_fetch_data, mock_apply_async):
        # Mock external dependencies
        mock_fetch_data.return_value = {
            'name': 'Salmaan Ali',
            'leaderboardPosition': 1,
            'ranks': {'languages': {'ruby': 48, 'javascript': 83, 'python': 25, 'java': 71, 'groovy': 6}}
        }

        # Make a request to the /fetchcodewars endpoint
        response = self.app.get('/fetchcodewars?username=sallyman128')

        # Check if the response is successful (status code 200)
        self.assertEqual(response.status_code, 200)

        # Check if the expected Analytics instance is created
        expected_analytics = Analytics(
            name='Salmaan Ali',
            leaderboardPosition=1,
            language_scores={'ruby': 48, 'javascript': 83, 'python': 25, 'java': 71, 'groovy': 6},
            topLanguage='javascript'
        )
        mock_apply_async.assert_called_with(args=[{'eventType': 'RESPONSE_SENT', 'payload': expected_analytics.to_dict()}])

    @patch('app.publishEvent.apply_async')
    @patch('app.fetch_data_from_codewars')
    def test_fetch_codewars_invalid_username(self, mock_fetch_data, mock_apply_async):
        # Mock external dependencies
        mock_fetch_data.return_value = None

        # Make a request to the /fetchcodewars endpoint with an invalid username
        response = self.app.get('/fetchcodewars?username=invaliduser')

        # Check if the response indicates an invalid username (status code 400)
        self.assertEqual(response.status_code, 400)

        # Check if the expected event for an invalid username is produced
        expected_event = {'eventType': 'INVALID_USERNAME', 'payload': None}
        mock_apply_async.assert_called_with(args=[expected_event])

if __name__ == '__main__':
    unittest.main()
