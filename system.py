from ticketobject import Ticket
from colors import bcolors
from status import status

    



class Ticket_system():

  def __init__(self):
      self.tickets = []
      self.counter = 2000;
      
      # DUMMY DATA
      t = Ticket(self.counter, "INNAM", "Inna", "inna@whitecliffe.co.nz", "My monitor stopped working", )
      self.counter += 1;
      self.tickets.append(t)

      t = Ticket(self.counter, "MARIAH", "Maria", "maria@whitecliffe.co.nz", "Request for a videocamera to conduct webinars", )
      self.counter += 1;
      self.tickets.append(t)


  def change_status(self):
      print(bcolors.OKBLUE + "****** REOPEN TICKET ******" + bcolors.ENDC )
      id = int(input("Please enter the Ticket id:  "))
      
      for t in self.tickets:
          #for only closed...
            if (t.ticket_id == id) and (t.ticket_status == status.CLOSED):
                t.ticket_status = status.OPEN
                t.display();
                
  

  def create_ticket(self):
      print("\n\n\n\n\n")
      print(bcolors.OKBLUE + "****** ENTER NEW TICKET ******" + bcolors.ENDC )
      staff_id = input("What is your Staff I.D?  ")
      ticket_creator_name = input("What is your name? ")
      email = input("What is your Email Address:  ")
      description = input("Please enter the issue description:  ")
      print(bcolors.OKGREEN + "****** TICKET SUBMITTED ******" + bcolors.ENDC)
      print("\n\n\n\n\n")


      # create a new instance of the ticket class and append it to the ticket list
      t = Ticket(self.counter, staff_id, ticket_creator_name, email, description, )
      self.counter += 1;
      self.tickets.append(t)

  def print_all_tickets(self):
      if self.tickets == []:
          print("There are no tickets availible :(")
      else: 
        for t in self.tickets:
            t.display();
      
  def respond_ticket(self):
      print("\n\n\n\n\n")
      print(bcolors.OKBLUE + "****** TICKET RESPONSE ******" + bcolors.ENDC )
      id = int(input("Please enter the Ticket id:  "))

      
      for t in self.tickets:
          
            if t.ticket_id == id:
                t.display();
                res = input("What is your response? ")
                t.response = res
                t.ticket_status = status.CLOSED


  def ticket_stats(self):
      open_counter = 0
      sub_counter = 0
      close_counter = 0


      for t in self.tickets:
          if t.ticket_status == status.OPEN:
              open_counter += 1
          if t.ticket_status == status.SUBMITTED:
              sub_counter += 1
          if t.ticket_status == status.CLOSED:
              close_counter += 1
              
      total = open_counter + sub_counter + close_counter

      print("\n\n\n\n\n")
      print(bcolors.OKBLUE + "****** TICKET STATISTICS ******"  + bcolors.ENDC)
      print("TICKETS " + status.OPEN + ":  ", open_counter)
      print("TICKETS " + status.SUBMITTED + ":  ", sub_counter)
      print("TICKETS " + status.CLOSED + ":  ", close_counter)
      print("************************")
      print("TOTAL: " + str(total) )
      print("\n\n\n\n\n")





            
            
      





