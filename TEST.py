import requests

MY_API1 = "https://fast-api-test-gjqi-git-master-thebimfactorys-projects.vercel.app/"

# Định nghĩa header cho request
API_KEY = "TBF-123"
headers = {
    "X-API-Key": API_KEY,
}

params = {
    'a': 2,
    'b': 3
}

response = requests.get(f"{MY_API1}calculate", headers=headers, params=params)
print(response.content)

# Kiểm tra trạng thái của phản hồi
if response.status_code == 200:
    try:
        data1 = response.json().get("Cong")
        data2 = response.json().get("Nhan")
    except ValueError:
        print("Không thể giải mã JSON từ phản hồi")
        data1 = None
        data2 = None
        
else:
    print(f"Lỗi: Nhận được mã trạng thái {response.status_code}")
    data1 = None
    data2 = None

print("Data 1: ", data1)
print("Data 2: ", data2)
