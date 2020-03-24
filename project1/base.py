from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    pic = (Image.open('pictures/montain.jpg')).convert('L')
    pic_array = np.array(pic)
    # print(pic_array)

    dir_count = {}
    for i in pic_array:
        for j in i:
            if j in dir_count:
                dir_count[j] += 1
            else:
                dir_count[j] = 1
    total_num = len(pic_array) * len(pic_array[0])
    # print(f'{len(pic_array)} * {len(pic_array[0])} = {total_num}')

    dir_list = sorted(dir_count)
    table = {}
    sum_rate = 0
    for i in dir_list:
        rate = dir_count[i] / total_num
        sum_rate += rate
        table[i] = int(round(255 * sum_rate, 0))
    # print(table)

    deal_array = []
    row = 0
    for i in pic_array:
        deal_array.append([])
        for j in i:
            deal_array[row].append(table[j])
        row += 1

    deal_array = np.array(deal_array)
    img_deal = Image.fromarray(deal_array)

    img_deal.convert('RGB').save('deal.jpg')

    plt.hist(deal_array.flatten(), 256)
    plt.hist(pic_array.flatten(), 256)
    plt.show()
