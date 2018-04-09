#使用wmi读取，
#wbemtest

import wmi
bios = wmi.WMI().Win32_BIOS()[0]

print(bios.BIOSVersion)