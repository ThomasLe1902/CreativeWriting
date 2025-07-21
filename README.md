To run the code, please follow these instructions:

1.  **Create a virtual environment** in the project folder. Open the terminal in your IDE and type:
    ```bash
    python -m venv [YOUR_VENV_NAME_HERE]
    ```
    Once the setup is complete, run:
    ```bash
    [YOUR_VENV_NAME_HERE]\Scripts\activate
    ```

2.  **Install necessary libraries:**
    ```bash
    pip install -r "requirements.txt"
    ```

3.  **Download the dataset:**
    Go to `https://huggingface.co/datasets/euclaise/WritingPrompts_preferences` and download the file named "train-00000-of-00005.parquet".

4.  **Run the files:**
    * To train the model:
        ```bash
        py train.py
        ```
    * To run the prompt to the model:
        ```bash
        py demo.py
        ```
