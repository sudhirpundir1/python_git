ips='192.00.76.123,192.77.87.100,192.65.65.99'
list_ips=ips.split(',')
print(list_ips)

list_ips=': '.join(list_ips)

print(list_ips)

#----Example 2
names_list = ['Alice', 'Bob', 'Eve']
## Converting list to string
names_str = ','.join(names_list)
print(names_str)
url= 'www.python.org'
## Converting string to list
url_list = url.split('.')
print(url_list)