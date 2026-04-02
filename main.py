import requests

def fetch_and_save_data():
    url = "https://apiservice.mol.gov.tw/OdService/download/A17000000J-000003-U9H"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        response.encoding = 'utf-8-sig'

        with open("data.csv", "w", encoding="utf-8-sig") as f:
            f.write(response.text)
            
        print("data.csv saved!\n")
        
    except Exception as e:
        print(f"failed: {e}")

if __name__ == "__main__":
    fetch_and_save_data()