import requests
from bs4 import BeautifulSoup


URL = "https://www.ufc.com/rankings"
# Send HTTP GET request to URL and store HTML data that server sends back as Python object
page = requests.get(URL)

# Create Beautiful Soup object - pass page.content instead of page.text to avoid problems with character encoding
pageContent = BeautifulSoup(page.content, "html.parser")

# Get every 'rankings table'
rankingTables = pageContent.findAll("table", class_="views-table views-view-table cols-0")

# Iterate over every table in rankingTables
for rankingTable in rankingTables:
    champField = rankingTable.find("h5")
    champName = (champField.find("a")).text
    tableCaption = (rankingTable.find("h4")).text
    if tableCaption[1:4] == "Men":
        print("==== Men's Rankings ====")
        tableCaption = tableCaption[1:22]
        print(tableCaption)
        print("Top rank: " + champName)
    elif tableCaption[1:4] == "Wom": # Other Women's dvisions don't have the extra space in front
        print() 
        print("==== Women's Rankings ====")
        tableCaption = tableCaption[1:24]
        print(tableCaption)
        print("Top rank: " + champName)
    else:
        print(tableCaption)
        print("Champ: " + champName)

    rankingTableRow = rankingTable.findAll("tr")
    for tableRow in rankingTableRow:
        rankChangeAmount = tableRow.find("span")
        if rankChangeAmount != None:
            rankChange = (tableRow.find("td", class_="views-field views-field-weight-class-rank-change")).text
            fighterName = (tableRow.find("a")).text
            fighterRank = (tableRow.find("td", class_="views-field views-field-weight-class-rank")).text
            print(fighterName + " (" + fighterRank.strip() + ")" + ": " + rankChange)

    print()