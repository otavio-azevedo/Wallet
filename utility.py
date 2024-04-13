import pandas
import matplotlib.pyplot as plt


def formatNumericColumnValues(parsedDataFrame):
    parsedDataFrame = parsedDataFrame.replace(
        ' ', '', regex=True)
    parsedDataFrame = pandas.to_numeric(
        parsedDataFrame, errors='coerce').fillna(0)
    return parsedDataFrame


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
