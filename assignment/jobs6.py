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

# PROXY = "11.456.448.110:8080"
# chrome_options = WebDriver.ChromeOptions()
# chrome_options.add_argument('--proxy-server=%s' % PROXY)

website = """
#########################################
#           WEBSITE: INDEED.FR          #
######################################### 
"""
print(website)
start_time = datetime.now()
print('Crawl starting time : {}' .format(start_time.time()))
print()

def generate_url(index):
    if index == 1:
        return "https://www.naukri.com/machine-learning-engineer-jobs-in-india"
    else:
        return format("https://www.naukri.com/machine-learning-engineer-jobs-in-india-{}".format(index))
    return url

def write_file(index, soup):
    file = open("jobs/machine_learning_engineer/page-{}.txt".format(index), "w")
    file.write(str(soup))
    file.close()

def get_total_jobs():
    url = "https://www.naukri.com/data-science-data-scientist-machine-learning-engineer-jobs-in-india?k=data%20science%2C%20data%20scientist%2C%20machine%20learning%20engineer&l=india&nignbevent_src=jobsearchDeskGNB"
    driver.get(url)
    get_url = driver.current_url
    sleep(randint(7,10))
    print('Collecting data for "{}"...' .format(job))
    if get_url == url:
        page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')
    total_jobs = soup.find('span', class_="styles_count-string__DlPaZ").text
    print(total_jobs)
    total_jobs = total_jobs.strip().split(" ")
    print(total_jobs)
    total_jobs = total_jobs[-1]
    total_jobs = int(total_jobs)
    print("- Number of open positions : {}" .format(total_jobs))

def extract_rating(rating_a):
    if rating_a is None or rating_a.find('span', class_="main-2") is None:
        return "None"
    else:
        return rating_a.find('span', class_="main-2").text

def parse_job_data_from_soup(page_jobs):
    # print(page_jobs)
    for job in page_jobs:
        row1 = job.find('div', class_="row1")
        row2 = job.find('div', class_="row2")
        row3 = job.find('div', class_="row3")
        row4 = job.find('div', class_="row4")
        row5 = job.find('div', class_="row5")
        row6 = job.find('div', class_="row6")
        print("*************START***************")
        job_title = row1.a.text
        # print(row2.prettify())
        company_name = row2.span.a.text
        rating_a = row2.span
        rating = extract_rating(rating_a)
        
        job_details = row3.find('div', class_="job-details")
        ex_wrap = job_details.find('span', class_="exp-wrap").span.span.text
        location = job_details.find('span', class_="loc-wrap ver-line").span.span.text

        min_requirements = row4.span.text

        all_tech_stack = []
        for tech_stack in row5.ul.find_all('li', class_="dot-gt tag-li "):
            tech_stack = tech_stack.text
            all_tech_stack.append(tech_stack)

        print("Job Title : {}" .format(job_title))
        print("Company Name : {}" .format(company_name))
        print("Rating : {}" .format(rating))
        print("Experience : {}" .format(ex_wrap))
        print("Location : {}" .format(location))
        print("Minimum Requirements : {}" .format(min_requirements))
        print("All Tech Stack : {}" .format(all_tech_stack))

        print("***************END***************")
        
options = webdriver.ChromeOptions() 
options.headless = True 
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

for i in range(72,420):
    print(i)
    url = generate_url(i)
    driver.get(url)
    sleep(randint(5, 10))
    get_url = driver.current_url
    if get_url == url:
        page_source = driver.page_source

    soup = BeautifulSoup(page_source, 'html.parser')
    page_jobs = soup.find_all('div', class_="srp-jobtuple-wrapper")
    write_file(i, page_jobs)
# file = open("jobs/MyFile.txt", "r")
# file.close()

# print('Collecting data for "{}"...' .format(job))
# page_source = file.read()
# file.close()

# parse_job_data_from_soup(soup)

# file1 = open("MyFile.txt", "w") 
# file1.write("Hello \n")
# file1.close()


# total_jobs = soup.find('span', class_="styles_count-string__DlPaZ").text
# print(total_jobs)
# total_jobs = total_jobs.strip().split(" ")
# print(total_jobs)
# total_jobs = total_jobs[-1]
# total_jobs = int(total_jobs)
# print("- Number of open positions : {}" .format(total_jobs))
