import os

source = '/home/s13/projects/sensehat_chatbot/embedded/assets/audio_files/current_user_prompt'
destination = '/home/s13/projects/sensehat_chatbot/embedded/assets/audio_files/old_user_prompt'


def move_stuff():    
    allfiles = os.listdir(source)
    print("files in here", allfiles)
    for f in allfiles:
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination, f)
        os.rename(src_path, dst_path)

def main():
    move_stuff()



if __name__ == "__main__":
    main()
