
import re
import json
import requests
from urllib.parse import urlencode

headers={"User-Agent": "Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148"}

job_id_list = [
    'f6288f8af00406b1',
     '56ab4e4fe59ae782',
     '29bd7638828fab65',
     '697a7a3f18590465',
     '08e92505e27442d3',
     '105529f69e3fdae2'
]

full_job_data_list = []

for job_id in job_id_list:
    try:
        indeed_job_url = 'https://www.indeed.com/m/basecamp/viewjob?viewtype=embedded&jk=' + job_id
        response = requests.get(indeed_job_url, headers=headers)
        print(response)
        if response.status_code == 200:
            script_tag  = re.findall(r"_initialData=(\{.+?\});", response.text)
            if script_tag is not None:
                json_blob = json.loads(script_tag[0])
                job = json_blob["jobInfoWrapperModel"]["jobInfoModel"]
                full_job_data_list.append({
                    'company': job.get('jobInfoHeaderModel').get('companyName') if job.get('jobInfoHeaderModel') is not None else '',
                    'jobkey': job_id,
                    'jobTitle': job.get('jobInfoHeaderModel').get('jobTitle') if job.get('jobInfoHeaderModel') is not None else '',
                    'jobDescription': job.get('sanitizedJobDescription').get('content') if job.get('sanitizedJobDescription') is not None else '',
                })
            
            
    except Exception as e:
        print('Error', e)

print(full_job_data_list)
