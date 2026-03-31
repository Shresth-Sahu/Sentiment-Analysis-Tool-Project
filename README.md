# Sentiment-Analysis-Tool-Project
An AI based sentiment analyzer

# Text Sentiment Analyzer CLI

## Overview
The Text Sentiment Analyzer is a Command Line Interface (CLI) application that utilizes Natural Language Processing (NLP) to evaluate the emotional tone of text. It calculates a mathematical polarity score for user inputs and classifies the text as Positive, Negative, or Neutral. All analysis sessions are persistently logged to a local CSV database.

## Features
* **Real-Time Analysis:** Evaluates text sentiment instantly using the `textblob` library.
* **Data Storage:** Automatically records input text, polarity scores, and sentiment classifications to `sentimentLogs.csv`.
* **Interactive Menu:** Provides a terminal-based navigation system with built-in input validation to prevent execution errors.

## Prerequisites
Python must be installed on your system to run this application. Additionally, you must install the required NLP dependency. 

Execute the following command in your terminal:

pip install textblob

## Execution
    Download or clone the repository to your local machine.

    Open your terminal or command prompt.

    Navigate to the project directory:
    Bash

    cd path/to/your/folder

    Run the application:

    python analyzer.py

## Usage
Upon launching the application, you will be prompted with a system menu containing the following options:

    Analyze New Text: Prompts for a text input and returns the calculated polarity score and sentiment classification.

    Review Analysis History: Retrieves and displays all past analysis records from the local CSV database.

    Exit System: Safely terminates the application.
