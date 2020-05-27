# priming-session
priming session python script for Sleep and Dream Study Project at Universität Osnabrück, 2020

Author: Marketa Becevova

## input
#### based on the randomization.csv file including all subject numbers and randomized block orders etc.
- subject number (two ciphers)
- group - 1, 2 or 3
- order - order in which positive / negative image block is displayed. Enter in the following format: 'A,B' or 'B,A' (without the quotes, no space after comma)
\n  A = block of positive images
\n  B = block of negative images
\n  C = block of neutral images

## output

#### all subject overview file
  - can be found in priming-session/all_participant_summary.csv
  - includes subject number, group number and the block order

#### detailed individual subject .csv file
  - can be found in priming-session/data
  - includes subject number, group number, block order, order of the images within each block, etc.

#### psydata file
  - can be found in priming-session/data
  - includes experiment information


## folder organisation structure
- priming-session:
  - priming.psyexp = main experimental file. Opens priming session in psychopy environment
  - priming.py = python code of the priming session. Run through writing the following in the cmd and pressing enter after each line
      cd /d <path to the priming-session folder>
      python priming.py
  - all_participant_summary.csv = overview of all subject data, see description above in 'output'
- priming-session/data: for each participant/session there is a .csv and .psydat file
- priming-session/experiment: contains all condition files
- priming-session/stimuli: contains all priming pictures divided into folders (positive, negative, neutral)


### Created using Psychopy
Peirce, J. W., Gray, J. R., Simpson, S., MacAskill, M. R., Höchenberger, R., Sogo, H., Kastman, E., Lindeløv, J. (2019). PsychoPy2: experiments in behavior made easy. Behavior Research Methods. 10.3758/s13428-018-01193-y
