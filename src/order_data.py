class OrderData:

    user_data = [['', 'Ivanova', '123456', 'Error: First Name is required'],
                 ['Elena', '', '123456', 'Error: Last Name is required'],
                 ['Elena', 'Ivanova', '', 'Error: Postal Code is required']]

    user_data_with_valid_credentials = ['Elena', 'Barteneva', '123456']
    successful_message = 'Thank you for your order!'