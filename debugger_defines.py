from ctypes import *
# Micrsoft types to ctypes
WORD        =c_ushort
DWORD       =c_ulong
LPBYTE      =POINTER(c_ubyte)
LPTSTR      =POINTER(c_char)
HANDLE      =c_void_p
# Constants
DEBUG_PROCESS   =0x00000001