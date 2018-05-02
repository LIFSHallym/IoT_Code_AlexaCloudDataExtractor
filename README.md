# IoT_CloudDataExtractor
#### *To use the code*
1. Clone this repository
2. Run **Download_cloud_data_UI.py** with command line or with your fevourite editor and run it
3. User interface will be opened if the code run successfully
4. Choose folder to save the downloaded file, click **Browse** button.
5. The interface is generic for more than one device. at this time, it only contain **Amazon Alexa** cloud extraction.
6. Select Credential method. For **Amazon**, either choose **Login** credential or **cookies**
7. You should have either have a cookie or a valid user account to use this parser. Select *cookies* and *browse* the cookie file, or select login and enter username and password. The username and password authentication opens firefox browser, so you also need firefox browser and its driver, see how to setup below.
    - install selenium - **pip install selenium**
    - download Mozilla webdriver - https://github.com/mozilla/geckodriver/releases
    - put the driver in python Scripts *(python_installation_path/Scripts)* and add the scripts path to PATH Variable
8. At the end of the interface, there is an option to include the **calling and messaging data** and **audio data** from the cloud. The audio data is the voice command the user ordered Alexa, it may contain a lot of file and may be too large. So, include it whenever it is necessary, because it may take a while to download it.
9. Click **Download** button and wait for dialog. The dialog may be error or success!
10. It should be optimized, error handled and restructured, we are working to make it better.

#### N.B:
* The code does not support data extraction from the phone Image, only extract data from Alexa cloud (needs valid user account or a cookie)

#### Cloud APIs and Android App traces
Cloud APIs and android phone traces spreadsheet - https://drive.google.com/open?id=1XxRro8goJUB1vei5E4zx-n2CxN_bKl6ow4PBG4ekL94
