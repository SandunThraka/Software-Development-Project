class requisition:
    requisition_counter = 10000

    def __init__(self, staff_id):
        requisition.requisition_counter +=1
        self.staff_id = staff_id
        self.requisition_id = requisition.requisition_counter
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Pending Approval"
        requisition.all_requisitions.append(self)

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

    def check_approval(self):
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference = "APR-" + str(self.requisition_id)
        else:
            self.status = "Pending"
            self.approval_reference = "Pending Approval"
    def manager_response(self, response):
        if self.status == "Pending":
            if response == "approve":
                self.status = "Approved"
                self.approval_reference = "APR-" + str(self.requisition_id)

            elif response == "reject":
                self.status = "Not approved"
                self.approval_reference = "Rejected"

            else:
                print("Invalid manager response")

        else:
            print("This requisition does not need a manager response")

    def display_requisition(self):
        print("\nRequisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Items:", self.items)
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference:", self.approval_reference)


r1 = requisition("S001")
r1.cal_requisition("Key", 2, 10)
r1.check_approval()
r1.manager_response("approve")
r1.display_requisition()




