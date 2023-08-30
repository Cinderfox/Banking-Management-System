# Banking Management System

The Banking Management System is a Python program designed to simulate the operations of a comprehensive banking system. This program allows users to interact with a range of banking functionalities, including account management, transactions, loans, and card issuance.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
  - [Admin Menu](#admin-menu)
  - [Customer Menu](#customer-menu)
- [Installation](#installation)
- [Usage](#usage)
  - [Admin Menu Usage](#admin-menu-usage)
  - [Customer Menu Usage](#customer-menu-usage)
- [Data Storage and Retrieval](#data-storage-and-retrieval)
- [Requirements](#requirements)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Banking Management System is a versatile tool that demonstrates the concepts of object-oriented programming, data storage using files, and user interaction through console-based menus. It provides a platform for both administrators and customers to manage their banking needs efficiently.

## Features

### Admin Menu

Administrators have access to the following features within the admin menu:

#### Set Bank Interest Rates

Administrators can set and adjust the interest rates for different types of loans and credit cards. These interest rates play a critical role in calculating loan repayments and determining credit card charges.

#### Set Card Limits

Administrators can establish specific limits for credit and debit cards. This includes defining the maximum withdrawal amount for debit cards and the spending limit for credit cards. These limits help control customer transactions and manage potential financial risks.

### Customer Menu

Customers can perform a variety of actions within the customer menu:

#### Register New Account

Customers can initiate the process of registering a new account. They are prompted to provide essential details such as their full name, email address, category (general or student), and initial account balance. Upon registration, a unique customer ID is assigned.

#### Log In

Registered customers can log in to their accounts using their customer ID and password. This secure authentication process ensures that customer data remains confidential.

#### Account Operations

Customers can manage their accounts through various operations:

- **Modify Account Details**: Customers can update their account information, including their name and email address.
- **View Account Information**: Customers can view their account details, including current balance, pending loans, and card details.
- **Delete Account**: Customers can choose to delete their accounts. This action removes all associated account information.

#### Transactions

Customers can perform essential financial transactions:

- **Transfer Money**: Customers can transfer funds between their own accounts or to other customer accounts within the bank.
- **Deposit Money**: Customers can deposit money into their accounts, which directly increases their account balance.
- **Withdraw Money**: Customers can withdraw money from their accounts, provided they have sufficient funds.

#### Loan Application

Customers have the option to apply for various types of loans, including:

- **Student Loan**: Available only to customers in the student category. The loan amount is based on the school fee, with a predefined maximum borrowing limit and interest rate.
- **Mortgage Loan**: Available to customers in the general category. The loan amount is based on the value of an asset submitted to the bank, with predefined limits and interest rates.
- **Small Business Loan**: Available to general category customers. The loan amount is again based on the value of an asset submitted to the bank, with predefined limits and interest rates.
- **Automobile Loan**: Available to general category customers. The loan amount is based on the value of an automobile asset, with predefined limits and interest rates.
- **Personal Loan**: Available to general category customers. The loan amount is based on the value of an asset submitted to the bank, with predefined limits and interest rates.

#### Loan Repayment

Customers with outstanding loans can make repayments. The program calculates the remaining balance and updates the account accordingly. This feature helps customers manage their loan obligations.

#### Card Issuance

Customers have the option to apply for credit and debit cards:

- **Credit Card Issuance**: Available to customers in the general category. The credit card comes with an interest rate and predefined credit limit.
- **Debit Card Issuance**: Available to customers in both general and student categories. Debit card issuance includes setting a daily withdrawal limit.

#### Log Out

Customers can securely log out of their accounts, ensuring the privacy and security of their banking information.

## Data Storage and Retrieval

The program utilizes file-based data storage to maintain customer and bank information:

- `customer0.dat`: This file stores customer data using the pickle module. Customer accounts are stored as dictionary entries, where each customer ID serves as a key. Customer details, including name, email, category, balances, and card details, are stored as values associated with these keys.

- `bankdetails0.dat`: This file stores bank-related data, such as interest rates for loans and credit cards, as well as card limits. Similar to customer data, this information is stored as a dictionary using the pickle module.

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Download the program files and save them to a directory of your choice.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory where the program files are located.
3. Run the program using the command: `python main.py`.

### Admin Menu Usage

Administrators can access the admin menu by selecting the relevant option in the main menu. From there, they can set interest rates for loans and define card limits.

### Customer Menu Usage

Customers can access the customer menu by selecting the corresponding option in the main menu. They can register new accounts, log in to existing accounts, and perform a range of banking operations.

## Requirements

- Python 3.x

## Contributing

Contributions are welcome! If you'd like to enhance the program's features, improve its interface, or fix any issues, feel free to submit a pull request.

## License

This program is open-source and distributed under the MIT License.

Feel free to customize this README to match the specifics of your program. The goal is to provide clear instructions and comprehensive information for users and potential contributors.
