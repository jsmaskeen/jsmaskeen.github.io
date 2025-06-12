---
layout: post
title: IITGN Summer Siege CTF Write-up
date: 2025-06-13 01:35:13
description: A write-up covering all questions I attemted for the CTF.
tags: CTF

toc:
  beginning: true
---

# Introduction

Hi, this is a write-up for all the questions I attempted in the IITGN Summer Siege CTF Contest. I will proceed with the question description and any hints and files if provided.

Most of the questions are standalone, as in they don't require any external server or anything, so you can follow along if you want to solve them.

Let's start; I will list the questions in alphabetical order.

---

---

# Question: BASEic


| Details |  |
|---|---|
| Points 	| 50 	|
| Category 	| Crypto 	|
| Hints 	| None |
| Date 	| 30-05-2025 	|
|Files | None |
|Flag | `SSCTF{n0t_41w4y5_b453ga}` |
|OS |Windows |


## Description:
```
You know the drill:

S05KVUdWQ0dQTlhEQTVDN0dRWVhPTkRaR1ZQV0VOQlZHTlRXQzdJPQ==
```

## First Attempt
BASE hints at base64 decoding, and decoding `S05KVUdWQ0dQTlhEQTVDN0dRWVhPTkRaR1ZQV0VOQlZHTlRXQzdJPQ==` using base64 results in `KNJUGVCGPNXDA5C7GQYXONDZGVPWENBVGNTWC7I=`.

