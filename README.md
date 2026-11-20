# Requisition System

## Project Description
This is a basic Requisition System programmed using Python and the OOP concept for the BACT7501 Software Development Project.

The system lets staff enter a requisition for items from the terminal and calculates the total price. Requests under $500 are approved automatically, and a manager can respond to the pending ones. It also shows the details and statistics of all requisitions.

## Features
- Staff enter their date, staff ID and staff name from the terminal.
- A unique requisition ID is created for each requisition (starting from 10001).
- Add items with their prices.
- Calculate the total price.
- Approve requests less than $500 automatically and give an approval reference number.
- Keep requests of $500 or more as Pending.
- Manager can approve, not approve or leave pending requests.
- Show information about all requisitions.
- Show statistics about requisitions.

## Technologies Used
- Python (classes and objects)
- Visual Studio Code
- Git and GitHub

## Running the Program
1. Download or clone this repository.
2. Open the project folder in Visual Studio Code.
3. Open the Terminal.
4. Enter the following command:

```bash
python requisition.py
```

## How to Use
1. Enter how many requisitions you want to add.
2. For each requisition, enter the Date, Staff ID and Staff Name.
3. Enter each item name and price. Type `yes` to add another item or `no` to finish.
4. The program shows the total, status and approval reference number.
5. All requisitions and statistics are displayed.
6. For each pending requisition, the manager types `Approved`, `Not Approved` or `Pending`.
7. The updated requisitions and statistics are displayed.

## Approval Rules
- Less than $500: Automatically Approved.
- $500 or more: Pending.
- Manager can approve or not approve pending requests.
- Approval reference number = Staff ID + last three digits of the Requisition ID (for example FN19001).

## Testing
The program was tested by entering 5 requisitions in the terminal:
- Requisitions under $500 to test automatic approval.
- A requisition of exactly $500 to test that it stays Pending.
- Requisitions over $500 to test pending requests.
- Manager response to test approving, not approving and leaving a request pending.
- Statistics were checked before and after the manager response.

## Author
Name: Sandun Tharaka

Course: BACT7501

Project: Assessment 2 - Requisition System
