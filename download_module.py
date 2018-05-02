import json
import os
import requests
import sqlite3
from sqlite3 import Error
import time
from Save_module import get_file_Save
from utils import Utils


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return None

def extract_cookies_from_db(conn):
    """
    Extract cookies from cookies database
    :param conn: the Connection object
    :return: cookies
    """
    cur = conn.cursor()
    query = cur.execute("SELECT * FROM cookies")
 
    rows = query.fetchall()
    row = {}
    for r in rows:
        row[r['name']] = r['value']

    cur.close()
    cur.connection.close()
    return row

def download_files(cookies_from_db, saving_path, include_messaging, include_audio):
    try:    
        #instantiate/create the class
        downloadAndSave = get_file_Save(cookies_from_db,saving_path)

        #url to get/download
        api_activities = 'https://pitangui.amazon.com/api/activities?startTime=&endTime=&size=50&offset=1'
        api_phoenix = 'https://pitangui.amazon.com/api/phoenix'
        cards_api = 'https://pitangui.amazon.com/api/cards'
        webconfig_api = 'https://pitangui.amazon.com/api/wifi/configs'
        todo_list_api = 'https://pitangui.amazon.com/api/todos?type=TASK&size=100&complete=true|false'
        shopping_lists_api = 'https://pitangui.amazon.com/api/todos?type=SHOPPING_ITEM&size=100&complete=true|false'
        devices_api = 'https://pitangui.amazon.com/api/devices/device'
        device_pre_api = 'https://pitangui.amazon.com/api/device-preferences'
        bluetooth_connected_api = 'https://pitangui.amazon.com/api/bluetooth'
        customer_info_api = 'https://pitangui.amazon.com/api/authentication'
        notification_api = 'https://pitangui.amazon.com/api/notifications'
        
        #calling and messaging cloud data and APIs
        account_detail = 'https://alexa-comms-mobile-service-na.amazon.com/accounts/'
        user_detail = 'https://alexa.amazon.com/api/users/me'
        base_api = 'https://alexa-mobile-service-na-preview.amazon.com/users/'
        
        #Download from the cloud and save to the local disk
        downloadAndSave.get_saveUsingApi(cards_api,"cards.json")
        downloadAndSave.get_saveUsingApi(webconfig_api,"web_config.json")
        downloadAndSave.get_saveUsingApi(todo_list_api,"to_do.json")
        downloadAndSave.get_saveUsingApi(shopping_lists_api,"shopping_lists.json")
        downloadAndSave.get_saveUsingApi(devices_api,"devices.json")
        downloadAndSave.get_saveUsingApi(device_pre_api,"devices_preference.json")
        downloadAndSave.get_saveUsingApi(bluetooth_connected_api,"bluetooth_connected.json")
        downloadAndSave.get_saveUsingApi(customer_info_api,"owner_info.json")
        downloadAndSave.get_saveUsingApi(notification_api,"notifications.json")
        downloadAndSave.get_saveUsingApi(api_phoenix,"phoenix.json")
        
        #download the activities - as an option audio data can be downloaded if needed, set the include_audio paramerer 1. 
        downloadAndSave.download_activities_json_audio(api_activities, include_audio)

        #Download calling and messaging data; account info, user detail, contacts, conversations, and indiv conv
        if include_messaging == 1:
            downloadAndSave.Download_callingAndMessaging(user_detail,'user_info.json', 'none')
            downloadAndSave.Download_callingAndMessaging(account_detail,'account_detail.json', 'account')
            downloadAndSave.Download_callingAndMessaging(base_api,'contacts.json', 'contacts')
            downloadAndSave.Download_callingAndMessaging(base_api,'conversations.json', 'conv')
            
        Utils.showMessage("Complated!", "Finished downloading!")

    except:
        Utils.showMessage("Error!", "Something got wrong!")

def main(database_path, saving_path, include_messaging,include_audio):
    #database name, extract from the application data (data/data/amazon...) that comes from the imaged phone....
    conn = create_connection(database_path)
    conn.row_factory = sqlite3.Row

    #cookies from the database
    cookies_from_db = extract_cookies_from_db(conn)

    download_files(cookies_from_db, saving_path, include_messaging,include_audio)

if __name__ == '__main__':
    database_path = os.path.expanduser('~') + "\Documents\workingDirectory\Cookies"
    
    saving_path = os.path.expanduser('~') + "\\Documents\\workingDirectory\\downloads\\"
    main(database_path,saving_path,0,0)