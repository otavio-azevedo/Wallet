import tabula
import pandas
import utility
#filePath = '.\\resources\\202402.pdf'
filePath = '.\\resources\\202403.pdf'

# Define dictionary of patterns and their corresponding categories
originCategoryDict = {
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


# Geting raw table from pdf file
tables = tabula.read_pdf(filePath, pages="all")
originalDataFrame = tables[0]

# Creating a new DataFrame for further analysis
parsedDataFrame = pandas.DataFrame({
    'Date': originalDataFrame.iloc[:, 0],
    'Origin': originalDataFrame.iloc[:, 2],
    'Debit': originalDataFrame.iloc[:, 3],
    'Credit': originalDataFrame.iloc[:, 4],
    'Balance': originalDataFrame.iloc[:, 5]
})

# Format numeric values properly
parsedDataFrame['Debit'] = utility.formatNumericColumnValues(
    parsedDataFrame['Debit'])
parsedDataFrame['Credit'] = utility.formatNumericColumnValues(
    parsedDataFrame['Credit'])
parsedDataFrame['Balance'] = utility.formatNumericColumnValues(
    parsedDataFrame['Balance'])

# print(parsedDataFrame)
# Remove rows with 0 debit
parsedDataFrame = parsedDataFrame[parsedDataFrame['Debit'] != 0]

utility.categorizeData(parsedDataFrame, originCategoryDict)

# Group data by 'Origin' and calculate total debit for each group
debitGrouped = parsedDataFrame.groupby('Category')['Debit'].sum(
).reset_index().sort_values(by='Debit', ascending=False)

# Print results
print("\nTotal values:")
print(parsedDataFrame)
print("\nTotal debit grouped by category:")
print(debitGrouped)

# Plotting the pie chart
# plotDebitPieGraph(debitGrouped)

# Plotting the bar chart with percentages
utility.plotDebitChartGraph(debitGrouped)
