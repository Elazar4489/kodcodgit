# פונקציה :1

def load_tasks(filename):
    """
    :dicts קוראת את הקובץ ומחזירה רשימה של
    [{'id': 1, 'status': 'PENDING', 'desc': 'ללמוד Python'}, ...]
    אם הקובץ לא קיים — מחזירה רשימה ריקה
    """
    list_of_dicts=[]
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line=line.split("|")
                dicti={"id": line[0], "status": line[1], "desc": line[2]}
                list_of_dicts.append(dicti)
        return list_of_dicts
    except FileNotFoundError:
        return list_of_dicts




# פונקציה :2

def save_tasks(filename, tasks: list[dict]):
    """
    שומרת את רשימת המשימות לקובץ
    description|status|id :פורמט כל שורה
    """
    with open(filename, "w", encoding="utf-8") as file:
        for dicti in tasks:
            for val in dicti.values():
                file.write(f"{val}|")
            file.write("\n")
    return None



# פונקציה :3

def add_task(filename, description):
    """
    :מוסיפה משימה חדשה עם
    מספר המשימה הבאה = ID -
    - status = 'PENDING'
    הפרמטר שניתן = description -
    """
    with open(filename, "a", encoding="utf-8")as file:
        last_line=file.readlines()[-1].split("|")


    pass
# פונקציה :4

def complete_task(filename, task_id):
    '''
    DONE-ל PENDING-מ id_task של משימה status משנה את
    לא קיים — מדפיסה הודעת שגיאה ID-אם ה
    '''
    pass
# פונקציה :5

def list_tasks(filename):
    '''
    :מציגה את כל המשימות בפורמט מסודר
    ]✓[ 2 [ 2 |לכת תרתרג 1
    ] [ 3 | לסיים את הפרויקט
    '''
    pass