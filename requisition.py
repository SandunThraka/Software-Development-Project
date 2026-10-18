class Requisition:

    requisition_counter = 10000
    requisitions = []

    # Initialise requisition information
    def __init__(self, date, staff_id, staff_name):
        Requisition.requisition_counter = Requisition.requisition_counter + 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = Requisition.requisition_counter

        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

        Requisition.requisitions.append(self)

    # Task 1: Add items and calculate the total
    def add_requisition(self, items):
        self.items = items
        self.total = 0

        for item in self.items:
            self.total = self.total + item[1]

        return self.total

    
