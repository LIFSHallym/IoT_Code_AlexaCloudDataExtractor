import os
from os.path import expanduser
import requests
import datetime
import json
from utils import Utils

class get_file_Save:
  '''donwload files using API and cookies
     and save to disk
  '''

  def __init__(self,cookies,path):
    self.cookie = cookies
    self.path = path
    self.commsId = None

  def get_saveUsingApi(self, api, fileName):
    download_path = os.path.join(self.path + '/', fileName)
    get_content = requests.get(api, cookies=self.cookie)
    Utils.save_to_file(download_path,get_content.json())

  def Download_callingAndMessaging(self, api, fileName, indicator):
      location = os.path.join(self.path + '/', 'calling_messaging_data')
      if not os.path.exists(location):
          os.makedirs(location)
      download_path = os.path.join(location + '/', fileName)
      get_content = None
      if indicator == 'none':
          get_content = requests.get(api, cookies=self.cookie)
      elif indicator == 'account':
          get_content = requests.get(api, cookies=self.cookie)
          data = get_content.json()
          self.commsId = data[0]['commsId']
          Utils.save_to_file(download_path, get_content)
      elif indicator == 'contacts':
          contacts_api = os.path.join(api + self.commsId + '/', 'contacts')
          get_content = requests.get(contacts_api, cookies=self.cookie)
          Utils.save_to_file(download_path, get_content)
      elif indicator == 'conv':
          conv_api = os.path.join(api + self.commsId + '/', 'conversations')
          get_content = requests.get(conv_api, cookies=self.cookie)
          Utils.save_to_file(download_path, get_content)
          data = get_content.json()
          for eachactivity in data['conversations']:
               conv_id = eachactivity['conversationId']
               message_id = eachactivity['lastMessageId']
               last_modified = eachactivity['lastModified']
               file_name = last_modified.replace(':','-')
               single_conv_thread_API = os.path.join(conv_api + '/' + conv_id + '/', 'messages')
               conv_save_path = os.path.join(location + '/', file_name)
               get_single_thread = requests.get(single_conv_thread_API, params = {'startId':message_id},cookies=self.cookie)
               Utils.save_to_file(conv_save_path + '.json', get_single_thread)

  def download_activities_json_audio(self, api, include_audio):
      #audio global api
      audio_api_global = 'https://pitangui.amazon.com/api/utterance/audio/data?id='
      #activites global api
      activity_api_global = 'https://pitangui.amazon.com/api/activities'
      dialog_activity_api = 'https://pitangui.amazon.com/api/activity-dialog-items?activityKey='
      new_api = api
      size = 50
      offset =- 1
      next_json = ''
      #create new folder in the current directory save all the activities
      location = os.path.join(self.path + '/', 'activities')
      if not os.path.exists(location):
          os.makedirs(location)

      while True:
          #get the activities json, iterating through all activities by changing the url params
          activities = requests.get(activity_api_global, params = {'startTime':next_json,'size':size,'offset':offset},cookies=self.cookie)
          
          #convert json text to python dictionary
          data = activities.json()
          next_json = data['startDate']
          end_time = data['endDate']
          name = Utils.to_human_timestamp(end_time)
          download_path = os.path.join(location + '/', name)
          #Check if there is no data in the activity json, it means we reach the final activity
          if len(data['activities']) == 0:
              break
          else:
              Utils.save_to_file(download_path + ".json", activities.json())
              #Iterate through the the activites to get all the individual activities including the voice command
              #Mind that with one url/api, we only get 50 individual avtivities history, it includes 50 voice part of the file
              if include_audio == 1:
                  for eachactivity in data['activities']:
                      descreption = eachactivity['description']
                      f_name = eachactivity['creationTimestamp']
                      activity_id = eachactivity['id']
                      utterance_id = eachactivity['utteranceId']
                      new_path = os.path.join(location + '/', str(f_name))

                  #audio url/api to the cloud
                  #check if there is no audio
                      if(utterance_id is None):
                          pass
                      else:
                          new_api = audio_api_global + utterance_id
                      #get/request the audio
                          get_voice_data = requests.get(new_api,cookies=self.cookie)

                      #individual Activity API
                      id = activity_id.replace('#','%23')
                      single_activity_api = dialog_activity_api + id
                    
                      #get the single activity
                      get_single_activity = requests.get(single_activity_api,cookies=self.cookie)
                    
                      with open(new_path  + ".json", "wb") as wav:
                          wav.write(get_single_activity.content)
                    
                      #save the audio file
                      with open(new_path  + ".wav", "wb") as wav:
                          wav.write(get_voice_data.content)