\connect wallet;

-- Define an enum type for the operation column
CREATE TYPE operation_type AS ENUM ('debit', 'credit');

-- Create the statement_history table with the operation column using the enum type
CREATE TABLE statement_history (
    id SERIAL PRIMARY KEY,
    transaction_date DATE NOT NULL,
    origin VARCHAR(100),
    operation operation_type NOT NULL,
    amount NUMERIC NOT NULL,
    balance NUMERIC
);