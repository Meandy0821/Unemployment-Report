


from app.stocks import format_usd, fetch_stocks_data

from pandas import DtaFrame

def test_usd_formatting(4.5) == "$4.5"



        # assert 2 + 2 == 4


        assert format_usd(4.5) == "$4.5"

         assert format_usd(4.555555) == "$4.56"

          assert format_usd(1234567890) == "$1,234,567,890.00"




def test_data_fetching():
        result = fetch_stocks_data("NFLX")
        assert isintance(result, DataFrame)


        assert "timestamp" in result.columns 
        assert "adjsuted_close" in result.columns 
        assert "high" in result.columns 
        assert "low" in result.columns

        assert len(result) => 100 