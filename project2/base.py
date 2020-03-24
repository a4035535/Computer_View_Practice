from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def conv(data, kernel):
    n, m = data.shape
    img_new = []
    for i in range(n - 3):
        line = []
        for j in range(m - 3):
            a = data[i:i + 3, j:j + 3]
            line.append(np.sum(np.multiply(kernel, a)))
        img_new.append(line)
    return np.array(img_new)


if __name__ == '__main__':
    img = Image.open('pictures/lena.jpg').convert('L')
    # plt.imshow(img, 'gray')
    img = np.array(img)

    kernel = np.array([[1 / 3, 1 / 3, 1 / 3], [0, 0, 0], [-1 / 3, -1 / 3, -1 / 3]])
    img_new = conv(img, kernel)
    plt.imshow(img_new, 'gray')
    plt.show()

    kernel = np.array([[-1 / 3, 0, 1 / 3], [-1 / 3, 0, 1 / 3], [-1 / 3, 0, 1 / 3]])
    img_new = conv(img, kernel)
    plt.imshow(img_new, 'gray')
    plt.show()
