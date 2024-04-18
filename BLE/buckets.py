import sys
import shutil
import uuid

# Get the input file name from command line arguments
input_file = sys.argv[1]

# Get the output file name from command line arguments
output_file = sys.argv[2]

# Open the input file for reading
with open(input_file, "r") as f:
    # Read all lines from the input file
    lines = f.readlines()

# Filter lines containing "BRDA"
filtered_lines = [line.strip().replace("BRDA:", "")
                  for line in lines if "BRDA" in line]

# Open the output file for writing
with open(output_file, "w") as f:
    # Write the filtered lines to the output file
    for line in filtered_lines:
        f.write(line + "\n")

print("Filtered data has been stored in", output_file)

print("DONE")

# Define the input file name
input_file = "filtered_data.txt"

# Create a dictionary to store the data
data_dict = {}

# Open the file and populate the dictionary
with open(input_file, "r") as f:
    for line in f:
        # Split each line into individual parts
        parts = line.strip().split(',')
        # Extract the first three numbers as the key and the fourth number as the value
        key = tuple(parts[:3])
        value = int(parts[3])
        print(key)
        print(value)
        # Store the data in the dictionary
        data_dict[key] = value

# Function to search for the fourth value based on the first three numbers


def search_value(first, second, third):
    key = (first, second, third)
    if key in data_dict:
        return data_dict[key]
    else:
        return None


# Example usage
first = '228'
second = '0'
third = '3'
result = search_value(first, second, third)
if result is not None:
    print(f"The fourth value for ({first}, {second}, {third}) is: {result}")
else:
    print("No matching entry found for the given first three numbers.")


def update_buckets_and_get_score(inp):
    buckets = {
        0: [[0, 1], [1, 2], [2, 4], [4, 8], [8, 16], [16, 32], [32, 64], [64, 128], [128, 256], [256, 512]],
        1: [[1, 2], [2, 4], [4, 8], [8, 16], [16, 32], [32, 64], [64, 128], [128, 256], [256, 512], [512, 1024]],
        2: [[0, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]],
        3: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [9, 10]],
        4: [[0, 2], [2, 4], [4, 6], [6, 8], [8, 10], [10, 12], [12, 14], [14, 16], [16, 18], [18, 20]]
    }
    files = ["b1.txt", "b2.txt", "b3.txt", "b4.txt", "b5.txt"]
    key = tuple(inp[:3])
    value = inp[3]
#    print(f"Key: {key}, Value: {value}")
#    print(f"Type of key: {type(key[0])}")

    bucket_score = 0

    for i, file in enumerate(files):
        with open(file, 'r') as f:
            lines = f.readlines()
        updated_lines = []
        found = False
        for line in lines:
            parts = line.strip().split(',')
            identifier = tuple(map(int, parts[:3]))
            slots = parts[3:]
#            print(f"Identifier: {identifier}, Slots: {slots}")
#            print(f"Type of identifier: {type(identifier[0])}")
            if identifier == key:
                found = True
                slots_ints = [int(x) for x in slots]
                for n, _range in enumerate(buckets[i]):
                    if _range[0] <= value and slots_ints[n] == 0:
                        bucket_score += 1
                        slots_ints[n] = 1
                updated_line = ','.join(
                    map(str, list(identifier) + slots_ints))
                updated_lines.append(updated_line + '\n')
            else:
                updated_lines.append(line)

        if not found:
            new_line = f"{key[0]},{key[1]},{key[2]},1" + ",0" * 9 + "\n"
            updated_lines.append(new_line)
            bucket_score = 5

        with open(file, 'w') as f:
            f.writelines(updated_lines)

    return bucket_score


def is_interesting(bucket_score):
    if (bucket_score >= 2):
        # IF INTERESTING:
        unique_filename = str(uuid.uuid4())  # Creates a unique file name
        shutil.copy(f"./lcov.info",
                    f"./IsInterestingLcovs/{unique_filename}.info")
        print("estts")
        # TODO: add isInteresting inputs to isIntersting.txt file
        with open("isInteresting.txt", "a") as file:
            file.write(f"Bucket score: {bucket_score}\n")
        return bucket_score >= 2


# Example of usage
inp = [1, 2, 3, 11]
bucket_score = update_buckets_and_get_score(inp)
print(f"Bucket score is: {bucket_score}")
print(f"Is interesting: {is_interesting(bucket_score)}")
