import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import numpy as np

#caches the data by formatting it in a dictionary, so it won't have to load it every time
@st.cache_data
def load_data():
    #gives a readable name to each of the file
    files = {
        "CO2 emission": "annual-co2-emissions-per-country.csv",
        "CO2 per Capita": "co-emissions-per-capita.csv",
        "GDP": "gdp-worldbank-constant-usd.csv",
        "land area": "land-area-km.csv",
        "population": "population-with-un-projections.csv"
    }

    #creates a empty dictionary which contains the name of the data to pull from when plotting
    datasets = {}

    #loops over the dictionary and loads the data
    for name, filename in files.items():
        data = pd.read_csv(filename)
        data.columns = data.columns.str.strip()

        #renames the columns to make it easier to write code for and to make it consistent
        data = data.rename(columns={
            "country": "entity",
            "Country": "entity",
            "Entity": "entity",
            "Code": "code",
            "year": "year",
            "Year": "year"
        })

        #converts the string value in year to integers
        data["year"] = pd.to_numeric(
            data["year"], errors="coerce"
        )

        #removes teh rows where entity(entity was used as name of country because this is what the csv file used) or year is missing
        data = data.dropna(subset=["entity", "year"])

        #converts the year into integers because it was displaying years as float point numbers
        data["year"] = data["year"].astype(int)

        #this puts the cleaned dataframe in the directory under its name, ex: puts the data for CO2 emission in its csv file name as the key
        datasets[name] = data

    return datasets

#data_list contains all 5 variables
data_list = load_data()

#this connects the name of the columns with the name displayed to the user
VALUE_COLUMNS = {
    "CO2 emission": "emissions_total",
    "CO2 per Capita": "CO2 emissions per capita",
    "GDP": "GDP",
    "land area": "Land area (sq. km)",
    "population": "Population"
}

#makes the program heading
def program_heading():
    st.title(
        "This is an app to see CO2 emission of a country "
        "or compare between 2 countries"
    )
    st.divider()

#function to take the input of the countries
def country_input_taker(data, key):
    #sorts the name of the entities in the data and takes only the unique names
    country_list = sorted(
        data["entity"].dropna().unique().tolist()
    )

    #returns none if the list is empty
    if not country_list:
        st.error("No countries are available in this dataset.")
        return None

    #sets teh default country, if it is not in the list of countries sets the alphabatically first country as teh first country
    default_country = "Canada"
    default_country_index = (
        country_list.index(default_country)
        if default_country in country_list
        else 0
    )

    #shows the dropdown box
    return st.selectbox(
        "Select a country",
        options=country_list,
        index=default_country_index,
        key=key
    )

#takes the input for the year
def year_input_taker(data, country, key):
    country_years = data.loc[
        data["entity"] == country, "year"
    ].dropna()

    #checks if the country_years is empty
    if country_years.empty:
        st.warning(
            f"No year data is available for {country}."
        )
        return None

    #gives the min and max year to set limit of the slider
    min_year = int(country_years.min())
    max_year = int(country_years.max())

    #sets the default year
    default_year = min(2020, max_year)

    #makes the default year to be as close to 2020 as possible if it is not availabe
    default_year = max(min_year, default_year)

    #shows the slider to set the year
    return st.slider(
        "What year would you like to see the data from?",
        min_value=min_year,
        max_value=max_year,
        value=default_year,
        step=1,
        key=key
    )


#gets the data to plot
def get_data_to_plot(data, country, year, value_column):
    #gives error if the column value_column does not match the column in the dataset
    if value_column not in data.columns:
        st.error(
            f"Column '{value_column}' was not found. "
            f"Available columns: {data.columns.tolist()}"
        )
        #returns the empty table with a year and another column whose name comes from value_column, makes so that program knows what to do even if there is no data in it
        return pd.DataFrame(
            columns=["year", value_column]
        )

    #gets the data to plot and stores it in plot_data
    plot_data = data.loc[
        (data["entity"] == country)
        & (data["year"] >= year),
        ["year", value_column]
    ].copy()

    # Convert values to numeric
    plot_data[value_column] = pd.to_numeric(
        plot_data[value_column],
        errors="coerce"
    )

    # Remove missing values
    plot_data = plot_data.dropna(
        subset=["year", value_column]
    )

    # Remove infinite values such as inf and -inf
    plot_data = plot_data[
        np.isfinite(plot_data[value_column])
    ]

    # Sort by year
    return plot_data.sort_values("year")


