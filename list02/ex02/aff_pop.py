from load_csv import load
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def main():
    """
    Compare the population of the campus country (Brazil) with France.

    Loads population_total.csv with load() from ex00, keeps the years
    1800 to 2050, converts values like "534k", "2.5M" and "1.2B" to
    numbers and plots both countries on the same graph, with a title,
    axis labels and a legend. Does nothing if the file can't be loaded
    (load() already prints the error). Any other error, or a Ctrl+C,
    is caught and reported without a traceback.
    """
    try:
        df = load("population_total.csv")
        if df is None:
            return
        df = df[df["country"].isin(["France", "Brazil"])]
        df = df.set_index("country")
        df.columns = df.columns.astype("int")
        df = df.loc[:, 1800:2050]
        df = df.replace({
            r"k$": "e3",
            r"M$": "e6",
            r"B$": "e9"
        }, regex=True)
        df = df.astype(float)
        ax = df.T.plot(
            kind="line",
            title="Population Projections",
            xlabel="Year",
            ylabel="Population",
            color=["blue", "green"],
            figsize=(10, 7),
            xticks=range(1800, 2051, 40),
            yticks=range(20_000_000, int(df.max().max()) + 1, 20_000_000),
        )
        ax.yaxis.set_major_formatter(
            FuncFormatter(lambda x, pos: f"{x / 1e6:g}M")
        )
        ax.legend(loc="lower right", title=None)
        plt.show()
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")


if __name__ == "__main__":
    main()
