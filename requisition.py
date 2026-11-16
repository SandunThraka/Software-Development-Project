class Requisition:
    requisition_counter = 10000
    all_requisitions = []

    def __init__(self, staff_id):
        Requisition.requisition_counter +=1
        self.staff_id = staff_id
        self.requisition_id = Requisition.requisition_counter
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Pending Approval"
        Requisition.all_requisitions.append(self)

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
                print("Invalid manager response. Please check your input.")

        else:
            print("This Requisition doesn't need manager responses")

    def display_requisition(self):
        print("\nRequisition ID:", self.requisition_id)
        print("Staff ID:", self.staff_id)
        print("Items:", self.items)
        print("Total: $", self.total)
        print("Status:", self.status)
        print("Approval Reference:", self.approval_reference)

##connect method with class
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

        print("\nRequisition Statistics")
        print("Total:", total_count)
        print("Approved:", approved_count)
        print("Pending:", pending_count)
        print("Not approved:", not_approved_count)
    
        Requisition.requisition_statistics()
## Requisition 1: Under $500
        r1 = Requisition("S100")
        r1.add_requisition("Keyboard", 2, 80)
        r1.check_approval()

## Requisition 2: Under $500
        r2 = Requisition("S101")
        r2.add_requisition("Mouse", 3, 30)
        r2.check_approval()

## Requisition 3: $500 or more
        r3 = Requisition("S102")
        r3.add_requisition("Monitor", 2, 300)
        r3.check_approval()

## Requisition 4: $500 or more
        r4 = Requisition("S103")
        r4.add_requisition("Laptop", 1, 1200)
        r4.check_approval()

## Requisition 5: Exactly $500
        r5 = Requisition("S104")
        r5.add_requisition("Office equipment", 1, 500)
        r5.check_approval()

## Manager responses for pending requisitions
        r3.manager_response("approve")
        r4.manager_response("reject")

## Display result
        Requisition.display_all_requisitions()
        Requisition.requisition_statistics()