Now decoding this again with base64 results in gibberish, so lets try base32 [Why ? Because putting the string on [Cipher Identifier](https://www.dcode.fr/cipher-identifier) indicates base32].

Using base32 decoding, we get `SSCTF{n0t_41w4y5_b453ga}` which is the flag.

Note: All decoding done in [CyberChef](https://gchq.github.io/CyberChef/).

> Answer `SSCTF{n0t_41w4y5_b453ga}`

---

# Question: Become the admin

| Details |  |
|---|---|
| Points 	| 100 	|
| Category 	| Miscellaneous 	|
| Hints 	| Password = "itis\*\*\*\*\*password" and all lowercase |
| Date 	| 30-05-2025 	|
|Files | None |
|Flag | `CTF{ctfmaster-techctf@iitgn.ac.in-itisaweekpassword}` |
|OS |Windows |


## Description:
```
http://20.244.35.150

Find username ,email, password of administrator of this website.

FORMAT: CTF{username-email-password}
```

## First Attempt
Upon loading the webpage, this is shown
{% include figure.liquid path="/assets/iitgnssctf/become_the_admin/image.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

The CMS made simple hints at the website manager/creator used.

We are to find the username, email, and password, so it looks like we need to get access to the database. Navigating to a few random hyperlinks on the webpage indicates that PHP is being used.

So, the first instinct is to scan using Nmap for open ports on the URL.

{% include figure.liquid path="/assets/iitgnssctf/become_the_admin/image-1.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

Doing that results in ports 80 and 22 being open for SSH.

But ssh isn't helpful unless we know the username or public/private key.

So, we are stuck.

Googling about CMS and databases reveals SQL injection might be possible. Searching for that tells us that there is a vulnerability in CMS version < 2.2.10. 

{% include figure.liquid path="/assets/iitgnssctf/become_the_admin/image-4.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

And at [exploit-db](https://www.exploit-db.com/exploits/46635) there is a script available to extract username, email and password. See [bcmadmn.py](/assets/iitgnssctf/become_the_admin/bcmadmn.py).

Running the script with rockyou.txt and the given host, reveals the following:
{% include figure.liquid path="/assets/iitgnssctf/become_the_admin/image-2.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

Now we know the password format is `itis*****password` and it is all lowercase, So we only need to check $26^5$ possibilites. We can use a simple python script to do that. See [bcmadmn2.py](/assets/iitgnssctf/become_the_admin/bcmadmn2.py).

{% include figure.liquid path="/assets/iitgnssctf/become_the_admin/image-3.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

> Answer `CTF{ctfmaster-techctf@iitgn.ac.in-itisaweekpassword}`

---

# Question: Capture and Crack

| Details |  |
|---|---|
| Points 	| 100 	|
| Category 	| Network Security 	|
| Hints 	| None |
| Date 	| 30-05-2025 	|
|Files | 1. [handshake.cap](/assets/iitgnssctf/capture_and_crack/handshake.cap) |
|Flag | `CTF{simplicity}` |
|OS |Windows |


## Description:
```
Your friend ran out of mobile data, but being skilled in networking, he managed to capture a Wi-Fi handshake (.cap file) from a nearby network. He’s now asking for your help to crack the password from the captured file.

Can you retrieve the Wi-Fi password from the handshake?
```

## First Attempt
We have to get the password somehow using the .cap file. Googling it gives us a hint about using [aircrack-ng](http://aircrack-ng.org/). Using the GUI version and putting in the .cap file and the wordlist rockyou.txt results in us knowing the password.

{% include figure.liquid path="/assets/iitgnssctf/capture_and_crack/image.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}



> Answer `CTF{simplicity}`

---

# Question: Cursed Schedule

| Details |  |
|---|---|
| Points 	| 50 	|
| Category 	| OSINT 	|
| Hints 	| None 	|
| Date 	| 02-06-2025 	|
|Files | None |
|Flag | `CTF{100k_d$$p_in_c0de}` |
|OS |Windows |


## Description:
```
A seemingly ordinary timetable… or is it? [https://timetable-ky2z.onrender.com](https://timetable-ky2z.onrender.com)

The flag is hiding in plain sight, all you need is a hacker’s eye to spot it.
```

## First Attempt
Opeining the webpage and inspecting the code, gives us this base64 encoded comment.

`Y29kZWJhc2UgbWF5IGdpdmUgbW9yZSBpbmZvcm1hdGlvbg` = `codebase may give more information`

{% include figure.liquid path="/assets/iitgnssctf/cursed_schedule/image.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

This when decoded tells us to look through the codebase.

On the [github repo](https://github.com/Naveen-Pal/timetable), we look at the commit history for `index.html` for when was the above comment added,
which gives us this [commit](https://github.com/Naveen-Pal/timetable/commit/6f0a594).

Now we look for files changed in recent commits in neighborhood of this commit and find that in style.css, [see commit](https://github.com/Naveen-Pal/timetable/commit/61420dd),
`Q1RGezEwMGtfZCQkcF9pbl9jMGRlfQ==` was added as a comment.

Which when decoded gives us our flag, `CTF{100k_d$$p_in_c0de}`.

> Answer `CTF{100k_d$$p_in_c0de}`

---

# Question: Depths of Deception

| Details |  |
|---|---|
| Points 	| 40 	|
| Category 	| Forensics 	|
| Hints 	| None |
| Date 	| 01-06-2025 	|
|Files | [ctf.zip](/assets/iitgnssctf/depths_of_deception/ctf.zip) |
|Flag | `CTF{f0c4946a4e0e24784716590f0fc48f96fb27dbf63b025f6766c5fe9fe25cf826}` |
|OS |Windows |


## Description:
```
A notorious hacker known as The Archivist concealed their greatest secret within an elaborate, randomly generated directory maze named ctf/. Each folder you explore leads you deeper into a web of deceptive subdirectories and decoy files designed to throw you off the scent. Somewhere within this tangled labyrinth lies a single, genuine file that holds the key to the true flag. Can you navigate the deception, avoid the dead ends, and uncover the one real clue hidden among the distractions? Good luck!

PS: Don’t be disappointed after you find the flag—the answer has been right in front of your eyes all along.
```

## First Attempt
After downloading the zip and looking at its size, it is 80MB, and we are given that it contains a nested directory structure, so extracting the entire zip would be a disaster. So, we need some way to look into the contents of this zip file, that is, see all the folders and the files.

So run `tar -tvf ctf.zip > contents.txt`.
This gives us the detailed list of all the folders and files present in the archive. See [content.txt](/assets/iitgnssctf/depths_of_deception/content.txt).

Now searching for lines which don't end with `/` as the question says a `file` holds the key to flag, and files dont end with `/`, we find the following files:

```
-rw-r--r--  0 501    20        137 Jun 01 02:07 ctf/m6iqv2mija/jtlk63hd6l/usozih83cg/7gcb5cmt7f/ksqr914fyu/ph12u9cdno/g2ngloxvxs/j8xpujpdez/pilvhqvqln/fu5c5n1wrb/hof0obspqv/jgpg31r0zm/klkm35kxtufqy5x.bruh
-rw-r--r--  0 501    20        137 Jun 01 02:08 ctf/m6iqv2mija/jtlk63hd6l/usozih83cg/7gcb5cmt7f/ksqr914fyu/ph12u9cdno/g2ngloxvxs/j8xpujpdez/pilvhqvqln/5e481cba6b/iys6lmkoie/w5jlq4jh3f/i1uyiv6r64/lvtwsutmu3/q1t00lg4io03wuf.bruh
-rw-r--r--  0 501    20        107 Jun 01 02:08 ctf/m6iqv2mija/jtlk63hd6l/phe02aeqo7/n2epbsw5rq/401s1cng1x/3ax7nn8dz7/jmv9zzvrvo/wu1lynz401/lso9rmt81f/cvbv1cngdg/tuuclzqqgt/0stxv8eaks/pzwj1j8j67/2jfx4s7nhu/ht1pbab8114rzvg.bruh
-rw-r--r--  0 501    20        137 Jun 01 02:08 ctf/m6iqv2mija/jtlk63hd6l/phe02aeqo7/n2epbsw5rq/ozjzga6ye2/eytq9y601m/aid0x4v2sc/in8n4jrqi2/cwxwlqtore/o40udtr6cz/83nwjkbwcj/xq7lsz9gsa/e168au4s3y/s0g032j0lh/mpeiipqsgww5b1a.bruh
-rw-r--r--  0 501    20        137 Jun 01 02:08 ctf/m6iqv2mija/jtlk63hd6l/phe02aeqo7/n2epbsw5rq/ux5wbwuhqm/74bf3kn991/6t1idnxvqf/5isyy3i2rn/lo4lht2fky/wz7tkeseo0/w7322aa3m9/dmap8psdm0/pcsqsur6cy/tntkr1chti/z914i3nghl/zwg23qyd1l/5sk3m9qbv6beik0.bruh
```

Now looks like four out of the five files are of the same size. So we extract all these files from [ctf.zip](/assets/iitgnssctf/depths_of_deception/ctf.zip), using,

```
tar -xvf ctf.zip ctf/m6iqv2mija/jtlk63hd6l/usozih83cg/7gcb5cmt7f/ksqr914fyu/ph12u9cdno/g2ngloxvxs/j8xpujpdez/pilvhqvqln/fu5c5n1wrb/hof0obspqv/jgpg31r0zm/klkm35kxtufqy5x.bruh
```

After that we move all these files out so that we don't need to traverse down the directory path every time to take a look at these.

```
mv ctf/m6iqv2mija/jtlk63hd6l/usozih83cg/7gcb5cmt7f/ksqr914fyu/ph12u9cdno/g2ngloxvxs/j8xpujpdez/pilvhqvqln/fu5c5n1wrb/hof0obspqv/jgpg31r0zm/klkm35kxtufqy5x.bruh .
```

Now we have `ht1pbab8114rzvg.burh`, `klkm35kxtufqy5x.bruh`, `mpeiipqsgww5b1a.bruh`, `q1t00lg4io03wuf.bruh`, and `5sk3m9qbv6beik0.bruh`.

As noted earlier, `klkm35kxtufqy5x.bruh`, `mpeiipqsgww5b1a.bruh`, `q1t00lg4io03wuf.bruh`, and `5sk3m9qbv6beik0.bruh` have the same size as well as the same content.

```
87?1?/0K4VFWbFAF*&O;Dfd+DEc5c1ARlr,6?RAmDJ<Tl+EqaECER,-@:O(eDJ()6BOr;tDI[TqBl7Q9+A69WE$/\*B4kprB.P0IBOu3q+DGm>D/XH++Eq7.FD5W*+D,P4+F.mJ+T
```

And `ht1pbab8114rzvg.burh` has a different size, with contents,

```
<+ohcAo(mg+DGm>FD,5.F(eu;2)ZRj@<6*)De:,6BOr;i8PgOJAfu2/BlbD.DKKT5AKYT'Ch.*t/0JYE+EV:.+D,P4D..N/6W?O%BOPsqI/
```

Now `ht1pbab8114rzvg.burh` seems to lead to correct flag, while others might be a decoy.

Using the cipher identifier at [dcode.fr](https://www.dcode.fr/cipher-identifier),
we observe that both strings are ASCII-85 encoded.

Decoding both of them gives us,

{% include figure.liquid path="/assets/iitgnssctf/depths_of_deception/image.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

and

{% include figure.liquid path="/assets/iitgnssctf/depths_of_deception/image-1.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

So we guessed correctly, that the four files were a decoy and one files leads to correct flag.

Computing SHA-256 of the archive using a simple script, leads us to the right flag.
{% raw %}
```py
import hashlib

def sha256_file(file_path: str) -> str:
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()

file_path = "ctf.zip"
print(f"CTF{{{sha256_file(file_path)}}}")
```
{% endraw %}

> Answer `CTF{f0c4946a4e0e24784716590f0fc48f96fb27dbf63b025f6766c5fe9fe25cf826}`

---

# Question: Forgotten Credentials

| Details |  |
|---|---|
| Points 	| 50 	|
| Category 	| Crypto 	|
| Hints 	| None |
| Date 	| 30-05-2025 	|
|Files | None |
|Flag | `SSCTF{goodpassword123}` |
|OS |Windows |


## Description:
```
You’re a developer who built a sleek, minimal login system for your internal app — clean UI, local-only, no cloud fuss. Everything was working fine until you forgot the admin password... again.

When you dug into your backend database, you found the password stored like this:

a0805b87ae9333c16f9645abec3e6c9a
No password reset feature. No second chance. Your only way in? Recover the forgotten password from this hash.

You’re 100% sure the password was one of your usual go-to's... but which one? You’ve reused it so many times it's probably leaked by now.

Flag format: SSCTF{recovered_password}
```

## First Attempt
The question seems easy. We know that in the database, the password is stored as a hash, and we know the password has probably been leaked, so we can check online for leaked hashes and try to guess the password.

So going to [https://crackstation.net/](https://crackstation.net/) and searching for the hash, we immediately get the password is: `goodpassword123`


> Answer `SSCTF{goodpassword123}`

---

# Question: Shattered Pixels

| Details |  |
|---|---|
| Points 	| 50 	|
| Category 	| Miscellaneous 	|
| Hints 	| None 	|
| Date 	| 30-05-2025 	|
|Files |1. [capture.pcap](/assets/iitgnssctf/shattered_pixels/capture.pcap) |
|Flag | `CTF{my_br4in_is_4m4zing}` |
|OS |Windows |


## Description:
```
Briefing: A message scattered across the ether, hidden in the pulse of network traffic. Each fragment drifts aimlessly, broken and incomplete, waiting to be drawn back together.

The image was never meant to be whole. It was split, dispersed across time and space.

Find the missing pieces. Reconstruct what was once intactâ€”and unveil the hidden truth within.

Flag Format: CTF{...}
```

## First Attempt
First instinct was to open the pcap file, and we require [wireshark](https://www.wireshark.org/) to do that,
{% include figure.liquid path="/assets/iitgnssctf/shattered_pixels/image.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

Looking at the first packet, we see that the data has a PNG header, so if the last packet also contains the IEND footer, we have an entire PNG image in this pcap file.

{% include figure.liquid path="/assets/iitgnssctf/shattered_pixels/image-1.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

As it turns out the last packet does have IEND footer. So lets extract the image from this pcap fil using python.

```py
from scapy.all import rdpcap, TCP
packets = rdpcap("capture.pcap")
payload = bytearray()
for pkt in packets:
    if TCP in pkt and pkt[TCP].payload:
        payload.extend(bytes(pkt[TCP].payload))
start_sig = b"\x89PNG\r\n\x1a\n"
end_sig   = b"IEND\xaeB`\x82"

start = payload.find(start_sig)
end   = payload.find(end_sig, start + len(start_sig))
if start != -1 and end != -1:
    png_data = payload[start:end + len(end_sig)]
    with open("recovered.png", "wb") as f:
        f.write(png_data)
    print("Yay")
else:
    print("Shit")
```

This gives us the recovered.png file, from where we can clearly see the flag.

{% include figure.liquid path="/assets/iitgnssctf/shattered_pixels/image-2.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

> Answer `CTF{my_br4in_is_4m4zing}`

---

# Question: The Sound of Secrets

| Details |  |
|---|---|
| Points 	| 10 	|
| Category 	| Hackrush CTF Unsolved 	|
| Hints 	| 1. HRCTF{y0u_4r3_r1ckr0113d} is not the flag. JS script is the next thing to try.<br>2. Lal Minar is the landmark tower of IIT Gandhinagar. 	|
| Date 	| 05-04-2025 	|
|Files |1. [eeeasssy.wav](/assets/iitgnssctf/sound_of_secrets/eeeasssy.wav) |
|Flag | `HRCTF{ch3ck_th3_EX1F_m3t4d4t4_b3f0r3_y0u_sh4r3}` |
|OS |Windows |

## Description:
```
The answer lies not in what you hear, but in what you see. Examine the frequencies, not the waves. Tools like Sonic Visualizer may help you see the truth. Sometimes, secrets hide in the spectrum of sound.
```

## First Attempt
Upon first listening to the audio file, one gets rickrolled first 😆, then at the end one notices binary sounds.

Opening the audio file in [Sonic Visualiser](https://www.sonicvisualiser.org/), the waveform at the ends looks something like this:
{% include figure.liquid path="/assets/iitgnssctf/sound_of_secrets/image.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}
which is quite different from the waveform preceeding the cursor.

Next as the problem statement suggests, looking at the spectrogram (Pane -> Add Spectrogram ) reveals this flag.
{% include figure.liquid path="/assets/iitgnssctf/sound_of_secrets/image-7.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}
> Wrong Flag 1: `HRCTF{y0u_4r3_r1ckr0113d}`

## Looking more closely at audio file
So, now one might think there is some hidden data in the audio file. So one might try to extract all the strings in the .wav file, using the [strings.exe from Sysinternals Suite](https://learn.microsoft.com/en-us/sysinternals/downloads/strings).

> Run `strings.exe eeeasssy.wav > sound_of_secrets.txt`

This gives the [sound_of_secrets.txt](/assets/iitgnssctf/sound_of_secrets/sound_of_secrets.txt) file. Scrolling down towards the end, one observes a really long string, which seems encoded in **base64**.
{% include figure.liquid path="/assets/iitgnssctf/sound_of_secrets/image-2.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

Decoding this gives us two things, first a hint, and second a really long base64 encoded string.
{% include figure.liquid path="/assets/iitgnssctf/sound_of_secrets/image-3.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

> //Hint:_try_to_to_spectral_analysis_using_audacity.ref:watch?v=EVsx0pE8uPI

This links to a [youtube video](https://www.youtube.com/watch?v=EVsx0pE8uPI), which tells how to use audacity to hide images in audio. However they use the frequency technique which was our first attempt hence this is of no use.

However if one decodes the really long base64 string again and again around five times, one gets some long javascript code. See [jscode.js](/assets/iitgnssctf/sound_of_secrets/jscode.js)

If one pastes this code in console window of our browser, one can see an alert, which tells us to go look at the IITGN's wikipedia page.
{% include figure.liquid path="/assets/iitgnssctf/sound_of_secrets/image-4.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

Going to IITGN's wikipedia page, and looking at the [edit history](https://en.wikipedia.org/w/index.php?title=IIT_Gandhinagar&action=history) around the time of HackRush 25, reveals some important things.

{% include figure.liquid path="/assets/iitgnssctf/sound_of_secrets/image-8.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

Comparaing these two versions one sees two things,
1. A new file is added.
{% include figure.liquid path="/assets/iitgnssctf/sound_of_secrets/image-1.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}
2. A test flag was deleted.
{% include figure.liquid path="/assets/iitgnssctf/sound_of_secrets/image-5.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

So looks like one is on the right track. However `HRCTF{trial}` is invalid flag for this problem. So one figures out that there must be somehting hidden in the image, [Lal_Minar_IIT_Gandhinagar](/assets/iitgnssctf/sound_of_secrets/Lal_Minar_IIT_Gandhinagar.png).

If one uploads this image to an online [image stegnography decoder](https://stylesuxx.github.io/steganography/), one can directly see the actual flag, which is the answer to the question.
{% include figure.liquid path="/assets/iitgnssctf/sound_of_secrets/image-6.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

> Answer `HRCTF{ch3ck_th3_EX1F_m3t4d4t4_b3f0r3_y0u_sh4r3}`

## Note:
I am sorry for writing this in second person! Somehow I liked it.

---

# Question: Tic-Tac-Toe


| Details |  |
|---|---|
| Points 	| 30 	|
| Category 	| Miscellaneous 	|
| Hints 	| None 	|
| Date 	| 30-05-2025 	|
|Files |1. [XOX.html](/assets/iitgnssctf/tic-tac-toe/XOX.html) |
|Flag | `CTF{XOX_XOX_XOX_is_easy}` |
|OS |Windows |


## Description:
```
Win the Tic Tac Toe
```

## First Attempt
Just opening the html file and winning tic tac toe gives,
```
DUG|YPY`YPY`YPY`jt`fbtz~
```

which is not the flag.

So we look at the source code, and observe the function, 

```js
// Function to encrypt the flag
function encryptFlag(flag) {
    let encryptedFlag = "";
    for (let i = 0; i < flag.length; i++) {
        let charCode = flag.charCodeAt(i);
        encryptedFlag += String.fromCharCode(charCode + 1);
    }
    return encryptedFlag;
}
```
Reversing this function (Caesar Cipher),
```js
function decryptFlag(encryptedFlag) {
    let decryptedFlag = "";
    for (let i = 0; i < encryptedFlag.length; i++) {
        let charCode = encryptedFlag.charCodeAt(i);
        decryptedFlag += String.fromCharCode(charCode - 1);
    }
    return decryptedFlag;
}
```

And running 
```js
decryptFlag('DUG|YPY`YPY`YPY`jt`fbtz~')
```
 in console gives us the flag.

> Answer `CTF{XOX_XOX_XOX_is_easy}`

---

# Question: Triple-Locked Secrets

| Details |  |
|---|---|
| Points 	| 70 	|
| Category 	| Miscellaneous 	|
| Hints 	| Another secret was released EgUROSUnNCE7MB07LC4wJx04LCQlMCcuPw== <br>It is said that "Order matters. The key is '0x42'." 	|
| Date 	| 30-05-2025 	|
|Files | None |
|Flag | `CTF{triple_layer_mastery}` |
|OS |Windows |


## Description:
```
Mission Briefing: Deep within the archives of the derelict starcruiser NOVA-X9, a secure datacore was discovered. Encoded with ancient encryption tech, it contains a string—Hm0xJTYNNVU2CDIRNwQwAg==—suspected to hold critical intel from the long-lost Terran Federation.

Your objective: Decrypt the cipher. Unveil the hidden flag. Save the stars.

Flag Format: CTF{...}
```

## First Attempt
At first `Hm0xJTYNNVU2CDIRNwQwAg==` looks like base64 encoded, however decoding it gives us gibberish.

Even [Cipher Identifier](https://www.dcode.fr/cipher-identifier) fails to give a good result.

Looking at `EgUROSUnNCE7MB07LC4wJx04LCQlMCcuPw==` and the key, `0x42`, suggests a bitwise operation (like XOR decryption).

`Order matters` means bytes are to be decrypted sequentially using XOR with `0x42`.

So, we simply evecute the following script to decrypt both encoded strings:

```py
import base64
key = 0x42
y = lambda x: bytes(b ^ key for b in base64.b64decode(x)).decode('utf-8')
for i in ['Hm0xJTYNNVU2CDIRNwQwAg==','EgUROSUnNCE7MB07LC4wJx04LCQlMCcuPw==']:
    print(y(i))
```

We get the following output:

```
\/sgtOwtJpSuFr@
PGS{gevcyr_ynlre_znfgrel}
```

We notice that curly braces `{ }` are present in the second line, so our flag should be here.

Applying ROT13, onto the second line:
{% raw %}
```py
import codecs
flag = codecs.decode("PGS{gevcyr_ynlre_znfgrel}", "rot_13")
print(f"CTF{{{flag}}}")
```
{% endraw %}
Gives us the flag.


> Answer `CTF{triple_layer_mastery}`

## Note
This problem is unsolvable without the hint! (Confirme by the author of the problem.). The first given base 64 string gives us nothing to work with.


---

# Question: What the Game!

| Details |  |
|---|---|
| Points 	| 70 	|
| Category 	| Miscellaneous 	|
| Hints 	| 1. He uses Torrent 	|
| Date 	| 04-06-2025 	|
|Files | [idk_how_can_i_help.jpeg](/assets/iitgnssctf/what_the_game/idk_how_can_i_help.jpeg) |
|Flag | `CTF{1029959.68}` |
|OS |Windows |


## Description:
```
My friend plays a famous game (mod version) in his phone. Find the size of game (in KB). I just have a picture which he clicked with his phone.

Example Flag: CTF{999.99}

B/w he watches a lot of movies(ofcause pirated)
```

## First Attempt
The image seems to be innocent looking, there doesn't seem to be any hidden message. Looking at the properties, under details tab we see a comment.

{% include figure.liquid path="/assets/iitgnssctf/what_the_game/image.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

`27.59.119.32`

This looks like an IPv4 address. We know that he pirates stuff, and most often people use torrent (also comes from the fact that we are given an IP and are expected to tell file size of a modded game he downloaded).

So we need to look at the recent p2p traffic on this IP. That can be done on [https://iknowwhatyoudownload.com/](https://iknowwhatyoudownload.com/).

{% include figure.liquid path="/assets/iitgnssctf/what_the_game/image-1.png" class="img-fluid rounded z-depth-1 mx-auto d-block w-75" style="max-width:400px; max-height:90vh; width:auto; height:auto;"  %}

The last entry is fot GTA Vice city and is of size `1005.82MB`. Converting this to KiB, we have our flag `CTF{1029959.68}`.

> Answer `CTF{1029959.68}`

## Note
Technically, problem setter should have said to report the game size in KiB as KiB is different from KB.

# The End
That is all. I really enjoyed this CTF.