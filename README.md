Responsive Django Webpage
This is a Django-based project that creates a responsive webpage with the following features:
- A fixed navbar that remains at the top when scrolling.
- A collapsible left menu, a main content area, and a right-side panel.
- A footer at the bottom of the page.
- The page adjusts its scale based on the screen width using JavaScript.

Setup Instructions:
1. Clone the repository:
   git clone https://github.com/your-username/responsive-django-webpage.git
   cd responsive-django-webpage

2. Create a virtual environment:
   python -m venv venv

3. Activate the virtual environment:
   - On macOS/Linux:
     source venv/bin/activate
   - On Windows:
     .\venv\Scripts\activate

4. Install required dependencies:
   pip install -r requirements.txt

5. Migrate the database (even if unused):
   python manage.py migrate

6. Run the Django development server:
   python manage.py runserver

7. Open a browser and visit:
   http://127.0.0.1:8000/

Project Features:
- Fixed Navbar
- Collapsible Left Menu
- Responsive Design with Page Scaling
- Footer

JavaScript Features:
- Shrinks the webpage based on screen width:
  - If screen width is between 992px and 1600px, shrink by 90%.
  - If screen width is between 700px and 767px, shrink by 80%.
  - If screen width is between 600px and 700px, shrink by 75%.
  - If screen width is <= 600px, shrink by 50%.

Notes:
- Ensure that Django is installed in your environment.
- The project uses Django for the backend, and static files for frontend functionality.
