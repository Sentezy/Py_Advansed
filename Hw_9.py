from multiprocessing import Process, Pipe
from time import sleep
from os import getpid


def ponger(receiver, sender, response):
    while True:
        print(f"Process {getpid()} got message: {receiver.recv()}")
        sleep(2)
        sender.send(response)


if __name__ == "__main__":
    receiver_1, sender_1 = Pipe()
    receiver_2, sender_2 = Pipe()

    sender_1.send("ping")
    process_1 = Process(target=ponger, args=(receiver_2, sender_1, "ping")).start()
    process_2 = Process(target=ponger, args=(receiver_1, sender_2, "pong")).start()

