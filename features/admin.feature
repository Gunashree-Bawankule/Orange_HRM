# Feature: Admin Page Functionality
#
# Scenario: Add a new user in the admin page
# Given user logged into the OrangeHRM
# When user navigates to the admin page
# And user added a new user with <employee_name> "John Doe" <user_role> "admin"
# Then the user "John Doe" should be created successfully
#
# Scenario: Admin adds a new system user
# Given the admin is logged into OrangeHRM
# And the admin navigates to the "Admin" section
# When the admin clicks on the "Add" button
# And the admin fills in the user details with
# | Field            | Value         |
# | Employee Name    | James  Butler |
# | Username         | Smith         |
# | Password         | Password123   |
# | Confirm Password | Password123   |
# And the admin clicks the "Save" button
# Then the system should display a success message
