import sys
import os
import threading


PATH = sys.argv[1]

total_count = 0
html_count = 0
css_count = 0
js_count = 0
python_count = 0
csharp_count = 0
cpp_count = 0
c_count = 0
java_count = 0
plain_count = 0

accepted_formats = ["html", "css", "js", "py", "pyw", "cs", "cpp", "c", "java", "txt"]


try:
    print("")
    os.stat(PATH)
except FileNotFoundError as e:
    print("Not valid path:", PATH)
    sys.exit()


list_of_files = []

for root, dirs, filenames in os.walk(PATH):
    list_of_files.extend(filenames)

print(list_of_files)


def readFiles(filename, extension):
    count = 0
    global total_count
    global html_count
    global css_count
    global js_count
    global python_count
    global csharp_count
    global cpp_count
    global c_count
    global java_count
    global plain_count
    extension = extension.lower()
    if extension in accepted_formats:
        if extension == accepted_formats[0]:
            with open(PATH+"/"+filename+"."+extension, "r")as f:
                f = f.read()
                for i in f:
                    html_count = html_count + 1
                    count = count + 1
        if extension == accepted_formats[1]:
            with open(PATH+"/"+filename+"."+extension, "r")as f:
                f = f.read()
                for i in f:
                    css_count = css_count + 1
                    count = count + 1
        if extension == accepted_formats[2]:
            with open(PATH+"/"+filename+"."+extension, "r")as f:
                f = f.read()
                for i in f:
                    js_count = js_count + 1
                    count = count + 1
        if extension == accepted_formats[3] or extension == accepted_formats[4]:
            with open(PATH+"/"+filename+"."+extension, "r")as f:
                f = f.read()
                for i in f:
                    python_count = python_count + 1
                    count = count + 1
        if extension == accepted_formats[5]:
            with open(PATH+"/"+filename+"."+extension, "r")as f:
                f = f.read()
                for i in f:
                    csharp_count = csharp_count + 1
                    count = count + 1
        if extension == accepted_formats[6]:
            with open(PATH+"/"+filename+"."+extension, "r")as f:
                f = f.read()
                for i in f:
                    cpp_count = cpp_count + 1
                    count = count + 1
        if extension == accepted_formats[7]:
            with open(PATH+"/"+filename+"."+extension, "r")as f:
                f = f.read()
                for i in f:
                    c_count = c_count + 1
                    count = count + 1
        if extension == accepted_formats[8]:
            with open(PATH+"/"+filename+"."+extension, "r")as f:
                f = f.read()
                for i in f:
                    java_count = java_count + 1
                    count = count + 1
        if extension == accepted_formats[9]:
            with open(PATH+"/"+filename+"."+extension, "r")as f:
                f = f.read()
                for i in f:
                    plain_count = plain_count + 1
                    count = count + 1
    else:
        print("")
        print(f"file format not support: {filename}.{extension}")
    total_count += count

for files in list_of_files:
    file_extension = files.rsplit(".", 1)[1]
    filename = files.rsplit(".", 1)[0]
    readFiles(filename, file_extension)
    pass


def calc(x, y):
    return round(x / y * 100, 2)

print("")
print(f"HTML: {html_count}------------- {calc(html_count, total_count)}%")
print(f"CSS: {css_count}---------------- {calc(css_count, total_count)}%")
print(f"JavaScript {js_count}---------- {calc(js_count, total_count)}%")
print(f"Python: {python_count}------------- {calc(python_count, total_count)}%")
print(f"C#: {csharp_count}----------------- {calc(csharp_count, total_count)}%")
print(f"C++: {cpp_count}---------------- {calc(cpp_count, total_count)}%")
print(f"C: {c_count}------------------ {calc(c_count, total_count)}%")
print(f"Java: {java_count}--------------- {calc(java_count, total_count)}%")
print(f"Plain: {plain_count}-------------- {calc(plain_count, total_count)}%")
print("Total count", total_count)