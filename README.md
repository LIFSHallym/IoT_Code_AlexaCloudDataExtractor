# IoT_CloudDataExtractor
#### *To use the code*
1. Clone this repository
2. Run **Download_cloud_data_UI.py** with command line
3. Or open the above file with your fevourite editor and run from the editor
4. User interface will be opened if the code run successfully
5. Choose folder to save the downloaded file, click **Browse** button.
6. The interface is generic for more than one device. at this time, it only contain **Amazon Alexa** cloud extraction.
7. Select Credential method. For **Amazon**, either choose **Login** credential or **cookies**
8. You should have either have a cookie or a valid user account to use this parser. Select *cookies* and *browse* the cookie file, or select login and enter username and password. The username and password authentication opens firefox browser, so you also need firefox browser and its driver, see how to setup below.
    - install selenium - #### *pip install selenium*
    - download [Mozilla webdriver] (https://github.com/mozilla/geckodriver/releases)
    - put the driver in python Scripts *(python_installation_path/Scripts)* and add the scripts path to PATH Variable
9. At the end of the interface, there is an option to include the **calling and messaging data** and **audio data** from the cloud. The audio data is the voice command the user ordered Alexa, it may contain a lot of file and may be too large. So, include it whenever it is necessary, because it may take a while to download it.
10. Click **Download** button and wait for dialog. The dialog may be error or success!
11. It is a *demo/experiment* application, it should be optimized and restructured in a professional way.

#### N.B: 
* Anyone who wants to edit and contribute should create a branch and edit on the branch before merging to the master
* The code does not support data extraction from the phone Image, only extract data from the cloud (needs valid user account or cookie)

#### Cloud APIs and Android App traces
[Cloud APIs and android phone traces spreadsheet] (https://docs.google.com/spreadsheets/d/1XxRro8goJUB1vei5E4zx-n2CxN_bKl6ow4PBG4ekL94/edit)
