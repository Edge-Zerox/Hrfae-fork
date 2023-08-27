import numpy as np
import os
index = 62951
# Đường dẫn đến tệp tin .npy
file_path = "data/ffhq.npy"
image_dir = "./data/ffhq/"
label = "./data/ffhq.npy"
label = np.load(label)


th = str(index//1000)+'000' if (index > 9000) else '0'+str(index//1000)+'000' 
img_name = os.path.join(image_dir,th,label[index][0])

# Sử dụng hàm load của NumPy để đọc tệp tin .npy
loaded_data = np.load(file_path)

# In ra dữ liệu đã đọc
# print(loaded_data[0:20])
print(img_name)


