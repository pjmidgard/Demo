from time import time
cvf=0
import os
import binascii
self="'"

namez = input("for compress c? ")
#@Author Jurijus pacalovas
class compression:

    def cryptograpy_compression(self):
                
                self.name = "Author: Jurijus pacalovas"
                
                if namez=="c":
                    corridors=0
                    cor=7
                    name = input("What is name of file? ")
                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit
                    Deep=100
                    Deep100=100
                        
                    namea="file.W"
                    namem=""
                    namema="?"
                    Portal=2
                    assxw=0
                    blockw=5
                    blockw1=4
                    nameas=name
                    nac=len(nameas)
           

                    nameas=name+".bin"
                
                    nac=len(nameas)
                    
                    countraz=0
                    cvf=2
                    cvf1=0
                    s=""
                    e2=0
                    e3=2
                    e4=""
                    c=2
                    sw=2
                    elw=0
                    sw1=0
                    sw2=0
                    sw3=0
                    sw5=0
                    sw4=0
                    sw6=0
                    sw7=0
                    n1=0
                    n=0
                    n2=0
                    n3=0
                 
                    sda3=""
                    sda2=""

                    sscvf=0
                    
                    qqqqwzl=0

                    block=1

                    x=0
                    x1=0
                    x2=0
                    x = time()

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                        if len(data)==0:
                            x4=0.0
                            print(x4)
                            raise SystemExit
                            
                      
                 
                       

                  
                        s=str(data)
                        
                     
                       
                        lenf1=len(data)
                        lenf5=len(data)
                        
                        assx=0
                        qqqwz=0
                       
                        while assx<10:
                       
                            aas1=0
                            a1=0

                            cvf=cvf+1
                            
                            countraz=countraz+1

                            with open(nameas, "ab") as f2:
                                if countraz==1:
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    sda=sda+sda2

                                    if countraz==1:
                                        sda2=sda
                            
                                    n = int(sda2, 2)
                                
                                    qqwslenf=len(sda2)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                    sssssw=len(jl)
                                    
                                    data=jl
                                    qqqwz=qqqwz+1
                                   
                                    if countraz==1:

                                        lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    xc=(lenf1*8)-lenf
                                    z=0
                                    if xc!=0:
                                        while z<xc:
                                            sda="0"+sda
                                            z=z+1

                                    sda2=sda

                                    lenf3=len(sda2)
                                lenf2=len(sda2)  
                                
                                sda3=sda2
                                long_file=len(sda3)
                                sda10=""
                                sda9=""
                                sda5=""
                                fda5=""
                                sda4=""
                                sda6=""
                                sda7=""
                                sda12=""
                                sda19=""
                                sda10=sda3
                                predict=-1
                                Where2=0
                                Where3=0
                                Deep101=0
                                
                                

                                cvf1=1
  
                                if cvf1==1:
                                    times_compression=0  
                                    compress_no=0
                                    compress_yes=0
                                    long2=len(sda3)
                                    Deep=long2//28
                                    times2=Deep
                                    Deep100=16
                                    
                                
                                    
                                    
                                    block_compression2=0
                                    
                                    start=-1
                                    Find_guess=0
                                    while Find_guess!=1:
                                        while  times_compression!=times2 and len(sda3)>=184+Deep100:


                                                    
                                                        

                                                    start=0
                                                    blocks=Deep100
                                                    size_compress=40
                                                    end=blocks
                                                    
                                                    find_matches1_number1=0
                                                    find_matches1_number2=0
                                                    find_matches1_number3=0   
                                                    
                                                    predict=predict+1
                                                    if predict==16:
                                                        predict=0
                                                    
                                                    
                                                                                                 
                                                                                                                                        
                
                                                    block=0
                                                    b=format(predict,'04b')
                                                    
                                                    Find=1
                                                    block_compression1=0
                                                    block_compression=0
                                                    block_compression2=0
                                                    long=len(sda3)
                                                    #print(long)
                                                    
                                                    while block<long:
                                                                                str_find_tree_maches=sda3[block:block+blocks]
                                                                                if b[0:2]=="01":
                                                                                                       b="10"+b[2:]
                                                                                                       
                                                        

                                                                                
                                                                                            
                                                                                
                                                                                sub2=b
                                                                                sub_info=b
                                                                                
                                                                    
                                                                                
                                                                                find_matches1=str_find_tree_maches.find(sub_info, start, end)
                                                                                find_matches1_1=int(find_matches1)

                                                                                if find_matches1_1==-1:
                                                                                    Find=0 
                                                                                
                                                                                if find_matches1_1!=-1:
                                                                                    
                                                                                    find_matches1_number1=int(find_matches1)
                                           
                                                                                    if find_matches1_1==0:

                                                                                        sda4=str_find_tree_maches[:0]+"01"+str_find_tree_maches[4:]
                                                                                        Where3=block+0
                                                                                        Where2=Where2+2
                                                                                        
                                                                                        
                                                                                        
                                                                                        


                                                                                    Where=0
                                                                                     
                                                                                    sub_info1="01"                                       
                                                                                    find_matches2=str_find_tree_maches.find(sub_info1, start, end)
                                                                                    find_matches1_2=int(find_matches2)
                                                                                    if find_matches1_2==0:
                                                                                        Where=block+0
                                                                                        
                                                                                        if Where!=0:
                                                                                    
                                                                                            sda20=bin(Where-Where2)[2:]
                                                                                            lenf=len(sda20)
                                                                                            if lenf>size_compress:
                                                                                                print("File too big")
                                                                                                raise SystemExit
                                                                                                
                                                                                                
                                                                                            
                                                                                            add_bits118=""
                                                                                            count_bits=size_compress-lenf%size_compress
                                                                                            z=0
                                                                                            if count_bits!=0:
                                                                                                if count_bits!=size_compress:
                                                                                                    while z<count_bits:
                                                                                                        add_bits118="0"+add_bits118
                                                                                                        z=z+1
                                                                                                                        
                                                                                                                        
                                                                                            sda30=sda20
                                                                                            bits=len(add_bits118)
                                                                                            sda25=bin(bits)[2:]
                                                                                            lenf=len(sda25)
                                                                                            if lenf>6:
                                                                                                print("File too big")
                                                                                                raise SystemExit
                                                                                                
                                                                                                
                                                                                            
                                                                                            add_bits119=""
                                                                                            count_bits=6-lenf%6
                                                                                            z=0
                                                                                            if count_bits!=0:
                                                                                                if count_bits!=6:
                                                                                                    while z<count_bits:
                                                                                                        add_bits119="0"+add_bits119
                                                                                                        z=z+1
                                                                                                                        
                                                                                                                        
                                                                                            sda19="1"+sda19+add_bits119+sda25+sda30
                                                                                            
                                                                                            Find=0

                                                                                    
                                                                                    
                                                                                                                         
                                                                                if Find!=0:
                                                                                    
                                                                                   
                                                                                    sda6=sda6+sda4    
                                                                                    compress_yes=compress_yes+1                                                                
                                                                              
                                                                                    sda5=""
                                                                                    sda7=""
                                                                                    sda12=""
                                                                                    sda4=""
                                                                                    block_compression2=0
                                                                                    Find=1
                                            
                                                                                elif Find==0:
                                                                                    compress_no=compress_no+1
                                                                                    #print(compress_no)
                                                                                
                                                                                    block_compression=0
                                                                                    block_compression1=0
                                                                                    sda6=sda6+str_find_tree_maches
                                                                                    
                                                                                    sda5=""
                                                                                    sda7=""
                                                                                    sda12=""
                                                                                    block_compression2=0
                                                                                    Find=1
                                                                                        
                                                                                block=block+blocks
                                                                                #print(block)
                                                         
                                                    times_compression=times_compression+1
                                                    sda19=sda19+"0"
                                                    #print(times_compression)
                                                    
                                                    
                                                         
                                                        
                
                                                    sda3=sda6
                                                    Where2=0
                                                    Where3=0
                                                    
                                                    #print(len(sda6))
                                                    sda6=""
                                                    
                                        long_after=len(sda3)
                                        
                                        if long_file<=long_after or long_after<=1:
                                            sda9="0"+sda10
                                        elif long_file>long_after:
                                            sda9="1"+sda3

                                        #print(sda9)
                                        long=len(sda19)    
                                        sda21=bin(long)[2:]
                                        lenf=len(sda21)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                        
                                                                                       
                                                                                    
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                    
                                        sda22=add_bits118+sda21+sda19     
                                        sda9="1"+sda22+sda9

                                        
                                        lenf=len(sda9)
                                        
                                        add_bits118=""
                                        count_bits=8-lenf%8
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=8:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                    
                                                                    
                                        sda9=add_bits118+sda9

                                        sda24=bin(times_compression)[2:]
                                        lenf=len(sda24)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                            
                                                                                            
                                                                                        
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                                                                    
                                                                                                                    
                                        sda9=add_bits118+sda24+sda9
                                        
                                        sda24=bin(Deep100)[2:]
                                        lenf=len(sda24)
                                        if lenf>40:
                                                print("File too big")
                                                raise SystemExit
                                                                                            
                                                                                            
                                                                                        
                                        add_bits118=""
                                        count_bits=40-lenf%40
                                        z=0
                                        if count_bits!=0:
                                            if count_bits!=40:
                                                while z<count_bits:
                                                    add_bits118="0"+add_bits118
                                                    z=z+1
                                                                                                                    
                                                                                                                    
                                        sda9=add_bits118+sda24+sda9

                                        long_file=len(sda10)
                                        long_after=len(sda9)
                                        if long_file>long_after and long_after<=120 or lenf>39 or Deep100>=long_after:
                                            sda11=sda9
                                            Find_guess=1
                                            
                                        elif long_file<=long_after:
                                            sda3=sda9
                                            Deep100=Deep100+1
                                            Deep101=Deep101+1
                                            sda9=""
                                            sda19=""
                                            start=-1
                                            times_compression=0
                                            predict=-1
                                            
                                        elif long_file>long_after:
                                            sda3=sda9
                                            Deep100=Deep100+1
                                            Deep101=Deep101+1
                                            sda9=""
                                            sda19=""
                                            start=-1
                                            times_compression=0
                                            predict=-1
                                            
                                    sda24=bin(Deep101)[2:]
                                    lenf=len(sda24)
                                    if lenf>40:
                                        print("File too big")
                                        raise SystemExit
                                                                                            
                                                                                            
                                                                                        
                                    add_bits118=""
                                    count_bits=40-lenf%40
                                    z=0
                                    if count_bits!=0:
                                        if count_bits!=40:
                                            while z<count_bits:
                                                add_bits118="0"+add_bits118
                                                z=z+1
                                                                                                                    
                                                                                                                    
                                    sda9=add_bits118+sda24+sda
                                    
                                    n = int(sda11, 2)
                                
                                    qqwslenf=len(sda11)
                                    qqwslenf=(qqwslenf/8)*2
                                    qqwslenf=str(qqwslenf)
                                    qqwslenf="%0"+qqwslenf+"x"
                             
                                    jl=binascii.unhexlify(qqwslenf % n)
                                
                                    size_after=len(jl)
                                   
                                    qqqwz=qqqwz+1
                                    szxzzza=""
                                    szxzs=""
                            
                                    assxw=assxw+1
                                    if assxw==1:
                                        assx=10
                                        if assx==10:

                                            f2.write(jl)
                                            x2 = time()
                                            x3=x2-x
                                            return print(x3)

                                


 
                  
self=""                                
d=compression()
    
xw=d.cryptograpy_compression()
print(xw)
