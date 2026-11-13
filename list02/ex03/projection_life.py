import pandas as pd
from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Load the GDP per capita and life expectancy datasets and plot, for
    every country, the life expectancy against the GDP of the year 1900.
    """
    try:
        gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
        if gdp is None:
            return
        life = load("life_expectancy_years.csv")
        if life is None:
            return
        gdp = gdp.set_index("country")
        life = life.set_index("country")
        gdp = gdp["1900"]
        life = life["1900"]
        gdp_life = pd.concat([gdp, life], axis=1, keys=['GDP', 'Life'])
        gdp_life = gdp_life.dropna()

        plt.scatter(gdp_life['GDP'], gdp_life['Life'])
        plt.xscale("log")
        plt.xticks([300, 1000, 10000], ["300", "1k", "10k"])
        plt.title("1900")
        plt.xlabel("Gross domestic product")
        plt.ylabel("Life Expectancy")
        plt.show()

    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
