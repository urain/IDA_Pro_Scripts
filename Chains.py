#  _____  _   _   ___  _____ _   _  _____ 
# /  __ \| | | | / _ \|_   _| \ | |/  ___|
# | /  \/| |_| |/ /_\ \ | | |  \| |\ `--. 
# | |    |  _  ||  _  | | | | . ` | `--. \
# | \__/\| | | || | | |_| |_| |\  |/\__/ /
#  \____/\_| |_/\_| |_/\___/\_| \_/\____/ 
#
# Chains will find all Xrefs to the current function where your cursor is located. It will continue to find
# Xrefs to those Xrefs until it cannot find any more Refs (that's a lot of refs.) This will then order them
# in ascending order, color the opcode refs red, and display the subfunction/opcode in the output window. 
# This will allow you to follow the rabbit hole from the beginning of the EXE or DLL to the location you are 
# interested in.

import idaapi

print "\n\n\n"
z = ScreenEA()
print("Starting Chain: \n%s\t%x\t%s %s\n\n"%(GetFunctionName(z),z,GetMnem(z),GetOpnd(z,0)))
opChain   = []
funcChain = []

# add our initial xrefs to our target func
for xref in XrefsTo(idaapi.get_func(ScreenEA()).startEA):
    opChain.append(xref.frm)
    
# for func/opcode that ref'd our target, find refs to it
for i in opChain:
    try:
        for y in XrefsTo(idaapi.get_func(i).startEA):
            if y.frm not in opChain:
                opChain.append(y.frm)
    except:
        continue
# sort ascending
chainSorted = sorted(opChain)

# output to the window
for i in chainSorted:
    SetColor(i, CIC_ITEM, 0x2020c0)
    print("%s\t%x\t%s %s"%(GetFunctionName(i),i,GetMnem(i),GetOpnd(i,0)))
