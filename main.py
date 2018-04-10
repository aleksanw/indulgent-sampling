import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


sample_resolution = 1000000
histogram_bins = 1000


def main():
    ax1 = plt.figure().gca()
    plot_indulgency_demo(ax1, normal_distribution, "Normal distribution")

    ax2 = plt.figure().gca()
    plot_indulgency_demo(ax2, uniform_distribution, "Uniform distribution")

    plt.show()


def normal_distribution(n):
    return np.random.normal(0.0, 1.0, n)


def uniform_distribution(n):
    return np.random.uniform(0.0, 1.0, n)


def indulgent(level, n, sampler):
    # For each indulgent sample, generate <level> samples and select the
    # largest.
    return np.max(sampler([level, n]), axis=0)


def plot_indulgency_demo(ax, distribution, distribution_name):
    df = pd.DataFrame()

    for level in [1,2,5,10]:
        df[level] = indulgent(level, sample_resolution, distribution)

    df.plot.hist(ax=ax, histtype='step', density=True, bins=histogram_bins,
            alpha=0.8)

    ax.set(
        title="Indulgent sampling on " + distribution_name,
        xlabel="Value",
        ylabel="P(Value)",
        )
    ax.legend(
        title='Trials',
        loc='upper left',
        )


if __name__ == '__main__':
    main()
