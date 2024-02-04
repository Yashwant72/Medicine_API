# Medicine API
# Overview

This project involves the creation of a Python-based server for managing users and medicine-related information. MongoDB is used as the database, and the server is designed to handle CRUD operations for users and various queries related to medicine.

# Getting Started
Follow the steps below to set up and run the project locally:
# 1. Create a Virtual Environment

  # Create a virtual environment
    python -m venv venv

  # Activate the virtual environment
  # On Windows
    venv\Scripts\activate
  # On Unix or MacOS
    source venv/bin/activate

# 2. Install Dependencies
  # Install the required dependencies specified in the requirements.txt file.
    pip install -r requirements.txt
# 3. Run the Server
  # Ensure that MongoDB is running, then execute the following command to start the server:
  # Run the server
    python server.py

# Routes
# Users
  # Register User:
    - Endpoint: `/registerUser`
    - Method: POST
    - Description: Register a new user.

  # Get All Users:
    - Endpoint: `/getAllUsers`
    - Method: GET
    - Description: Retrieve all users.
  # Get User by ID:
    - Endpoint: `/getUser/:id`
    - Method: GET
    - Description: Retrieve a user by ID.

  # Update User by ID:
    - Endpoint: `/updateUser/:id`
    - Method: PUT
    - Description: Update a user's information by ID.

  # Delete User by ID:
    - Endpoint: `/deleteUser/:id`
    - Method: DELETE
    - Description: Delete a user by ID.
# Medicine

  # Query by Proprietary Name:
    - Endpoint: `/api/ProprietaryName/:name`
    - Method: GET
    - Description: Run a query on the `product.txt` dataset based on proprietary name.

  # Query by Substance Name:
    - Endpoint: `/api/SubstanceName/:name`
    - Method: GET
    - Description: Run a query on the `product.txt` dataset based on substance name.

  # Query by Non-Proprietary Name:
    - Endpoint: `/api/NonProprietaryName/:name`
    - Method: GET
    - Description: Run a query on the `product.txt` dataset based on non-proprietary name.

  # Query by Disease Name:
    - Endpoint: `/api/DiseaseName/:name`
    - Method: GET
    - Description: Run a query on the `product.txt` dataset based on disease name.

# Database

The application uses MongoDB to store user information and queries a `product.txt` dataset for medicine-related information.

# Note

Make sure to customize any configuration settings, such as MongoDB connection details, based on your specific environment and requirements. Ensure that the `product.txt` dataset is available and properly formatted for the medicine-related queries.
