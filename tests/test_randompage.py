import main

def test_sanity():
    sample_data = {
    "items": [
        {"title": "John Doe", "subjects": ["Bank Robbery"], "field_offices": ["New York"]}
    ]
}
    process_data = main.format_data(sample_data)
    assert process_data == None



    