from pathlib import Path
import requests
virus_total_api_url="https://www.virustotal.com/api/v3/files"
virus_total_api_key="688a87eaf53337b3281c825b7af8630b8b27463f302ace285a7661feec13342a"
def scan_file(file_path):
    print(f"scaning file:{file_path}")
    response = requests.post(url=virus_total_api_url, headers={'x-apikey': virus_total_api_key}, files={'file': open(file_path, 'rb')})
    response=response.json()
    return response["data"]["id"]
def get_analysis(id):
    request=requests.get(virus_total_api_url,headers={'x-apikey':virus_total_api_key})
    if request.status_code==200:
        print("request sucssed!")
    else:
        print("request didnt sucsses! ERROR!")

def iterate_directory_contents(directory_path):
    directory_path=Path(directory_path)
    for item in directory_path.iterdir():
        if item.is_file():
            scan_file(item)
        else:
           iterate_directory_contents(item)


    

