import tkinter as tk #importing tkinter for GUI
from datetime import datetime  # importing datetime from datetime module for current date and time
import re  # importing regular expression module for pattern matching

def send_message():  #define function to take input from user
    user_input = entry.get().lower()  #get user input and convert it to lowercase for case insensitive matching
    if not user_input:  
        return  
    
    chat_log.config(state='normal') #enable chat log in normal state to allow text insertion
    chat_log.insert(tk.END, "You: " + entry.get() + "\n") #insert user input in chat log

    response = ""  #initialize response variable to store chatbot response
  
#check exit or quit command
    if user_input in ["exit", "quit"]:  
        response = "Goodbye! Have a nice day."
        chat_log.insert(tk.END, "ChatEase: " + response + "\n")
        chat_log.config(state='disabled')
        root.after(1000, root.destroy)  
        return

#check for greetings 
    greetings = ["hello", "hi", "hey"]
    if any(user_input.startswith(greet) for greet in greetings):
        response = "Hello there! How can I assist you?"

#check elif for specific phrases    
    elif "your name" in user_input:
        response = "My name is ChatEase. What is your name?"

    elif "my name is" in user_input:
        response = "Nice name! How can I assist you today🤖?"

    elif "how are you" in user_input:
        response = "I'm just a program, but thanks for asking! How can I help you?"  
    
    elif "created you" in user_input or "made you" in user_input:
        response = "I was created by Ayesha Malik."
   
    elif "date" in user_input or "day" in user_input:
        today = datetime.now()
        day_name = today.strftime("%A")
        date_str = today.strftime("%B %d, %Y")
        response = f"Today is {day_name}, {date_str}."
   
    elif "bye" in user_input or "see you" in user_input or "goodbye" in user_input:
        response = "Goodbye! It was nice talking to you."
    
# here we use regex to check for specific patterns to solve math problems    
    elif re.fullmatch(r'[\d\+\-\*/\.\s]+', user_input):
        try:
            result = eval(user_input)
            response = f"The answer is {result}"
        except Exception:
            response = "Sorry, I can't compute that."
    else:
        response = "I'm sorry, I don't understand that."

    
    chat_log.insert(tk.END, "ChatEase: " + response + "\n")  #insert chatbot response in chat log
    chat_log.config(state='disabled') #disable chat log to prevent user from editing it
    entry.delete(0, tk.END)  #clear the entry box

#Window setup
root = tk.Tk()
root.title("ChatEase")  
root.configure(bg="#f0f0f0")  #set background color light grey

#Set window size and set chatbox and text color
chat_log = tk.Text(root, state='disabled', width=65, height=25, wrap='word',
                   bg="#ffffff", fg='#000000')  
chat_log.grid(row=0, column=0, columnspan=2, padx=15, pady=3)

#set scrollbar for scrolled a chat
scrollbar = tk.Scrollbar(root, command=chat_log.yview)
scrollbar.grid(row=0, column=2, sticky='ns', pady=10)
chat_log['yscrollcommand'] = scrollbar.set

#set entery box for user input and set it's background and text color
entry = tk.Entry(root, width=70, bg='#ffffff', fg='#000000')
entry.grid(row=1, column=0, padx=5, pady=5, sticky='ew')

#set send button and set it's background and text color
send_button = tk.Button(root, text="Send", command=send_message,
                        bg="#005eff", fg='#ffffff')  # Blue background, white text
send_button.grid(row=1, column=1, padx=10, pady=10)

#bind the enter key to send message function
root.bind('<Return>', lambda event: send_message())

#set the welcome message in chat log
chat_log.config(state='normal')
welcome_message = "👋 Hi! I am ChatEase 🤖 your AI chatbot. How can I assist you today?"
chat_log.insert(tk.END, "ChatEase: " + welcome_message + "\n")
chat_log.config(state='disabled')

#start the main loop for the GUI
root.mainloop()
