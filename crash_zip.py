# -*- coding: utf-8 -*-
import zipfile

def getPw(filename,dictFile):
    password = open(dictFile, 'r')
    for p in password:
        zf = zipfile.ZipFile(filename)
        p = p.strip('\n')
        try:
            zf.extractall("./sample", pwd=p)
            print "crash. Password is %s" % p
            exit(0)
        except:
            pass

if __name__ == '__main__':
    # filename：需要解压的文件；dictFile：字典
    filename="sample.zip"
    dictFile="pwdict.txt"
    getPw(filename, dictFile)



