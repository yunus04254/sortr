# Sortr - macOS File Organiser

## Screenshots
![sortr](https://github.com/yunus04254/sortr/assets/146735322/c382fcd7-7336-428d-97e4-dd6a60143f6b)

## Description
Sortr is a Python-based macOS menu bar application that essentially runs in background while organising files within a directory based on their types, such as audio, video, images, and others. It provides an easy-to-use interface with the ability to set a sorting interval and run the sorting process.

## Features
- Organise files into specific folders based on their types.
- Set a custom sorting interval in minutes.
- Display a timer that shows the time until the next sorting operation
- Easily customisable to add more file extensions and folder names for sorting.

## Table of Contents
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Getting Started

### Prerequisites
Before you can use Sortr, you need to have the following installed on your system:
- Python 3.x
- [rumps](https://pypi.org/project/rumps/)

### Installation
1. Clone or download the Sortr repository to your local machine.
2. Install the required Python packages using pip:
```python
pip install rumps
```

## Usage
1. Run the Sortr application by executing the Python script:

```python
python sortr.py
```

2. The Sortr menu bar will appear with the following options:
- **Sort:** Initiates the sorting process for files in the specified directory.
- **Set Interval (minutes):** Allows you to set the automated sorting interval in minutes.
- **Quit:** Exits the Sortr application.

3. When you click "Sort," the application will organise files in the specified directory into folders based on their types (audio, video, images, and others).

4. You can set the sorting interval by clicking "Set Interval (minutes)" and entering the desired interval.

5. The timer label will display the time until the next sorting operation.

6. To stop the application, click "Quit."

## Contributing
If you would like to contribute to sortr, feel free to fork the repository, make your changes, and submit a pull request.

---

