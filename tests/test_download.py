import main

def test_sanity():
    data = main.get_data_fromApi(1)
    assert data is not None
    assert len(data.get('items', [])) > 0