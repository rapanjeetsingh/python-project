🌍 CO₂ Emissions Visualizer

An interactive Python application for exploring and comparing CO₂ emissions and other country-level indicators over time.

Launch the Application | View Source Code

About the Project

I developed this project to explore how programming and data visualisation can make environmental data easier to understand and analyse.

The application allows users to explore historical CO₂ emissions data for individual countries and compare two countries using interactive graphs. It also includes other indicators, such as GDP, population, land area, and CO₂ emissions per capita, to provide a broader view of differences between countries.

By combining data processing with an interactive interface, I wanted to create a tool that allows users to investigate the data themselves rather than simply view predefined results.

Features
Country-level analysis: Select a country and starting year to explore its historical data.
Country comparisons: Plot two countries on the same graph to compare their trends over time.
Percentage comparisons: Calculate the percentage difference between two countries using a year for which both have data.
Multiple indicators: Explore total CO₂ emissions, CO₂ emissions per capita, GDP, land area, and population.
Interactive visualisations: Select which indicators to display using Streamlit controls.
Historical trend analysis: Examine changes in country-level indicators across available years.
Logarithmic scaling: Display positive CO₂ emission values on a logarithmic scale where appropriate.
Data cleaning: Handle missing values, convert data into appropriate numerical formats, and organise datasets for plotting.
Caching: Use Streamlit caching to reduce repeated data loading.
Technologies Used
Technology	Purpose
Python	Main programming language
Streamlit	Interactive web application and user controls
Pandas	Loading, cleaning, merging, and processing data
Matplotlib	Creating and customising graphs
Seaborn	Styling data visualisations
NumPy	Numerical operations and validation
Data Sources

The datasets used in this project come from Our World in Data, which publishes research and data on global issues, including climate change, energy, population, and economic development.

The application uses the following CSV files:

Indicator	Dataset file
Annual CO₂ emissions	annual-co2-emissions-per-country.csv
CO₂ emissions per capita	co-emissions-per-capita.csv
GDP	gdp-worldbank-constant-usd.csv
Land area	land-area-km.csv
Population	population-with-un-projections.csv

Original data portal: Our World in Data.

The datasets may cover different years and use different units. Comparisons should therefore be interpreted in the context of each indicator's definition and data availability.

Getting Started
Requirements
Python 3
pip
Git (optional)
1. Clone the repository
bash
git clone https://github.com/rapanjeetsingh/python-project.git
cd python-project


Alternatively, download the repository as a ZIP file from GitHub and extract it.

2. Install dependencies

Install the required Python libraries:

bash
pip install -r requirements.txt

3. Run the application

Start the Streamlit application:

bash
streamlit run app.py


Open the local URL displayed in the terminal to use the application in your browser.

Make sure the CSV datasets are available in the location expected by the application.

How to Use
Select the first country you want to investigate.
Choose the starting year for its data.
Decide whether to compare it with another country.
If comparing, select the second country and its starting year.
Choose one or more indicators to display.
Examine the graphs to explore historical trends and differences.
Review the percentage comparison for the latest year available to both countries.
What I Learned

Developing this project gave me practical experience in:

Breaking a larger programming task into reusable functions.
Processing real-world datasets with Pandas.
Building interactive applications with Streamlit.
Using data visualisation to communicate patterns and comparisons.
Handling missing values and differences in data availability.
Calculating percentage differences and interpreting numerical results.
Improving graph readability through formatting and scale selection.

The project also helped me understand the importance of data quality and context when comparing countries. A graph can make patterns easier to see, but the conclusions drawn from it depend on the quality, coverage, and meaning of the underlying data.

Future Development

Potential areas for further development include:

Adding more environmental and economic indicators.
Providing more detailed information about individual datasets and their units.
Improving options for comparing countries over the same time period.
Exploring relationships between emissions, population, and economic growth.
Live Application

Try the deployed application:

CO₂ Emissions Visualizer

The hosted application may take a short time to load if the hosting service has temporarily put it to sleep.

Author

Rapanjeet Singh

Built as a personal Python project exploring data analysis, programming, and environmental data visualisation.

GitHub Repository
