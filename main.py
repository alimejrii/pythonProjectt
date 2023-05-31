import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiM2YzZmUxZDMtNmRkNy00ZjEyLTg0MTQtYTVkZmNmMGExZDBjIiwidHlwZSI6ImFwaV90b2tlbiJ9.8mC2pH-Lx2z2p6DUwnifnaAbA0WKCGiPfIOZRMt2VwM"}

url="https://api.edenai.run/v2/ocr/resume_parser"
data={"providers": "affinda"}
files = {'file': open("C:/Users/USER/Downloads/mejrialiWevioo_CV (1).pdf",'rb')}

response = requests.post(url, data=data, files=files, headers=headers)

result = json.loads(response.text)
print(result['affinda']['extracted_data'])