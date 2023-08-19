import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Replace '/Users/rajshekharsingh/Downloads/GME_stock.csv' with the actual path to your CSV file
csv_file_path = '/Users/rajshekharsingh/Downloads/TSLA.csv'

# Read the CSV file into a DataFrame
tsl_data = pd.read_csv(csv_file_path)

# Reset the index
tsl_data.reset_index(drop=True, inplace=True)

# Save the DataFrame to a CSV file
tsl_data.to_csv('gme_data.csv', index=False)

# Display the first five rows of the gme_data DataFrame
print("First five rows of GME stock data:")
print(tsl_data.head())
print("Last five rows of GME stock data:")
print(tsl_data.tail())

# Ticker symbols for AMD and Tesla
amd_stock_symbol = "AMD"
tesla_stock_symbol = "TSLA"

# Get stock data using yfinance
amd_stock = yf.Ticker(amd_stock_symbol)
tesla_stock = yf.Ticker(tesla_stock_symbol)

# Get historical data for AMD and Tesla stocks
amd_stock_data = amd_stock.history(period="max")
tesla_stock_data = tesla_stock.history(period="max")

# Reset the index of the DataFrames
amd_stock_data.reset_index(inplace=True)
tesla_stock_data.reset_index(inplace=True)

# Obtain the volume traded on the first day for AMD and Tesla
first_day_volume_amd = amd_stock_data.loc[0, 'Volume']
first_day_volume_tesla = tesla_stock_data.loc[0, 'Volume']

print("Volume traded on the first day for AMD:", first_day_volume_amd)
print("Volume traded on the first day for Tesla:", first_day_volume_tesla)

# Display the first five rows of the AMD stock data
print("First five rows of AMD stock data:")
print(amd_stock_data.head())

# Display the last five rows of the tesla_stock_data DataFrame
print("Last five rows of Tesla stock data:")
print(tesla_stock_data.tail())
def make_graph(dataframe, title, date_column, price_column):
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe[date_column], dataframe[price_column], label='Closing Price')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title(title)
    plt.legend()
    plt.grid()
    plt.show()

# Provide a title for the graph
graph_title = "Tesla Stock Data"

# Specify the column names for date and price in your DataFrame
date_column_name = 'Date'
price_column_name = 'Close'

# Call the make_graph function to create the graph
make_graph(tsl_data, graph_title, date_column_name, price_column_name)