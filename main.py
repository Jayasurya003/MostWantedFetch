import json
import argparse
import csv
import sys
import requests

# delimiter
THORN = 'þ'

# url
BASE_URL = "https://api.fbi.gov/wanted/v1/list?page="

# get data from API
def get_data_fromApi(page):
    url = f"{BASE_URL}{page}"
    result = requests.get(url)
    result.raise_for_status()
    return result.json()

# get data from a local JSON file
def get_data_fromFile(location):
    with open(location, 'r') as file:
        return json.load(file)

# save api data to a JSON file
def save_data_toJsonFile(data, fileName='fbi_data.json'):
    with open(fileName, 'w') as json_file:
        json.dump(data, json_file, indent=2)
    #print(f"JSON data saved to {fileName}")

# Format data with thorn delimiter and save to CSV file
def format_data(data, outFile='FBIMostWanted.csv'):
    with open(outFile, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=THORN)
        writer.writerow(['Title', 'Subjects', 'Field Offices'])

        for item in data['items']:
            title = item.get('title', '')

            subjects = item.get('subjects', [])
            field_offices = item.get('field_offices', [])

            if not isinstance(subjects, list):
                subjects = [subjects] if subjects else []
            if not isinstance(field_offices, list):
                field_offices = [field_offices] if field_offices else []

            subjects_str = ', '.join(subjects)
            field_offices_str = ', '.join(field_offices)

            # Write to CSV
            writer.writerow([title, subjects_str, field_offices_str])
            
            print(f"{title}{THORN}{subjects_str}{THORN}{field_offices_str}")

# Main function to handle command-line arguments
def main(page=None, file_location=None):
    if page:
        data = get_data_fromApi(page)
        save_data_toJsonFile(data)  
    elif file_location:
        data = get_data_fromFile(file_location)
    else:
        print("Error: You should specify either --page or --file-location.")
        sys.exit(1)

    format_data(data)
    #print("Output data has been saved to FBIMostWanted.csv")

# Command-line argument parsing
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Get, Format & Save FBI wanted data.")
    parser.add_argument("--page", type=int, required=False, help="The page number to fetch from the FBI API.")
    parser.add_argument("--file-location", type=str, required=False, help="The file location of the JSON data for testing.")

    args = parser.parse_args()

    if args.page and args.file_location:
        print("Error: Only one of --page or --file-location should be specified.")
        sys.exit(1)
    
    main(page=args.page, file_location=args.file_location)










def bubbleSort(arr):
    
    n = len(arr)

    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
            
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def selectionSort(array, size):
    
    for s in range(size):
        min_idx = s
        
        for i in range(s + 1, size):
            
            # For sorting in descending order
            # for minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i

        # Arranging min at the correct position
        (array[s], array[min_idx]) = (array[min_idx], array[s])





def insertion_sort(list1):  
  
        # Outer loop to traverse on len(list1)  
        for i in range(1, len(list1)):  
  
            a = list1[i]  
  
            # Move elements of list1[0 to i-1], 
            # which are greater to one position
            # ahead of their current position  
            j = i - 1  
          
            while j >= 0 and a < list1[j]:  
                list1[j + 1] = list1[j]  
                j -= 1  
                
            list1[j + 1] = a  
            
        return list1  




def countingSort(arr, exp1):

    n = len(arr)

    # The output array elements that will have sorted arr
    output = [0] * (n)

    # initialize count array as 0
    count = [0] * (10)

    # Store count of occurrences in count[]
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1

    # Change count[i] so that count[i] now contains actual
    # position of this digit in output array
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copying the output array to arr[],
    # so that arr now contains sorted numbers
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]




def insertRec(root, key): 
  
  # If the tree is empty, 
  # return a new node 
  
  if (root == None): 
    root = Node(key) 
    return root 
  
  # Otherwise, recur 
  # down the tree  
  if (key < root.key): 
    root.left = insertRec(root.left, key) 
  elif (key > root.key): 
    root.right = insertRec(root.right, key) 
  
  # return the root
  return root



















