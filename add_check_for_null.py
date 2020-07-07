import os


def add_all(path):
    g = os.walk(path)
    for root, dirs, files in g:
        for file in files:
            if root.find("domain") > 0:
                addcheckForNull(root+"\\"+file)
        for dir in dirs:
            add_all(dir)


def addcheckForNull(file_name):
    print(file_name)
    f = open(file_name, 'rb')
    #f = open(file_name, 'r')
    result = ""
    is_import = False
    for lineByte in f.readlines():
        line=str(lineByte, encoding = "UTF-8")
        if not is_import and line.lstrip().startswith("import"):
            new_line = line + "import javax.annotation.CheckForNull;\n"
            result += new_line
            is_import = True
            continue
        if line.lstrip().startswith("private"):
            new_line = "    @CheckForNull\n" + line;
            result += new_line
        else:
            result += line
    f.close()
    f = open(file_name, 'wb+')
    f.write(result.encode(encoding="utf-8"))
    f.close()


if __name__ == '__main__':
    add_all("D:\server")
    addcheckForNull("TestUser.java")
