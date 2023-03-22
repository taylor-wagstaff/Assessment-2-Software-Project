from ticket import *


# To Do:

# Display Tickets
# Add Tickets
# Respond to a ticket by providing a feedback response.
# “Password Change”
# Tracking The number of tickets submitted, number of resolved tickets,
# Number of open tickets,A way to display those statistics to the console


if __name__ == "__main__":
    ts = Ticket_system()



while True:
      print("                    ")
      print("****** Menu ******")
      print("[Press 1] To display all Tickets: ")
      print("[Press 2] To add Ticket: ")
      print("[Press 3] To provide a response: ")
      print("[Press 4] To reopen a Ticket: ")
      print("[Press 5] To Display Statistics: ")
      print("[Press 0] Press 0 to Leave: ")
      print("                    ")
      select = int(input("Please make a Selection:  "))

      if select == 1:
          ts.print_all_tickets()
      elif select == 2:
          ts.create_ticket()
      elif select == 3:
          ts.respond_ticket()
      elif select == 4:
          ts.change_status()
      elif select == 5:
          ts.ticket_stats()
      elif select == 0:
          quit()
      elif select != int:
          print("Please enter a valid number")
      else:
          print("Invalid Selection :(")
          






# call the method