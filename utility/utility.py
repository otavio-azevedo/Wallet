import datetime
import pandas
import matplotlib.pyplot as plt


def format_numeric_column_values(parsedDataFrame):
    parsedDataFrame = parsedDataFrame.replace(
        ' ', '', regex=True)
    parsedDataFrame = pandas.to_numeric(
        parsedDataFrame, errors='coerce').fillna(0)
    return parsedDataFrame


def formatDateValues(row):
    # Convert the float value to a string and remove any trailing decimal zeros
    row_str = str(row)

    # Parse day and month from the input string
    month, day = map(int, row_str.split("."))

    # Get the current year
    current_year = datetime.date.today().year

    # Combine day, month, and current year to form a complete date
    return datetime.date(current_year, month, day)


def categorizeData(parsedDataFrame, originCategoryDict):
    # Create a new column 'Category' filled based on the origin and the mapping dictionary
    # Initialize 'Category' column with default value 'Other'
    # Iterate over each pattern and corresponding category
    parsedDataFrame['Category'] = 'Other'
    for pattern, category in originCategoryDict.items():
        # Use regular expression to search for pattern in 'Origin' column
        mask = parsedDataFrame['Origin'].str.contains(
            pattern, case=False, regex=True)
        # Assign the corresponding category to rows matching the pattern
        parsedDataFrame.loc[mask, 'Category'] = category


def plotDebitPieGraph(debitGrouped):
    plt.figure(figsize=(6, 6))
    plt.pie(debitGrouped['Debit'], labels=debitGrouped['Category'],
            autopct='%1.1f%%', startangle=140)
    # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.axis('equal')
    plt.title('Distribution of Total Debit by Category', fontsize=16,
              fontweight='bold', color='red', loc='center', pad=20)
    plt.show()


def plotDebitChartGraph(debitGrouped):
    debitGrouped['Percentage'] = (
        debitGrouped['Debit'] / debitGrouped['Debit'].sum()) * 100

    plt.figure(figsize=(10, 6))
    plt.bar(debitGrouped['Category'],
            debitGrouped['Percentage'], color='skyblue')
    plt.xlabel('Category', fontsize=12)
    plt.ylabel('Percentage of Total Debit (%)', fontsize=12)
    plt.title('Percentage of Total Debit by Category',
              fontsize=14, fontweight='bold')
    plt.xticks(rotation=45, ha='right')
    plt.grid(axis='y', linestyle='--', alpha=0.7)  # Add horizontal grid lines
    plt.tight_layout()  # Adjust layout to prevent overlapping labels
    plt.show()


def get_statements_dataframe(tables):
    parsed_tables = []

    for table in tables:
        # Creating a new DataFrame for further analysis
        parsed_df = pandas.DataFrame({
            'transaction_date': table.iloc[:, 0],
            'origin': table.iloc[:, 2],
            'debit': table.iloc[:, 3],
            'credit': table.iloc[:, 4],
            'balance': table.iloc[:, 5]
        })

    # Appending the parsed DataFrame to the list
        parsed_tables.append(parsed_df)

# Concatenate all parsed DataFrames into a single DataFrame
    statements_dataframe = pandas.concat(parsed_tables, ignore_index=True)

    statements_dataframe['transaction_date'] = statements_dataframe['transaction_date'].apply(
        formatDateValues)

# Format numeric values properly
    statements_dataframe['debit'] = format_numeric_column_values(
        statements_dataframe['debit'])
    statements_dataframe['credit'] = format_numeric_column_values(
        statements_dataframe['credit'])
    statements_dataframe['balance'] = format_numeric_column_values(
        statements_dataframe['balance'])

    return statements_dataframe


# Define dictionary of patterns and their corresponding categories
origin_category_dict = {
    r'(Maria Joana)': 'Rent',
    r'(EDP)': 'Energy',
    r'(INDAQUA)': 'Water',
    r'(VODAFONE)': 'Internet',
    r'(MEDICARE)': 'Health Insurance',
    r'(PAG-ESTADO | Luis)': 'Taxes',
    r'(CONTINENTE|LIDL|PINGO DOCE|FARMACIA|PAD PORT|WELL)': 'Grocery',
    r'(BOLT|UBER|TIP PORTO)': 'Transport',
    r'(ARCADIA|CACHORRA|GLOVO|PIZZA|GELATARIA|SANTIAGA|NATA|PANS|ACAI)': 'Restaurant',
    r'(E-FIT)': 'Gym',
    r'(PRIMARK|ZARA)': 'Shopping',
}

# Remove rows with 0 debit
#concatenated_dataframe = concatenated_dataframe[concatenated_dataframe['debit'] != 0]
#concatenated_dataframe.reset_index(drop=True, inplace=True)

# utility.categorizeData(concatenated_dataframe, originCategoryDict)

# # Group data by 'origin' and calculate total debit for each group
# debitGrouped = concatenated_dataframe.groupby('Category')['debit'].sum(
# ).reset_index().sort_values(by='debit', ascending=False)

# Print results
#print("\nTotal values:")
# print(statements_dataframe)
# print("\nTotal debit grouped by category:")
# print(debitGrouped)

# Plotting the pie chart
# plotdebitPieGraph(debitGrouped)

# Plotting the bar chart with percentages
# utility.plotdebitChartGraph(debitGrouped)
