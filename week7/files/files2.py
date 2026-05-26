
def create_grades_file(filename):
    students = [
     ("Dan", [85, 90, 78]),
     ("MOMO", [92, 88, 95]),
     ("Yoni", [70, 65, 80]),
     ("Avi", [100, 95, 98]),
     ("Sara", [60, 72, 68]),
    ]
    with open("grades.txt", "w", encoding="utf-8")as g:
        for tp in students:
            g.write(f"{tp[0]},")
            for grade in tp[1]:
                g.write(f"{grade},")
            g.write("\n")


def calculate_averages(filename):
    dicti={}
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            line=line.split(",")
            name=line[0]
            avg=0
            div=0
            for item in line:
                try:
                    avg+=int(item)
                    div+=1
                except TypeError, ValueError:
                    continue
            dicti[name]=avg/div
    return dicti



def save_results(averages, output_filename):

    averages=dict(sorted(averages.items(), key=lambda item: item[1], reverse=True))
    with open(output_filename, "w", encoding="utf-8") as of:
        of.write("=== Student Results ===\n")
        i = 1
        for  k, v in averages.items():
            of.write(f'{i}. {k}: {v:.1f}\n')
            i+=1

    return None

def add_results(filename, averages):
    avg=sum(averages.values()) / len(averages)
    maxi=None
    mini=None
    counter=0
    for k, v in averages.items():
        if v==max(averages.values()):
            maxi=(k, v)
        if v == min(averages.values()):
            mini=(k, v)
        if v >= 60:
            counter += 1
    with open(filename, "a", encoding="utf-8")as of:
        of.write(f"=== Statistics ===\n")
        of.write(f"Class average: {avg:.1f}\n")
        of.write(f"Highest: {maxi[0]} ({maxi[1]:.1f})\n")
        of.write(f"Lowest: {mini[0]} ({mini[1]:.1f})\n")
        of.write(f"Passing  (>=60) : {counter}/{len(averages)}\n")
    return None
