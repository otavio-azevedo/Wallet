from services.statements import read_and_persist_statements
import warnings

# Suppress FutureWarning from tabula
warnings.filterwarnings(
    "ignore", message="errors='ignore' is deprecated", category=FutureWarning)


read_and_persist_statements()
