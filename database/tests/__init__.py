import unittest
from unittest.mock import patch, MagicMock
from app import save_to_database, Event, engine, Base

class TestCeleryTasks(unittest.TestCase):
    def setUp(self):
        # Set up the test database
        Base.metadata.create_all(engine)

    def tearDown(self):
        # Drop all tables after each test
        Base.metadata.drop_all(engine)

    @patch('app.logger')
    @patch('app.Session')
    def test_save_to_database_successful(self, mock_session, mock_logger):
        # Mock external dependencies
        mock_event_data = {'eventType': 'TEST_EVENT', 'payload': 'Test payload'}
        mock_event = MagicMock(**mock_event_data)
        mock_session_instance = mock_session()
        mock_session_instance.add.return_value = None
        mock_session_instance.commit.return_value = None

        # Call the task
        save_to_database(mock_event_data)

        # Check if the event instance is added to the session and committed
        mock_session_instance.add.assert_called_once_with(Event(eventType='TEST_EVENT', payload='Test payload'))
        mock_session_instance.commit.assert_called_once()

        # Check if the success message is logged
        mock_logger.info.assert_called_once_with('Event saved to the database: %s', mock_event_data)

    @patch('app.logger')
    @patch('app.Session')
    def test_save_to_database_exception(self, mock_session, mock_logger):
        # Mock external dependencies to simulate an exception during saving
        mock_event_data = {'eventType': 'TEST_EVENT', 'payload': 'Test payload'}
        mock_event = MagicMock(**mock_event_data)
        mock_session_instance = mock_session()
        mock_session_instance.add.return_value = None
        mock_session_instance.commit.side_effect = Exception('Test exception')

        # Call the task
        save_to_database(mock_event_data)

        # Check if the error message is logged
        mock_logger.error.assert_called_once_with('Error saving event to the database: %s', 'Test exception', exc_info=True)

if __name__ == '__main__':
    unittest.main()
