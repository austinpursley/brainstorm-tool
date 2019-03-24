"""
    Filename: brainstorm.py
    Author: Austin Pursley
    Created: 9/9/2018
    Edited: 3/24/2019
    Python Version 2.7
"""

import random
import datetime
import time

def brainstorm(subject_list=[], max_subjects=5, minutes=3.0, file_name='brainstorm.txt'):
    """
    Crativiety tool, record as mnany ideas as you can given random ideas from list.
    
    Keyword arguments:
    subject_list -- list of ideas to randomly sample from
    max_subjects -- maximum number of random ideas to brainstorm from
    minutes -- how many minutes to brainstorm with.
    file_name -- name of the file where brainstormed ideas going to be recorded
    
    """
    
    # get number of randomly chosen ideas from idea list
    num_subjects = raw_input("How many random subjects? (max: " + str(max_subjects) + ")")
    while True:
        try:
            int(num_subjects)
        except ValueError:
            print("needs to be a number should be between 1 and " + str(max_subjects))
            num_subjects = raw_input("How many random subjects?")
        else:
            num_subjects = int(num_subjects)
            if (num_subjects <= max_subjects) and (num_subjects > 0):
                break
            else:
                print("number should be between 1 and " + str(max_subjects))
                num_subjects = raw_input("How many random subjects?")
    # get the random sample of ideas from list and output them for user
    rand_samp = random.sample(subject_list, num_subjects)
    print("\nYour subjects are: ")
    sub_str = ""
    for sub in rand_samp:
        print(sub)
        sub_str += ("_" + sub.replace(" ", ""))
    # get a chance to review the ideas
    raw_input('\nReview these ideas if needed, then press enter to continue\n')
    # write ideas to file
    f= open(file_name,"a")
    ts = time.time()
    date = datetime.datetime.fromtimestamp(ts).strftime('%Y.%m.%d')
    f.write("Date: " + date + "\n")
    f.write("Subjects: ")
    for idea in rand_samp:
         f.write(idea + ", ")
    f.write('\nIdeas:\n')
    # enter as many ideas as possible in time given/entered
    t_end = time.time() + 60 * minutes
    while time.time() < t_end:
        idea = raw_input("Input an idea: \n")
        st = datetime.datetime.fromtimestamp(time.time()).strftime('%H:%M:%S ')
        f.write(st + idea + '\n')
    f.write('\n')
    f.close()
    return()

