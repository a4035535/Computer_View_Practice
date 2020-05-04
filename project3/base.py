import numpy as np
import PIL.Image as image
from sklearn.cluster import KMeans


def load_data(file_path):
    f = open(file_path, 'rb')
    data = []
    img = image.open(f)
    m, n = img.size
    for i in range(m):
        for j in range(n):  # 将每个像素点RGB颜色处理到0-1范围内并存放data
            x, y, z = img.getpixel((i, j))
            data.append([x / 256.0, y / 256.0, z / 256.0])
    f.close()
    return np.mat(data), m, n


if __name__ == '__main__':
    img_data, row, col = load_data('pictures/image.bmp')
    label = KMeans(n_clusters=5).fit_predict(img_data)
    label = label.reshape([row, col])  # 聚类获得每个像素所属的类别
    pic_new = image.new("L", (row, col))  # 调整为灰度图
    for i in range(row):
        for j in range(col):
            pic_new.putpixel((i, j), int(256 / (label[i][j] + 1)))
    pic_new.save('111.jpg')
