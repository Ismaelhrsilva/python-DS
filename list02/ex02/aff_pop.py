import matplotlib.pyplot as plt

from load_csv import load


def main() -> None:
    """
    Compare the population of the campus country with another one.

    Loads population_total.csv through load() from ex00 and plots one
    curve per country, for the years 1800 to 2050. The graph must have
    a title, a label on both axes and a legend naming each curve
    (subject requirement).

    Note: the values are stored as strings such as "1.16M" or "20.5k",
    they have to be converted to numbers before being plotted.
    """
    country = "Brazil"
    other_country = "France"
    data = load("population_total.csv")
    if data is None:
        return

    # TODO: for each country, select its row, keep the years 1800 to
    #       2050, convert "1.16M" / "20.5k" to numbers and plot it with
    #       label=<country name> so the legend is filled.

    plt.title(f"{country} vs {other_country} population projections")
    plt.xlabel("Year")
    plt.ylabel("Population")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
