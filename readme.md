# E-commerce Web Application

This is a Django-based e-commerce application designed to allow users to browse products, register, log in, place orders, and manage their profile. It includes a payment gateway integration (Razorpay) and administrative functionalities.

## Features

* **User Authentication**: Secure user registration, login, logout, and password change.
* **User Profiles**: View personal details and order history.
* **Product Catalog**: Browse products categorized by type (Coffee, Tea, Unique items).
* **Product Details**: View detailed information for each product, including price, description, and available quantity.
* **Order Management**: Users can place orders, and the system tracks order details and updates product stock.
* **Payment Gateway Integration**: Seamless integration with Razorpay for handling online payments.
* **Contact & Feedback Forms**: Dedicated sections for users to send inquiries and provide feedback.
* **Admin Panel**: A fully functional Django admin interface for managing all data, including categories, products, user registrations, orders, contact messages, and feedback.
* **Responsive Design**: Built with Bootstrap 5 for a modern and responsive user interface across different devices.

## Technologies Used

* **Backend**: Python 3.x, Django 4.1.2
* **Database**: SQLite3 (default for development; easily configurable for PostgreSQL, MySQL in production)
* **Frontend**: HTML, CSS (Bootstrap 5, custom `style.css`), JavaScript (including Font Awesome for icons, Razorpay Checkout SDK)
* **Payment Gateway**: Razorpay

## Project Structure