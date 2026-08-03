import matplotlib.pyplot as plt

from load_csv import load


def main() -> None:
    """
    Plot life expectancy against gross domestic product for year 1900.

    Loads both income_per_person_gdppercapita_ppp_inflation_adjusted.csv
    and life_expectancy_years.csv through load() from ex00, then draws
    one point per country for the year 1900. The graph must have a
    title and a label on both axes (subject requirement).
    """
    year = "1900"
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    life = load("life_expectancy_years.csv")
    if income is None or life is None:
        return

    # TODO: scatter plot with the income of `year` on x and the life
    #       expectancy of `year` on y, one point per country.
    #       The x axis is a log scale in the subject example.

    plt.title(f"{year}")
    plt.xlabel("Gross domestic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.show()


if __name__ == "__main__":
    main()
