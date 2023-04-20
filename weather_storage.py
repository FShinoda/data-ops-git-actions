from bs4 import BeautifulSoup
from google.cloud import storage
from google.oauth2 import service_account
import requests

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

credentials_dict = {
  "type": "service_account",
  "project_id": "cobalt-poet-342917",
  "private_key_id": "80261ad49716ada7cdaa3172785b72963a98e056",
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDMxKihy4WzLWky\nl5fNLYtkBlTGfZeGPnUqCOo39P8NVfw2g7VyxFyoGiR6YwlAyyMAFNcdYJMcH0I1\n+G0YZVlchbvPZBGf6XwQi7+NAHcsf+wevJ6URPWWXBLpWGISl4g/jfZfP/V1oqmv\nef1fMWMuAsa9n4fZ0AjC+dfXihBRrvI6zd3EoWStH9nwmNGjs84Albzpp3q6cdwT\nxvRzaDO5SLywJsbqVJmOJ5hP5sytTl6zBCn708H64G8OBa3ucWj1rynzyiyJoQky\nnpMS2dYF04I/+qxZNr9xL6nGa8HOux/qqOF33jCZflLQUSu0xJNr2IB120rRoydL\nwmUjbVIDAgMBAAECggEAU+fvq6Cwb/vXI+5/OwmDGSEJAu66tL0KGIffpb9D9cx6\nlUICC32P9CgGM4o6Y+z5MhLYFMcacMcUQ/ZAieMZq3J3Q2OfXzX26vbArn/21Wqz\nr+KdXmcldQ/Uhf577V9fap96yYv1Qlc9jdSAcM3VdKiZlGD281cuB+sFuWHvDvDS\nv/Tg+LoiQwxjqsw1F7Uvq5QRy0y3odlwgof+TOOijRjvn70eHSXQDl6uUtypGoum\ny+y78J+OxdJYXhCRGjP/J7FNEPtn3LisJ7h3MBYp+XdX39WucLnYEKWS9UoEerb5\nemNMPP4o3phN+H+QGLVLxsd9UivHvxnt4Mi/ypZF9QKBgQD/GofMfSA8ASbnUfef\nFnQZqYieSPTeJIx8zyK5dXc7i2HJYvznJ1KqSl2GxU7lgndTYJOPoMeGskN2y2T3\nGlyrFipnLJblm2CxPlgYJBn0YMFnDRsLCqO5bUw0Nt0Vr0qdxa3OaLaYbMOs40pr\nYcyQDo9LY8slvfPMX15U4HHOvQKBgQDNfNnMfncWZ7OUcpReBvKF2vbu4ji+i7H1\nQiEspDCp7ToEfzzCkwswZ+NS77QnaEM0mnNjSSUljMWdtWPBN3g35r/rVTw9S+gS\nDjoz6FhJjnI8r5nSuxufKlLauE5EDiIOURxH6724F9JnRLCu2Qj8jW3Zw2u7hU9l\nzZk6PvMPvwKBgB9EwDp3Z9kTBxK5gFGWrfprRlyocqM79aBiv03eMRQyXHUT1g37\nSu2mmdooGyiUmk20+8FSIsLG3PAVtDV5nLw3xlDJLWHNbseq7Z9f5XKH3YzlFViA\nIFtdI0cPJoA+8TVvgoNXYHJEeqOZZIjO/wT1U+kYvVDN/LEjS2u56xk9AoGBAILL\njIqYmM6fFXRQ9lVfULGY7YKiZgILQyvceudCX2NaB4rjPlaPaBjYl56ryt0mhViP\nUxEIdueO0h6PXb6XwyK58sElkOFnVoFfovZ1VvUDAX3VPDEhPfSy6OglVlQFNvIr\n+Ldiu3DZYOiwlVHF/e1bTGfG9uT2dtJS6sxjUy1bAoGAWyxqm6yjTfsEVxnbKk9j\nY09D9b6BCwEjcDbaHIwsrRDz+26rYRdd/VGJLzN5cbWwbdNWotRTpD0gmtVVppsi\nRWb6OHqVa60rMUHX+XrfSXE9tRq6TMx/BGisBIq4KwBUmyIyQO8vPBNtfYr3ZzRF\n3vyv6PYk9iukD46TXRTE7y8=\n-----END PRIVATE KEY-----\n",
  "client_email": "497642440814-compute@developer.gserviceaccount.com",
  "client_id": "102686299752836455954",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/497642440814-compute%40developer.gserviceaccount.com"
}

try:
  res = requests.get(
    f'https://www.google.com/search?q=SaoPauloCidade&oq=SaoPauloCidade&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

  print("Loading...")

  soup = BeautifulSoup(res.text, 'html.parser')

  info = soup.find_all("span", class_="LrzXr kno-fv wHYlTd z8gr9e")[0].getText()
  
  print(info)

  """Uploads a file to the bucket."""
  credentials = service_account.Credentials.from_service_account_info(credentials_dict)
  storage_client = storage.Client(credentials=credentials)
  bucket = storage_client.get_bucket('data-ops-teste')
  blob = bucket.blob('weather_info.txt')

  blob.upload_from_string(info + '\n')

  print('File uploaded.')

  print("Finished.")
except Exception as ex:
  print(ex) 