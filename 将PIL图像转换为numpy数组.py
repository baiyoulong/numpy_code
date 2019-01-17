from io import BytesIO
from PIL import Image
import PIL, requests
import numpy as np

URL = 'https://upload.wikimedia.org/wikipedia/commons/8/8b/Denali_Mt_McKinley.jpg'
response = requests.get(URL)

I = Image.open(BytesIO(response.content))
I = I.resize([150, 150])
arr = np.asarray(I)

im = PIL.Image.fromarray(np.uint8(arr))
Image.Image.show(im)