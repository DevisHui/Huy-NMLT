# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 14:23:58 2024

@author: Chi
"""

a = float(input("Nhập giá trị của a:"))
b = float(input("Nhập giá trị của b:"))
if a != 0:
    x = b/a
    print("Nghiệm của phương trình x là:", x)
else:
    if b == 0 :
       print("Phương trình có vô số nghiệm.")
    else:
        print("Phương trình vô nghiệm.")