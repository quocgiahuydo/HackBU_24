import requests
import json

url = "https://api.api2convert.com/v2/jobs"

payload = "{     \"input\": [{         \"type\": \"remote\",       \"source\": \"https://example-files.online-convert.com/raster%20image/jpg/example_small.jpg\"   }],   \"conversion\": [{         \"category\": \"category\",       \"target\": \"png\"}]  }"
headers = {
  'x-oc-api-key': '263c20a5806184f7dc34732dd90cdb12',
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
