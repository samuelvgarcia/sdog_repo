col0, col1, col2 = [], [], []

fmt = "{:>10} {:<6}"
x = round(12 - len("column0")/2)
x = int(x/2)

#Column 0
col0.append("  " + "{:}".format( x*"_" +"Column0" + x*"_"))
col0.append(fmt.format("blah:", 124) )
col0.append(fmt.format("this:", 1024))

#Column 1
col1.append(" "+"{:}".format(x*"_" + "Column1" + x*"_"))
col1.append(fmt.format("Hello:", 4389 ))
col1.append(fmt.format("world:", 19 ))

#Column 2
col2.append("  "+"{:}".format(x*"_" + "Column2" + x*"_"))
col2.append(fmt.format("whatever:", 7311))
col2.append(fmt.format(   "sucks:", 10714))

for k in range(len(col0)):
    print(col0[k], col1[k], col2[k])