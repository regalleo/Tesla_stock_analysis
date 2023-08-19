# Tesla Stock Data Analysis

This repository contains a Python script for analyzing and visualizing Tesla stock data using the yfinance library and pandas.

## Table of Contents

- [Introduction](#introduction)
- [Requirements](#requirements)
- [Usage](#usage)
- [Results](#results)
- [Graph](#graph)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This script utilizes the yfinance library to fetch historical stock data for Tesla (TSLA) from Yahoo Finance. The data is then analyzed and visualized using pandas and matplotlib.

## Requirements

- Python (>=3.6)
- yfinance library
- pandas library
- matplotlib library

Install the required libraries using the following command:
*pip install yfinance pandas matplotlib

## usage

Clone this repository to your local machine.
Replace the csv_file_path variable with the actual path to your Tesla stock data CSV file.
Run the script using Python:
python analyze_tesla_stock.py

## Results

The script performs the following tasks:

Reads Tesla stock data from the provided CSV file.
Resets the index of the DataFrame for consistency.
Saves the DataFrame to a new CSV file named 'gme_data.csv'.
Displays the first and last five rows of the Tesla stock data.

## Graph

The script also generates a graph showing the closing prices of Tesla stock over time. The graph is saved as a PNG image in the repository.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
