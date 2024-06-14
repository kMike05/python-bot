import re

def extract_proxies(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            match = re.search(r'(\d{1,3}(?:\.\d{1,3}){3}:\d{1,5})', line)
            if match:
                outfile.write(match.group(1) + '\n')

input_file = 'dirty_socks.txt'
output_file = 'clean_socks.txt'
extract_proxies(input_file, output_file)

print(f"Proxies extracted and saved to {output_file}")
