
# 1
count=0
def dump():
    global count
    count+=1
def value():
    global count
    return count

# 2

def make_counter():
    n=0
    def counter():
        nonlocal n
        n+=1
        return n
    return counter

# 3
"""
x = 10
def f():
    x = 20
    print(x)
f()
print(x)

הקוד הבא ידפיס קודם 20 ואחר כך 10
למה?
כי פייתון קורא את הקוד בצורה של קודם מה שהכי קרוב אלי במודל LEGB
 
"""
# 4

# זה מעלה שגיאת  TypeError כי שיניתי את המשתנה ה - build in של הגדרת וקאסטינג של רשימה למשהו אחר
# הקוד המתוקן
# list1 = [1, 2, 3]
# print(list(range(5)))

# 5
def print_from_imports():
    import mathutils

    print(mathutils.square(5))
    print(mathutils.cube(3))

    from mathutils import square, cube

    print(square(5))
    print(cube(3))

# 6

# 7

from datetime import datetime as dt; print(dt.now())

# 8
import math

def public_names(m):
    return [item for item in dir(m) if not item.startswith("_")]

# 9

def add_item(item, bag=[]):
    bag.append(item)
    return bag
"""
הבאג המרכזי הוא הגדרת רשימה והשמתה בתוך שדות הארגיומנטים ולכן אם נריץ אותה פעמיים עם שני פריטים שונים, בפעם השניה היא תדפיס גם את הפריט הראשון כי רשימה היא ברת שינויי והמידע נשמר בדאטה של הפונקצייה
קלט:
print(add_item(1))
print(add_item(2))
print(add_item(3))
פלט: 
[1]
[1, 2]
[1, 2, 3]
"""
# תיקון

def add_item_better(item, bag=None):
    if bag is None:
        bag=[]
    bag.append(item)
    return bag


"""
כעת שלא מוגדרת רשימה בתוך השדהת הפונקצייה יוצרת כל פעם רשימה חדשה שלא קשורה למה שנוצר בפעמים הקודמות
קלט:
print(add_item_better(1))
print(add_item_better(2))
print(add_item_better(3))
פלט: 
[1]
[2]
[3]
"""

# 10

import geometry.circle

import geometry.rectangle

print(geometry.circle.area(5))
print(geometry.rectangle.area(4,6))






