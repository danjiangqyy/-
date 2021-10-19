from PIL import Image
from PIL import ImageChops
from PIL import Image
import cv2
import math
import operator
from functools import reduce
from PIL import Image
from PIL import ImageChops
def compare_images(path_one, path_two, diff_save_location):
  """
  比较图片，如果有不同则生成展示不同的图片
  @参数一: path_one: 第一张图片的路径
  @参数二: path_two: 第二张图片的路径
  @参数三: diff_save_location: 不同图的保存路径
  """
  image_one = Image.open(path_one)
  image_two = Image.open(path_two)
  print(image_two.size,image_one.size)
  try:
      diff = ImageChops.difference(image_one, image_two)
      if diff.getbbox() is None:

    # 图片间没有任何不同则直接退出
          print("【+】We are the same!")
          diff.save(diff_save_location)
      else:
          diff.save(diff_save_location)
  except ValueError as e:
      # print(diff.getbbox())
      # diff.save(diff_save_location)
      text = ("表示图片大小和box对应的宽度不一致，参考API说明：xxx")
      print("【{0}】{1}".format(e,text))
def image_contrast(img1, img2):
  image1 = Image.open(img1)
  image2 = Image.open(img2)


  h1 = image1.histogram()
  h2 = image2.histogram()
  # print(str(h1))
  result = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
  return result



def trans_size(img1,img2):

    img=cv2.imread(img1)
    img2=cv2.imread(img2)
    w=img.shape[0]

    h=img.shape[1]

    resized = cv2.resize(img2,(h,w))
    print('目前电子档图片大小={}\n'
          '原来的客户图片大小={}\n'
          '修改后现在的客户图片大小={}'.format(img.shape,img2.shape,resized.shape))
    img3=cv2.imwrite(r'C:\Users\little\Desktop\111.png',resized)


if __name__ == '__main__':
    img1 = r'C:\Users\little\Desktop\2.png'
    img2 = r'C:\Users\little\Desktop\4.png'



    trans_size(img1,img2)
    img3=r'C:\Users\little\Desktop\111.png'

    compare_images(img1,
                   img3,
                   r'C:\Users\little\Desktop\我们.png')
    img_1=cv2.imread(img1)
    img_3=cv2.imread(img3)

    result = image_contrast(img1, img3)

    if result < 100 and result >= 10:
        print('接近')
    elif result < 10:
        print('是同一张图')
    else:
        print('有点差别')
    print(result)


    cv2.imshow('dianzi', img_1)
    cv2.imshow('kehu', img_3)
    cv2.waitKey()
    cv2.destroyAllWindows()