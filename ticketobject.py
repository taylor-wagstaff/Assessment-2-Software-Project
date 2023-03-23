from colors import bcolors
from status import status

class Ticket():
    ticket_id: None;
    ticket_status: None;
    staff_id: None;
    ticket_creator_name: None;
    email: None;
    description: None;
    response: None;
    

    #a class constructor, intialise all our attributes
    def __init__(self, ticket_id, staff_id="", ticket_creator_name="", email ="", description="", response="Not Yet Provided"  ):
        self.staff_id = staff_id
        self.ticket_creator_name = ticket_creator_name
        self.email = email
        self.description = description
        self.response = response 
        self.ticket_id = ticket_id
        self.ticket_status = status.SUBMITTED
        #set function inside the class
        self.password_change()
        
        
    #methods, self is a varible which allows access to attributes
    def display(self):
        print("\n\n")
        print(bcolors.HEADER + "****** TICKET ******" + bcolors.ENDC)
        print("Ticket ID: ", self.ticket_id)
        print("Ticket Status: ", self.ticket_status)
        print("Staff ID: ", self.staff_id)
        print("Ticket Creator: ", self.ticket_creator_name)
        print("Email: ", self.email)
        print("Description: ", self.description)
        print("Response: ", self.response)
        print("\n\n")
        

    def password_change(self):
        substring1 = "password"
        substring2 = "change"


        if (substring1 in self.description.lower()) and (substring2 in self.description.lower()):
            print(bcolors.OKGREEN + "****** PASSWORD CHANGED ******" + bcolors.ENDC)
            
            id = self.staff_id[0:2]
            id2 = self.ticket_creator_name[0:3]

            new_password = id + id2
            self.response = "your new password is: " + new_password
            self.ticket_status = status.CLOSED

