from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Light:
    def turn_on(self):
        print("the light is on")

    def turn_off(self):
        print("the light is off")

class LightOnCommand(Command):
    def __init__(self, light: Light):
       self._light = light

    def execute(self):
        self._light.turn_on()

class LightOffCommand(Command):
    def __init__(self, light: Light):
       self._light = light

    def execute(self):
        self._light.turn_off()

class RemoteControll:
    def __init__(self) -> None:
        self._commands = {}

    def set_command(self, button, command: Command):
        self._commands[button] = command

    def press_button(self, button):
        if button in self._commands:
            self._commands[button].execute()
        else:
            print(f"No command set for button {button}")

if __name__ == "__main__":
    light = Light()

    light_on = LightOnCommand(light)
    light_off = LightOffCommand(light)

    remote = RemoteControll()

    remote.set_command("ON", light_on)
    remote.set_command("OFF", light_off)

    remote.press_button("ON")
    remote.press_button("OFF")
    remote.press_button("UP")