from request import Request
from response import Response
import time
import subprocess



class Problems:
    
    def __init__(self, request: Request, response: Response) -> None:
        self.request = request
        self.response = response

    def poblem(self):
        if self.request.method == 'POST':
            time.sleep(3)
            command = "xdotool search --onlyvisible --class \"google-chrome\" windowactivate --sync key F11"  # Ваша команда для увеличения громкости
            subprocess.call(command, shell=True)
            command = "amixer sset Master unmute"
            subprocess.call(command, shell=True)
            command = "amixer sset Master 100%+"  # Ваша команда для увеличения громкости
            subprocess.call(command, shell=True)
            command = "xdg-open https://www.youtube.com/watch?v=fJAqdW3wIeM&t=1s&ab_channel=Dobryak"  # Ваша команда для увеличения громкости
            subprocess.call(command, shell=True)
            command = "xdotool search --onlyvisible --class \"google-chrome\" windowactivate --sync key 2"  # Ваша команда для увеличения громкости
            subprocess.call(command, shell=True)
            count = 1
            while True:
                if count % 150 == 0:
                    command = "xdg-open https://www.youtube.com/watch?v=fJAqdW3wIeM&t=1s&ab_channel=Dobryak"  # Ваша команда для увеличения громкости
                    subprocess.call(command, shell=True)
                count += 1
                command = "amixer sset Master unmute"
                subprocess.call(command, shell=True)
                command = "amixer sset Master 100%+"  # Ваша команда для увеличения громкости
                subprocess.call(command, shell=True)
                command = "xdotool search --onlyvisible --class \"google-chrome\" windowactivate --sync key F11"  # Ваша команда для увеличения громкости
                subprocess.call(command, shell=True)