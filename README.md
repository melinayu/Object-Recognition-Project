# Face Recognition System

Welcome to the Face Recognition System! This project consists of two primary Jupyter Notebooks that facilitate face registration and attendance management using facial recognition technology.

## Features
- **Face Registration:** Register new users by capturing and storing their facial data.
- **Attendance Program:** Automatically recognize registered users and mark attendance based on their faces.

---

## Prerequisites
Ensure you have the following installed on your system:

1. **Python 3.8+**
2. Required Libraries (install via pip):
   - OpenCV
   - NumPy
   - dlib
   - face_recognition
   - pandas
   - Jupyter Notebook

Run the following command to install the dependencies:
```bash
pip install opencv-python numpy dlib face_recognition pandas notebook
```

---

## Directory Structure
```
face_recognition_system/
├── notebooks/
│   ├── face_registration.ipynb
│   └── attendance_program.ipynb
├── data/
│   ├── faces/
│   └── attendance.csv
└── README.md
```
- **notebooks/**: Contains the Jupyter Notebooks for registration and attendance.
- **data/faces/**: Stores images of registered users.
- **data/attendance.csv**: Stores attendance logs.

---

## How to Use

### 1. Face Registration
Use the `face_registration.ipynb` notebook to register new users.

#### Steps:
1. Open the `face_registration.ipynb` notebook.
2. Run the cells to:
   - Capture images from your webcam.
   - Enter the name of the person being registered.
   - Save the facial data for future recognition.
3. Confirm that the images are saved in the `data/faces/` directory.

### 2. Attendance Program
Use the `attendance_program.ipynb` notebook to run the facial recognition attendance system.

#### Steps:
1. Open the `attendance_program.ipynb` notebook.
2. Run the cells to:
   - Load registered facial data.
   - Activate the webcam to detect and recognize faces.
   - Automatically log attendance in the `data/attendance.csv` file.
3. Verify that the attendance is recorded in the `attendance.csv` file.

---

## Output
- **Registered Faces:** Images of each registered user stored in the `data/faces/` directory.
- **Attendance Logs:** A CSV file (`data/attendance.csv`) containing:
  - Name of the person
  - Date
  - Time of recognition
  - Mood

---

## Notes
- Ensure the lighting is adequate for accurate face recognition.
- Maintain a clean background during face registration for best results.
- Avoid registering users with similar facial features under poor lighting conditions.

---

## Future Improvements
- Add a graphical user interface (GUI) for easier use.
- Integrate email notifications for attendance confirmation.
- Improve the model’s accuracy under various lighting and angle conditions.

---

## License
This project is licensed under the MIT License. Feel free to use and modify the system as needed.

---

## Contact
For any issues or suggestions, feel free to reach out:
- **Email:** your.email@example.com
- **GitHub:** [YourGitHubProfile](https://github.com/YourGitHubProfile)