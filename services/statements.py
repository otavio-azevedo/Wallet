import tabula
import constants
import utility.utility as utility
from db.statements import queries
import os


def read_and_persist_statements():
    # Directory containing the PDF files
    directory = constants.RESOURCE_DIRECTORY

    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            # Construct the full file path
            filePath = os.path.join(directory, filename)

            # Get raw table from PDF file
            tables = tabula.read_pdf(filePath, pages="2-3")
            statements_dataframe = utility.get_statements_dataframe(tables)

            # Bulk insert
            queries.bulk_insert(statements_dataframe)
