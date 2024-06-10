#Task 1

        #Open a new service ticket.
        #Update the status of an existing ticket  to "closed".
        #Display all tickets.

service_tickets = {
    1: {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    2: {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

'''
1- Open a new service ticket
2- Update the status to "closed"
3- Display all tickets'''

def next_id():              #Created a function that will return an id I can use to make a new service ticket
    last_id = 0
    for id in service_tickets.keys():
        if id > last_id:
            last_id = id

    return last_id + 1

def new_ticket():
    while True:
        new_id = next_id()
        customer = input("Please enter the customer name: \n")
        issue = input("Please state the issue: \n")
        print(f"Is this information correct: \nName: {customer} \nIssue: {issue}")
        correct = input("Does this information look correct? y/n").lower()
        if correct == 'y':
            service_tickets[new_id] = {'Customer': customer, 'Issue': issue, 'Status': 'Open'}
            break       
        else:           #Go back to the top
            continue

def status_update():
    while True:
        try:
            print(service_tickets)
            update = int(input('Enter the number for the ticket you want to close: \n'))
            if update in service_tickets:
                service_tickets[update]['Status'] = "Closed"
                print(service_tickets[update])
                confirmation = input('Does this look correct?\nYes or No').upper()
                if confirmation == "YES":
                    break
                else:
                    continue
        except:
            print('Enter a valid numeber!')
            continue





        

def main():
    while True:
        ans = input('''
SERVICE TICKET MANAGER\n                    
1- Open a new service ticket
2- Update the status to "closed"
3- Display all tickets
4- Quit
''')
        if ans == '1':
            new_ticket()
        elif ans == '2':
            status_update()    #Function to update and existing ticket
        elif ans == '3':
            for key in service_tickets:
                print(key, ' : ', service_tickets[key])
        
            #Function to display all current tickets
        elif ans == '4':
            print("Thanks for making a service ticket. Have a great day and we will be in touch soon!")
            break


main()

# customer = input("What is your name: ").title

# for customer in service_tickets.values():
#      if customer 