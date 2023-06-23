
# Shark Tank India
Shark Tank India is a Django-based web application that showcases the episodes, pitches, and deals from the Indian version of the popular TV show "Shark Tank." The application provides information about entrepreneurs, investors (sharks), products, and investments made during each episode.

## Setup and Installation
run the following commands to run project on your machine

1. Clone the repository:
``` git clone https://github.com/satyajitgiram/shark-tank-india-backend```

2. Create virtual environment:
```python -m venv venv```

3. Activate the virtual environment:

- On Windows:

  ```
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```
  source venv/bin/activate
  ```

4. Install the project dependencies:
```pip install -r requirements.txt```

5. Go into project folder:
```cd shark-tank-india-backend ```

6. Creating migrations for the database:
``` python manage.py makemigrations```

7. Applying that migrations into database
``` python manage.py migrate```

8. Create your admin credentials:
``` python manage.py createsuperuser```

9. Start the development server:
``` python manage.py runserver 0.0.0.0:8080 ```

9. Open your browser and navigate to `http://localhost:8080` to access the application.

10. Use that credentials to login into the django admin panel
username - admin@gmail.com   
password - admin

## Technologies Used

- Django web framework
- JWT Authentication
- Swagger Documentation

## Features

- Display episodes, pitches, and deals from Shark Tank India.
- Show details of each episode, including entrepreneurs, investors, products, and investment information.
- Highlight successful deals and investments made by the sharks.
- Social media integration to share episodes and contact the entrepreneurs.
- user can add pitch in the database
- user can submit pitch requests

## Contributing

Contributions are welcome! If you'd like to contribute to the Shark Tank India project, please follow these steps:

1. Fork the repository.

2. Create a new branch:

3. Make your changes and commit them:

4. Push the changes to your forked repository:

5. Create a pull request on the main repository.

## Contact

For any inquiries or suggestions, please feel free to contact : [Satyajit Giram](mailto:satyajigiram.dev@gmail.com).

