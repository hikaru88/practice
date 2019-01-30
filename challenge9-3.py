import csv

text = [["Top Gun",
         "Risky Business",
         "Minority Report"
         ],
        ["Titanic",
         "The Revenant",
         "Inception"
         ],
        ["Training Day",
         "Man on Fire",
         "Flight"
         ]]


with open("challenge9.csv", "w", newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for row in text:
        w.writerow(row)
