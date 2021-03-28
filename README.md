<img src="http://pfuscha.cool:3000/" width="120" />

# cc2 — drag and drop it like it's hot.  
cc2 is a easy to use video encoder for Windows and MacOS. Let's say you need your ```.mp4``` video as a ```.webm``` and ```.ogv```? In a small file size, without quality loss? Just drag and drop your video into your predefined folder and see magic happens.

### How to start:
The easiest way to get started is to clone this repo and to start with installing all requirements. For this simply run:
```python
pip install -r requirements.txt
```
> Note: cc2 uses the [@FFmpeg](https://www.ffmpeg.org/) framework to compress and convert the videos. So make sure ffmpeg is already installed on your system. 

### Preferences:
Have a quick look at the ```settings.json```. 

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
            "notification": true,
            "cc2_folder" : "your_folder_name/"
        }
    ]
}
```
