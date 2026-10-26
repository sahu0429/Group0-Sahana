
from unittest.mock import Mock, patch

from sahana_sridhar_fintech.client import fetch_live_data


@patch("sahana_sridhar_fintech.client.requests.get")
def test_fetch_live_data(mock_get):
    mock_response = Mock()
    mock_response.json.return_value = {
        "available": [{"currency": "eur", "amount": 1500}],
        "livemode": False,
    }
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    result = fetch_live_data()

    assert result["status"] == "LIVE_SUCCESS"
    assert result["currency"] == "EUR"
    assert result["available_balance"] == 15.0
    assert result["livemode"] is False

    mock_get.assert_called_once()
    mock_response.raise_for_status.assert_called_once()
