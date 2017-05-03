#  ######   #######  ##        #######  ########  #### ########     ###    
# ##    ## ##     ## ##       ##     ## ##     ##  ##  ##     ##   ## ##   
# ##       ##     ## ##       ##     ## ##     ##  ##  ##     ##  ##   ##  
# ##       ##     ## ##       ##     ## ########   ##  ##     ## ##     ## 
# ##       ##     ## ##       ##     ## ##   ##    ##  ##     ## ######### 
# ##    ## ##     ## ##       ##     ## ##    ##   ##  ##     ## ##     ## 
#  ######   #######  ########  #######  ##     ## #### ########  ##     ## 

import idaapi
 
#**********
#INIT STUFF
#*********
heads = Heads(0, 0xFFFFFFFF)
funcCalls = []
antiVM = []
xor = []
 
#******************
#PROCESS instrcutions
#******************
for i in heads:
#check if its a call
 if GetMnem(i) == "call":
  funcCalls.append(i)
 
# check if its anti vm also added some potential anti debugging stuff
 if (GetMnem(i) == "sidt" or GetMnem(i) == "rdtsc" or GetMnem(i) == "sgdt" or GetMnem(i) == "sldt" or GetMnem(i) == "smsw" or GetMnem(i) == "str" or GetMnem(i) == "in" or GetMnem(i) == "cpuid"):
  antiVM.append(i)
 
#check non zeroing xors  
 if GetMnem(i) == "xor":
  if (GetOpnd(i,0) != GetOpnd(i,1)):
   xor.append(i)
     
#****************
#COLOR and PRINT
#****************
print "Number of calls: %d" % (len(funcCalls))
for i in funcCalls:
 SetColor(i, CIC_ITEM, 0x005000) #green
 
print "Number of potential Anti-VM instructions: %d" % (len(antiVM))
for i in antiVM:
 print "Anti-VM potential at %x" % i
 SetColor(i, CIC_ITEM, 0x0000ff) #red
 
print "Number of xor: %d" % (len(xor))
for i in xor:
 SetColor(i, CIC_ITEM, 0x00a5ff) #orange
