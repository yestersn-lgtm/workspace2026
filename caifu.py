import requests

url = 'https://www.eastmoney.com/'

response = requests.get(url)
# 'utf-8'  # gbk
response.encoding = 'utf-8'

print(f'Status Code: {response.status_code}')
print(f'Content Length: {len(response.content)}')
print(f'Content Preview: {response.text[:100]}')  # Print first 100 characters of the content
print('Request completed successfully.')

data_str = response.text
print(f'Data Type: {type(data_str)}')
# print(data_str)  # Uncomment to print the full content

with open('caifu.html', 'w', encoding='utf-8') as file:
    file.write(data_str)
    print('Data written to caifu.html')
print('Program ended.')
