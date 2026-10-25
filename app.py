import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

@st.cache_data
def load_data():
    files = {
        "CO2 emission": "annual-co2-emissions-per-country.csv",
        "CO2 per Capita": "co-emissions-per-capita.csv",
        "GDP": "gdp-worldbank-constant-usd.csv",
        "land area": "land-area-km.csv",
        "population": "population-with-un-projections.csv"
    }

    datasets = {}

    for name, filename in files.items():
        data = pd.read_csv(filename)
        data.columns = data.columns.str.strip()

        data = data.rename(columns={
            "country": "entity",
            "Country": "entity",
            "Entity": "entity",
            "Code": "code",
            "year": "year",
            "Year": "year"
        })

        data["year"] = pd.to_numeric(
            data["year"], errors="coerce"
        )

        data = data.dropna(subset=["entity", "year"])
        data["year"] = data["year"].astype(int)

        datasets[name] = data

    return datasets


data_list = load_data()

VALUE_COLUMNS = {
    "CO2 emission": "emissions_total",
    "CO2 per Capita": "CO2 emissions per capita",
    "GDP": "GDP",
    "land area": "Land area (sq. km)",
    "population": "Population"
}


def program_heading():
    st.title(
        "This is an app to see CO2 emission of a country "
        "or compare between 2 countries"
    )
    st.divider()


def country_input_taker(data, key):
    country_list = sorted(
        data["entity"].dropna().unique().tolist()
    )

    if not country_list:
        st.error("No countries are available in this dataset.")
        return None

    default_country = "Canada"
    default_country_index = (
        country_list.index(default_country)
        if default_country in country_list
        else 0
    )

    return st.selectbox(
        "Select a country",
        options=country_list,
        index=default_country_index,
        key=key
    )


def year_input_taker(data, country, key):
    country_years = data.loc[
        data["entity"] == country, "year"
    ].dropna()

    if country_years.empty:
        st.warning(
            f"No year data is available for {country}."
        )
        return None

    min_year = int(country_years.min())
    max_year = int(country_years.max())

    default_year = min(2020, max_year)
    default_year = max(min_year, default_year)

    return st.slider(
        "What year would you like to see the data from?",
        min_value=min_year,
        max_value=max_year,
        value=default_year,
        step=1,
        key=key
    )


def data_validator(country, year, data):
    matching_data = data[
        (data["entity"] == country)
        & (data["year"] == year)
    ]

    if matching_data.empty:
        st.warning(
            f"No data is available for {country} in {year} "
            "in this dataset."
        )
        return False

    return True


def get_data_to_plot(data, country, year, value_column):
    if value_column not in data.columns:
        st.error(
            f"Column '{value_column}' was not found. "
            f"Available columns: {data.columns.tolist()}"
        )
        return pd.DataFrame(
            columns=["year", value_column]
        )

    plot_data = data.loc[
        (data["entity"] == country)
        & (data["year"] >= year),
        ["year", value_column]
    ].copy()

    plot_data[value_column] = pd.to_numeric(
        plot_data[value_column], errors="coerce"
    )

    return plot_data.dropna(
        subset=["year", value_column]
    ).sort_values("year")


def what_graphs_to_graph():
    st.subheader("Which graphs would you like to plot?")

    selected_graphs = []

    for graph in VALUE_COLUMNS:
        selected = st.checkbox(
            graph,
            value=(graph == "CO2 emission"),
            key=f"graph_{graph}"
        )

        if selected:
            selected_graphs.append(graph)

    if not selected_graphs:
        st.warning("Please select at least one graph.")

    return selected_graphs


def plot_one_country_data(country, year, data, graph):
    value_column = VALUE_COLUMNS[graph]

    plot_data = get_data_to_plot(
        data, country, year, value_column
    )

    if plot_data.empty:
        st.warning(
            f"No {graph} data is available for {country} "
            f"from {year} onward."
        )
        return

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

    if graph == "CO2 emission" and (
        plot_data[value_column] > 0
    ).all():
        ax.set_yscale("log")

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



def plot_comparison(
    data, country_1, year_1, country_2, year_2, graph
):
    value_column = VALUE_COLUMNS[graph]

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
    choice = st.radio(
        "Would you like to compare your country with another one?",
        ["Yes", "No"],
        horizontal=True,
        key="comparison_choice_input"
    )

    return choice == "Yes"


def main():
    program_heading()

    CO2 = data_list["CO2 emission"]

    entity_1 = country_input_taker(
        CO2,
        key="country_1"
    )

    if entity_1 is None:
        return

    st.divider()

    year_1 = year_input_taker(
        CO2,
        entity_1,
        key="year_1"
    )

    if year_1 is None:
        return

    st.divider()

    comparison = choice_of_comparison()

    entity_2 = None
    year_2 = None

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

    if not selected_graphs:
        return

    st.divider()

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
