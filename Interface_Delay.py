#!/usr/bin/python3
import os
import tkinter as tk
import subprocess

my_gui = tk.Tk()

entry1 = tk.StringVar()
entryI = tk.StringVar()
entryT = tk.StringVar()

my_gui.geometry('600x600')
my_gui.title("Ping Delay")

lp=tk.Label(my_gui, text="Enter target IP or host as required.")
lp.place(x=350, y=130)
ep=tk.Entry(my_gui, textvariable=entry1)
ep.place(x=380, y=150)

li=tk.Label(my_gui, text="Enter target Interface")
li.place(x=65, y=80)
ei=tk.Entry(my_gui, textvariable=entryI)
ei.place(x=50, y=100)
lt=tk.Label(my_gui, text="Enter Delay Value with ms")
lt.place(x=45, y=180)
et=tk.Entry(my_gui, textvariable=entryT)
et.place(x=50, y=200)



def delay_fun():
    cmd = ["sudo", "tc", "qdisc", "add", "dev", entryI.get(), "root", "netem", "delay", entryT.get()]
    subprocess.run(cmd)
    return

def ping():
    png = ["ping", entry1.get(), "-c", "5"]
    output = subprocess.check_output(png)

    print('>', output)
    # put result in label
    result['text'] = output.decode('utf-8')

    return

def delay_res():
    subprocess.run("sudo tc qdisc del dev {} root".format(entryI.get()), shell=True)
    return

b1=tk.Button(my_gui, text="Delay", command=delay_fun)
b2=tk.Button(my_gui, text="Ping", command=ping)
b3=tk.Button(my_gui, text="Reset", command=delay_res)
b1.place(x=100, y=230)
b2.place(x=400, y=230)
b3.place(x=250, y=230)

exp = tk.Label(my_gui, text="Have to add this Line in /etc/sudoers file\n <username> ALL=(ALL) NOPASSWD:<python script directory>, /usr/sbin/tc", fg="red")
exp.place(x=0, y=0)
result = tk.Label(my_gui)
result.place(x=100, y=300)


my_gui.mainloop()
