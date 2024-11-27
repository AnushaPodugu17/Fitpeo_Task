README for Fitpeo Revenue Calculator Test Script

OVERVIEW:
This script automates the testing of the Fitpeo Revenue Calculator functionality using Selenium. It performs operations like navigating to the Fitpeo website, interacting with the revenue calculator slider, updating input fields, and validating results.

------Prerequisites-----
    1. Python 3.11 installed on your system.
    2. Install selenium 4.10.0
    3. Download the appropriate ChromeDriver version for your Chrome browser and ensure it is added to your system's PATH.(I used ChromeDriver 131.0.6778.85 )

----How to Run------
     1. Clone or Download the script to your local machine using git hub link.
     2. Open the terminal/command prompt.
     3. Run the script using following command:
                 --->> pytest -s task_fitpeo_test.py


----Script Steps---
     1.Opens the Fitpeo homepage.
     2.Navigates to the Revenue Calculator.
     3.Scrolls to the slider and adjusts it to  value 820.
     4.Updates the input field with a 560 value and validates the slider synchronization.
     5.Selects specific CPT codes by checking the boxes.
     6.Displays the Total Recurring Reimbursement value.
     7.Validating  Total Recurring Reimbursement value is '$75600'
       --NOTE: Here when "Total individual per month" is '820' then Total Recurring Reimbursement value is '$110700.'
               and when  "Total individual per month" is '560' then Total Recurring Reimbursement value is '$75600.'
     8.Closes the browser.

------ Tests--------
 1."task_fitpeo_test.py" is test script for calculating Total Recurring Reimbursement value when  "Total individual per month" is '560'."
 2."task_fitpeo_test2.py" test script for calculating Total Recurring Reimbursement value when "Total individual per month" is '820'".


NOTES:
 ->Ensure a stable internet connection for smooth operation.
 ->If encountering issues, update your ChromeDriver version to match your Chrome browser.

