#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 00:37:39 2021

@author: hotsonhor
"""

'''
Name: Iran Grade Transfer to 4.33 & 4 GPA
'''
import time

'''
Show massages to user.
'''
m1 = 'Hello to Iran 🇮🇷 Grade Transfer to 4.33 & 4 Program. '
m1_list = m1.split()
for i in range(len(m1_list)):
    print('', m1_list[i], end='')
    time.sleep(0.3)
    
time.sleep(0.7)

print('\n')
m2 = 'Created by HotsonHor . . . . . . . . . . . .'
m2_list = m2.split()
for i in range(len(m2_list)):
    if m2_list[i] == 'HotsonHor':
        print(' \033[1;3;33mHotsonHor\033[m', end='')
        continue
    print('', m2_list[i], end='')
    time.sleep(0.3)

print(' .')
time.sleep(0.75)


print('\n')
m3 = '  for helping Iranian Student. 😊 '
m3_list = m3.split()
for i in range(len(m3_list)):
    print('', m3_list[i], end='')
    time.sleep(0.3)

'''
End to show massages to user.
'''

'''
Variables 
'''
Iran_Grade = 0

def four():
    print('You choose 4 scale GPA')
    Iran_Grade = 0
    while Iran_Grade != 'done':
        Iran_Grade = input('Please type your Iran Curse Grade: ')
        if Iran_Grade.isalpha() == False:
            if float(Iran_Grade) >= 16:
                GPA_four_scale = float(4)
            elif float(Iran_Grade) <= 9.99:
                GPA_four_scale = float(0)
            else:
                GPA_four_scale = (float(Iran_Grade) /2 - 4)
            print(GPA_four_scale)
        elif Iran_Grade == 'done':
           break
        
        else:
            print("\nPlease enter your Grade or done.")
            continue
       
    
def four_33():
    print('You choose 4.33 scale GPA')
    Iran_Grade = 0
    while Iran_Grade != 'done':
        Iran_Grade = input('Please type your Iran Curse Grade: ')
        if Iran_Grade.isalpha() == False:
            if float(Iran_Grade) >= 18:
                GPA_four_33_scale = float(4.33)
            else:
                GPA_four_33_scale = round(((float(Iran_Grade) * 5 - 55) * 2.33 / 35 + 2), 2)
            print(GPA_four_33_scale)
        elif Iran_Grade == 'done':
           break
        
        else:
            print("\nPlease enter your Grade or done.")
            continue
        

def main():
    Kind_of_GPA = input('\nPlease choose GPA scale: \n\n1. \033[1;32m4.33\033[m \n2. \033[1;34m4\033[m \n\n(Only type "1" or "2" and click enter): ')

    if int(Kind_of_GPA) == 2:
        four()
        
    else:
        four_33()
    

main()    



print('Dedicated to My Love: Elham ❤️ (Latin: Dicata Elham ❤️ )')
    

    

    













