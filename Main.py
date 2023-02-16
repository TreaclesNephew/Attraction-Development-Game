import tkinter as tk
from tkinter import ttk

# Define a list of prefabricated rides
ride_options = [
    {"name": "Roller Coaster", "cost": 50},
    {"name": "Ferris Wheel", "cost": 20},
    {"name": "Water Slide", "cost": 35},
    {"name": "Carousel", "cost": 15}
]

# Set up the initial game state
budget = 100
rides = []

# Create the main window
root = tk.Tk()
root.title("Attraction Manufacturing Company Game")

# Create a label to display the player's budget
budget_label = tk.Label(root, text=f"Budget: ${budget}")
budget_label.pack()

# Create a listbox to display the player's rides
rides_label = tk.Label(root, text="Rides:")
rides_label.pack()
ride_listbox = tk.Listbox(root)
ride_listbox.pack()

# Create a frame for the ride customization controls
custom_frame = tk.Frame(root)
custom_frame.pack()

# Create a label and entry box for the ride name
name_label = tk.Label(custom_frame, text="Ride Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(custom_frame)
name_entry.grid(row=0, column=1)

# Create a label and entry box for the ride cost
cost_label = tk.Label(custom_frame, text="Ride Cost:")
cost_label.grid(row=1, column=0)
cost_entry = tk.Entry(custom_frame)
cost_entry.grid(row=1, column=1)

# Create a dropdown menu to select a prefabricated ride
ride_var = tk.StringVar()
ride_var.set(ride_options[0]["name"])  # Set default option to first ride in the list
ride_menu = ttk.OptionMenu(custom_frame, ride_var, *list(map(lambda x: x["name"], ride_options)))
ride_menu.grid(row=2, column=0)

# Create a button to buy a new ride
def buy_ride():
    global budget
    global rides
    ride_cost = int(cost_entry.get())
    if budget >= ride_cost:
        budget -= ride_cost
        new_ride = name_entry.get() if name_entry.get() else ride_var.get()
        rides.append((new_ride, ride_cost))
        ride_listbox.insert(tk.END, f"{new_ride} (${ride_cost})")
        budget_label["text"] = f"Budget: ${budget}"

buy_button = tk.Button(custom_frame, text="Buy new ride", command=buy_ride)
buy_button.grid(row=2, column=1)

# Create a button to remove a ride
def remove_ride():
    global budget
    global rides
    selected_ride = ride_listbox.curselection()
    if selected_ride:
        selected_ride = selected_ride[0]
        ride_to_remove = rides[selected_ride]
        rides.pop(selected_ride)
        ride_listbox.delete(selected_ride)
        budget += int(ride_to_remove[1] * 0.5)
        budget_label["text"] = f"Budget: ${budget}"

remove_button = tk.Button(custom_frame, text="Remove ride", command=remove_ride)
remove_button.grid(row=3, column=0)

# Run the main event loop
root.mainloop()
