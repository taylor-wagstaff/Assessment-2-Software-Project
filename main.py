from system import *




if __name__ == "__main__":
    ts = Ticket_system()



while True:
      
      print("\n")
      print(bcolors.OKBLUE + "****** MENU ******" + bcolors.ENDC)
      print(bcolors.OKGREEN + "[Press 1]" + bcolors.ENDC + " To display all Tickets: ")
      print(bcolors.OKRED + "[Press 2]" + bcolors.ENDC + " To add Ticket: ")
      print(bcolors.OKYELLOW + "[Press 3]" + bcolors.ENDC + " To provide a response: ")
      print(bcolors.OKVIOLET + "[Press 4]" + bcolors.ENDC + " To reopen a Ticket: ")
      print(bcolors.OKBEIGE + "[Press 5]" + bcolors.ENDC + " To Display Statistics: ")
      print("[Press 0] Press 0 to Leave: ")
      print("\n")
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
          

