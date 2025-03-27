class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None  # in gigabytes
        self.hdd = None  # in gigabytes
        self.gpu = None
        self.touch_screen = None

    def __str__(self):
        info = (f'Serial number: {self.serial}', f'Touch screen: {self.touch_screen}', f'Memory: {self.memory}GB', f'Hard Disk: {self.hdd}GB', f'Graphics Card: {self.gpu}')
        return '\n'.join(info)


class ComputerBuilder:
    serial_counter = 0

    def __init__(self):
        serial_number = ComputerBuilder.serial_counter
        ComputerBuilder.serial_counter += 1
        self.computer = Computer(serial_number)

    def configure_touch_screen(self, is_touch_screen):
        self.computer.touch_screen = is_touch_screen

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory: int, hdd: int, gpu: str, touch_screen: bool):
        self.builder = ComputerBuilder()
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)
        self.builder.configure_touch_screen(touch_screen)

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti', touch_screen=False)
    computer = engineer.computer
    print(f"Computer:\n{computer}\n")

    engineer.construct_computer(hdd=64, memory=2, gpu='Snapdragon', touch_screen=True)
    tablet = engineer.computer
    print(f"Tablet:\n{tablet}\n")


if __name__ == '__main__':
    main()
