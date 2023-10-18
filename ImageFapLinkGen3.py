import urllib.request
from time import sleep
import numpy as np
from datetime import datetime
from tqdm import tqdm

def get_sleep_time(avg):
    return np.random.uniform(0.5 * avg, 1.5 * avg)

def main():
    AVG_SLEEP_TIME = 2

    # Get the URL of the gallery from the user
    url = input("Please type or paste the URL of the gallery (Example: https://www.imagefap.com/pictures/12345678/Gallery%20Name):\n")
    url = url.split("?")[0]
    url += "?view=2&page=0"
    page_number = 0
    group_links = []

    # Extract the short date from the current date
    current_datetime = datetime.now()
    short_date = current_datetime.strftime("%Y%m%d")

    # Extract the gallery ID from the given URL
    url_parts = url.split("/pictures/")
    if len(url_parts) > 1:
        gallery_id = url_parts[1].split("/")[0]
    else:
        gallery_id = "unknown"

    # Create the filename based on the format 'IF-<short date>-<gallery_id>.html'
    filename = f"IF-{short_date}-{gallery_id}.html"

    # Step 1: Scanning pages
    print("Scanning pages...")
    while True:
        request = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
        response = str(urllib.request.urlopen(request).read())
        splitstring = "/photo/"
        response = response.split(splitstring)

        if len(response) == 1:
            break

        for i in range(1, len(response), 24):
            group_link = "https://www.imagefap.com/photo/" + response[i].split("\"")[0]
            if group_link in group_links:
                break
            group_links.append(group_link)
        else:
            # Update and print the progress
            print("Page", page_number + 1, "is scanned", end='\r')
            page_number += 1
            url = url.split("page=")[0] + "page=" + str(page_number)
            sleep(get_sleep_time(AVG_SLEEP_TIME))
            continue

        break

    image_links = []
    image_links_short = []

    # Step 2: Getting image links
    total_links = len(group_links)
    for i, link in tqdm(enumerate(group_links), total=total_links, desc="Progress", unit=" image"):
        request = urllib.request.Request(link, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:20.0) Gecko/20100101 Firefox/20.0'})
        while True:
            response = str(urllib.request.urlopen(request).read())
            splitstring = "https://cdn.imagefap.com/images/full/"
            response = response.split(splitstring)
            if len(response) == 1:
                sleep(get_sleep_time(AVG_SLEEP_TIME))
                continue
            break

        for j in range(1, len(response), 2):
            image_link = "https://cdn.imagefap.com/images/full/" + response[j].split("\"")[0]
            image_link_short = image_link.split("?")[0]
            if image_link_short not in image_links_short:
                image_links_short.append(image_link_short)
                image_links.append(image_link)

        sleep(get_sleep_time(AVG_SLEEP_TIME))

    # Step 3: Save image links to an HTML file
    with open(filename, "w") as html_file:
        html_file.write("<html>\n<head>\n</head>\n<body>\n")
        for image_link in image_links:
            # Write image links as clickable hyperlinks in the HTML file
            html_file.write(f'<a href="{image_link}">{image_link}</a><br />\n')
        html_file.write("</body>\n</html>")

    # Step 4: Print completion message
    print(f"\n{len(image_links_short)} image links are collected and saved to {filename}")
    print("Process completed. You can now close this window.")

if __name__ == "__main__":
    main()
