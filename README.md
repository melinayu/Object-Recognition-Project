# Face Recognition System

Welcome to the Face Recognition System! This project consists of two primary Jupyter Notebooks that facilitate face registration and attendance management using facial recognition technology.

## Features
- **Face Registration:** Register new users by capturing and storing their facial data.
- **Attendance Program:** Automatically recognize registered users and mark attendance based on their faces.

---

## Prerequisites
Ensure you have the following installed on your system:
1. **Python version: 3.12.5**
2. Required Libraries (install via pip):
   - OpenCV version: 4.10.0
   - NumPy version: 2.0.2
   - scikit-learn version: 1.5.2
   - pandas version: 2.2.3
   - DeepFace version: 0.0.93
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
│   ├── add_faces.py
│   └── test.ipynb
├── data/
│   ├── faces_data.pkl
│   └── names.pkl
│   └── haarcascade_frontalface_default.xml
├── attendace/
│   └── attendance_16_01-2025.csv
├── README.md
```
- **notebooks/**: Contains the Jupyter Notebooks for registration and attendance.
- **data/faces/**: Stores images of registered users.
- **data/attendance.csv**: Stores attendance logs.

---

## How to Use

### 1. Face Registration
Use the `add_faces.py` notebook to register new users.

#### Steps:
1. Open the `add_faces.py` notebook.
3. Confirm that the images are saved in the `data/faces_data.pkl/` directory.

### 2. Attendance Program
Use the `test.ipynb` notebook to run the facial recognition attendance system.

#### Steps:
1. Open the `test.ipynb` notebook.
2. Run the cells to:
   - Load registered facial data.
   - Activate the webcam to detect and recognize faces.
   - Automatically log attendance in the `data/attendance_16_01-2025.csv` file.
3. Verify that the attendance is recorded in the `attendance_16_01-2025.csv` file.

---

## Output
- **Registered Faces:** Images of each registered user stored in the `data/face_data.pkl/` directory.
- **Attendance Logs:** A CSV file (`data/attendance_16_01-2025.csv`) containing:
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

## Contact
For any issues or suggestions, feel free to reach out:
- **Email:** melinayusafitri@gmail.com, ghaisanrabbani5@gmail.com, putriemma2010@gmail.com
- **GitHub:** [Ghaisan](https://github.com/ghaisanr)
              [Melin](https://github.com/melinayu)
              [Emma](https://github.com/emmaputri)
