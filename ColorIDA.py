#                                                                                                                                                   
#                                                                                                                                                   
#        CCCCCCCCCCCCC                 lllllll                                           IIIIIIIIIIDDDDDDDDDDDDD                  AAA               
#     CCC::::::::::::C                 l:::::l                                           I::::::::ID::::::::::::DDD              A:::A              
#   CC:::::::::::::::C                 l:::::l                                           I::::::::ID:::::::::::::::DD           A:::::A             
#  C:::::CCCCCCCC::::C                 l:::::l                                           II::::::IIDDD:::::DDDDD:::::D         A:::::::A            
# C:::::C       CCCCCC   ooooooooooo    l::::l    ooooooooooo   rrrrr   rrrrrrrrr          I::::I    D:::::D    D:::::D       A:::::::::A           
#C:::::C               oo:::::::::::oo  l::::l  oo:::::::::::oo r::::rrr:::::::::r         I::::I    D:::::D     D:::::D     A:::::A:::::A          
#C:::::C              o:::::::::::::::o l::::l o:::::::::::::::or:::::::::::::::::r        I::::I    D:::::D     D:::::D    A:::::A A:::::A         
#C:::::C              o:::::ooooo:::::o l::::l o:::::ooooo:::::orr::::::rrrrr::::::r       I::::I    D:::::D     D:::::D   A:::::A   A:::::A        
#C:::::C              o::::o     o::::o l::::l o::::o     o::::o r:::::r     r:::::r       I::::I    D:::::D     D:::::D  A:::::A     A:::::A       
#C:::::C              o::::o     o::::o l::::l o::::o     o::::o r:::::r     rrrrrrr       I::::I    D:::::D     D:::::D A:::::AAAAAAAAA:::::A      
#C:::::C              o::::o     o::::o l::::l o::::o     o::::o r:::::r                   I::::I    D:::::D     D:::::DA:::::::::::::::::::::A     
# C:::::C       CCCCCCo::::o     o::::o l::::l o::::o     o::::o r:::::r                   I::::I    D:::::D    D:::::DA:::::AAAAAAAAAAAAA:::::A    
#  C:::::CCCCCCCC::::Co:::::ooooo:::::ol::::::lo:::::ooooo:::::o r:::::r                 II::::::IIDDD:::::DDDDD:::::DA:::::A             A:::::A   
#   CC:::::::::::::::Co:::::::::::::::ol::::::lo:::::::::::::::o r:::::r                 I::::::::ID:::::::::::::::DDA:::::A               A:::::A  
#     CCC::::::::::::C oo:::::::::::oo l::::::l oo:::::::::::oo  r:::::r                 I::::::::ID::::::::::::DDD A:::::A                 A:::::A 
#        CCCCCCCCCCCCC   ooooooooooo   llllllll   ooooooooooo    rrrrrrr                 IIIIIIIIIIDDDDDDDDDDDDD   AAAAAAA                   AAAAAAA 

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
