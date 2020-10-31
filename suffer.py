#!/usr/bin/python
import os
import argparse

pog = """
{1}╔═{0}[You're invited to]{1}═══════{0}[x]{1}═╗\033[0m
{1}║                               {1}║\033[0m
{1}║   {0}  Suffer                   {1}║\033[0m
{1}║                      {0}[Join]{1}   ║\033[0m
{1}╚═══════════════════════════════╝\033[0m
"""

def translate(num : int):
    if num == 0:
        return ''
    if num == 1:
        return '\033[31m'
    if num == 2:
        return '\033[32m'
    if num == 3:
        return '\033[33m'
    if num == 4:
        return '\033[34m'
    if num == 5:
        return '\033[35m'
    if num == 6:
        return '\033[36m'
    if num == 7:
        return '\033[37m'
    if num > 7 :
        print("--color [1,2,3,4,5,6,7]")
        exit()

def main(color1, color2):
    print(pog.format(color1, color2))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="You're Invited to Suffer!")
    parser.add_argument('--color1', help="Text&Buttons Color [1,2,3,4,5,6,7]" ,type=int, default=3)
    parser.add_argument('--color2', help="Box Color [1,2,3,4,5,6,7]" ,type=int, default=1)
    args = parser.parse_args()

    color1trans = translate(num=args.color1)
    color2trans = translate(num=args.color2)

    main(color1=color1trans , color2=color2trans)
