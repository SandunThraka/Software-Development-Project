class Requisition:

    requisition_counter = 10000
    requisitions = []

   ###innitialize requisitions ############
    def __init__(self, date, staffId, staffName):

        Requisition.requisition_counter = Requisition.requisition_counter + 1
        self.date = date
        self.staffId = staffId
        self.staffName = staffName
        self.requisitionId = Requisition.requisition_counter

        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approvalReference = "Not Available"

        Requisition.requisitions.append(self)

    #### Task 1: Ask for item and calculate the tot ######
    def cal_requisition(self):
        print("Requisition ID:", self.requisitionId)
        print("--------------Add your item----------------")

        anotherItem = "yes"

        while anotherItem  == "yes":
            itemName = input("Item Name:: ")
            itemPrice = float(input("Item Price: "))

            self.items.append([itemName, itemPrice])
            self.total = self.total + itemPrice

            anotherItem = input("Add another item (yes/no): ")

        print("Total: $" + str(self.total))
        return self.total

    # #####Task 2: Automatically approve requisitions under $500 ###############
    def approve_requisition(self):
        if self.total < 500:
            self.status = "Approved"

            lastThree = str(self.requisitionId)[-3:]
            self.approvalReference = self.staffId + lastThree
        else:
            self.status = "Pending"
            self.approvalReference = "Not Available"

        print("Status:", self.status)
        print("Approval Reference Number:", self.approvalReference)

    ###### Task 3: Allowing manager to respond to pending requisition #####################
    def respond_requisition(self, response):
        if self.status == "Pending":
            if response == "Approved":
                self.status = "Approved"

                lastThree = str(self.requisitionId)[-3:]
                self.approvalReference = self.staffId + lastThree

            elif response == "Not Approved":
                self.status = "Not Approved"
                self.approvalReference = "Not Available"

            elif response == "Pending":
                self.status = "Pending"

            else:
                print("Invalid response.")

        else:
            print("This requisition already processed.")

    ######### Task 4: Displaying all requisitions ################################
    def display_requisitions(self):
        print("\n--- ALL REQUISITION DETAILS ---")

        for requisition in Requisition.requisitions:
            print("\nDate:", requisition.date)
            print("Requisition ID:", requisition.requisitionId)
            print("Staff ID:", requisition.staffId)
            print("Staff Name:", requisition.staffName)
            print("Total: $" + str(requisition.total))
            print("Status:", requisition.status)
            print("Approval Reference Number:",
                  requisition.approvalReference)

    ############ Task 5: Display Requisition Statistics #############################
    def requisition_statistics(self):
        totalRequisitions = len(Requisition.requisitions)
        approved = 0
        pending = 0
        notApproved = 0

        for requisition in Requisition.requisitions:
            if requisition.status == "Approved":
                approved = approved + 1
            elif requisition.status == "Pending":
                pending = pending + 1
            elif requisition.status == "Not Approved":
                notApproved = notApproved + 1

        print("\n--- REQUISITION STATISTICS ---")
        print("The total number of requisitions submitted:", totalRequisitions)
        print("The total number of approved requisitions:", approved)
        print("The total number of pending requisitions:", pending)
        print("The total number of not approved requisitions:", notApproved)


############ Staff enter their data ###############
number = int(input("How many requisitions do you want to enter? "))

for i in range(number):
    print("\nEnter your information for requisition", i + 1)
    date = input("Date: ")
    staffId = input("Staff ID: ")
    staffName = input("Staff Name: ")

    r = Requisition(date, staffId, staffName)
    r.cal_requisition()
    r.approve_requisition()

# Display requisitions and statistics
r.display_requisitions()
r.requisition_statistics()


##########  Manager responds to pending requisitions #############
print("\n--- MANAGER RESPONSE ---")

for requisition in Requisition.requisitions:
    if requisition.status == "Pending":
        print("\nRequisition ID:", requisition.requisitionId)
        print("Staff Name:", requisition.staffName)
        print("Total: $" + str(requisition.total))

        response = input("Enter Approved, Not Approved or Pending : ")
        requisition.respond_requisition(response)


#####  Display updated requisition############**********************
r.display_requisitions()
r.requisition_statistics()
