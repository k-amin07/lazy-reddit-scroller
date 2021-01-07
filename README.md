# lazy-reddit-scroller
A simple script which scrolls Reddit for you, so you can sit back and stare at your screen without having to do even the bare minimum.

## Requirements:
- Python 3
- Selenium
- Chrome/Chromium Browser
- chromedriver

## How To Run:
> python ./lazy_scroll.py

The script will open an instance of Chrome/Chromium browser with the data directory /var/tmp/chrome_reddit, to keep it isolated from your other data.

## Chromedriver:
You must download chromedriver relevant to your Chrome/Chromium browser version. To check your browser version run:
> google-chrome-stable --version

Then go to https://chromedriver.chromium.org/ and download the version that matches your browser version. Extract the zip file and in terminal run
> chmod +x /path/to/chromedriver

to make it executable

## Selenium
Install selenium by running
python -m pip install selenium

## Command Line Arguments:
The script accepts the following arguments:

> --driver: Path to chromedriver. By default it will look for chromedriver in the current directory

> --directory: Data directory for chrome. Default is /var/tmp/chrome_reddit, but you can give any valid path as long as another instance of Chrome/Chromium browser isnt using it.

> --login: If you want to use an account to browse reddit. If this flag is enabled, username and password must also be provided

> --no-login: Scroll reddit without login

> --wait: Seconds to wait before scrolling to the next post.

## Caveats:
There are certain caveats to using this script. For instance you cannot stop scrolling unless you kill the script, which would also kill the browser instance. Feel free to add functionality to this script, this is just my lazy attempt at sitting back and enjoying Reddit. 

Happy Scrolling!
