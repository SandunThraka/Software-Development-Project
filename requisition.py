
class Requisition:
    requisition_counter = 10000
    all_requisitions = []

    def __init__(self, date, staff_id, staff_name):
        Requisition.requisition_counter += 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.requisition_counter
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

        Requisition.all_requisitions.append(self)

    ### Add items and calculate total
    def cal_requisition(self, item_name, quantity, price):
        item_total = quantity * price

        item = {
            "name": item_name,
            "quantity": quantity,
            "price": price,
            "total": item_total
        }

        self.items.append(item)
        self.total += item_total

   ## # Check Automatic Approvals
    def check_approval(self):
        if self.total < 500:
            self.status = "Approved"

            last_three_digits = str(self.requisition_id)[-3:]

            self.approval_reference = self.staff_id + last_three_digits

        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

    # Manager approval || rejection
    def manager_response(self, response):
        if self.status == "Pending":

            if response == "approve":
                self.status = "Approved"

                last_three_digits = str(self.requisition_id)[-3:]

                self.approval_reference = self.staff_id + last_three_digits

            elif response == "reject":
                self.status = "Not approved"
                self.approval_reference = "Not available"

            else:
                print("Invalid manager responses.")

        else:
            print("This req doesn't need manager responses.")

    ## Display onerequisition
    def display_requisition(self):

        print("\nDate:", self.date)
        print("Requisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Staff Name:", self.staff_name)
        print("Total: $" + str(self.total))
        print("Status:", self.status)
        print("Approval Reference Number:", self.approval_reference)

        # Display req
            # Display all requisitions
    def display_all_requisitions(self):
        for requisition in self.all_requisitions:
            requisition.display_requisition()

    # Display requisition statistics
    def requisition_statistics(self):
        approved = 0
        pending = 0
        not_approved = 0

        for requisition in self.all_requisitions:
            if requisition.status == "Approved":
                approved += 1
            elif requisition.status == "Pending":
                pending += 1
            else:
                not_approved += 1

        print("\nDisplaying the Requisition Statistics\n")
        print("Total requisitions:", len(self.all_requisitions))
        print("Approved requisitions:", approved)
        print("Pending requisitions:", pending)
        print("Not approved requisitions:", not_approved)


##### FIVE REQUISITIONS


# Requisition .1
r1 = Requisition("03/04/2024", "FN19", "John Paul")
r1.cal_requisition("Keyboard", 3, 150)
r1.check_approval()


# Requisition .2
r2 = Requisition("05/04/2024", "FN20", "Tracy Brown")
r2.cal_requisition("Laptop", 1, 1000)
r2.check_approval()


# Requisition .3
r3 = Requisition("07/05/2024", "FN15", "Emma Wellington")
r3.cal_requisition("Computer", 1, 3500)
r3.check_approval()
r3.manager_response("reject")


# Requisition .4
r4 = Requisition("03/05/2024", "FN02", "Catlin White")
r4.cal_requisition("Office Supplies", 1, 490)
r4.check_approval()

r5 = Requisition("01/05/2024", "FN025", "Cad Whiter")
r5.cal_requisition("Mouse", 1, 650)
r5.check_approval()

# Display all requisition-------
for requisition in Requisition.all_requisitions:
    requisition.display_requisition()


# Display Statistics-------------------------
r1.display_all_requisitions()
r1.requisition_statistics()