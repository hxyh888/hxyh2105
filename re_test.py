import re

name_list = ["name","!admin","name?","de#mo","1name","na1n","_name"]
for i in name_list:
    result = re.match("^[A-Za-z_][A-Za-z_0-9]{%d}[A-Za-z_0-9]$"%(len(i)-2),i)
    if result:	
        print("%sfuheguize"%result.group())
    else:
        print("%sbufuheguize"%i)


