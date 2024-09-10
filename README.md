# CIS 6930FA24 - Assignment0

## Author
Guttapati Jayasurya Reddy

## Description
This Python package retrieves data from the FBI's Most Wanted API and formats the information in a thorn-separated (þ) format. The package allows you to retrieve data either by specifying a page number from the API or by loading a local JSON file for testing purposes.

The output contains the title, subjects, and FBI field offices associated with each record in the API, separated by a thorn character (þ).

<!-- ## How to install
```bash
pipenv install -e . -->

## How to Run
We can run the program in 2 ways. Either by specifying a page from the FBI API or by using a local JSON file. (!!Make sure you have the virtual environment activated.!!) And also make sure that you have installed pipenv requests pytests.


Running with API : "pipenv run python main.py --page 1"

Running with Local File: "pipenv run python main.py --file <path_to_json_file>" 

## Functions

main.py - This is the entry point of the program where it calls the appropriate functions based on the input.


download.py
download_data(page):

Downloads data from the FBI API for the specified page.
process_data(data):

Processes the downloaded data to format the title, subjects, and field offices with thorn separators (þ).
read_from_file(file_path):

Reads data from a local JSON file for testing.

## Testing

To run the tests, use pytest: "pipenv run pytest"




