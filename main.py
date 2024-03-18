import requests
import threading

## Base path
BASE_PATH = 'http://127.0.0.1:5000/'
## List of Existing Path
PATHS = []

## Take all world of world lists
file = open("dir_list.txt", "r")
content = file.readlines()
words_array = [word.strip() for word in content]

## Method who will call the given URL and define original path
def define_original_path(mocked_paths):
    for mocked_path in mocked_paths:
        ## mock an url from given string
        temp_url = BASE_PATH + mocked_path
        response = requests.get(temp_url)
        code = response.status_code
        ## define if code is 200 and 500 
        if code == 200 or code == 500:
            PATHS.append(mocked_path)
            print("\n One fish: " + mocked_path)
            PATHS.append(temp_url)

## We will divide the array of list on two part to increase 
## processing time
divided_array_len = len(words_array) // 2
first_half = words_array[:divided_array_len]
second_half = words_array[divided_array_len:]

## Creating two threads for each array
thread1 = threading.Thread(target=define_original_path, args=(first_half,))
thread2 = threading.Thread(target=define_original_path, args=(second_half,))

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("All threads have finished.")

# Function to stylize and print the array
def stylized_print(array):
    for index, word in enumerate(array):
        if index % 2 == 0:
            print(f"\033[1;32m{word}\033[0m", end=" ")  # Green color for even indices
        else:
            print(f"\033[1;34m{word}\033[0m", end=" ")  # Blue color for odd indices
    print() 

stylized_print(PATHS)