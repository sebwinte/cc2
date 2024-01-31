cc2 — drag and drop, like it's hot.
-------------------------------------
This is the default folder. 

You can change it to any folder you like, just have a quick look at the ```settings.json``` and define the path of your 'cc2_folder'. Initially this folder is named 'your_folder_name', but you can name it as you want. Make sure you're using an absolute path like ```"C:\\Users\\Your\\Path\\To\\your_folder_name\\"``` on Windows and ```"/Users/Your/Path/To/your_folder_name/"``` on MacOS. During use, you're going to drag and drop your videos into the folder and automatically start the encoding process. During the process, cc2 generates a status file which shows the encoding process and different status. All options can be easily turned on or off.

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