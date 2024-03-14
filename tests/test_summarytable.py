from lianapy.misc.summarytable import SummaryTable


def test_summarytable():
    summary = SummaryTable()

    n = 10

    for i in range(n):
        summary.record("i", i)
        summary.record("i^2", i**2)

    df = summary.to_pandas()

    assert df.shape == (n, 2)
