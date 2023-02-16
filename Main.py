import csv
import tkinter as tk
from tkinter import ttk

class Ride:
    def __init__(self, tech, rtype, vtype, name, capacity, max_speed, max_height, max_length, max_gforce):
        self.tech = tech
        self.type = rtype
        self.vehicle_type = vtype
        self.name = name
        self.capacity = capacity
        self.max_speed = max_speed
        self.max_height = max_height
        self.max_length = max_length
        self.max_gforce = max_gforce

def read_ride_data():
    ride_list = []
    with open('ride_data.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row in reader:
            tech = row[0]
            rtype = row[1]
            vtype = row[2]
            name = row[3]
            capacity = row[4]
            max_speed = row[5]
            max_height = row[6]
            max_length = row[7]
            max_gforce = row[8]
            ride_list.append(Ride(tech, rtype, vtype, name, capacity, max_speed, max_height, max_length, max_gforce))
    return ride_list

def display_ride_data(ride_list):
    root = tk.Tk()
    root.title('Ride Data')

    table = ttk.Treeview(root, columns=('Technology', 'Type', 'Vehicle Type', 'Name', 'Capacity', 'Max Speed (m/s)', 'Max Height (m)', 'Max Length (m)', 'Max G-Force'))
    table.heading('#0', text='Index')
    table.heading('Technology', text='Technology')
    table.heading('Type', text='Type')
    table.heading('Vehicle Type', text='Vehicle Type')
    table.heading('Name', text='Name')
    table.heading('Capacity', text='Capacity')
    table.heading('Max Speed (m/s)', text='Max Speed (m/s)')
    table.heading('Max Height (m)', text='Max Height (m)')
    table.heading('Max Length (m)', text='Max Length (m)')
    table.heading('Max G-Force', text='Max G-Force')
    table.column('#0', width=50)
    table.column('Technology', width=120)
    table.column('Type', width=120)
    table.column('Vehicle Type', width=120)
    table.column('Name', width=120)
    table.column('Capacity', width=120)
    table.column('Max Speed (m/s)', width=120)
    table.column('Max Height (m)', width=120)
    table.column('Max Length (m)', width=120)
    table.column('Max G-Force', width=120)
    table.grid(row=0, column=0)

    for i, ride in enumerate(ride_list):
        table.insert('', 'end', text=i, values=(ride.tech, ride.type, ride.vehicle_type, ride.name, ride.capacity, ride.max_speed, ride.max_height, ride.max_length, ride.max_gforce))

    root.mainloop()

ride_list = read_ride_data()
display_ride_data(ride_list)
