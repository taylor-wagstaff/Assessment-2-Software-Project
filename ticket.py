
class Ticket_system():

  def __init__(self):
      self.tickets = []
      self.response = ["Not Yet Provided"]


  def create_ticket(self):
      print("                    ")
      print("                    ")
      print("                    ")
      print("                    ")
      print("****** Enter New Ticket ******")
      staff_id = input("What is your Staff I.D?  ")
      ticket_creator_name = input("What is your name? ")
      email = input("What is your Email Address:  ")
      description = input("Please enter the issue description:  ")
      print("****** Ticket Submitted ******                    ")
      print("                    ")
      print("                    ")
      print("                    ")
  
      # create a new instance of the ticket class and append it to the ticket list
      t = Ticket(staff_id, ticket_creator_name, email, description )
      self.tickets.append(t)

  def print_all_tickets(self):
      if self.tickets == []:
          print("There are no tickets availible :(")
      else: 
        for t in self.tickets:
            t.display();
      
  def response(self):
      print("                    ")
      print("****** Ticket Response ******")
      self.response = input("What is your response? ")
      # t = Ticket()
      





class Ticket():
    counter = 0
    ticket_id: None;
    ticket_status: None;
    staff_id: None;
    ticket_creator_name: None;
    email: None;
    description: None;
    response: None;
    

    #a class constructor, intialise all our attributes
    def __init__(self, staff_id, ticket_creator_name, email ="", description="", response="", ticket_id="", ticket_status="" ):
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.email = email
        self.description = description
        self.response = response 
        self.ticket_id = Ticket.counter + 2000
        self.ticket_status = ticket_status
        Ticket.counter += 1
         

    #methods, self is a varible which allows access to attributes
    def display(self):
        print("                    ")
        print("                    ")
        print("****** Ticket ******")
        print("Ticket ID: ", self.ticket_id)
        print("Ticket Status: ", self.ticket_status)
        print("Staff ID: ", self.staff_id)
        print("Ticket Creator: ", self.ticket_creator_name)
        print("Email: ", self.email)
        print("Description: ", self.description)
        print("Response: ", self.response)
        print("                    ")
        print("                    ")


        


    def password_change(self):
        #If the ticket’s description of the issue 
        # contains the words “Password Change”, 
        # the new password should be generated 
        # following the rule,
        #######
        # The first two characters of the staffID, 
        # followed by the first three characters 
        # of the ticket creator name.
        # consider: split(), join(), string operations)
        print("password change")


      