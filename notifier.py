from plyer import notification
import subprocess
import platform

class Notifier:
    def send(self, message):
        notification.notify(
            title="Class Monitor Alert",
            message=message,
            timeout=5
        )

    def check_network(self):
        try:
            if platform.system() == "Windows":
                cmd = ["ping", "-n", "1", "8.8.8.8"]
            else:
                cmd = ["ping", "-c", "1", "8.8.8.8"]

            result = subprocess.run(
                cmd,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )

            return result.returncode == 0
        except:
            return False
