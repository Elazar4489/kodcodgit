# פונקציה :1
import os.path


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
    if os.path.exists(filename):
        with open(filename, "r+", encoding="utf-8")as file:
            last_line=str(int(file.readlines()[-1].split("|")[0])+1)
            file.write(f"{last_line}|PENDING|{description}\n")
    else:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"1|PENDING|{description}\n")

    return None



# פונקציה :4

def complete_task(filename, task_id):
    """
    DONE-ל PENDING-מ id_task של משימה status משנה את
    לא קיים — מדפיסה הודעת שגיאה ID-אם ה
    """
    lines=[]
    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            lines.append(line)
    is_task_id = None
    for i in range(len(lines)):
        line=lines[i].split("|")
        if str(task_id) == line[0]:
            line[1]="DONE"
            lines[i]=str("|".join(line))
            is_task_id=True
    if not is_task_id:
        print("task id not found")
        return None
    with open(filename, "w",encoding="utf-8") as file:
        for line in lines:
            file.write(line)
    print("the status changed")
    return None


# פונקציה :5

def list_tasks(filename):
    """
    :מציגה את כל המשימות בפורמט מסודר
    ]✓[ 2 [ 2 |לכת תרתרג 1
    ] [ 3 | לסיים את הפרויקט
    """

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            list_line=line.split("|")
            if list_line[1]=="PENDING":
                print(f"[ ] {list_line[0]} | {list_line[2]}")
            elif list_line[1]=="DONE":
                print(f"[✓] {list_line[0]} | {list_line[2]}")

    return None





def main():
    FILENAME="tasks.txt"
    flag=True
    while flag:
        try:
            print("\n=== To-Do List Manager ===")
            print("1. show tasks")
            print("2. add task")
            print("3. mark complete")
            print("4. exit")
            choice=input("choice: ")
            if choice == "1":
                list_tasks(FILENAME)
            elif choice =="2":
                desc=input("task description: ")
                add_task(FILENAME,desc)
                print("the task added")
            elif choice == "3":
                try:
                    task_id=int(input("task id: "))
                    complete_task(FILENAME,task_id)
                except ValueError:
                    print("invalid input")
                    continue
            elif choice == "4":
                print("good bye")
                flag = False
            else:
                print("invalid choice")
        except FileNotFoundError:
            print("FileNotFoundError")

if __name__ == "__main__":
    main()

