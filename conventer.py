from PIL import Image
import os
import shutil

episode = 0

while (episode<180):
    belgeList = []

    with os.scandir('C:/Users/Pc/Desktop/sl/episode{}'.format(episode)) as tarama:
        for belge in tarama:
            if belge.name.endswith("jpg"):
                belgeList.append(int(belge.name.rstrip(".jpg")))
    belgeList.sort()

    imgPathList = []
    imgList = []
    for i in belgeList:
        imgPathList.append(Image.open(r'C:\Users\Pc\Desktop\sl\episode{}\{}.jpg'.format(episode,i)))
        if (i == 0):
            img0 = imgPathList[i].convert('RGB')
            continue
        imgList.append(imgPathList[i].convert('RGB'))
    img0.save(r'C:\Users\Pc\Desktop\soloLeveling\{}.pdf'.format(episode), save_all=True, append_images=imgList)
    print("{}.pdf kaydedildi".format(episode))
    shutil.rmtree('C:/Users/Pc/Desktop/sl/episode{}'.format(episode))
    episode = episode + 1

    #içi boş dosya silmek için os.remove() kullanılır ama içi dolu dosyalarda shutil.rmtree() kullan