# Assessment-2-Software-Project
Taylor's Assessment 2: Software Project


This assessment represents 50% of your final grade.

# Assessment Overview
Think about the Software Project like a piece of art, only you're creating a Software Project based on your own technical research and emerging practice.

Learning Outcomes
LO1: Develop program logic to a professional working brief.

LO2: Apply the stages of software development to develop a simple code solution. 

Conditions
It is recommended that you spend between 20 and 25 hours on this assignment. It is better to
add content as you find it, rather than at the end.
All course materials, and any other resources, can be used to complete this assessment.
The work you submit must be your own work. It is an individual assessment.

You can ask your facilitator to clarify the instructions, and/or for advice, but they cannot do or solve the assessment tasks – you must carry out the tasks yourself!

# Assessment Instructions
This assessment gives hands-on experience of the language of the Software Development Fundamentals. 

1. Please read the scenario below and apply code solutions to develop a Help Desk ticketing system prototype.  
2. Record the stages of the Software Development Life Cycle (SDLC) and include with the submission of your Software Project.

It is valuable to record your experiences during the Software Development Lifecycle (SLDC), which is why we ask you to submit this with your  Software Project.   These experiences will help you to professionally communicate and contextualize your practice as a professional and build confidence in your technical skills and practice. 

# Scenario 
Help Desk Ticketing System Prototype

Client Requirements

The client would like a Help Desk ticketing system prototype developed.

The Help Desk ticketing system should handle tickets from internal customers only.

Tickets will be requested for assistance from the Help Desk by staff members of the organisation.

 

# Requirements of the Help Desk Ticketing System

Tickets:

Tickets can be submitted by providing all of the following information:
Staff ID,
Ticket creator name,
Contact email
Description of the issue
 Internal Tickets’ ticket number should be assigned automatically using the counter static field plus 2000.

 All information must be provided as input while submitting the ticket.

# Responding to tickets:

If the ticket’s description of the issue contains the words “Password Change”, the new password should be generated following the rule,
The first two characters of the staffID, followed by the first three characters of the ticket creator name.
Hint: (can be useful to consider: split(), join(), string operations)

 

There should be an option, after the ticket has been submitted, to respond to a ticket by providing a feedback response.
Default response can be set as “Not Yet Provided”.                                                                                                                                                                                                                                            

# Statistics:

There should be a way to keep track of:
The number of tickets submitted
The number of resolved tickets
The Number of open tickets
A way to display those statistics to the console.
 

If the staff member has submitted the “Password change” request, after the new password is generated and the ticket’s response has been updated, the ticket should close, with the number of closed tickets increased and the number of open tickets reduced by 1. Ticket’s status should be changed to “Closed”.
 

Once a member of the IT department provides the response to a ticket, the ticket should close, with the number of closed tickets increased and the number of open tickets reduced by 1. Ticket’s status should be changed to “Closed”.
 

There should be an option for the IT department to reopen the ticket. At this point the number of open tickets should be increased and the number of closed tickets should be reduced by 1. Ticket’s status should be changed to “Reopened”
 

# Displaying the ticket:

There should be a way to display the ticket information:
Ticket number,
Name of the ticket’s creator,
StaffID,
Email address,
Description of the issue,
Response from the IT department and ticket status (open, closed or reopened).
 

The output format is shown in the examples at the end of Technical Requirements section.

                                                                                                                                     

# Technical Requirements

The senior developer has provided you with the following technical requirements for the project.

The Ticket class should contain common ticket information in the Ticket class.
The Ticket class should also have method allowing the staff to submit ticket and the IT team to respond to the tickets, specifically resolve, reopen and provide a response to the ticket.
The Ticket class should contain a method for resolving password change requests. As well as calling the method that would generate the new password, it should set up a response for the ticket and change the ticket status to closed.
There should be a method to print information for all the ticket objects.
             Hint: research and use List<Ticket>

The TicketStats method in Ticket class should contain information on ticket statistics and shall be able to return the statistics information.
The main class, containing the Main method.
Create at least one instance of submitting tickets and include at least one ticket with the request of “Password change”.
After the tickets are created, display ticket statistics.
Resolve some of the tickets, then display the ticket information and ticket statistics. o Reopen some of the resolved tickets, then display the ticket information and ticket statistics.
 

The example output is provided below:
Displaying Ticket Statistics

Tickets Created: 3

Tickets Resolved: 1

Tickets To Solve: 2

Printing Tickets:

Ticket Number: 2001

Ticket Creator: Inna

Staff ID: INNAM

Email Address: inna@whitecliffe.co.nz

Description: My monitor stopped working

Response: Not Yet Provided

Ticket Status: Open

 

Ticket Number: 2002

Ticket Creator: Maria

Staff ID: MARIAH

Email Address: maria@whitecliffe.co.nz

Description: Request for a videocamera to conduct webinars

Response: Not Yet Provided

Ticket Status: Open

 

Ticket Number: 2003

Ticket Creator: John

Staff ID: JOHNS

Email Address: john@whitecliffe.co.nz

Description: Password change

Response: New password generated: JOJoh

Ticket Status: Closed

 

Displaying Ticket Statistics

Tickets Created: 3

Tickets Resolved: 2

Tickets To Solve: 1

 

Printing Tickets:

Ticket Number: 2001

Ticket Creator: Inna

Staff ID: INNAM

Email Address: inna@whitecliffe.co.nz

Description: My monitor stopped working

Response: The monitor has been replaced.

Ticket Status: Closed

 

Ticket Number: 2002

Ticket Creator: Maria

Staff ID: MARIAH

Email Address: maria@whitecliffe.co.nz

Description: Request for a videocamera to conduct webinars

Response: Not Yet Provided

Ticket Status: Open