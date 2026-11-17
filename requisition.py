
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

    # Add items and calculate total
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

    # Check Automatic Approvals
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
        @classmethod
        def display_all_requisitions(cls):
            for requisition in cls.all_requisitions:
                requisition.display_requisition()

    # Display requisition statistics
    @classmethod
    def requisition_statistics(cls):
        total_count = len(cls.all_requisitions)
        approved_count = 0
        pending_count = 0
        not_approved_count = 0

        for requisition in cls.all_requisitions:

            if requisition.status == "Approved":
                approved_count += 1

            elif requisition.status == "Pending":
                pending_count += 1

            elif requisition.status == "Not approved":
                not_approved_count += 1

        print("\nDisplaying the Requisition Statistics\n")

        print("The tot number of Requisitions submitted:", total_count)

        print("The tot number of Approved requisitions:", approved_count)

        print("The tot number of Pending Requisitions:", pending_count)

        print("The tot number of not Approved Requisitions:", not_approved_count)


# FIVE REQUISITIONS


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


# Display statistics-------------------------
Requisition.requisition_statistics()