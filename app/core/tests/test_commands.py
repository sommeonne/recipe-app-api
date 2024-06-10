from unittest.mock import patch
from psycopg2 import OperationalError as psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


class CommandsTestCase(SimpleTestCase):
    def test_wait_for_db_ready(self):
       pass
