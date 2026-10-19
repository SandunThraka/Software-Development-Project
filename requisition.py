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


r1 = requisition("S001")
r1.cal_requisition("Key", 2, 10)
r1.check_approval()


print(r1.total)
print("Status:", r1.status)
print("Reference:", r1.approval_reference)