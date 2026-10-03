import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


CO2 = pd.read_csv("annual-co2-emissions-per-country.csv")


def program_heading():

    st.title(
        'This is a app to see CO2 emission of a country '
        'or compare between 2 countries'
    )

    st.write(
        '*******************************************************************'
    )


def country_input_taker(key):

    country = st.text_input(
        'what countries would you like to see the graph for? :',
        key=key
    )

    return country.strip()


def year_input_taker(key):

    try:
        year = st.number_input(
            label='what year would you like to see the graph for? :',
            value=2020,
            step=1,
            format='%d',
            key=key
        )

    except ValueError:
        st.error('Please enter a number')
        return None

    return int(year)


def data_validator(country, year, data):

    matching_countries = data[
        data['entity'].str.lower() == country.lower()
    ]

    if matching_countries.empty:
        st.error(
            f'Sorry, {country} is not in our database.'
        )
        return False

    country = matching_countries.iloc[0]['entity']

    entity_data = data[
        data['entity'] == country
    ]

    earliest_year_of_data_available = entity_data['year'].min()

    country_data = data[
        (data['entity'] == country) &
        (data['year'] == year)
    ]

    if country_data.empty:
        st.error(
            f'Sorry, we do not have the data for the year {year}. '
            f'The earliest year we have the data for is '
            f'{earliest_year_of_data_available}.'
        )
        return False

    return True


def get_data_to_plot(data, country, year):

    return data.loc[
        (data['entity'] == country) &
        (data['year'] >= year),
        ['year', 'emissions_total']
    ]


def plot_one_country_data(country, year, data):

    plot_data = get_data_to_plot(
        data,
        country,
        year
    )

    sns.set_theme(
        style="darkgrid",
        context="notebook",
        palette="deep"
    )

    fig, ax = plt.subplots()

    sns.lineplot(
        data=plot_data,
        x="year",
        y="emissions_total",
        color="#2E8B57",
        linewidth=2.5,
        marker="o",
        markersize=4,
        ax=ax
    )

    ax.set_yscale("log")

    ax.set_title(
        f"CO2 Emissions — {country}",
        fontsize=18,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel(
        "Year",
        fontsize=12
    )

    ax.set_ylabel(
        "CO2 Emissions",
        fontsize=12
    )

    ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


def plot_comparison(data, country_1, year_1, country_2, year_2):

    country_1_plot = get_data_to_plot(
        data,
        country_1,
        year_1
    )

    country_2_plot = get_data_to_plot(
        data,
        country_2,
        year_2
    )

    sns.set_theme(
        style="whitegrid",
        context="notebook",
        palette="muted"
    )

    fig, ax = plt.subplots()

    sns.lineplot(
        data=country_1_plot,
        x="year",
        y="emissions_total",
        label=country_1,
        linewidth=2.5,
        marker="o",
        markersize=4,
        ax=ax
    )

    sns.lineplot(
        data=country_2_plot,
        x="year",
        y="emissions_total",
        label=country_2,
        linewidth=2.5,
        marker="o",
        markersize=4,
        ax=ax
    )

    ax.set_yscale("log")

    ax.set_title(
        f"CO2 Emissions — {country_1} vs {country_2}",
        fontsize=18,
        fontweight="bold",
        pad=15
    )

    ax.set_xlabel("Year", fontsize=12)

    ax.set_ylabel("CO2 Emissions", fontsize=12)

    ax.tick_params(axis="x", rotation=45)

    plt.tight_layout()

    st.pyplot(fig)

    plt.close(fig)


def choice_of_comparison():

    choice = st.radio(
        'Would you like to compare the country of your choice with another one?: ',
        ['Yes', 'No'],
        horizontal=True,
        key='comparison_choice_input'
    )

    if choice == 'Yes':
        return True

    else:
        return False


def main():

    program_heading()

    entity_1 = country_input_taker(
        key='country_1'
    )

    st.write(
        '*******************************************************************'
    )

    year_1 = year_input_taker(
        key='year_1'
    )

    if entity_1 == '':
        st.warning('Please enter a country.')
        return

    if year_1 is None:
        return

    valid = data_validator(
        entity_1,
        year_1,
        CO2
    )

    if not valid:
        return

    st.write(
        '*******************************************************************'
    )

    comparison = choice_of_comparison()

    if comparison == True:

        st.write(
            '*******************************************************************'
        )

        entity_2 = country_input_taker(
            key='country_2'
        )

        st.write(
            '*******************************************************************'
        )

        year_2 = year_input_taker(
            key='year_2'
        )

        if entity_2 == '':
            st.warning('Please enter the second country.')
            return

        if year_2 is None:
            return

        valid = data_validator(
            entity_2,
            year_2,
            CO2
        )

        if not valid:
            return

        plot_comparison(
            CO2,
            entity_1,
            year_1,
            entity_2,
            year_2
        )

        st.write(
            '*******************************************************************'
        )

        result = [
            entity_1,
            year_1,
            entity_2,
            year_2
        ]

        st.write(result)

    else:

        plot_one_country_data(
            entity_1,
            year_1,
            CO2
        )

        st.write(
            '*******************************************************************'
        )


if __name__ == "__main__":

    main()



