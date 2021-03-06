from django.core.management.base import BaseCommand
from ...logs import logging_for_management_command
from ... import exportimport


class Command(BaseCommand):
    help = "Export database records for a collection"

    def add_arguments(self, parser):
        parser.add_argument('collection_name', type=str, help="Unique collection name.")

    def handle(self, collection_name, *args, **options):
        logging_for_management_command(options['verbosity'])
        exportimport.export_db(collection_name)
