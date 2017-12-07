# IoT_CloudDataExtractor
#### *To use the code*
1. Clone this repository
2. Run *Download_cloud_data_UI.py* with command line 
3. Or open the above file file with your fevourite editor and run from the editor, I use Visual Studio Code (VS Code)
4. User interface will be opened if succesfully run the code
5. Choose folder to save the file, click **Browse** button
6. Choose device such as **Amazon Alexa**, **Google OnHub** or **Mother sen.se**. In this case, choose the default that is **Amazon Alexa**
7. Choose Credential method, OnHub do not use any credential. For **Amazon**, either choose **Login** credential or **cookies**
8. The cookie file is included on the directory, so select *cookies* and *browse* the cookie file.
9. At the end of the interface, there is an option to include the **calling and messaging data** and **audio data** from the cloud. The audio data is the voice command the user ordered alexa, it may contain a lot of file and may be large. So, include it whenever it is necessary because it may take a while to download it.
10. Click **Download** button and wait for dialog. The dialog may be error or success!
11. It is a *demo* application, it should be optimized in a professional way.

#### N.B: 
Anyone who wants to edit and contribute should create a branch and edit on the branch before merging to the master branch
