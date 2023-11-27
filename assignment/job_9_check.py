from selenium import webdriver
from datetime import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from time import time
from time import sleep
import pandas as pd
from random import randint

from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import codecs
import re
from webdriver_manager.chrome import ChromeDriverManager

def scrape_naukri_jobs(url):
    driver.get(url)
    sleep(5)
    get_url = driver.current_url
    
    if get_url == url:
        page_source = driver.page_source

        soup = BeautifulSoup(page_source, "html.parser")
        job_cards = soup.find_all("div", class_="styles_jlc__main__VdwtF")
        
        jobs = []
        
        for card in job_cards:
            title = card.find("a", class_="title")
            if title:
                title = title.text.strip()

            company = card.find("a", class_="comp-name mw-25")
            if company:
                company = company.text.strip()

            location = card.find("span", class_="locWdth")
            if location:
                location = location.text.strip()            

            experience = card.find("span", class_="expwdth")
            if experience:
                experience = experience.text.strip()

            salary = card.find("span", class_="ni-job-tuple-icon ni-job-tuple-icon-srp-rupee sal")
            if salary:
                salary = salary.text.strip()

            skills = card.find("ul", class_="tags-gt")
            if skills:
                skills = [skill.text.strip() for skill in skills.find_all("li")]
            print("********")
            print(jobs)

            jobs.append({
                "Title": title,
                "Company": company,
                "Location": location,
                "Experience": experience,
                "Salary": salary,
                "Skills": skills
            })
        
        return jobs
    
options = webdriver.ChromeOptions() 
options.headless = True 
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Example usage:
url = "https://www.naukri.com/data-scientist-jobs-in-india"
jobs = scrape_naukri_jobs(url)
print(jobs)

# if jobs_data:
#     for job in jobs_data:
#         print("Title:", job["Title"])
#         print("Company:", job["Company"])
#         print("Location:", job["Location"])
#         print("Experience:", job["Experience"])
#         print("Salary:", job["Salary"])
#         print("Skills:", job["Skills"])
#         print("=" * 50)
# else:
#     print("No jobs found.")