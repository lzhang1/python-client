import os
def runTest(dPath):
    for f in os.listdir(dPath):
        fPath = os.path.join(dPath, f)
        if os.path.isdir(fPath):
            os.listdir(fPath)
        else:
            if fPath.endswith('tests.py'):
                yield fPath
            else:
                continue

if __name__ == "__main__":
    dPath = os.path.abspath('test/functional/android/')
    for file in runTest(dPath):
        print(file)
