import os


with open("diary.txt", "w", encoding="utf-8") as di:
    di.write("2024-01-15: was plenty day in project today\n"
             "2024-01-16: I studied about file handling in python\n"
             "2024-01-17: I fixed the first exs")
print("the dictionary created successfully")
with open("diary.txt", "r", encoding="utf-8") as di:
    print(di.read())

def add_entry(filename, date, content):
    with open(filename, "a", encoding="utf-8")as f:
        f.write(f"{date}: {content}")


def search_diary(filename, keyword):
    if safe_read_diary(filename):

        list_of_lines=[]
        with open(filename,"r",encoding="utf-8")as f:
            for line in f:
                if keyword in line.split(" "):
                    list_of_lines.append(line)
        return list_of_lines
    return "File Not Found!"

def safe_read_diary(filename):
    if os.path.exists(filename):
        return True
    return False
