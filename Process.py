import os
from rembg import remove
from PIL import Image


Path_in = 'Img_select'
Path_out = '.\Img_return'
path_driver = r'C:\Users\lucas.tremontini\u2net\u2net.onnx'

for idx,i in enumerate(os.listdir(Path_in)): 
    remove(Image.open(
            os.path.join(Path_in,i))
            ).save(os.path.join(
                Path_out,f'_remove_{idx}')
    )

