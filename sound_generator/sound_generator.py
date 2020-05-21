import threading
import vlc
import time
import random

class Sound_generator():
    def __init__(self,max_seq_length=5,intertime=1/2,min_sleep=2,max_sleep=5):
        self.max_seq_length = max_seq_length
        self.intertime = intertime
        self.min_sleep = min_sleep
        self.max_sleep = max_sleep
        self.flag = False
        self.notes_list = ["Ab4","Ab5","Bb4","Db4","Db5","Eb4","Eb5","Gb4","Gb5"]
        self.note_trigger = "bass"
        
    
    def launch(self):
        while(self.flag):
        
            l_seq = random.randrange(self.max_seq_length)

            for i in range(l_seq):
                self.play(random.choice(self.notes_list))
                time.sleep(self.intertime/random.choice((1,2)))

            time.sleep(random.uniform(self.min_sleep,self.max_sleep))
        
    
    def start(self):
        """
        Starts the random sequence generation
        """
        self.flag = True
        self.main_thread = threading.Thread(target=self.launch)
        self.main_thread.start()
    
    
    def stop(self):
        """
        Stops the random sequence generation
        """
        self.flag = False
    
    
    def trigger(self):
        """
        Plays a note to accompagny a jump or another transition
        """
        self.play("bass")
        
    
    def play(self,note):   
        player = vlc.MediaPlayer("piano_notes/"+note+".mp3")
        t = threading.Thread(target=player.play)
        t.start()