import matplotlib.pyplot as plt

from load_csv import load


def main() -> None:
    """
    Display the life expectancy of the campus country over the years.

    Loads life_expectancy_years.csv through load() from ex00 and plots
    the row of the campus country. The graph must have a title and a
    label on both axes (subject requirement).
    """
    country = "Brazil"
    data = load("life_expectancy_years.csv")
    if data is None:
        return

    # TODO: select the row of `country` and plot the years (x) against
    #       the life expectancy values (y).

    plt.title(f"{country} Life expectancy Projections")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy")
    plt.show()


if __name__ == "__main__":
    main()
