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
        tts.tts_speak("""відобразити час ...
        відкривати браузер ...
        відкривати ютуб ...
        тестувати швидкість інтернету ...
        тестувати характеристики пристрою ...""")

    elif cmd == 'ctime':
        print("Використано оперативної пам'яті програмою (МБ): ")
        a = memory_usage()
        print(round(a[0]))
        now = datetime.datetime.now()
        print("Зараз: " + f"{now.hour}:" + f"{now.minute}")

    elif cmd == 'browser':
        print("Використано оперативної пам'яті програмою (МБ): ")
        a = memory_usage()
        print(round(a[0]))
        webbrowser.open("https://google.com")
        tts.tts_speak("Браузер був відкритий на ваш запит.")

    elif cmd == 'youtube':
        print("Використано оперативної пам'яті програмою (МБ): ")
        a = memory_usage()
        print(round(a[0]))
        webbrowser.open("https://www.youtube.com")
        tts.tts_speak("Ютуб був відкритий на ваш запит.")

    elif cmd == 'ping':
        print("Використано оперативної пам'яті програмою (МБ): ")
        a = memory_usage()
        print(round(a[0]))
        tts.tts_speak("Зачекайте, вимірюю швидкість вашої мережі. Це може зайняти певний час.")
        stest = speedtest.Speedtest()
        download = stest.download()
        upload = stest.upload()

        print(f"Швидкість завантаження: {humansize(download)} \nШвикість вивантаження: {humansize(upload)}")
        print("OK")

    elif cmd == 'sysinfo':
        m = platform.machine()
        print("Тип машини: " + m)
        ver = platform.version()
        print("Версія: " + ver)
        plt = platform.platform()
        print("Платформа: " + plt)
        sys = platform.system()
        print("Система: " + sys)
        pr = platform.processor()
        print("Процесор: " + pr)
        arc = platform.architecture()
        print("Архітектура: ")
        print(arc)
        pv = platform.python_version()
        print("Версія Python: " + pv)
        rel = platform.release()
        print("Версія Windows: " + rel)
        psutil.cpu_percent()
        psutil.virtual_memory()
        dict(psutil.virtual_memory()._asdict())
        used_ram = psutil.virtual_memory().percent
        total, used, free = shutil.disk_usage("\\")
        print("Загально %d гігабайт пам'яті.\n" % (total // (2 ** 30)) +
              "Використано з них %d гігабайт.\n" % (used // (2 ** 30)) +
              "Вільно: %d гігабайт.\n" % (free // (2 ** 30)) +
              "Використано " + str(used_ram) + " відсотків оперативної пам'яті.")
        tts.tts_speak("Ось ваша детальна інформація про систему.")

    elif cmd == 'quit':
        tts.tts_speak("Допобачення. Гарного вам дня!")
        exit(0)