# AI Market Maker

This project is a simple web application that uses a powerful AI to turn a user's idea into a structured, verifiable, and tradeable market concept. It's built with a Flask backend and a plain HTML/JavaScript frontend.

## Features

*   **AI-Powered Market Generation:** Leverages Google's Generative AI to analyze user input.
*   **Structured Output:** Produces a clean, four-part market summary including a title, description, a verifiable URL for the underlying metric, and an interest rating.
*   **Simple Web Interface:** An easy-to-use interface to input ideas and view the generated market data.
*   **Flask Backend:** A lightweight Python server to handle AI API requests.

## Project Setup

Follow these instructions to get the project running on your local machine.

### 1. Prerequisites

*   **Python 3:12 Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### 2. Clone the Repository

First, clone this project to your local machine using Git:

```bash
git clone <your-repository-url>
cd <your-repository-directory>
```

### 3. Create a Python Virtual Environment

It's a best practice to use a virtual environment for Python projects. This creates an isolated space for your project's dependencies, so they don't interfere with other Python projects on your computer.

**Why use a virtual environment?** Imagine you have two projects, and one needs version 1.0 of a library, while the other needs version 2.0. A virtual environment solves this by keeping each project's libraries separate.

**Create the virtual environment:**

Open your terminal in the project directory and run the following command. We'll name our environment `.venv`.

```bash
# For macOS/Linux
python3 -m venv .venv

# For Windows
python -m venv .venv
```

This command creates a new folder named `.venv` in your project directory, which will contain the Python interpreter and libraries for this project.

**Activate the virtual environment:**

Before you can use the new environment, you need to "activate" it.

```bash
# For macOS/Linux
source .venv/bin/activate

# For Windows
.\.venv\Scripts\activate
```

When the environment is active, you will see its name (e.g., `(.venv)`) at the beginning of your terminal prompt. This shows that any Python commands you run or packages you install will be contained within this environment.

### 4. Install Dependencies

With your virtual environment active, you can now install the necessary Python packages listed in the `requirements.txt` file.

Run this command to install the dependencies:

```bash
pip install -r requirements.txt
```

### 5. Set Up Your Environment Variables

The application needs an API key for Google's AI services to work. You must store this key in a file that is kept private and not shared publicly (like on GitHub).

You can create an API Key from here: 

https://aistudio.google.com/api-keys

Google offers a generous free tier for their AI services, so you shouldn't incur any costs unless you exceed the limits.

*   Create a new file in the root of your project directory named `.env`. You can copy the exiting `.env.example` file and rename it to `.env`.
*   Open the `.env` file and add your API key in the following format:
    ```
    GEMINI_API_KEY="YOUR_API_KEY_HERE"
    ```

*   Replace `"YOUR_API_KEY_HERE"` with your actual API key from Google AI Studio.

The `.env` file is loaded by the application at startup, but it is listed in the `.gitignore` file (you should add it if it isn't there) to prevent it from being committed to version control.

### 6. Run the Application

Now you're ready to start the application!

1.  **Start the Flask Backend:**
    Make sure your virtual environment is still active. Then, run the `app.py` file:

    ```bash
    python app.py
    ```

    Your backend server is now running at `http://localhost:5000`.
2.  **Open the Frontend:**
    Navigate to the project folder in your file explorer and open the `index.html` file in your web browser.

You can now enter an idea into the input box and click "Generate" to get a response from the AI!