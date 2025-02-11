Stock Price Monitoring and Email Notification System  : 
This Python script monitors the stock price percentage change from the Zagreb Stock Exchange (ZSE) and sends an email notification if the stock price drops below a specified threshold. The project uses Selenium for web scraping, yagmail for sending emails, and environment variables for secure email credentials.

Features  :
Web Scraping: Fetches the stock price percentage change from the ZSE website.

Email Notification: Sends an email alert if the stock price percentage change drops below -0.10%.

Automation: Fully automated and can be scheduled to run at regular intervals.

Prerequisites  ;
Before running the script, ensure you have the following installed:

Python 3.x: Download and install Python from python.org.

ChromeDriver: Download the version of ChromeDriver that matches your Chrome browser version from here.

Required Python Libraries: Install the required libraries using pip.

Installation : 
Clone the Repository:

bash ; 
Copy
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
Install Dependencies:

bash : 
Copy
pip install selenium yagmail
Set Up Environment Variables:

Create a .env file in the root directory of the project.

Add your email credentials to the .env file:

Copy
email=your-email@gmail.com
password=your-email-password
Note: If you're using Gmail, you may need to generate an App Password for secure access.

Download ChromeDriver:

Place the chromedriver executable in the project directory or add its path to your system's PATH environment variable.

How It Works
Fetch Stock Price:

The script uses Selenium to navigate to the ZSE website and scrape the stock price percentage change.

Check Threshold:

If the stock price percentage change is less than -0.10%, the script triggers an email notification.

Send Email:

The script uses yagmail to send an email alert to the specified receiver.

Code Structure
get_driver(): Initializes and configures the Selenium WebDriver.

stock_value(): Fetches the stock price percentage change from the ZSE website.

send_email(): Sends an email notification using yagmail.

sending_email_recpect_to_stock(): Checks the stock price and sends an email if the threshold is met.

Usage : 
Run the Script:

bash : 
Copy this -------> 
python main.py
Scheduling (Optional):

Use a task scheduler (e.g., cron on Linux or Task Scheduler on Windows) to run the script at regular intervals.

Example Output : 
If the stock price percentage change is -0.15%, the script will send an email with the following content:

Copy : 
Subject: Stock Value Alert!
Body: The stock price percent is low!


Notes : 

Security: Never hardcode your email credentials in the script. Always use environment variables or a secure vault.

ChromeDriver Compatibility: Ensure the version of ChromeDriver matches your installed Chrome browser version.

Error Handling: Add error handling for cases where the website structure changes or the email fails to send.

Contributing : 
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

License : 
This project is licensed under the MIT License. See the LICENSE file for details.

Author
islam mekawy
