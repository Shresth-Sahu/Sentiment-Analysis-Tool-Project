import os
import csv
from textblob import TextBlob

# path for the db
logFile = "sentimentLogs.csv"

def prepFile():
    # setup csv if it doesn't exist yet
    if not os.path.exists(logFile):
        with open(logFile, mode='w', newline='', encoding='utf-8') as f:
            # using generalized business headers
            csv.writer(f).writerow(["Input Text", "Polarity Score", "Sentiment"])

def calcSent(usrTxt):
    # let textblob do the math
    nlpTool = TextBlob(usrTxt)
    polVal = nlpTool.sentiment.polarity
    
    # figure out the general category
    if polVal >= 0.1:
        sentLbl = "Positive"
    elif polVal <= -0.1:
        sentLbl = "Negative"
    else:
        sentLbl = "Neutral"
        
    return polVal, sentLbl

def saveData(usrTxt, polVal, sentLbl):
    # append mode so we don't wipe old data
    with open(logFile, mode='a', newline='', encoding='utf-8') as f:
        csv.writer(f).writerow([usrTxt, round(polVal, 3), sentLbl])

def viewHist():
    print("\nAnalysis History")
    
    if not os.path.exists(logFile):
        print("No records found in the database.")
        return

    with open(logFile, mode='r', encoding='utf-8') as f:
        csvReader = csv.reader(f)
        next(csvReader) # skip the header row
        savedRecs = list(csvReader)
        
        if len(savedRecs) == 0:
            print("The database is currently empty.")
        else:
            # print out the logs
            for idx, row in enumerate(savedRecs, 1):
                print(f"Log {idx} | Sentiment: {row[2]} | Score: {row[1]} | Text: '{row[0]}'")

def runCli():
    # start the db
    prepFile()
    print("Text Sentiment Analyzer CLI")

    # main app loop [cite: 246-248]
    while True:
        print("\nSystem Menu")
        print("1. Analyze New Text")
        print("2. Review Analysis History")
        print("3. Exit System")
        
        menuOpt = input("Select an option (1-3): ").strip()
        
        if menuOpt == '1':
            usrTxt = input("\nEnter text to analyze: ").strip()
            
            # stop empty spam [cite: 231-233]
            if len(usrTxt) < 3:
                print("Error: Please enter a valid, complete sentence.")
                continue
                
            # process and save
            polVal, sentLbl = calcSent(usrTxt)
            saveData(usrTxt, polVal, sentLbl)
            
            print("\nAnalysis Complete")
            print(f"Detected Sentiment: {sentLbl}")
            print(f"Polarity Matrix Score: {polVal:.3f}")
            
        elif menuOpt == '2':
            viewHist()
            
        elif menuOpt == '3':
            print("Terminating system. Data saved securely.")
            break
            
        else:
            print("Invalid input. Use numbers 1, 2, or 3.")

if __name__ == "__main__":
    runCli()