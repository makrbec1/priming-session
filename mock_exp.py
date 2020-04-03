from PIL import Image
import glob
import random

pos_image_list = []
for filename in glob.glob('D:\Documents\MSc\sleepysleepy\programming_group\priming-session\stimuli\primes_pos\*.jpg'):
    pos_img=Image.open(filename)
    pos_image_list.append(pos_im)
print(pos_image_list)
pos_img.show()

random.shuffle(pos_img)


# create two lists of filenames (or modify your existing code to import
# them from disk):
# pos_img  = ['image_'+ str(i)+'.jpg' for i in range(30)]
# neg_img = ['image_'+ str(i)+'.jpg' for i in range(30)]

# print(pos_img)

# randomise their order:
# random.shuffle(pos_img)
# random.shuffle(neg_img)
