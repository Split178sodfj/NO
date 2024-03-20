import os

# Get the current working directory
current_directory = os.getcwd()

# Location of CMSeek
cmseek_location = os.path.join(current_directory, "cmseek.py")

# User-inputed URL
target_url = input("Enter the URL to scan: ")

# Running CMSeek scan
print("Starting CMSeek scan...")
os.system(f"python3 {cmseek_location} -u {target_url}")
print("CMSeek scan completed.")

# Specify the absolute path for the output file
json_output_file = "/home/def/unite/NewOne/reports.json"
print("Starting WPScan scan...")

# Running WPScan with sudo and providing the sudo password via stdin using 'echo' and '|'
os.system(f"sudo wpscan --url {target_url} --enumerate u,p --plugins-detection aggressive "
          f"--api-token VUx0qG6XBJkZ7VJ6GjDssKsquBhjouSwsKGEHclULIg --disable-tls-checks -o {json_output_file} --format json")
print(f"WPScan scan completed and saved to {json_output_file}.")
