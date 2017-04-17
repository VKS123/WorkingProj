# import tkinter as tk
#
# root = tk.Tk()
#
# status = tk.Label(root, text="Working")
# status.grid()
#
# def update_status(w):
#
#     # Get the current message
#     current_status = status["text"]
#
#     # If the message is "Working...", start over with "Working"
#     if current_status.endswith("..."): current_status = w
#
#     # If not, then just add a "." on the end
#     else: current_status += "."
#
#     # Update the message
#     status["text"] = current_status
#
#     # After 1 second, update the status
#     root.after(1000, update_status,'work')
#
# # Launch the status message after 1 millisecond (when the window is loaded)
# root.after(1, update_status,'work')
#
# root.mainloop()

try:
    from Tkinter import Frame, Entry, Tk
except ImportError:
    from tkinter import Frame, Entry, Tk

root = Tk()
frame1 = Frame(root, highlightbackground="green", highlightcolor="green", highlightthickness=1, width=100, height=100,
               bd=10)
frame1.pack()
frame1.pack_propagate(False)

Entry(frame1).pack()

frame2 = Frame(root, highlightbackground="red", highlightcolor="red", highlightthickness=1, width=100, height=100, bd=0)
frame2.pack()
frame2.pack_propagate(False)

Entry(frame2).pack()

root.mainloop()