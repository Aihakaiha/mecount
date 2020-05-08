from pathlib import Path
import sys
import os
import threading
import subprocess
from win10toast import ToastNotifier


PATH = sys.argv[1]

toast = ToastNotifier()

total_count = 0
total_lines = 0
html_count = 0
html_lines = 0
css_count = 0
css_lines = 0
js_count = 0
js_lines = 0
python_count = 0
python_lines = 0
csharp_count = 0
csharp_lines = 0
cpp_count = 0
cpp_lines = 0
c_count = 0
c_lines = 0
java_count = 0
java_lines = 0
batch_count = 0
batch_lines = 0
plain_count = 0
plain_lines = 0

accepted_formats = ["html", "htm", "css", "js", "py", "pyw", "cs", "cpp", "c", "java", "txt", "bat"]


try:
    print("")
    os.stat(PATH)
except FileNotFoundError as e:
    print("Not valid path:", PATH)
    sys.exit()



list_of_files = []
for item in os.listdir(PATH):
    if os.path.isfile(os.path.join(PATH, item)):
        list_object = PATH+"/"+item
        print(list_object)
        list_of_files.append(list_object)
    else:
        for items in os.listdir(PATH+"/"+item):
            if os.path.isfile(os.path.join(PATH+"/"+item, items)):
                list_object = PATH+"/"+item+"/"+items
                print(list_object)
                list_of_files.append(list_object)
            else:
                for more_items in os.listdir(PATH+"/"+item+"/"+items):
                    if os.path.isfile(os.path.join(PATH+"/"+item+"/"+items, more_items)):
                        print(more_items)
                        list_object = PATH+"/"+item+"/"+items+"/"+more_items
                        print(list_object)
                        list_of_files.append(list_object)
                    else:
                        for even_more_items in os.listdir(PATH+"/"+item+"/"+items+"/"+more_items):
                            if os.path.isfile(os.path.join(PATH+"/"+item+"/"+items+"/"+more_items, even_more_items)):
                                list_object = PATH+"/"+item+"/"+items+"/"+more_items+"/"+even_more_items
                                list_of_files.append(list_object)
                            else:
                                for alot_more_items in os.listdir((PATH+"/"+item+"/"+items+"/"+more_items+"/"+even_more_items)):
                                    if os.path.isfile(os.path.join(PATH+"/"+item+"/"+items+"/"+more_items+"/"+even_more_items, alot_more_items)):
                                        list_object = PATH+"/"+item+"/"+items+"/"+more_items+"/"+even_more_items+"/"+alot_more_items
                                        print(list_object)
                                        list_of_files.append(list_object)


print(list_of_files)




def readFiles(file, extension):
    count = 0
    global total_count
    global total_lines
    global html_count
    global html_lines
    global css_count
    global css_lines
    global js_count
    global js_lines
    global python_count
    global python_lines
    global csharp_count
    global csharp_lines
    global css_lines
    global cpp_count
    global cpp_lines
    global c_count
    global c_lines
    global java_count
    global java_lines
    global batch_count
    global batch_lines
    global plain_count
    global plain_lines
    extension = extension.lower()
    if extension in accepted_formats:
        if extension == accepted_formats[0] or extension == accepted_formats[1]:
            with open(file, "r")as f:
                f = f.read()
                html_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())
                
                for _ in f:
                    html_count = html_count + 1
                    count = count + 1
        if extension == accepted_formats[2]:
            with open(file, "r")as f:
                f = f.read()
                css_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())

                for _ in f:
                    css_count = css_count + 1
                    count = count + 1
        if extension == accepted_formats[3]:
            with open(file, "r")as f:
                f = f.read()
                js_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())

                for _ in f:
                    js_count = js_count + 1
                    count = count + 1
        if extension == accepted_formats[4] or extension == accepted_formats[5]:
            with open(file, "r")as f:
                f = f.read()
                python_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())

                for _ in f:
                    python_count = python_count + 1
                    count = count + 1
        if extension == accepted_formats[6]:
            with open(file, "r")as f:
                f = f.read()
                csharp_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())

                for _ in f:
                    csharp_count = csharp_count + 1
                    count = count + 1
        if extension == accepted_formats[7]:
            with open(file, "r")as f:
                f = f.read()
                cpp_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())

                for _ in f:
                    cpp_count = cpp_count + 1
                    count = count + 1
        if extension == accepted_formats[8]:
            with open(file, "r")as f:
                f = f.read()
                c_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())

                for _ in f:
                    c_count = c_count + 1
                    count = count + 1
        if extension == accepted_formats[9]:
            with open(file, "r")as f:
                f = f.read()
                java_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())

                for _ in f:
                    java_count = java_count + 1
                    count = count + 1
        if extension == accepted_formats[10]:
            with open(file, "r")as f:
                f = f.read()
                plain_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())

                for _ in f:
                    plain_count = plain_count + 1
                    count = count + 1
        if extension == accepted_formats[11]:
            with open(file, "r") as f:
                f = f.read()
                batch_lines += len(open(file).read().splitlines())
                total_lines += len(open(file).read().splitlines())

                for _ in f:
                    batch_count = batch_count + 1
                    count = count + 1
    else:
        print("")
        print(f"file format not support: {file}")
    total_count += count

for files in list_of_files:

    if "." in files:
        file_extension = files.rsplit(".", 1)[1]
        #
        readFiles(files, file_extension)
        pass
    else:
        pass

def calc(x, y):
    return round(x / y * 100, 2)

print("")
if html_count != 0 and html_lines != 0:
    print(f"HTML: {html_count}------------- {calc(html_count, total_count)}% --- Lines: {html_lines}")
if css_count != 0 and css_lines != 0:
    print(f"CSS: {css_count}---------------- {calc(css_count, total_count)}% --- Lines: {css_lines}")
if js_count != 0 and js_lines != 0:
    print(f"JavaScript {js_count}---------- {calc(js_count, total_count)}% --- Lines: {js_lines}")
if python_count != 0 and python_lines != 0:
    print(f"Python: {python_count}------------- {calc(python_count, total_count)}% --- Lines: {python_lines}")
if csharp_count != 0 and csharp_lines != 0:
    print(f"C#: {csharp_count}----------------- {calc(csharp_count, total_count)}% --- Lines: {csharp_lines}")
if cpp_count != 0 and cpp_lines != 0:
    print(f"C++: {cpp_count}---------------- {calc(cpp_count, total_count)}% --- Lines: {cpp_lines}")
if c_count != 0 and c_lines != 0:
    print(f"C: {c_count}------------------ {calc(c_count, total_count)}% --- Lines: {c_lines}")
if java_count != 0 and java_lines != 0:
    print(f"Java: {java_count}--------------- {calc(java_count, total_count)}% --- Lines: {java_lines}")
if batch_count != 0 and batch_lines != 0:
    print(f"Batch: {batch_count}--------------- {calc(batch_count, total_count)}% --- Lines: {batch_lines}")
if plain_count != 0 and plain_lines != 0:
    print(f"Plain: {plain_count}-------------- {calc(plain_count, total_count)}% --- Lines: {plain_lines}")
print("Total count", total_count, "  Total lines", total_lines)
toast.show_toast("Read complete!", f"Read complete at {PATH}    Count: {total_count} LOC: {total_lines}", duration=3)
sys.exit()