#!/usr/bin/python
import os
import Tkinter
import tkMessageBox

# Console colors
W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan


class simpleapp(Tkinter.Tk):
   def __init__(self,parent):
      Tkinter.Tk.__init__(self,parent)
      self.parent=parent
      self.initialize()
   def initialize(self):
      self.textvari=Tkinter.StringVar()
      self.textcode=Tkinter.StringVar()
      self.chF=Tkinter.IntVar()
      self.chG=Tkinter.IntVar()
      self.chY=Tkinter.IntVar()
      self.chYa=Tkinter.IntVar()
      self.chAm=Tkinter.IntVar()
      self.inputloca=Tkinter.StringVar()
      self.inputpor=Tkinter.StringVar()
     


      self.inputloca.set("LOCATION IP")
      self.inputpor.set("PORT")

      self.textvari.set("SET RULE")
      self.textcode.set("Enter the IPTABLE Rule here and press SECRET BUTTON :) ")
      self.label=Tkinter.Label(self,text="CLICK TO BLOCK",bg="black",fg="white",height=3,width=10)
      self.label.grid(column=0,row=0,columnspan=5,sticky="EW")
      self.enterip=Tkinter.StringVar()
      self.enterip.set("ENTER THE IP FOR BLOCK")
      self.entryip=Tkinter.Entry(self,textvariable=self.enterip,bg='white',fg="black")
      self.entryip.grid(column=3,row=0,sticky="EW")
      self.buttonstatus=Tkinter.StringVar()
      self.buttonstatus.set("BLOCK")
      self.entryip.bind("<Return>",self.checklist)
      self.entryipbutton=Tkinter.Button(self,command=self.append,bg="white",fg="black",activebackground="black",activeforeground="white",textvariable=self.buttonstatus)
      self.entryipbutton.grid(column=4,row=0,sticky="ew",padx=4)

      self.label6=Tkinter.Label(self,bg="red",height=3,width=20)
      self.label6.grid(column=5,row=0,sticky="EW")
      

      self.packettext=Tkinter.StringVar()
      self.packettext.set("CLICK TO ON")
     
      file=open("/proc/sys/net/ipv4/ip_forward","r")
      string=file.read(1)
      print string[0]
      file.close()
      if (string[0]=='0'):
        print 'PROGRAMM IS ON THE RIGHT WAY'
      else:
        self.packettext.set("CLICK TO OFF")
        
      


      
      self.packetforward=Tkinter.Button(self,command=self.ip_forward_on_off,bg="purple",fg="black",activebackground="green",textvariable=self.packettext)
      self.packetforward.grid(column=5,row=0,sticky="EW")
      self.checkF=Tkinter.Checkbutton(self,command=self.chfacebook,text="FACEBOOK",bg="pink",fg="red",onvalue=1,offvalue=0,variable=self.chF,cursor="arrow")
      self.checkF.grid(column=0,row=1)
      self.checkG=Tkinter.Checkbutton(self,command=self.chgoogle,text="GOOGLE",bg="orange",offvalue=0,variable=self.chG,cursor="arrow")
      self.checkG.grid(column=1,row=1)
      self.checkY=Tkinter.Checkbutton(self,command=self.chyoutube,text="YOU TUBE",bg="green",fg="black",offvalue=0,cursor="arrow",variable=self.chY)
      self.checkY.grid(column=2,row=1)  
      self.checkYa=Tkinter.Checkbutton(self,command=self.chyahoo,text="YAHOO !",bg="#0DEF88",fg="black",offvalue=0,variable=self.chYa,cursor="arrow")
      self.checkYa.grid(column=3,row=1)
      self.checkAm=Tkinter.Checkbutton(self,command=self.chamazon,text="AMAZON",bg="#1DEF33",fg="brown",offvalue=0,variable=self.chAm,cursor="arrow")
      self.checkAm.grid(column=4,row=1)
      

      self.clear=Tkinter.Button(self,command=self.reset,bg="brown",fg="black",text="RESET RULES",activebackground="black",activeforeground="white")
      self.clear.grid(column=5,row=1,padx=2)


      self.label2=Tkinter.Label(self,text="ROOT SERVICES BLOCK",bg="#EB1153",fg="white",height=3,width=10)
      self.label2.grid(column=0,row=2,columnspan=6,sticky="EW",pady=4)
      self.chInput=Tkinter.IntVar()
      self.chOutput=Tkinter.IntVar()
      self.chForward=Tkinter.IntVar()
      self.checkInput=Tkinter.Checkbutton(self,command=self.chinput,text="INPUT TRAFFIC",bg="#117BE4",fg="red",onvalue=1,offvalue=0,variable=self.chInput,cursor="arrow",activebackground="red",activeforeground="white")
      self.checkInput.grid(column=0,row=3)
      self.checkForward=Tkinter.Checkbutton(self,command=self.chforward,text="FORWARD TRAFFIC",bg="white",fg="brown",onvalue=1,offvalue=0,variable=self.chForward,cursor="arrow",activebackground="#7FEB17")
      self.checkForward.grid(column=2,row=3)
      self.checkOutput=Tkinter.Checkbutton(self,command=self.choutput,text="OUTPUT TRAFFIC",bg="orange",fg="black",onvalue=1,offvalue=0,variable=self.chOutput,cursor="arrow",activebackground="#07E2F1")
      self.checkOutput.grid(column=4,row=3)
      self.label3=Tkinter.Label(self,text="REDIRECT COMPLETE TRAFFIC TO LOCATION",bg="#222233",fg="white",height=2,width=10)
      self.label3.grid(column=0,row=8,columnspan=6,sticky="EW",pady=2)
      self.inputlocation=Tkinter.Entry(self,textvariable=self.inputloca,fg="white",bg="#F76728")
      self.inputlocation.grid(column=0,row=9,pady=2,sticky="EW")
      self.inputport=Tkinter.Entry(self,textvariable=self.inputpor,fg="black",bg="#F76728")  
      self.inputport.grid(column=2,row=9,pady=2,sticky="EW")
      self.route=Tkinter.Button(self,command=self.routeon,text="REDIRECT !",fg="white",bg="red")
      self.route.grid(column=4,row=9,pady=2)

      self.label4=Tkinter.Label(self,text="CREATE YOUR OWN RULE :)       CODE=iptables -A/I/P INPUT/FORWARD/OUTPUT -p TCP/UDP/ICMP -s --sport -d --dport -j ACCEPT/DROP",fg="black",bg="#E71089",height=3,width=10)
      self.label4.grid(column=0,row=10,columnspan=6,sticky="EW",pady=2)
      self.labelv1=Tkinter.StringVar()
      self.labelv1.set("iptables")
      self.label5=Tkinter.Label(self,textvariable=self.labelv1,bg="orange",fg="white")
      self.label5.grid(column=0,row=11,sticky="ew")
      list1=('A','I','P')
      list2=('INPUT','FORWARD','OUTPUT')
      list3=('tcp','udp','icmp','ALL')
      self.v1=Tkinter.StringVar()
      self.v2=Tkinter.StringVar()
      self.v3=Tkinter.StringVar()
      self.v1.set(list1[0])
      self.v2.set(list2[1])
      self.v3.set(list3[0])
      self.Om1=Tkinter.OptionMenu(self,self.v1,*list1)
      self.Om1.grid(column=1,row=11,sticky="ew")
      self.Om2=Tkinter.OptionMenu(self,self.v2,*list2)
      self.Om2.grid(column=2,row=11,sticky="ew")      

      self.labelv2=Tkinter.StringVar()
      self.labelv2.set("PACKETS")
      self.label6=Tkinter.Label(self,textvariable=self.labelv2,bg="orange",fg="white")
      self.label6.grid(column=3,row=11,sticky="ew")
 
      self.Om3=Tkinter.OptionMenu(self,self.v3,*list3)
      self.Om3.grid(column=4,row=11,sticky="ew")


      self.sourcepacket=Tkinter.StringVar()
      self.sourcepacket.set("Source IP")
      self.sourcep=Tkinter.Entry(self,textvariable=self.sourcepacket,bg="red",fg="white")
      self.sourcep.grid(column=0,row=12,sticky="ew",pady=2)
      self.sourceport=Tkinter.StringVar()
      self.sourceport.set("Source PORT")
      self.sourcep=Tkinter.Entry(self,textvariable=self.sourceport,bg="red",fg="white")
      self.sourcep.grid(column=1,row=12,sticky="ew",pady=2)
      self.destinationpacket=Tkinter.StringVar()
      self.destinationpacket.set("Destination IP")
      self.sourcep=Tkinter.Entry(self,textvariable=self.destinationpacket,bg="red",fg="white")
      self.sourcep.grid(column=2,row=12,sticky="ew",pady=2)
      self.destinationport=Tkinter.StringVar()
      self.destinationport.set("Destination PORT")
      self.sourcep=Tkinter.Entry(self,textvariable=self.destinationport,bg="red",fg="white")
      self.sourcep.grid(column=3,row=12,sticky="ew",pady=2)
      listad=('ACCEPT','DROP')
      self.vari=Tkinter.StringVar()
      self.vari.set(listad[0])
      self.Om4=Tkinter.OptionMenu(self,self.vari,*listad)
      self.Om4.grid(column=4,row=12,sticky="ew",pady=2)      
      self.saverule=Tkinter.Button(self,command=self.saveiptable,bg="#34E610",fg="red",text="SAVE",height=4,activebackground="red",activeforeground="black")
      self.saverule.grid(column=5,row=11,rowspan=2,sticky="ew")
 
      self.grid_columnconfigure(0,weight=1)
      self.resizable(False,False)
      self.bind("<Control-Alt-Y>",self.entryboxsecret)
      self.bind("<Control-Alt-r>",self.resetrawtable)
      self.bind("<Control-Alt-R>",self.resetall)
      self.bind("<Control-Alt-N>",self.list)
     

      oforb=open("/root/Desktop/ip's.txt","r")
      oforbdata=oforb.readlines()
      oforb.seek(0)
      oforbdata1=oforb.read()
      oforb.close()
      
      ofc=open("/root/Desktop/ip's.txt","w+")
      for hashji in range(1,4):
         happy=oforbdata1.replace("\n\n","\n")
      ofc.write(happy)
      ofc.close()
     
      
      count=0
      for kitman in oforbdata1:
         if (kitman=='\n'):
           count=count+1 
      print count

      print oforbdata[0][:8] 
      os.system('iptables -F;iptables -X')
      for block in range(0,count):
         
         oforbdata[block]=oforbdata[block].strip()
         oforbdata[block]=oforbdata[block].replace('\n',"")
         print oforbdata[block]
         os.system('iptables -A FORWARD -p tcp -d %s -j DROP' % oforbdata[block])   
       

   def checklist(self,event):
      print 'YOU PRESSED ENTER ON THE KEYBORAD'
      file=open("/root/Desktop/ip's.txt","r")
      filedata=file.read()
      file.close()
      file2=open("/root/Desktop/ip's.txt","r")
      file2data=file2.readlines()
      file2.close()
      for line in file2data:
         print line
      if self.entryip.get() in filedata:
        self.buttonstatus.set("UNBLOCK")
      else:
        self.buttonstatus.set("BLOCK")


   def append(self):
      print 'you clicked the block button'
      if (self.buttonstatus.get()=='BLOCK'):
        os.system('iptables -I FORWARD 1 -p tcp -d %s -j DROP' % self.entryip.get())
         
        checkblock=open("/root/Desktop/ip's.txt","r")
        checkblockdata=checkblock.readlines()
        checkblock.close()
          
        for checklines in checkblockdata:
           
             addit=tkMessageBox.askokcancel("ADD IN LIST","Would you like to add this ip in the blocked ip list")
             if (addit==True):
               file1=open("/root/Desktop/ip's.txt","a+")
               file1.write('%s \n' % self.entryip.get())
               file1.close()
               break
             elif (addit==False):
               print 'YOU CHOOSE NOT TO ADD THIS IP IN THE IP BLOCK LIST'
             else:
               print 'THERE IS SOME PROBLEM IN THIS LIST PLEASE CONTACT TO YOUR SYSTEM ADMINISTRATOR MANOHAR SINGH'
             break


        print 'THE ADDRESS %s HAS BEEN BLOCKED' % self.entryip.get()       
      elif (self.buttonstatus.get()=='UNBLOCK'):
        os.system('iptables -I FORWARD 1 -p tcp -d %s -j ACCEPT' % self.entryip.get())
        file4=open("/root/Desktop/ip's.txt","r")
        file4data=file4.readlines()
        file4.close()
        file5=open("/root/Desktop/ip's.txt","w")
        for line1 in file4data:
           if (line1=='%s \n' % self.entryip.get()):
             print 'THE IP IS PRESENT IN BLOCKED LIST'
             file5.write('\n')
           else :
             file5.write(line1)
        print 'THE IP AS BEEN REMOVED FRO THE LIST OF BLOCEK IPs'     
        file5.close()        
        print 'THE ADDRESS %s HAS BEEN UNBLOCKED' % self.entryip.get()
    
    
   def ip_forward_on_off(self):
      print self.packettext.get()
      if (self.packettext.get()=="CLICK TO ON"):
        print 'NOW PACKET FORWARDING IS OFF'
        packeton=tkMessageBox.askokcancel("PACKET FORWARDING SYSTEM","Would you like to forward traffic through you system")
        if (packeton==True):
          os.system('sysctl net.ipv4.ip_forward=1')
          print 'PACKET FORWARDING THROUGH YOUR KERNEL IS NOW ACTIVE'
          self.packettext.set("CLICK TO OFF")
        elif (packeton==False):
          os.system('sysctl net.ipv4.ip_forward=0')
          print 'PACKET FORWARDING THROUGH YOUR KERNETL IS NOW DISABLE'
        else:
          print 'KERNEL PACKET PROBLEM CONTACT TO YOUR SYSTEM ADMINSTRATOR MANOHAR SINGH'
      elif (self.packettext.get()=="CLICK TO OFF"):
        print 'PACKET FORWARDING IS NOW ACTIVE THROUGHT YOUR KERNEL'
        packetoff=tkMessageBox.askokcancel("PACKET FORWARDING SYSTEM","Would you like to disable traffic through your system")
        if (packetoff==True):
          os.system('sysctl net.ipv4.ip_forward=0')
          print 'PACKET FORWARDING THROUGH YOUR SYSTEM IS NOW DIASBLED'
          self.packettext.set("CLICK TO ON")
        elif (packetoff==False):
          os.system('sysctl net.ipv4.ip_forward=1')
          print 'PACKET FORWARDING THROUGH YOUR KERNEL IS NOW ACTIVE'
        else:
          print 'KERNEL PROBLEM CONTACT TO YOUR SYSTEM ADMINISTRATOR MANOHAR SINGH'
      else:
          print 'THIS IS THE PROBLEM OF THE VALUE THAT IS ASSIGNED TO BUTTON'

   def saveiptable(self):
      s1=self.v1.get()
      s2=self.v2.get()
      s3=self.v3.get()
      ps=self.sourcepacket.get()
      pp=self.sourceport.get()
      pd=self.destinationpacket.get()
      dp=self.destinationport.get()
      dis=self.vari.get()
      rulesimple='iptables -%s %s -p %s -s %s --sport %s -d %s --dport %s -j %s' % (s1,s2,s3,ps,pp,pd,dp,dis)
      save=tkMessageBox.askokcancel("SAVE IPTABLES RULE",rulesimple)
      if (save==True):
        rulesimple1='iptables -%s %s -p %s -s %s --sport %s -d %s --dport %s -j %s' % (s1,s2,s3,ps,pp,pd,dp,dis)
        os.system(rulesimple1)
        print 'THE SELF CREATED RULE HAS BEEN SAVED'
      elif (save==False):
        print 'YOU CLICKED CANCEL SO RULE HAS BEEN DESTROYED'
      else:
        print 'Something is going wrong contact to your ADMINISTRATOR MANOHAR SINGH :)'
       


   def entryboxsecret(self,event):   
          self.label3=Tkinter.Label(self,text="FOR IPTABLES EXPERTS",bg="#44eedd",fg="#F11741",height=3,width=10)
          self.label3.grid(column=0,row=6,columnspan=6,pady=3,sticky="EW")
          self.entrytable=Tkinter.Text(self,bg="#B614E1",fg="white",height=2)
          self.entrytable.bind("<Control-Alt-M>",self.secretbutton)  
          self.entrytable.bind("<Control-Alt-x>",self.secretbutton2)
          self.entrytable.grid(column=0,row=7,columnspan=6,sticky="EW")

   def resetrawtable(self,event):
      os.system('iptables -F')
      os.system('iptables -X')
      os.system('iptables -L')
      for kit in range(1,3):
         print "_____________________________________________________________"
      print 'THE RAW TABLES HAS BEEN RESET'
   def resetall(self,event):
      os.system('iptables -F')
      os.system('iptables -X')
      os.system('iptables -t nat -F')
      os.system('iptables -t nat -X')
      for kittuman in range(1,3):
         print "_____________________________________________________________"
      print 'THE COMPLETE NORMAL TABLES HAS BEEN RESET'
      
   def routeon(self):
      route=tkMessageBox.askokcancel("ROUTE TRAFFIC","Would you like to route all traffic to LOCATION:%s and PORT:%s" % (self.inputloca.get(),self.inputpor.get()))
      if (route==True):
        os.system("iptables -t nat -I PREROUTING 1 -p tcp -j DNAT --to-destination %s:%s" % (self.inputloca.get(),self.inputpor.get()))
        os.system("iptables -t nat -A POSTROUTING -j MASQUERADE")
        print 'THE SYSTEM HAS SET RULE TO FIREWALL SUCCESSFULLY TO ROUTE TRAFFIC TO %s:%s' % (self.inputloca.get(),self.inputpor.get())
      elif (route==False):
        print 'You choose CANCEL please try again Sorry ! :)'
      else:
        print 'CONTACT TO ADMINISTRATOR MANOHAR SINGH'

   
   def chfacebook(self):

      if (self.chF.get() == 1):
        n=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to disable FaceBook")
        if (n==True):
          print 'FACEBOOK IS DISABLED BY ADMINISTATOR NOW'
          os.system('iptables -I FORWARD 1 -p ALL -d 31.13.79.246 -j DROP')
        elif (n==False):
          print 'you click CANCEL'
          self.chF.set("0")
        else: 
          print 'Something is going wrong contact ADMINISTRATOR MANOHAR SINGH'
      elif (self.chF.get() == 0):
        n1=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to enable FaceBook")
        if (n1==True):
          print 'FACEBOOK IS NOW ACTIVATED BY ADMINISTRATOR NOW'
          os.system('iptables -I FORWARD 1 -p ALL -d 31.13.79.246 -j ACCEPT')
        elif (n1==False):
          print 'you clicked CANCEL'
          self.chF.set("1")
        else:
          print 'Something is going wrong contact to your network administrator'
      else:
        print 'THIS IS SEEMS LIKE A PROBLEM'
        print self.chF.get()

   def chgoogle(self):

      if (self.chG.get() == 1):
       ng=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to disable GOOGLE")
       if (ng==True):      
         print 'GOOGLE IS DISABLED BY ADMINISTATOR NOW'
         os.system('iptables -I FORWARD 1 -p ALL -d 216.58.220.36 -j DROP')
         os.system('iptables -I FORWARD 2 -p ALL -d 216.58.196.99 -j DROP')
       elif (ng==False):
         print 'You click CANCEL'
         self.chG.set("0")
       else:
         print 'Something is going wrong contact ADMINISTRATOR MANOHAR SINGH'
      elif (self.chF.get() == 0):
        ng1=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to enable GOOGLE")
        if (ng1==True):
           print 'GOOGLE IS NOW ACTIVATED BY ADMINISTRATOR NOW'
           os.system('iptables -I FORWARD 1 -p ALL -d 216.58.220.36 -j ACCEPT')
           os.system('iptables -I FORWARD 2 -p ALL -d 216.58.196.99 -j ACCEPT')
        elif (ng1==False):
           print 'you clicked CANCEL'
           self.chG.set("1")
        else:
           print 'Something is goign wrong you should contact our ADMINISTRATOR MANOHAR SINGH'
      else:
        print 'THIS IS SEEMS LIKE A PROBLEM'
        print self.chF.get()
      
   def chyahoo(self):
     
      if (self.chYa.get() == 1):
        n=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to disable YAHOO INDIA")
        if (n==True):
          print 'YAHOO INDIA IS DISABLED BY ADMINISTATOR NOW'
          os.system('iptables -I FORWARD 1 -p ALL -d 106.10.212.150 -j DROP')
        elif (n==False):
          print 'you click CANCEL'
          self.chYa.set("0")
        else:
          print 'Something is going wrong contact ADMINISTRATOR MANOHAR SINGH'
      elif (self.chYa.get() == 0):
        n1=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to enable YAHOO INDIA")
        if (n1==True):
          print 'YAHOO INDIA IS NOW ACTIVATED BY ADMINISTRATOR NOW'
          os.system('iptables -I FORWARD 1 -p ALL -d 106.10.212.150 -j ACCEPT')
        elif (n1==False):
          print 'you clicked CANCEL'
          self.chYa.set("1")
        else:
          print 'Something is going wrong contact to your network administrator'
      else:
        print 'THIS IS SEEMS LIKE A PROBLEM'
        print self.chYa.get()

  
   
   def chyoutube(self):
 
      if (self.chY.get() == 1):
        n=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to disable You Tube")
        if (n==True):
          print 'You Tube :( IS DISABLED BY ADMINISTATOR NOW'
          os.system('iptables -I FORWARD 1 -p ALL -d 216.58.196.14 -j DROP')
        elif (n==False):
          print 'you click CANCEL'
          self.chY.set("0")
        else:
          print 'Something is going wrong contact ADMINISTRATOR MANOHAR SINGH'
      elif (self.chY.get() == 0):
        n1=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to enable You Tube")
        if (n1==True):
          print 'You Tube IS NOW ACTIVATED BY ADMINISTRATOR NOW'
          os.system('iptables -I FORWARD 1 -p ALL -d 216.58.196.14 -j ACCEPT')
        elif (n1==False):
          print 'you clicked CANCEL'
          self.chY.set("1")
        else:
          print 'Something is going wrong contact to your network administrator'
      else:
        print 'THIS IS SEEMS LIKE A PROBLEM'
        print self.chY.get()
      


   
   def chamazon(self):
      
    
     if (self.chAm.get() == 1):
        n=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to disable AMAZON INDIA")
        if (n==True):
          print 'AMAZON INDIA IS DISABLED BY ADMINISTATOR NOW'
          os.system('iptables -I FORWARD 1 -p ALL -d 178.236.7.18 -j DROP')
        elif (n==False):
          print 'you click CANCEL'
          self.chAm.set("0")
        else:
          print 'Something is going wrong contact ADMINISTRATOR MANOHAR SINGH'
     elif (self.chAm.get() == 0):
        n1=tkMessageBox.askokcancel("ADMIN MANOHAR","Would you like to enable AMAZON INDIA")
        if (n1==True):
          print 'AMAZON INDIA IS NOW ACTIVATED BY ADMINISTRATOR NOW'
          os.system('iptables -I FORWARD 1 -p ALL -d 178.236.7.18 -j ACCEPT')
        elif (n1==False):
          print 'you clicked CANCEL'
          self.chAm.set("1")
        else:
          print 'Something is going wrong contact to your network administrator'
     else:
        print 'THIS IS SEEMS LIKE A PROBLEM'
        print self.chAm.get()

  
   
   def reset(self):
      rest=tkMessageBox.askokcancel("ADMIN RESET","OK=COMPLETE  CANCEL=CHAIN RESET")
      if (rest==True):
         os.system('iptables -F')
         os.system('iptables -X')
         os.system('iptables -t nat -F')
         os.system('iptables -t nat -X')
      elif (rest==False):
         os.system('iptables -F')
         os.system('iptables -X')
      else:
         print 'Something is going wrong contact ADMINISTRATOR MANOHAR SINGH'
      print 'NOW ALL THE PROTOCOL IS FORWARDED THROUGH MANOHAR SINGH'
      print 'NOW YOU ARE FREE OF USE'


   def chinput(self):
      if (self.chInput.get()==1):
        os.system('iptables -P INPUT DROP')
        print 'THE COMPLETE TRAFFIC COMING TO THE MACHINE IS NOW DROPPED'
      elif (self.chInput.get()==0):
        os.system('iptables -P INPUT ACCEPT')
        print 'THE TRAFFIC TO LOCAL MACHINE IS NOW ACTIVATED'
      else:
        print 'some thing is going wrong contact to administrator'
        print self.chInput.get()
   
   def chforward(self):
      if (self.chForward.get()==1):
     

       self.chTcp=Tkinter.IntVar()
       self.chUdp=Tkinter.IntVar()
       self.chIcmp=Tkinter.IntVar()
       self.chAll=Tkinter.IntVar()
      
       self.checktcp=Tkinter.Checkbutton(self,command=self.chtcp,variable=self.chTcp,text=" TCP ",onvalue=1,offvalue=0)
       self.checktcp.grid(column=1,row=5,pady=2)
       self.checkudp=Tkinter.Checkbutton(self,command=self.chudp,variable=self.chUdp,text=" UDP ",onvalue=1,offvalue=0)
       self.checkudp.grid(column=2,row=5,pady=2)
       self.checkicmp=Tkinter.Checkbutton(self,command=self.chicmp,variable=self.chIcmp,text=" ICMP ",onvalue=1,offvalue=0)
       self.checkicmp.grid(column=3,row=5,pady=2)
       self.checkall=Tkinter.Checkbutton(self,command=self.chall,variable=self.chAll,text="ALL OF",onvalue=1,offvalue=0,fg="red",cursor="arrow")
       self.checkall.grid(column=4,row=5,pady=2)
       
          
          
     
      elif (self.chForward.get()==0):
        print 'YOU UNCHECKED THE FORWARD TRAFFIC CHECK BOX'
        
      else:
        print 'some thing is going wrong contact to administrator'
        print self.chForward.get()

  
   def choutput(self):
      if (self.chOutput.get()==1):
        os.system('iptables -P OUTPUT DROP')
        print 'THE COMPLETE TRAFFIC GOING THROUGH THIS MACHINE IS NOW DROPPED'
      elif (self.chOutput.get()==0):
        os.system('iptables -P OUTPUT ACCEPT')
        print 'THE TRAFFIC FROM THIS LOCAL MACHINE SERVER IS NOW ACTIVATED'
      else:
        print 'some thing is going wrong contact to administrator'
        print self.chOutput.get()
   
   def chtcp(self):
      if (self.chTcp.get()==1):
        os.system('iptables -I FORWARD 1 -p tcp -j DROP')
        print 'ALL THE TCP TRAFFIC FORWARDED IS DROPPED :('
 
      elif (self.chTcp.get()==0):
        os.system('iptables -I FORWARD 1 -p tcp -j ACCEPT')
        print 'ALL THE TCP IS ACCEPTED NOW :)'
      else:
        print 'something is going wrong contact ADMINISTRATOR'
   
   def chudp(self):
      if (self.chUdp.get()==1):
        os.system('iptables -I FORWARD 1 -p udp -j DROP')
        print 'ALL THE UDP TRAFFIC FORWARDED IS DROPPED :('
      elif (self.chUdp.get()==0): 
        os.system('iptables -I FORWARD 1 -p udp -j ACCEPT')
        print 'ALL THE UDP TRAFFIC FORWARDED IS ACCEPTED NOW :)'
      else:
        print 'something is going wrong contact ADMINISTRATOR'

   def chicmp(self):

      if (self.chIcmp.get()==1):
        os.system('iptables -I FORWARD 1 -p icmp -j DROP')
        print 'ALL THE ICMP IS NOW DROPPED YOU CANT PING NOW :('
     
      elif (self.chIcmp.get()==0): 
        os.system('iptables -I FORWARD 1 -p icmp -j ACCEPT')
        print 'ALL THE ICMP TRAFFIC IS NOW ACCEPTED HAVE PING :)'
      else:
        print 'something is going wrong contact ADMINISTRATOR'
   def chall(self):
      if (self.chAll.get()==1):
         os.system('iptables -P FORWARD DROP')
         print 'THE COMPLETE TRAFFIC TO OTHER SERVERS (eg. www.something.com) HAS BEEN DROPPED NOW'
      elif (self.chAll.get()==0):
         os.system('iptables -P FORWARD ACCEPT')
         print 'THE COMPLETE TRAFFIC TO OTHRE SEVERS NOW ACCEPTED'
      else:
         print 'SOME THING IS GOING WRONG CONTACT MANOHAR SINGH ADMINISTRATOR' 
   
   def secretbutton(self,event):
      print 'SECRET BUTTON PRESSED SUCCESSFULLY ENJOY NOW :)'
      print 'WE THINK YOU ARE THE ADMIN'
      codeget=self.entrytable.get("1.0",'end')
      submit=tkMessageBox.askokcancel("M@@NO#AR","Would you like to save rule in iptable")
      if (submit==True):
        os.system(codeget)
      elif (submit==False):
        print 'Sorry You Choose CANCEL'
      else:
        print 'something is going wrong you shoud contact your ADMINISTRATOR'
      

   def secretbutton2(self,event):
      print '2 SECRETE BUTTON PRESSED ENJOY THE FIREWALL'
      print 'WE THINK THAT YOU ARE ADMIN M@@NO#AR'
      codeget2=self.entrytable.get("1.0",'end')
      
     
      os.system(codeget2)
      print 'SUCCESSFULLY ADDED RULE TO FIREWALL'
   def list(self,event):
      print ''+R+''
      os.system("iptables -L")
      print ("\n")
      print ''+O+''
      os.system("iptables -t nat -L")
      print ''+T+''
      for maa in range(1,3):
         print "________________________________________________________________________"
      print ''+W+''
   def printsecret(self,event):
      print 'TESTED SUCCESSFULLY'    

if __name__=="__main__":
     app=simpleapp(None)
     app.title("STRICT FIREWALL BY M@@no#AR")
     app.mainloop()
