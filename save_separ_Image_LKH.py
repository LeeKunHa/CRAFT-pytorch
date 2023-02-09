#감지한 범위 이미지만 자르기

# 좌표 추출
from glob import glob
path = ('C:/Users/user/Foodinfo/data/image/infographic_result/') #탐지한 이미지 읽기
files = glob(f'{path}*.txt')
files = natsort.natsorted(files)

def coordinate(file_num):
    with open(files[file_num]) as f:
        list_ = []
        lines = f.readlines()
        for line in lines:
            list_.append(line)
    list_filter = []
    for i in range(len(list_)):
        if i%2 == 0:
            list_filter.append(list_[i].strip("\n").split(","))
    return list_filter






# 이미지 자르기
import os
error_list = [] #기울어진 사진?

for i in range(len(files)):
    img_path = ('C:/Users/user/Foodinfo/data/image/infographic_separ/')
    img_files = glob(f'{img_path}*.png')
    img_files = natsort.natsorted(img_files)
    image_raw = Image.open(img_files[i]) #원본이미지 읽기
    list_filter = coordinate(i)
    print("사진 원본 :", image_raw.size)
    for j in range(len(list_filter)):
        box_one = list_filter[j]
        left_up = box_one[:2]
        right_down = box_one[4:6]
        croppedImage=image_raw.crop((int(left_up[0]), int(left_up[1]), int(right_down[0]), int(right_down[1])))
        try:
            croppedImage.save('C:/Users/user/Foodinfo/data/image/infographic_crop/{}_{}.png'.format(img_files[i].split('\\')[1][:-4], j+1))
            #이미지의 크기 출력
            print("잘려진 사진 크기 :",croppedImage.size)
        except:
            error_list.append('{}_{}'.format(img_files[i].split('\\')[1][:-4], j+1))
            os.remove('data/image/infographic_crop/{}_{}.png'.format(img_files[i].split('\\')[1][:-4], j+1))