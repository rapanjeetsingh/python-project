🌍 CO2 Emissions Visualizer

A Python Streamlit application that allows users to visualize CO2 emissions for a country over time and compare the emissions of two countries.
Features

    View CO2 emissions for a selected country.

    Choose the starting year for the visualization.

    Compare the CO2 emissions of two different countries.

    Choose a different starting year for each country.

    Automatically validate country names against the dataset.

    Check whether data is available for the selected year.

    Display CO2 emissions using line graphs.

    Use a logarithmic scale to make differences between countries easier to visualize.

Preview

The application asks the user to enter a country and a starting year.

The user can then choose between:

    Viewing the emissions of one country.

    Comparing two countries.

The resulting graph displays annual CO2 emissions from the selected starting year onward.
Dataset

The application uses a CSV dataset containing annual CO2 emissions by country.

The dataset should contain the following columns:
Column	Description
entity	Name of the country or entity
year	Year of the recorded data
emissions_total	Total CO2 emissions

The CSV file should be stored in the same directory as the Python application.
Project Structure

CO2-Emissions-Visualizer/


├── app.py

├── annual-co2-emissions-per-country.csv

├── requirements.txt

└── README.md

Getting Started
1. Clone the repository

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git

Then move into the project directory:

cd CO2-Emissions-Visualizer

2. Install the dependencies

Install the packages listed in requirements.txt:

pip install -r requirements.txt

3. Run the application

Start the Streamlit application with:

streamlit run app.py

The application should open automatically in your web browser.
Using the Application
View One Country

    Enter the name of a country.

    Enter the starting year.

    Select No when asked whether you want to compare it with another country.

    The application will display a graph of the country's CO2 emissions from the selected year onward.

Compare Two Countries

    Enter the first country.

    Enter the starting year for the first country.

    Select Yes when asked whether you want to compare it with another country.

    Enter the second country.

    Enter the starting year for the second country.

    The application will display both countries on the same graph.

Data Validation

The application checks whether:

    A country name has been entered.

    The country exists in the dataset.

    Data is available for the selected year.

    Both countries are valid when using comparison mode.

If the requested country or year is not available, the application displays an appropriate error message.
Visualization

The application uses line graphs to display CO2 emissions over time.

A logarithmic y-axis is used because CO2 emissions can vary greatly between countries. This makes it easier to visualize trends for countries with significantly different emission levels.
Technologies

This project is written in Python and uses Streamlit for the user interface and data visualization libraries for the graphs.

The required Python packages are listed separately in requirements.txt.
Future Improvements

Some possible improvements include:

    Add a dropdown menu for selecting countries.

    Add interactive charts.

    Display exact emission values when hovering over data points.

    Allow users to upload their own datasets.

    Add additional CO2-related statistics.

    Improve the user interface.

    Deploy the application online.

    Add more comparison options.

Author

Created as a Python data visualization project.
