def filter_post_urls(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            url = line.strip().strip('",')
            if "/p/" in url:
                outfile.write(f'"{url}",\n')

if __name__ == "__main__":
    input_file = 'updatedmail_urls.txt'
    output_file = 'filtered_updatedmail_urls.txt'
    filter_post_urls(input_file, output_file)
