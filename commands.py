import datetime
import platform
import shutil
import webbrowser
import psutil
import speedtest
from memory_profiler import memory_usage
import tts


def humansize(nbytes):
    suffixes = ['B', 'KB', 'MB', 'GB', 'TB', 'PB']
    i = 0
    while nbytes >= 1024 and i < len(suffixes) - 1:
        nbytes /= 1024.
        i += 1
    f = ('%.2f' % nbytes).rstrip('0').rstrip('.')
    return '%s %s' % (f, suffixes[i])


def execute_cmd(cmd: str):
    if cmd == 'help':
        tts.tts_speak("""display time...
        open browser...
        open youtube ...
        test internet speed...
        test the characteristics of the device ...""")

    elif cmd == 'ctime':
        print("RAM used by the program (MB): ")
        a = memory_usage()
        print(round(a[0]))
        now = datetime.datetime.now()
        print("Now: " + f"{now.hour}:" + f"{now.minute}")

    elif cmd == 'browser':
        print("RAM used by the program (MB): ")
        a = memory_usage()
        print(round(a[0]))
        webbrowser.open("https://google.com")
        tts.tts_speak("The browser was opened at your request.")

    elif cmd == 'youtube':
        print("RAM used by the program (MB): ")
        a = memory_usage()
        print(round(a[0]))
        webbrowser.open("https://www.youtube.com")
        tts.tts_speak("YouTube was opened at your request.")

    elif cmd == 'ping':
        print("RAM used by the program (MB): ")
        a = memory_usage()
        print(round(a[0]))
        tts.tts_speak("Wait, I'm measuring your network speed. This may take some time.")
        stest = speedtest.Speedtest()
        download = stest.download()
        upload = stest.upload()

        print(f"Download speed: {humansize(download)} \nSpeed of unloading: {humansize(upload)}")
        print("OK")

    elif cmd == 'sysinfo':
        m = platform.machine()
        print("Computer: " + m)
        ver = platform.version()
        print("Version: " + ver)
        plt = platform.platform()
        print("Platform: " + plt)
        sys = platform.system()
        print("System: " + sys)
        pr = platform.processor()
        print("Processor: " + pr)
        arc = platform.architecture()
        print("Architecture: ")
        print(arc)
        pv = platform.python_version()
        print("Version Python: " + pv)
        rel = platform.release()
        print("Version Windows: " + rel)
        psutil.cpu_percent()
        psutil.virtual_memory()
        dict(psutil.virtual_memory()._asdict())
        used_ram = psutil.virtual_memory().percent
        total, used, free = shutil.disk_usage("\\")
        print("Total %d gigabytes of memory.\n" % (total // (2 ** 30)) +
              "Used %d gigabytes.\n" % (used // (2 ** 30)) +
              "Free: %d gigabytes.\n" % (free // (2 ** 30)) +
              "Used  " + str(used_ram) + " percent of RAM.")
        tts.tts_speak("Here is your detailed system information.")

    elif cmd == 'quit':
        tts.tts_speak("Goodbye. Have a nice day!")
        exit(0)