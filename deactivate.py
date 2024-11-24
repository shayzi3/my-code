import winreg
import os


# Winlogon
def deactivate_winlogon() -> None:
     registry_path = winreg.HKEY_LOCAL_MACHINE
     key_path = r'SOFTWARE\Microsoft\Windows NT\CurrentVersion\Winlogon'
     value = r'C:\WINDOWS\system32\userinit.exe,' 

     try:
          with winreg.OpenKeyEx(registry_path, key_path, winreg.KEY_WRITE) as registry_key:
               winreg.SetValueEx(registry_key, 'Userinit', 0, winreg.REG_SZ, value)
               
          print('[SUCCESS] Deactivate winlogon success')
          
     except Exception as ex:
          print(ex)
          os.system('pause')
     
     
# Автозагрузка
def deactivate_autoload() -> None:
     registry_path = winreg.HKEY_CURRENT_USER
     key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
     
     try:
          with winreg.OpenKeyEx(registry_path, key_path, 0, winreg.KEY_SET_VALUE) as registry_key:
               winreg.DeleteKeyEx(registry_key, 'SystemBootFile')
               
          print('[SUCCESS] Deactivate autoload success')
          os.system('pause')
          
     except Exception as ex:
          print(ex)
          os.system('pause')
     
     
def main():
     mode = input('Choose mode: W - Winlogon, A - Autoload: ').lower()
     
     if mode == 'w':
          deactivate_winlogon()
          
     elif mode == 'a':
          deactivate_autoload()
          
     else:
          print('[ERROR] Invalid mode')
          main()
          
          
if __name__ == '__main__':
     main()
          
          
     
     
     
     
     
     