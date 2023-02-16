### PROBLEM
```
Where was this photo taken? I think it used to be in the original photo, but someone cropped it out!

The flag is lactf{location}, where location is the name of the POI that this person hiked up to, 
all lowercase and replacing spaces with underscrolls. Use the google maps name of the POI
```
<img src="https://github.com/adaisyx/lactf22-writeup/blob/main/Hike-To-Where/picture.jpg"  width="300" height="400">

 

&nbsp;  


### SOLUTION
Conduct regular image checks:
1. Properties
2. Reverse image search
3. EXIF Tool

There was no result, so I proceeded to approach from a different angle. There is a man in the photo wearing a "UCLA Computer Science" shirt. We can see the following text:
```
Hike up to...
Thank you so much to...
Running this event
```
We're looking for a real man, who's hiked up to a real location, in a real event. (i.e. the opposite of every other OSINT ctf challenge I've ever done, where the social media accounts are all "fake".) 

&nbsp;  

On the UCLA computing faculty website ```https://samueli.ucla.edu/search-faculty/#cs``` we find the following profile:

<img src="https://github.com/adaisyx/lactf22-writeup/blob/main/Hike-To-Where/carey.png"  width="200" height="250">

We've found the man's identity: ```Carey Nachenberg```
It was here I proceeded to spend 1hour stalking this *very real man*. It was easy to get sidetracked because unlike a regular CTF OSINT where there are 1 or 2 sparse fake accounts created for the CTF, our *very real man* had a lot of *very real accounts*. 
I will not be posting links to any of his accounts, for the sake of his privacy, but I did find the following:
1. Facebook
2. Twitter
3. Instagram
4. Personal Website

I proceeded to try flags based on the hiking locations he shared on each of these social media sites, but none of them were correct. 
At this point, I recalled the insight from before: ```running this event```. 
Rather than continue to stalk this *very real man*, I proceeded to try to find this event directly.
Googling ```Cary Nachenberg hike``` (no google dork needed!) leads us to the following two results:
```
https://www.tickettailor.com/events/peaksprofessorsatucla/792649
https://www.peaksandprofessorsucla.org/post/11-06-skull-rock-via-temescal-canyon-w-carey-nachenberg
```
This confirmed the existence of this hiking event.

**Flag: lactf{skull_rock}**
