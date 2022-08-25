# OW-Stats-to-GS

Usage instructions:

1. Download files to Documents folder

   1-1. If not already downloaded and installed, install the google sheets python api by running the command in the terminal: 
        
        pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib 
        
2. In google_sheets_push.py change variable SPREADSHEET_ID to the id of the spreadsheet you want your statistics to be dumped into

3. Run the program, you will be prompted to login and once logged in the program will generate a token.json file

4. Run the program again to start logging data

5. Start a game in the overwatch workshop using the workshop code E8KVF
    
    5-1. *Make sure to turn on "Enable workshop inspector and workshop inspector log file" in the Overwatch settings under gameplay -> miscellaneous* 

6. Data will start being logged once players are let out of the ships

