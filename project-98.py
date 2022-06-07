def swapFiles() :
    file1name = input("write the name of the first file to swap contents ")
    file2name = input("write the name of the second file to swap contents ")

    a=open(file1name,"r")
    b=open(file2name,"r")

    data_a = a.read()
    data_b =b.read()

    a=open(file1name,"w")
    b=open(file2name,"w")

    a.write(data_b)
    b.write(data_a)

swapFiles()