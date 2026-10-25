# CO₂ Emissions Visualizer

An interactive Python application that allows users to explore historical CO₂ emissions data and compare countries using graphs and percentage differences. The application also includes GDP, population, land area, and CO₂ emissions per capita.

## Features

- **Country-level analysis:** Select a country and starting year to explore its historical data.
- **Country comparisons:** Plot two countries on the same graph to compare their trends over time.
- **Percentage comparisons:** Calculate the percentage difference between two countries using a year for which both have data.
- **Multiple indicators:** Explore total CO₂ emissions, CO₂ emissions per capita, GDP, land area, and population.
- **Interactive visualisations:** Choose which indicators to display through the Streamlit interface.
- **Historical trend analysis:** Examine changes in country-level indicators across available years.
- **Logarithmic scaling:** Display positive CO₂ emission values on a logarithmic scale where appropriate.
- **Data cleaning:** Handle missing values and convert data into appropriate numerical formats.
- **Caching:** Use Streamlit caching to reduce repeated data loading.

## Technologies Used

- **Python** - Main programming language.
- **Streamlit** - Interactive web application.
- **Pandas** - Data cleaning and processing.
- **Matplotlib** - Graph creation and customisation.
- **Seaborn** - Data visualisation and styling.
- **NumPy** - Numerical operations.

## Data Sources

The datasets used in this project are sourced from [Our World in Data](https://ourworldindata.org/).

The application uses CSV files containing:

- Annual CO₂ emissions.
- CO₂ emissions per capita.
- GDP.
- Land area.
- Population.

## Installation and Setup

### Requirements

- Python 3
- pip
- Git (optional)

### 1. Clone the Repository

Open a terminal and run:

```bash
git clone https://github.com/rapanjeetsingh/python-project.git
cd python-project
## Installation and Setup

## Requirements
- Python 3
- pip
- Git (optional)

## 1. Clone the Repository

Open a terminal and run:
 
```bash
git clone https://github.com/rapanjeetsingh/python-project.git
cd python-project
```

Alternatively, download the repository as a ZIP file from GitHub and extract it.

## 2. Install Dependencies

Install the required Python libraries:

```bash
pip install -r requirements.txt
```

## 3. Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

## 4. Open the Application

Streamlit will display a local URL in the terminal, usually http://localhost:8501. Open this URL in your web browser to use the application.

> 💡 **Note:** Make sure all required CSV datasets are in the location expected by the application before running it.

What I Learned

Developing this project gave me practical experience in:

    Breaking a larger programming task into reusable functions.
    Processing real-world datasets with Pandas.
    Building interactive applications with Streamlit.
    Using data visualisation to communicate patterns and comparisons.
    Handling missing values and differences in data availability.
    Calculating percentage differences and interpreting numerical results.
    Improving graph readability through formatting and scale selection.

The project also helped me understand the importance of data quality and context when comparing countries. A graph can make patterns easier to identify, but the conclusions drawn from it depend on the quality, coverage, and meaning of the underlying data.
Future Development

Potential areas for further development include:

    Adding more environmental and economic indicators.
    Providing more detailed information about individual datasets and their units.
    Improving options for comparing countries over the same time period.
    Exploring relationships between emissions, population, and economic growth.
Rapanjeet Singh




