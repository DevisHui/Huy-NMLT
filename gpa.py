# -*- coding: utf-8 -*-
"""
Created on Sat Aug 17 13:40:27 2024

@author: Chi
"""
gpa = float(input("Nhập điểm trung bình của bạn:"))
if gpa < 3.5:
    print("Học lực kém")
elif 3.5 <= gpa < 5.0:
    print("Học lực yếu")
elif 5.0 <= gpa < 7.0:
    print("Học lực trung bình")
elif 7.0 <= gpa < 8.0:
    print("Học lực khá")
elif 8.0 <= gpa < 9.0:
    print("Học lực giỏi")
elif 9.0 <= gpa <= 10:
    print("Học lực giỏi")
else: 
    print("Không xác định")