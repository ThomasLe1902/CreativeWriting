To run the code please follow the instruction:
1. Create an virtual environment in the project folder
  Open the terminal in your IDE and type:
    python -m venv [YOUR_VENV_NAME_HERE]
  Once the setup is complete run:
    [YOUR_VENV_NAME_HERE]\Scripts\activate
2. Install necessary libraries:
    pip install -r "requirements.txt"
3. Download the dataset: https://huggingface.co/datasets/euclaise/WritingPrompts_preferences
   Download the file name "train-00000-of-00005.parquet"
4. Run the files
   To train the model: py train.py
   To run the prompt to the model: py demo.py
