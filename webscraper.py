#imports the libraries needed for webscraping
import requests
from bs4 import BeautifulSoup
#The url of the website to scrape
URL= "https://realpython.github.io/fake-jobs/"
#the code below retrieves the html data and stores it in an object
page=requests.get(URL)
#a beautifulsoup object that inputs the html content and ensures the right parser is used
soup=BeautifulSoup(page.content, "html.parser")
#the line below finds the specific html element using id
results=soup.find(id="ResultsContainer")

#finds all the job postings on the site using html class
job_elements=results.find_all("div", class_="card-content")

#the lambda function identifies titles of all python job postings and converts them to lowercase
python_jobs=results.find_all("h2", string=lambda text:"python" in text.lower())

#this dictionary finds the html parent elements

python_jobs_elements=[
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

#for loop extracts the required job information 
for element in python_jobs_elements:
    title_element=element.find("h2",class_="title")
    company_element=element.find("h3", class_="company")
    location_element=element.find("p", class_="location")
    #prints all the extracted information and strips all whitespaces
    print(title_element.text.strip())
    print(company_element.text.strip())
    print(location_element.text.strip())
    print()

#scrapes all the links for extracted jobs
for job_element in python_jobs_elements:
    link_url = job_element.find_all("a")[1]["href"]
    print(f"Apply here: {link_url}\n")
