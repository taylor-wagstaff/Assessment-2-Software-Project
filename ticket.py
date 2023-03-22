

class Ticket_system():

  def __init__(self):
      self.tickets = []
      self.response = ["Not Yet Provided"]
      self.counter = 2000;
      
      t = Ticket(self.counter, "293245645", "Taylor", "Taylorwasgstaff@gmail.com", "description", )
      self.counter += 1;
      self.tickets.append(t)

      t = Ticket(self.counter, "54321", "Lee", "leee@gmail.com", "help please", )
      self.counter += 1;
      self.tickets.append(t)


  def change_status(self):
      
      id = int(input("What is your ticket number? "))
      
      
      for t in self.tickets:
          #for only closed...
            if t.ticket_id == id:
                t.ticket_status = "OPEN"
                t.display();
                
  

  def create_ticket(self):
      print("/n/n/n/n")
      # print("                    ")
      # print("                    ")
      # print("                    ")
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
      print("                    ")
      print("****** Ticket Response ******")
      id = int(input("What is your ticket number? "))
      
      
      for t in self.tickets:
          
            if t.ticket_id == id:
                t.display();
                var1 = input("What is your response? ")
                t.response = var1
                t.ticket_status = "CLOSED"


  def ticket_stats(self):
      open_counter = 0
      sub_counter = 0
      close_counter = 0


      for t in self.tickets:
          if t.ticket_status == "OPEN":
              open_counter += 1
          if t.ticket_status == "SUBMITTED":
              sub_counter += 1
          if t.ticket_status == "CLOSED":
              close_counter += 1
              
      print("Ticket Statistics")
      print("OPEN: ", open_counter)
      print("SUBMITTED: ", sub_counter)
      print("CLOSE: ", close_counter)




            
            
      





class Ticket():
    ticket_id: None;
    ticket_status: None;
    staff_id: None;
    ticket_creator_name: None;
    email: None;
    description: None;
    response: None;
    

    #a class constructor, intialise all our attributes
    def __init__(self, ticket_id, staff_id="", ticket_creator_name="", email ="", description="", response=""  ):
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.email = email
        self.description = description
        self.response = response 
        self.ticket_id = ticket_id
        self.ticket_status = "SUBMITTED"
        #fucntion inside the class
        self.password_change()
        
         

  

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
        # Response method.
        # Password
        # for resolving password change requests.
        #  As well as calling the method that would 
        # generate the new password, it should set up a response 
        # for the ticket and change the ticket status to closed.
        #If the ticket’s description of the issue 
        # contains the words “Password Change”, 
        # the new password should be generated 
        # following the rule,
        #######
        # The first two characters of the staffID, 
        # followed by the first three characters 
        # of the ticket creator name.
        # consider: split(), join(), string operations)
        
        substring1 = "password"
        substring2 = "change"


        if (substring1 in self.description.lower()) and (substring2 in self.description.lower()):
            print("Found!")
            
            id = self.staff_id[0:2]
            id2 = self.ticket_creator_name[0:3]

            new_password = id + id2
            self.response = new_password
            self.ticket_status = "CLOSED"


    # Method TicketStats
    #  in Ticket class should contain information on 
    # ticket statistics and shall be able to return 
    # the statistics information.

      