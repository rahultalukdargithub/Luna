import requests
from bs4 import BeautifulSoup
import datetime
import os
import glob
import random
from playsound import playsound
import t2t
import t2snew as t2s

# Directory paths
save_directory = "path-of-your-save-directory"
send_directory = "path-of-your-send-directory"

# Function to fetch weather information
def fetch_weather():
    search = "temperature in my location"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    sta = data.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text
    data = sta.split('\n')
    Time = data[0]
    sky = data[1]
    return Time, sky

# Function to take voice commands
def take_command(directory):
    os.listdir(directory)
    file = os.path.join(directory, os.listdir(directory)[-1])
    with open(file, 'r') as file:
        text = file.read()
    return text

# Initialize the text responses
Hello = ('hello', 'hey', 'hii', 'hi')
reply_Hello = ('Hello Sir, I Am Luna.', "Hey, What's Up? I Am Luna.", "Hey How Are You? I Am Luna.", "Hello Sir, Nice To Meet You. This is Luna.")
Bye = ('bye', 'exit', 'sleep', 'go', 'goodbye', 'good bye', 'good bye luna', 'go to sleep')
reply_bye = ('Bye Sir.', "It's Okay.", "It Will Be Nice To Meet You.", "Bye.", "Thanks.", "Okay.")
How_Are_You = ('how are you', 'are you fine')
reply_how = ('I Am Fine.', "Excellent.", "Moj Ho rhi Hai.", "Absolutely Fine.", "I'm Fine.", "Thanks For Asking. I Am Fine.")
nice = ('nice', 'good', 'thanks')
reply_nice = ('Thanks.', "Ohh, It's Okay.", "Thanks To You.")
Functions = ('functions', 'abilities', 'what can you do', 'features')
reply_Functions = ('I Can Perform Many Tasks Or Varieties Of Tasks, How Can I Help You?', 'I Can Call Your G.F.', 'I Can Message Your Mom That You Are Not Studying.', 'I Can Tell Your Class Teacher That You Had Attended All The Online Classes On Insta, Facebook, etc!', 'Let Me Ask You First, How Can I Help You?', 'If You Want Me To Tell My Features, Call: Print Features!')
sorry_reply = ("Sorry, That's Beyond My Abilities.", "Sorry, I Can't Do That.", "Sorry, That's Above Me.", "Repeat it again correctly.")

num = 1

# Main function to handle user queries
if __name__ == "__main__":
    processed_files = set()
    while True:
        new_files = [f for f in glob.glob(os.path.join(save_directory, "*.txt")) if f not in processed_files]
        if not new_files:
            continue
        for file_path in new_files:
            processed_files.add(file_path)
            try:
                query = take_command(save_directory).lower()
            except Exception as e:
                continue
            
            if query == "none":
                continue

            if query in Bye:
                reply = random.choice(reply_bye)
                path = t2s.te2sp(reply + "Wake me up whenever you need! I'm deleting all the saved MP3 and TXT files.")
                playsound(path)
                print("Goodbye sir!")
                files = glob.glob(os.path.join(save_directory, '*.mp3')) + glob.glob(os.path.join(save_directory, '*.txt'))
                for file in files:
                    try:
                        os.remove(file)
                        print(f"Deleted: {file}")
                    except Exception as e:
                        print(f"Error deleting {file}: {e}")
                break
            elif query in Hello:
                reply = random.choice(reply_Hello)
            elif query in How_Are_You:
                reply = random.choice(reply_how)
            elif query in nice:
                reply = random.choice(reply_nice)
            elif query in Functions:
                reply = random.choice(reply_Functions)
            else:
                reply = t2t.ansgen(query + ", write it in 1000 characters, don't write this \"1000 characters\" in the answer")

            # Save the reply to a new text file
            txt_file_path = os.path.join(send_directory, f'{num}.txt')
            num += 1
            with open(txt_file_path, 'w') as file:
                file.write(reply)
            print(reply)
