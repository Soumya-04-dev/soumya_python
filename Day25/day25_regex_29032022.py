import re

# for regular expression module name re is imported
# It is a search pattern between strings

# search , match , findall

# txt = "The rain in spain"
# x = re.search("^The.*spain$", txt)
# print(x.group(0))
'''
tenant_project_name = "pts-sre-sohil-2"
filesync_url = "https://filesync-server-1-pts-sre-sohil-2.platform.cloud.slb-ds.com/login"

#output = "https://filesync-server-1-pts-sre-sohil-2"

regex_pattern = f'^https://(.+?)-{tenant_project_name}'
print(re.search(regex_pattern, filesync_url).group(1))'''
'''
server_names= ['studio-server', 'license-server', 'license-server-1', 'filesync-server-2', 'filesync-ser', 'license-ser-2' 'ad-server',
'admirror-server', 'ad-server2', 'ad-server-2']

#regex_pattern = 'license(.+)'
regex_pattern = '(^ad-.+)'
for license_name in server_names:
    if re.search(regex_pattern, license_name):
        print(license_name)
'''

fo = open('servernames.txt', 'r')
contains = fo.read()
print(contains)
