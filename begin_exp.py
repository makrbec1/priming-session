import random
import pandas as pd

#DELETE (simulated input)
# find 'uncomment' and uncomment when in psychopy
condition = 11
participant = str(00)

# creating the text file for each subject
# participant = str(expInfo['participant']) #uncomment
# condition = expInfo['condition'] #uncomment
txtfile = open('subjinfo' + participant + ".txt","w")
txtfile.write('Subject Number: '+participant+ "\n")
txtfile.write('Condition: '+str(condition)+ "\n")
txtfile.close()
# create two lists of filenames (or modify your existing code to import
# them from disk):
pos_img  = ['image_'+ str(i)+'.jpg' for i in range(30)]
neg_img = ['image_'+ str(i)+'.jpg' for i in range(30)]


# randomise their order:
random.shuffle(pos_img)
random.shuffle(neg_img)

# write the randomised order in the subject info text file
txtfile = open('subjinfo' + participant + ".txt","w")
txtfile.write('Positive Images Sequence: '+str(pos_img)+ "\n")
txtfile.write('Negative Images Sequence: '+str(neg_img)+ "\n")
txtfile.close()
# condition if clause


images = []

if condition == 11:
    print('Group 1, PN')
    images = pos_img


elif condition == 12:
    print('Group 1, NP')
else:
    print('this is not a valid condition group')

# THIS in positive & negative block:

# for the "observe" routine:
# current_file = pos_img.pop() # get the next value
# thisExp.addData('current_file', current_file) # record it in the data



# write the image names to a text file details_subj*.txt

# PRINTING

# print('positive images: ')
# print(pos_img)
# print('negative images:')
# print(neg_img)

# txtfile.close()
