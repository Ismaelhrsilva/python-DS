from load_csv import load
import matplotlib.pyplot as plt


def main():
    """
    Display the life expectancy of the campus country (Brazil).

    Loads life_expectancy_years.csv with load() from ex00 and plots
    the Brazil row, years on the x axis (ticks every 40 years) and
    life expectancy on the y axis. Does nothing if the file can't be
    loaded (load() already prints the error). Any other error, or a
    Ctrl+C, is caught and reported without a traceback.
    """
    try:
        df = load("life_expectancy_years.csv")
        if df is None:
            return
        brazil = df.set_index("country").loc["Brazil"]
        brazil.index = brazil.index.astype(int)
        brazil.plot(
            kind="line",
            title="Brazil Life expectancy Projections",
            xlabel="Year",
            ylabel="Life expectancy",
        )
        plt.xticks(range(1800, 2081, 40))
        plt.show()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
