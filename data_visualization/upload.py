import requests

# now = "file_jane"
# now = now.strftime("%Y-%m-%d_%H-%M-%S")
url = 'http://viz-dev.isis.vanderbilt.edu:5991/upload?type=jane_viz'
files = {'upload_file': open('../feb14_photo.png', 'rb')}
ret = requests.post(url, files=files, allow_redirects=True)
print(ret)
if ret.status_code == 200:
    print('Uploaded!')