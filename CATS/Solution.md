## Challenge - CATS!

### Problem
```
CATS OMG I CAN'T BELIEVE HOW MANY CATS ARE IN THIS IMAGE I NEED TO VISIT CAN YOU FIGURE OUT THE NAME OF THIS CAT HEAVEN?

Answer is the domain of the website for this location. For example, if the answer was ucla, the flag would be lactf{ucla.edu}.
```
<img src="https://github.com/adaisyx/lactf22-writeup/blob/main/CATS/CATS.jpeg"  width="300" height="400">


### Solution
Conduct regular image checks:
1. Properties
2. Reverse image search
3. EXIF tool (https://exif.tools/)

The EXIF tool returns a location result: ```Lanai Cat Sanctuary```

<img src="https://github.com/adaisyx/lactf22-writeup/blob/main/CATS/lanai.png"  width="400" height="200">


From there, just google the sanctuary to find the website: ```https://lanaicatsanctuary.org/```

**Flag: lactf{lanaicatsanctuary.org}**
