# python-project
CO2 Emissions Visualizer 

A simple Streamlit web application for visualizing and comparing CO2 emissions by country over time.

The application allows you to:

View the CO2 emissions of a single country starting from a selected year.

Compare the CO2 emissions of two countries.

Enter different starting years for each country.

Visualize the data using interactive charts generated with Seaborn and Matplotlib.

Validate countries and years against the available dataset.

Technologies Used

Python

Streamlit — for the web application

Pandas — for loading and processing the data

Seaborn — for data visualization

Matplotlib — for creating the charts

Dataset

The application uses a CSV dataset containing annual CO2 emissions by country.

The dataset is expected to contain at least these columns:

entity — Country/entity name

year — Year of the measurement

emissions_total — Total CO2 emissions

Installation

Clone this repository:

git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd YOUR-REPOSITORY


Install the required Python packages:

pip install streamlit pandas seaborn matplotlib

Dataset Setup

The current version of the program uses a local file path:

C:\\Users\\rapan\\Downloads\\annual-co2-emissions-per-country.csv


This path will only work on the computer where the file exists.

For other users, download the dataset and either place it in the project folder or update the path in the Python file.

A better approach is to use a relative path, for example:

CO2 = pd.read_csv("annual-co2-emissions-per-country.csv")


Then place the CSV file in the same directory as the Python program.

Running the Application

Run the following command from the project directory:

streamlit run app.py


Replace app.py with the name of your Python file if it is different.

Streamlit will open the application in your web browser.

How to Use
Single Country

Enter a country name.

Enter the starting year.

Select No when asked whether you want to compare it with another country.

The application will display a graph showing CO2 emissions from the selected year onward.

Comparing Two Countries

Enter the first country.

Enter its starting year.

Select Yes when asked whether you want to compare it with another country.

Enter the second country.

Enter its starting year.

The application will display both countries on the same graph.

The graphs use a logarithmic scale for CO2 emissions, which makes it easier to visualize countries with significantly different emission levels.

Input Validation

The application checks whether:

A country was entered.

The country exists in the dataset.

Data is available for the selected year.

Both countries are valid when using comparison mode.

If invalid information is entered, an error or warning message is displayed.

Project Structure
project-folder/
│
├── app.py
├── annual-co2-emissions-per-country.csv
└── README.md

Future Improvements

Possible improvements include:

Add dropdown menus for selecting countries.

Add more visualization options.

Display the exact emission values when hovering over data points.

Improve the user interface.

Allow users to upload their own dataset.

Deploy the application online using Streamlit Community Cloud.

Remove the dependency on a hard-coded local file path.

Author

Created as a Python data visualization project using Streamlit, Pandas, Seaborn, and Matplotlib.
