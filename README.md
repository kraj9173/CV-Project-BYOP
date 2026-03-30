# Cat vs. Dog Binary Classifier (Computer Vision BYOP)

## 📌 Project Overview
This project is a high-performance command-line interface (CLI) application designed for **Binary Image Classification**. Utilizing a custom-trained **ResNet-18** architecture, the system distinguishes between cats and dogs by applying essential Computer Vision principles, including image normalization, tensor transformations, and deep pattern analysis. 

The application is optimized for execution in headless terminal environments, making it ideal for server-side deployment or automated pipelines.

---

## 🛠 1. Prerequisites
Before beginning, ensure you have the following installed:
* **Python:** Version 3.8 or higher.
* **Git:** To clone and manage the repository.

---

## ⚙️ 2. Environment Setup & Configuration

### **Step A: Clone the Repository**
```bash
git clone [https://github.com/kraj9173/CV-Project-BYOP.git](https://github.com/kraj9173/CV-Project-BYOP.git)
cd CV-Project-BYOP
```

### **Step B: Create & Activate a Virtual Environment**

**Windows:**
```bash
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 📦 3. Dependency Installation
Install the necessary Computer Vision and Machine Learning libraries:

```bash
pip install -r requirements.txt
```
> **Note:** The pre-trained model weights (`.pth` file) are located within the `trained_model/` directory and are loaded automatically by the script.

---

## 🚀 4. Project Execution
The application utilizes `argparse` to handle dynamic inputs. You can test the model using the provided sample image or your own image files.

**Run Command:**
```bash
python classification.py --input "sample/Screenshot 2026-03-27 021717.png"
```

---

## 📊 5. Expected Output
Upon successful execution, the script performs the following actions:

* **Terminal Output:** Prints the final prediction (`Cat` or `Dog`) directly to the console.
* **Directory Management:** Automatically generates an `output/` directory if it does not already exist.
* **Persistent Logging:** Appends the input filename and its predicted class to a log file located at `output/predictions.txt`.

### **Sample Log Format:**
| Filename | Prediction |
| :--- | :--- |
| `Screenshot 2026-03-27 021421.png` | cat |
| `Screenshot 2026-03-27 021717.png` | dog |