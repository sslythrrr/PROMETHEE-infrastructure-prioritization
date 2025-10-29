# PROMETHEE Infrastructure Prioritization

A simple web application designed to help prioritize projects or alternatives using the PROMETHEE method.

PROMETHEE (Preference Ranking Organization Method for Enrichment Evaluations) is a multi-criteria decision-making (MCDM) method used to rank a set of alternatives based on several, often conflicting, criteria.

---

## Key Features

* **Dynamic Alternatives**: Add two or more alternatives (e.g., infrastructure projects) to be compared.
* **Multi-Criteria Evaluation**: Assess each alternative against five predefined criteria using simple sliders (rated 1-5):
    * Biaya (Cost)
    * Waktu Penyelesaian (Completion Time)
    * Tingkat Kebutuhan (Level of Need)
    * Dampak Sosial (Social Impact)
    * Frekuensi Penggunaan (Frequency of Use)
* **PROMETHEE Calculation**: Implements the PROMETHEE algorithm to calculate preference indices, leaving/entering flows, and the final net flow for ranking.
* **Ranked Results**: Displays the final priority list, ranking alternatives from highest to lowest based on their net flow score.
* **Visualization**: Includes a simple bar chart to visually represent the net flow scores for each alternative.

---

## Technologies Used

* **Backend**: Python
    * **Framework**: Flask
    * **Calculation**: NumPy (for numerical operations and data normalization)
* **Frontend**: HTML5, CSS3, JavaScript
    * **Styling**: Bootstrap 5
    * **DOM Manipulation**: jQuery
    * **Charting**: Chart.js

---

## Prerequisites

Before you begin, ensure you have the following installed on your system:

* **Python** (Recommended: 3.8 or newer)
* **pip** (Python Package Manager, usually comes with Python)

---

## Installation and Setup

1.  **Clone the repository**:
    ```bash
    git clone [https://github.com/sslythrrr/promethee-infrastructure-prioritization.git](https://github.com/sslythrrr/promethee-infrastructure-prioritization.git)
    cd promethee-infrastructure-prioritization
    ```

2.  **Create and activate a virtual environment** (Recommended):
    * On macOS/Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    * On Windows:
        ```bash
        python -m venv venv
        .\venv\Scripts\activate
        ```

3.  **Install dependencies**:
    This project requires `Flask` and `numpy`. You can install them directly:
    ```bash
    pip install Flask numpy
    ```

4.  **Run the application**:
    ```bash
    python app.py
    ```

5.  **Access the application**:
    Open your web browser and navigate to `http://127.0.0.1:5000`.

---

## Example Usage

1.  **Home Page (`/`)**:
    * You will see a form to enter the names of your alternatives.
    * Enter at least two project names (e.g., "Build New Bridge", "Repair Main Road").
    * Click the "Tambah Alternatif" (Add Alternative) button to add more projects.
    * Click "Lanjut" (Continue) to proceed.

2.  **Recommendation Page (`/recommendation`)**:
    * You will see a card for each project you added.
    * For each project, use the sliders to set a score from 1 to 5 for each of the five criteria.
    * After scoring all projects, click "Hitung Prioritas" (Calculate Priority).

3.  **Result Page (`/calculate_promethee`)**:
    * The application will display the ranked list of your projects, with the highest priority project at the top.
    * You will see the calculated `net_flow` score for each project and a bar chart visualizing these scores.

---

## Contributing

Contributions are welcome! If you'd like to contribute, please follow these steps:

1.  **Fork** the repository on GitHub.
2.  **Clone** your forked repository to your local machine.
3.  Create a new **branch** for your feature or bug fix (`git checkout -b feature/your-feature-name`).
4.  Make your changes and **commit** them (`git commit -m 'Add some feature'`).
5.  **Push** your changes to your fork on GitHub (`git push origin feature/your-feature-name`).
6.  Open a **Pull Request** from your fork to the original repository.

Please ensure your code follows the project's coding style.

---

## License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.
