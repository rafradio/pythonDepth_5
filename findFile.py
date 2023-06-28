def parsePath(pathFull: str) -> tuple:
    absPath = pathFull.split('\\')
    fileDir = list(filter(lambda x: '.' in x, absPath))[0]
    fileName, extension = fileDir.split('.')
    pathVar = "/".join(filter(lambda x: x != fileDir, absPath))
    return (pathVar, fileName, extension)


if __name__ == '__main__':
    print(parsePath(str(__file__)))