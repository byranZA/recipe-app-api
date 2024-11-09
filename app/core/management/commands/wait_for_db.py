"""
Django command to wiat for DB to be available
"""
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.core.management.base import BaseCommand
from django.db.utils import OperationalError


class Command(BaseCommand):
    """
    Django command to wait for DB
    """

    def handle(self, *args, **options):
        """
        Entry point for command
        """
        self.stdout.write('Waiting for database...')
        db_up = False
        while not db_up:
            try:
                self.check(databases=['default'])
                db_up = True
            except (Psycopg2Error, OperationalError):
                msg = 'Database not available, waiting 1 second...'
                self.stdout.write(msg)
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('Database available'))