def what_graphs_to_graph():
    st.subheader("Which graphs would you like to plot?")

    selected_graphs = []

    #lets you choose the graph using a dropbox from the dictionary Value_columns which contains the name of the different graphs
    for graph in VALUE_COLUMNS:
        selected = st.checkbox(
            graph,
            value=(graph == "CO2 emission"),
            key=f"graph_{graph}"
        )

        #if the graph is selected it will add it to a list called selected_graphs
        if selected:
            selected_graphs.append(graph)

    #gives warning if nothing is selected
    if not selected_graphs:
        st.warning("Please select at least one graph.")

    return selected_graphs



def plot_one_country_data(country, year, data, graph):
    #assigns the name of the selected graphs to the variable named value_column
    value_column = VALUE_COLUMNS[graph]

    #stores the data in a variable
    plot_data = get_data_to_plot(
        data, country, year, value_column
    )


    if plot_data.empty:
        st.warning(
            f"No {graph} data is available for {country} "
            f"from {year} onward."
        )
        return

    #the graphs settings/config
    sns.set_theme(
        style="darkgrid",
        context="notebook",
        palette="deep"
    )

    fig, ax = plt.subplots(figsize=(10, 5))

    sns.lineplot(
        data=plot_data,
        x="year",
        y=value_column,
        color="#2E8B57",
        linewidth=2.5,
        marker="o",
        markersize=4,
        ax=ax
    )

    #sets a log scale for the CO2 graph
    if graph == "CO2 emission" and (
        plot_data[value_column] > 0
    ).all():
        ax.set_yscale("log")

        # Use readable labels on normal (linear) axes
    if ax.get_yscale() == "linear":
        ax.yaxis.set_major_formatter(
            mticker.FuncFormatter(
                lambda x, _: f"{x:,.0f}"
            )
        )

    #sets a title
    ax.set_title(
        f"{graph} — {country}",
        fontsize=18,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel(graph, fontsize=12)
    ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()
    st.pyplot(fig)
    plt.close(fig)

def show_percentage_difference(
    data, country_1, country_2, value_column,
    year_1, year_2
):
    # Get the data for each country
    data_1 = get_data_to_plot(
        data, country_1, year_1, value_column
    )
    data_2 = get_data_to_plot(
        data, country_2, year_2, value_column
    )

    # only uses the years that each country has in common so that there are no complications
    comparison_data = pd.merge(
        data_1,
        data_2,
        on="year",
        suffixes=("_1", "_2")
    )

    #checks if the list is empty
    if comparison_data.empty:
        st.warning(
            "There are no overlapping years to compare."
        )
        return

    # Use the latest year for both countries
    latest = comparison_data.sort_values(
        "year"
    ).iloc[-1]


    value_1 = latest[f"{value_column}_1"]
    value_2 = latest[f"{value_column}_2"]
    common_year = int(latest["year"])

    #if the value is zero it gives error, cant divide by zero
    if value_1 == 0:
        st.warning(
            "Percentage difference cannot be calculated "
            "because the first country's value is zero."
        )
        return

    #calculates the percentage
    percentage = (
        (value_2 - value_1) / abs(value_1)
    ) * 100

    #code for the table
    st.markdown(
        f"### Percentage comparison ({common_year})"
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        country_1,
        f"{value_1:,.2f}"
    )

    col2.metric(
        country_2,
        f"{value_2:,.2f}"
    )

    col3.metric(
        "Difference vs. " + country_1,
        f"{percentage:+,.2f}%",
        delta=f"{percentage:+,.2f}%"
    )

    # Show the percentage change for each shared year
    comparison_data["Percentage difference (%)"] = (
        (
            comparison_data[f"{value_column}_2"]
            - comparison_data[f"{value_column}_1"]
        )
        / comparison_data[f"{value_column}_1"].abs()
    ) * 100

    st.dataframe(
        comparison_data[
            ["year", "Percentage difference (%)"]
        ].rename(columns={"year": "Year"}),
        hide_index=True,
        use_container_width=True
    )

#the function assigns variables to the countries it is plotting and data to plot and plots them
def plot_comparison(
    data, country_1, year_1, country_2, year_2, graph
):
    value_column = VALUE_COLUMNS[graph]

    #makes the table which shows the percentage difference
    show_percentage_difference(
        data,
        country_1,
        country_2,
        value_column,
        year_1,
        year_2
    )


    country_1_plot = get_data_to_plot(
        data, country_1, year_1, value_column
    )

    country_2_plot = get_data_to_plot(
        data, country_2, year_2, value_column
    )

    country_1_plot = country_1_plot.copy()
    country_2_plot = country_2_plot.copy()

    country_1_plot["entity"] = country_1
    country_2_plot["entity"] = country_2

    plot_data = pd.concat(
        [country_1_plot, country_2_plot],
        ignore_index=True
    )

    if plot_data.empty:
        st.warning(
            f"No {graph} data is available for comparison."
        )
        return

    sns.set_theme(
        style="whitegrid",
        context="notebook",
        rc={
            "figure.facecolor": "#FFFFFF",
            "axes.facecolor": "#FFFFFF",
            "axes.edgecolor": "#E5E7EB",
            "axes.labelcolor": "#374151",
            "xtick.color": "#6B7280",
            "ytick.color": "#6B7280",
            "grid.color": "#E5E7EB",
            "grid.linewidth": 0.7,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titleweight": "bold",
            "axes.titlesize": 17,
            "axes.labelsize": 11,
            "legend.frameon": False
        }
    )

    fig, ax = plt.subplots(figsize=(11, 5.5))

    colours = ["#16845B", "#E58A32"]

    sns.lineplot(
        data=plot_data,
        x="year",
        y=value_column,
        hue="entity",
        palette={
            country_1: colours[0],
            country_2: colours[1]
        },
        linewidth=2.8,
        marker="o",
        markersize=4,
        ax=ax
    )

    if graph == "CO2 emission" and (
        plot_data[value_column] > 0
    ).all():
        ax.set_yscale("log")

    # Use readable labels on normal (linear) axes
    if ax.get_yscale() == "linear":
        ax.yaxis.set_major_formatter(
            mticker.FuncFormatter(
                lambda x, _: f"{x:,.0f}"
            )
        )

    ax.set_title(
        f"{graph}: {country_1} vs {country_2}",
        loc="left",
        pad=18
    )

    ax.set_xlabel("Year", labelpad=10)
    ax.set_ylabel(graph, labelpad=10)

    ax.grid(axis="y")
    ax.grid(axis="x", visible=False)

    ax.legend(
        title=None,
        loc="best"
    )

    ax.tick_params(
        axis="both",
        length=0,
        pad=8
    )

    ax.margins(x=0.02, y=0.12)

    fig.tight_layout()

    st.pyplot(fig, use_container_width=True)
    plt.close(fig)



def choice_of_comparison():
    #asks if want to compare and stores it in a variable called choice
    choice = st.radio(
        "Would you like to compare your country with another one?",
        ["Yes", "No"],
        horizontal=True,
        key="comparison_choice_input"
    )

    return choice == "Yes"


def main():
    program_heading()

    #starts by making CO2 as the default value
    CO2 = data_list["CO2 emission"]

    #sets entity_1 to be CO2 which will be the default value
    entity_1 = country_input_taker(
        CO2,
        key="country_1"
    )

    if entity_1 is None:
        return

    st.divider()

    #takes input of the year of the default value which being CO2
    year_1 = year_input_taker(
        CO2,
        entity_1,
        key="year_1"
    )

    if year_1 is None:
        return

    st.divider()

    #assigns comarison to the funciton choice_of_comparison
    comparison = choice_of_comparison()

    entity_2 = None
    year_2 = None

    #if comparison is true it asks for the second country, the code is the same for this so no comments for this
    if comparison:
        st.divider()

        entity_2 = country_input_taker(
            CO2,
            key="country_2"
        )

        if entity_2 is None:
            return

        year_2 = year_input_taker(
            CO2,
            entity_2,
            key="year_2"
        )

        if year_2 is None:
            return

    st.divider()

    selected_graphs = what_graphs_to_graph()

    #returns none if no graph is selected
    if not selected_graphs:
        return

    st.divider()

    #loops over the graphs in the selected_graphs list and plot them if a comparison is requested
    for graph in selected_graphs:
        st.subheader(graph)

        data = data_list[graph]

        if comparison:
            plot_comparison(
                data,
                entity_1,
                year_1,
                entity_2,
                year_2,
                graph
            )
        else:
            plot_one_country_data(
                entity_1,
                year_1,
                data,
                graph
            )

        st.divider()


if __name__ == "__main__":
    main()
