import signal
import subprocess
import time
import sys
import os

# Define the maximum run time (in seconds)
MAX_RUN_TIME = 60   # 1 minute

INPUT_DIR = "files"
OUTPUT_DIR = "files"


# function to handle the timeout


def timeout_handler(signum, frame):
    print("Timeout reached. Exiting...")
    sys.exit(0)


def main():
    # Set the signal handler for SIGALRM (alarm signal)
    # signal.signal(signal.SIGALRM, timeout_handler)

    # Set an alarm for the maximum execution time
    # signal.alarm(MAX_RUN_TIME)

    first_iteration = True
    # Main AFL-like loop
    while True:
        try:
            if first_iteration:
                with open('files/test_input.txt', 'r') as f:
                    content = f.readlines()
                subprocess.run(["python3", "run_ble_tester.py"], check=True)
                first_iteration = False
            else:
                subprocess.run(["./mutate", os.path.join(INPUT_DIR, "test_input.txt"),
                               os.path.join(OUTPUT_DIR, "mutate_output.txt")], check=True)
                # take in mutate_output.txt as input
                subprocess.run(["python3", "run_ble_tester.py"], check=True)

            # Check if the output file is empty
            output_file_path = os.path.join(OUTPUT_DIR, "test_output.txt")
            if os.stat(output_file_path).st_size == 0:
                print("Output file is empty.")
                return
            else:
                # Read the contents of the output file and print them
                with open(output_file_path, "r") as output_file:
                    output_data = output_file.read()
                    print("Contents of output file:")
                    print(output_data)

        except Exception as e:
            print("Error occurred:", e)
            break


if __name__ == "__main__":
    main()
