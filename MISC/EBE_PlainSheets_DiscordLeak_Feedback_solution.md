## CHALLENGE: EBE 

### PROBLEM
```
I was trying to send a flag to my friend over UDP, one character at a time, but it got corrupted! I think someone else was messing around with me and sent extra bytes, though it seems like they actually abided by RFC 3514 for once. Can you get the flag?
```

### SOLUTION

We're given a .pcap file with a bunch of UDP packets. The description did say that the flag was sent "one character at a time", and inspecting each packet seems to match this description. 

However, if you right click a packet and click ```Follow UDP stream```, it returns a bunch of garbage due to the "extra bytes" mentioned.

Thankfully, we know that the flag format is ```lactf{...}```, so we can observe that when we first see "lactf" appear in the packets, the contents are different from that of the irrelevant packets. There's a ```64```/ the character "d" at this part of the packet:

<img src="https://cdn.discordapp.com/attachments/979013758846394420/1073911796060127262/image.png">

Select this in wireshark, right click it and select ```Filter```.
I didn't know a neater way to do this, but I then pressed Ctrl + A and exported the selected packets into a seperate .pcap file.

Now we can open it and follow the UDP stream normally!

**Flag: lactf{3V1L_817_3xf1l7R4710N_4_7H3_W1N_51D43c8000034d0c}**


## CHALLENGE: hidden in plain sheets

### PROBLEM
```
I found this google sheets link on the internet. I'm sure it's hiding something, but I can't find anything? Can you find the flag?

https://docs.google.com/spreadsheets/d/1OYx3lCccLKYgOvzxkRZ5-vAwCn3mOvGUvB4AdnSbcZ4/edit#gid=0
```

### SOLUTION
We are greeted with a google spreadsheet with few useful features on the surface. Closer inspection shows that 1. The beginning sheet is useless 2. There's a hidden sheet named "flag" on the document (click view > hidden sheets).

Early into this challenge, we found a helpful article that seemed to be helpful for this exact scenario. Woefully, we did not find the ```stream-rows``` request that it mentioned - maybe google got around to patching it?
```https://blog.andrewcantino.com/blog/2019/01/27/why-security-expectations-matter-google-sheets-hidden-content/```

After a long time of struggling with those network requests, it was good ol find and replace that did the trick instead. Turns out that it finds characters from hidden sheets too! With some luck, we found that one character occupies 1 cell. From there, we searched each cell from flag!A1 to flag!AR1 (range) with a "." wildcard which will automatically give the value of the cell. We then strung the flag together. 

**Flag: lactf{H1dd3n_&_prOt3cT3D_5h33T5_Ar3_n31th3r}**

### COMMENTS

After the CTF, we also found out that you can simply import the contents of another google sheet into one you have access to. A convenient alternative. 


## CHALLENGE: discord l34k

### PROBLEM
```
My friend sent me this message link that apparently links to a "flag", but discord says "You don't have access to this link"! They did mention something about them being able to embed a list of online users on their own website, and sent me this image. Can you figure out how to join the server?

Note: Discord phone verification is NOT required for this challenge.
```
https://github.com/uclaacm/lactf-archive/blob/main/2023/misc/discord-leak/embed.png

The given image hints that embeds are useful. From googling, they seem to be referring to this:
```
https://www.wpbeginner.com/wp-tutorials/how-to-embed-discord-widget-into-wordpress/#:~:text=First%2C%20go%20to%20the%20WordPress,look%20on%20your%20WordPress%20website. 
```

I went to a discord server with admin perms and copied the ```server settings > widget code```. Then, I replaced the id with the first set of numbers in the given url.
```
<iframe src="https://discord.com/widget?id=1060030874722259057&theme=dark" width="350" height="500" allowtransparency="true" frameborder="0" sandbox="allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts"></iframe>
```

I then put the resultant code in ```https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic``` to view the embed. Thanks, w3schools! From there, it was a simple matter of clicking "Join server" and reading the flag from the starting channel.

**Flag: lactf{D15C0rD_W1D6375_134K_1NV1735}**


### SOLUTION


## CHALLENGE: feedback 

### PROBLEM
```
We really appreciate your feedback, so much so that we are forcing you to fill it out for points!
```

### SOLUTION

Who am I to reject some free points and to log down a free flag. Oh, but a twist! The flag is scattered through the survey! One part is at the start, one in an option to a question towards the end, and the last only given when you submit it. Do your feedback forms! 

**Flag: lactf{i_give_my_very_helpful_feedback_and_i_actually_submitted}**