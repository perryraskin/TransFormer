## TransFormer: Transaction Formatter
![](rm_image.jpg)

**Purpose:** To make managing personal finances ***actually personal***. This means that your financial information, including all your expenses and income, isn't on some third party website. It should be super simple, without needing to worry about your bank or credit card info getting stolen by very probable cyber attacks (on Mint, for example). And as much as websites like Mint have all these privacy policies, many of us stay paranoid, but still want a modern way to manage our finances and view colorful reports.

**Target Users:** Those who value spreadsheets and use them often for, well, everything. The ability to understand the basics of working with spreadsheets, and of course how CSV files work, is crucial. As of now, users also need to understand a certain level of programming to plot reports using the generated CSV file. Ideally this app evolves to have options for users without programming knowledge as well.

**Details:** Right now it's meant to leave you with a CSV file that includes all the basic data you would need to plot financial data. It takes data from Chase or CapitalOne transaction CSV downloads, and loads it into a usable CSV. To use with *Matplotlib* or anything you may use to plot data from a CSV. This assumes you can plot using Python or another language.

**Checklist:**

* :ballot_box_with_check: Chase CSV support
* :ballot_box_with_check: CapitalOne CSV support
* :ballot_box_with_check: Converts to specified CSV format: **[Date, Amount, Description, Category]**
* :ballot_box_with_check: Adds positive float number for purchases, negative float numbers for refunds

**To Do:**

* Integrate banks API for easy CSV transaction access
* Create a new CSV for every import, and only grab the new data
* Eventually develop a macOS/iOS app