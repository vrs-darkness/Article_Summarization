
---

# Article Summarization

This repository contains a Python implementation of the Text Rank algorithm, inspired by Google's Page Rank algorithm, specifically for summarizing non-premium articles on Medium. It also includes a web interface that allows users to input paragraphs and obtain summarized content directly.

## Features:

- Summarizes non-premium articles from Medium.
- Utilizes the Text Rank algorithm for generating summaries.
- Provides a web interface to summarize paragraphs or excerpts directly.
- Easy to use and integrate into your projects.

## Requirements:

Before running the summarizer or the web interface, ensure you have the necessary packages installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Installation:

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/Article_Summarization.git
   cd Article_Summarization
   ```

2. **Navigate to the project directory:**

   ```bash
   cd Article_Summarization
   ```

3. **Install the required packages:**

   ```bash
   pip install -r requirements.txt
   ```

## Running the Website Locally:

To run the website locally, follow these steps:

1. **Install the necessary requirements:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the `resources.py` script to prepare necessary resources:**

   ```bash
   python resources.py
   ```

3. **Start the Flask web server using `main.py`:**

   ```bash
   python main.py
   ```

4. **Access the website:**

   Open your web browser and navigate to `http://<your_ip>:5000/` to access the website on your home network.

## How It Works:

The summarizer works by following these steps:
  - Fetches the content of the provided Medium article.
  - Processes the text to identify the most important sentences.
  - Ranks these sentences using the Text Rank algorithm.
  - Generates a concise summary based on the highest-ranked sentences.

## Additional Resources:

- **Page Rank Algorithm**: [GeeksforGeeks](https://www.geeksforgeeks.org/page-rank-algorithm-implementation/)  
- **Text Rank Algorithm**: [Medium Article](https://ankitnitjsr13.medium.com/text-rank-algorithm-a8c2cc58ea9c)  

## Directory Structure:

- **`study/`**: Contains Jupyter notebooks with the entire summarization process.
- **`resources/`**: Contains research papers and additional resources used in the project.

## Contributors:

- Varshith P Singh - [GitHub](https://github.com/Varshith1510)

## Acknowledgements:

- The Text Rank algorithm is inspired by Google's Page Rank algorithm.

---

