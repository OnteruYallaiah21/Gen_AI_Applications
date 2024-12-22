import openai  # Ensure the OpenAI library is updated: pip install --upgrade openai
import time

# File paths for input and output
input_file = "D:\Projects\LangchainProjects\DataSets\Open_Api_keys.txt"  # Replace with your actual file path containing API keys
working_keys_file = "Working.txt"
not_working_keys_file = "NotWorking.txt"

# Initialize lists to store working and non-working keys
working_keys = []
not_working_keys = []

# Read API keys from the input file
with open(input_file, "r") as file:
    api_keys = [line.strip() for line in file if line.strip()]

# Process each API key
for index, key in enumerate(api_keys, start=1):
    try:
        # Set the OpenAI API key
        openai.api_key = key
        
        # Send a simple request to verify the key using the new Chat API
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use a valid model for the test
            messages=[{"role": "user", "content": "What is the capital of France?"}],  # Question to test the key
            max_tokens=5
        )
        
        # If no exception, the key is working
        working_keys.append(key)
        
    except Exception as e:
        # Handle any error (including invalid keys, rate limits, etc.)
        not_working_keys.append(key)

    # Optional: Add a delay between requests to avoid rate limits
    time.sleep(1)

# Save results to output files
with open(working_keys_file, "w") as working_file:
    for key in working_keys:
        working_file.write(f"{key}\n")

with open(not_working_keys_file, "w") as not_working_file:
    for key in not_working_keys:
        not_working_file.write(f"{key}\n")

# Print working and not working keys once at the end
print(f"Working keys: {working_keys}")
print(f"Not working keys: {not_working_keys}")

print("Verification complete. Check the output files for results.")
