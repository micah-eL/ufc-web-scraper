# UFC web scraper

This Python script was created for myself as a way to quickly check for changes in UFC rankings.
The script will list the champ, as well as any ranking changes within the top 15 of every division.
The functionality is fairly simple at the moment as this was my first foray into web scraping, but I intend on adding more features as well as a user interface sometime in the near future. I will most likely start by adding the ability to pull fight details for upcoming events, but if you are a MMA fan and have any recommendations/requests, feel free to reach out! 



##### Usage
1. Download the repo
2. Set up Pyton environment with required dependencies in requirements.txt (see below for more info)
3. Run *python main.py* in the appropriate directory

If you are unfamiliar with using virtual environments, the 2 libraries needed to run this script are beautifulsoup and requests:

pip install beautifulsoup4

pip install requests

Note: These libraries were downloaded in a Python3 virtual environment (i.e. pip3 was used).
