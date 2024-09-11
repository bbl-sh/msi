import requests
from bs4 import BeautifulSoup


file = open("HOD.txt", "a")

URL = "https://www.cuh.ac.in/hod.aspx"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find_all("td")

i = 9
for x in range(33):
    file.write("\n")
    file.write("department is : " + results[i].text.strip())
    file.write("\nName is : " + results[i+1].text.strip())
    file.write("\nDesignation is : " + results[i+2].text.strip())
    file.write("\nDepartment is : " + results[i+3].text.strip())
    file.write("\nContact number is : " + results[i+4].text.strip())
    file.write("\nOfficial email is : " + results[i+5].text.strip())
    file.write("\n---------")
    i = i + 7
print("document written success")

file.close()
