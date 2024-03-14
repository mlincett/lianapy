from lianapy.misc.summary_table import SummaryTable


def test_summarytable():
    summary = SummaryTable()

    for i in range(10):
        summary.record("i", i)
        summary.record("i^2", i**2)

    df = summary.to_pandas()

    assert df.shape == (10, 2)
