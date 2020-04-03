from PIL import Image
import glob
image_list = []
for filename in glob.glob('D:\Documents\MSc\sleepysleepy\programming_group\priming-session\stimuli\primes_pos\*.jpg'):
    im=Image.open(filename)
    image_list.append(im)
im.show()
