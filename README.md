<img src="http://pfuscha.cool:3000?" width="90px"/>

cc2 — drag and drop, like it's hot.
-------------------------------------
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)


cc2 is a easy to use video encoder for Windows and macOS. Let's say you need your ```.mp4``` video as a ```.webm``` and ```.ogv```? In a small file size, without quality loss? Just drag and drop your video into your predefined folder and see magic happens.

Update v1.1.0 :zap:
-----------------------------
- cc2 now supports container formats like: **mov**, **mkv**
- We implemented new features:
    - mute audio 
    - see the status of the converting process
- Set the "--copy" flag to copy, i.e. video, audio, subtitles, data and attachments
- Encoding and converting bug fixes

Installation and requirements
-----------------------------
Clone this repo and install all requirements. For this simply run:
```python
pip install -r requirements.txt
```
> Note: cc2 uses the [@FFmpeg](https://www.ffmpeg.org/) framework to compress and convert the videos. So make sure ffmpeg is already installed on your system. 

Quickstart
----------
Open the ```cc2``` folder in your terminal and run:
```
python main.py
```

<img src="https://user-images.githubusercontent.com/38649555/213193160-5ad1ed9a-8e48-453b-9bd9-b830c94757f2.gif"/>

Add custom 'cc2-flags' to your videos and drag it into your 'cc2-folder'. By default this folder is named 'your_folder_name':
```
my-cool-video--low--webm--ogv.mp4
```
After the process has finished, your .mp4 video is now available in a .webm and .ovg format with a low compression rate. Choose at least one container flag in order to start the process. The default compression rate then will be medium.

cc2-flags
---------
As shown in the quickstart example, cc2 works with custom flags which can be easily added to your videos file name. Each flag starts with a double hyphen.

| container         | flag              |
| :------------     | :------------     |
| mp4               | --mp4             | 
| webm              | --webm            |   
| ogv               | --ogv             |  
| mov               | --mov             |  
| mkv               | --mkv             |  

| audio             | flag              |        
| :------------     | :------------     |
| mute audio        | --mute            | 

| compression       | flag              |        
| :------------     | :------------     |
| low               | --low             | 
| medium            | --medium          |   
| high              | --high            |  

Stream copy
-----------
With the ```--copy``` flag you set all codec operations to copy, i.e. video, audio, subtitles, data and attachments. FFmpeg must support muxing the targeted stream into the output container. If it does not, the command will fail. This is very useful, if you only want to change the container format.

| mode              | flag              |
| :------------     | :------------     |
| copy              | --copy            | 


Preferences
-----------
Have a quick look at the ```settings.json``` and define the path of your 'cc2_folder'. Initially this folder is named 'your_folder_name', but you can name it as you want. Make sure you're using an absolute path like ```"C:\\Users\\Your\\Path\\To\\your_folder_name\\"``` on Windows and ```"/Users/Your/Path/To/your_folder_name/"``` on MacOS. During use, you're going to drag and drop your videos into the folder and automatically start the encoding process. During the process, cc2 generates a status file which shows the encoding process and different status. All options can be easily turned on or off.

```json
{   
    "compression":[
        {
            "low":30,
            "medium": 60,
            "high": 90
        }
    ],
    "settings":[
        {
            "notification" : true,
            "file_status" : true,
            "cc2_folder" : "your_folder_name"
        }
    ]
}
```
Useful cc2-flag combinations
----------------------------
cc2 offers different flag combinations. For example:
#### compression only (container reamains the same):
```
my-cool-video--low--medium.ogv
```
#### container only (default compression):
```
my-cool-video--mp4.webm
```
#### container and compression:
```
my-cool-video--low--medium--webm--ogv.mp4
```
#### stream copy and change container format:
```
my-cool-video--copy--mov.mp4
```

Supported container formats and codecs
-------------------------------------- 

| container         | codec         |
| :------------     |:------------  |
| mp4               | libx264       | 
| webm              | libvpx-vp9    |   
| ogv               | libtheora     | 
| mkv, mov          | libx264       | 

Troubleshooting
---------------
<details>
<summary>"Error directory not found"</summary>
<p>Make sure your 'cc2_folder' exists. Double check the path in the settings.json</p>  
</details>
<details>
<summary>"ImportError: No module named utils.helper"</summary>
<p>Python has to be at least version 3.6</p>  
</details>
