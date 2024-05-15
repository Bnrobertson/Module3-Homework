# Mars Data Scraping and Analysis

This project involves scraping data from Mars-related websites, analyzing the data using Python libraries, and visualizing the results. The project focuses on two main tasks:

1. Scraping Mars news articles.
2. Scraping and analyzing Mars temperature data.

# Project Overview

### Mars News Scraping
- Use Splinter to automate browsing and BeautifulSoup to extract news titles and previews from a Mars news site.
- Store the extracted data in a list of dictionaries.
### Mars Temperature Data Scraping and Analysis
- Scrape Mars temperature data from a table on a specific website.
- Store the data in a Pandas DataFrame.
- Perform data analysis to find insights such as the number of Martian months, the coldest and warmest months, and atmospheric pressure trends.
- Visualize the data using Matplotlib.
- Setup and Installation

#### Prerequisites
- Python 3.x
- Jupyter Notebook
- Libraries: 'splinter', 'beautifulsoup4', 'matplotlib', 'pandas'
#### Installation
1. Clone the repository:
git clone https://github.com/Bnrobertson/python_challenge.git
~ cd python_challenge
2. Install the required libraries:
pip install splinter, beautifulsoup4, matplotlib, pandas

# Mars News Scraping

### Step 1: Visit the Website
Automate browsing to visit the Mars news site and inspect the page to identify elements to scrape.

### Step 2: Scrape the Website
Create a BeautifulSoup object and use it to extract text elements from the website.

### Step 3: Store the Results
Extract the titles and preview text, store them in a list of dictionaries, and print the results.

# Mars Temperature Data Scraping and Analysis

### Step 1: Visit the Website
Automate browsing to visit the Mars Temperature Data Site and inspect the page to identify elements to scrape.
### Step 2: Scrape the Table
Create a BeautifulSoup object and scrape data from the HTML table.
### Step 3: Store the Data
Assemble the scraped data into a Pandas DataFrame and convert data types as needed.

# Data Analysis and Visualization

### Step 4: Analyze the Data
Analyze the dataset to answer specific questions.

# Saving the Data

### Step 6: Save the Data
Export the cleaned DataFrame to a CSV file.
