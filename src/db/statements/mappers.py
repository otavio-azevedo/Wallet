
def map_statements(row):
    operation = 'credit' if row['debit'] == 0 else 'debit'
    amount = row['credit'] if row['credit'] != 0 else row['debit']

    return (
        row['transaction_date'],
        row['origin'],
        operation,
        amount,
        row['balance']
    )
