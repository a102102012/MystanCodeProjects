"""
File: webcrawler.py
Name: 
--------------------------
This file collects more data from
https://www.ssa.gov/oact/babynames/decades/names2010s.html
https://www.ssa.gov/oact/babynames/decades/names2000s.html
https://www.ssa.gov/oact/babynames/decades/names1990s.html
Please print the number of top200 male and female on Console
You should see:
---------------------------
2010s
Male Number: 10890537
Female Number: 7939153
---------------------------
2000s
Male Number: 12975692
Female Number: 9207577
---------------------------
1990s
Male Number: 14145431
Female Number: 10644002
"""

import requests
from bs4 import BeautifulSoup


def main():
    for year in ['2010s', '2000s', '1990s']:
        print('---------------------------')
        print(year)
        url = 'https://www.ssa.gov/oact/babynames/decades/names' + year + '.html'

        response = requests.get(url)
        # print(response)
        html = response.text
        soup = BeautifulSoup(html, features="html.parser")
        # ----- Write your code below this line ----- #
        tags = soup.find_all('td')

        """
        Clean the list
        """
        lst = []
        for tag in tags:
            ele = tag.text.split(' ')
            for i in ele:
                if len(i) > 0:  # get rid of '' in first line
                    if not i.isalpha():  # get rid of name
                        lst += ele
        # print(lst)

        new_lst = []
        for i in range(len(lst)):
            # print(lst[i])
            new_char = ''
            for char in lst[i]:
                if char.isdigit():  # get rid of ',' from string the numbers
                    new_char += char
            new_lst.append(new_char)
        new_lst = new_lst[0:600]  # get rid of tail with useless info
        # print(new_lst)

        """
        The rule of the list is
        ['1', '183076', '194836', '2', '173797', '184355']
        ['rank', 'male_num', 'female_num']
        """
        male_number = 0
        female_number = 0
        for i in range(len(new_lst)):
            if i % 3 == 1:
                male_number += int(new_lst[i])
            elif i % 3 == 2:
                female_number += int(new_lst[i])

        print('male_number:', male_number)
        print('female_number:', female_number)


if __name__ == '__main__':
    main()
