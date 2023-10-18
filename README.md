# ifdl
A Python script to retrieve all image links from an ImageFap gallery.

This builds on the original project and adds the following functionality:

1. Instead of creating the links and putting them into the clipboard, this will save the links to an HTML file.
2. You can drag/open the HTML file with a browser.
3. You can use your download software to fetch the images from the links. I tested with downloadthemall and it works well.
4. There is a progress bar that might be helpful in the case of large image sets. 
5. Libraries needed: 
A. urllib.request: This library is part of Python's standard library and is used for making HTTP requests.
B. time: This library is part of Python's standard library and is used for time-related functions, including sleep to introduce delays.
C. numpy: It's an external library for numerical computing and is used here to generate random sleep times.
D. datetime: Part of Python's standard library, it's used for working with date and time information.
E. tqdm: This is an external library for creating progress bars. You can install it using pip: pip install tqdm

## Requirements for the script
Install the required libaries using: ```pip install urllib3 numpy time datetime tqdm```. 

## Using the script
The script ImageFapLinkGen3.py can be run from any machine with Python installed correctly.

## Notes
Original Notes:
- When using the script ([ifdl.py](ifdl.py)), the bot detection prevention can be tweeked. The average time between requests is 2 seconds, because bot detection caught on when 1 second was used.
- When a 302 error occurs, open a new browser window and visit the gallery page to complete a reCAPTCHA. 
- The executable keeps getting flagged as virus, so I took it down for the moment.
