import time


def timer():
    second = 30
    for i in range(second):
        print(str(second - i) + " second remain")
        time.sleep(1)
    print("Time up")
    print(score)


def result():
    if score == 0:
        print("Better Luck Next Time")
    elif score == 1:
        print("Poor")
    elif score == 2:
        print("Bad")
    elif score == 3:
        print("Good")
    elif score == 4:
        print("Strong")
    elif score == 5:
        print("Very Strong")


def mode():
    print("Select Difficulty Level")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    print("Enter Your Choice")
    a = int(input())
    if a == 1:
        easy()
    elif a == 2:
        medium()
    elif a == 3:
        hard()


def easy():
    global score
    score = 0
    w = 0
    print("Question No 1")
    print("During the process of encryption and decryption, what keys are shared?")
    print("A. Private keys")
    print("B. Public keys")
    print("C. Public and private keys")
    print("D. User passwords")
    timer()
    print("Enter Your Choice\n")
    ans1 = input()
    if ans1 == 'B' or ans1 == 'b':
        score += 1
    else:
        w += 1

    print("Question No 2")
    print("You are attempting to run an Nmap port scan on a web server."
          "Which of the following commands would result in a scan of common ports "
          "with the least amount of noise in order to evade IDS?")
    print("A. nmap -sT -O -T0")
    print("B. nmap -sP -p-65535 -T5")
    print("C. nmap -A --host-timeout 99 -T1")
    print("D. nmap -A - Pn")
    timer()
    print("Enter Your Choice\n")
    ans2 = input()
    if ans2 == 'A' or ans2 == 'a':
        score += 1
    else:
        w += 1

    print("Question No 3")
    print("Which of the following is a component of a risk assessment?")
    print("A. Logical interface")
    print("B. DMZ")
    print("C. Administrative safeguards")
    print("D. Physical security")
    timer()
    print("Enter Your Choice\n")
    ans3 = input()
    if ans3 == 'C' or ans3 == 'c':
        score += 1
    else:
        w += 1

    print("Question No 4")
    print("Which access control mechanism allows for multiple systems to use a central"
          "authentication server (CAS) that permits users to authenticate once and gain access "
          "to multiple systems?")
    print("A. Windows authentication")
    print("B. Discretionary Access Control (DAC)")
    print("C. Role Based Access Control (RBAC)")
    print("D. Single sign-on")
    timer()
    print("Enter Your Choice\n")
    ans4 = input()
    if ans4 == 'D' or ans4 == 'd':
        score += 1
    else:
        w += 1

    print("Question No 5")
    print("Which of the following incident handling process phases is responsible for defining "
          "rules, collaborating human workforce, creating a back-up plan, and testing the plans "
          "for an organization?")
    print("A. Containment phase")
    print("B. Recovery phase")
    print("C. Identification phase")
    print("D. Preparation phase")
    timer()
    print("Enter Your Choice\n")
    ans5 = input()
    if ans5 == 'D' or ans5 == 'd':
        score += 1
    else:
        w += 1
    result()


def medium():
    global score
    score = 0
    w = 0
    print("Question No 1")
    print("DNS cache snooping is a process of determining if the specified resource address is "
          "present in the DNS cache records. It may be useful during the examination of the "
          "network to determine what software update resources are used, thus discovering "
          "what software is installed. What command is used to determine if the entry is present "
          "in DNS cache?")
    print("A. nslookup -norecursive update.antivirus.com")
    print("B. nslookup -fullrecursive update.antivirus.com")
    print("C. dnsnooping -rt update.antivirus.com")
    print("D. dns --snoop update.antivirus.com")
    timer()
    print("Enter Your Choice\n")
    ans1 = input()
    if ans1 == 'A' or ans1 == 'a':
        score += 1
    else:
        w += 1

    print("Question No 2")
    print("Chandler works as a pen-tester in an IT-firm in New York. As a part of detecting "
          "viruses in the systems, he uses a detection method where the anti-virus executes the "
          "malicious codes on a virtual machine to simulate CPU and memory activities. Which "
          "type of virus detection method did Chandler use in this context?")
    print("A. Heuristic Analysis")
    print("B. Scanning")
    print("C. Code Emulation")
    print("D. Integrity checking")
    timer()
    print("Enter Your Choice\n")
    ans2 = input()
    if ans2 == 'B' or ans2 == 'b':
        score += 1
    else:
        w += 1

    print("Question No 3")
    print("Which method of password cracking takes the most time and effort?")
    print("A. Dictionary attack")
    print("B. Rainbow tables")
    print("C. Brute force")
    print("D. Shoulder surfing")
    timer()
    print("Enter Your Choice\n")
    ans3 = input()
    if ans3 == 'C' or ans3 == 'c':
        score += 1
    else:
        w += 1

    print("Question No 4")
    print("What is the most common method to exploit the Bash Bug ShellShock vulnerability?")
    print("A. Manipulate format strings in text fields")
    print("B. Through Web servers utilizing CGI (Common Gateway Interface) to send a malformed "
          "environment variable to a vulnerable Web server")
    print("C. SYN Flood")
    print("D. SSH")
    timer()
    print("Enter Your Choice\n")
    ans4 = input()
    if ans4 == 'B' or ans4 == 'b':
        score += 1
    else:
        w += 1

    print("Question No 5")
    print("Which of the following provides a security professional with most information about "
          "the systems security posture?")
    print("A. Port scanning, banner grabbing, service identification")
    print("B. Social engineering, company site browsing, tailgating")
    print("C. Wardriving, warchalking, social engineering")
    print("D. Phishing, spamming, sending trojans")
    timer()
    print("Enter Your Choice\n")
    ans5 = input()
    if ans5 == 'A' or ans5 == 'a':
        score += 1
    else:
        w += 1
    result()


def hard():
    global score
    score = 0
    w = 0
    print("Question No 1")
    print("What is a Collision attack in cryptography?")
    print("A. Collision attacks try to break the hash into two parts, with the same bytes in each part to "
          "get the private key.")
    print("B. Collision attacks try to break the hash into three parts to get the plaintext value.")
    print("C. Collision attacks try to get the public key")
    print("D. Collision attacks try to find two inputs producing the same hash.")
    timer()
    print("Enter Your Choice\n")
    ans1 = input()
    if ans1 == 'D' or ans1 == 'd':
        score += 1
    else:
        w += 1

    print("Question No 2")
    print("Which protocol and port number might be needed in order to send log messages to a "
          "log analysis tool that resides behind a firewall?")
    print("A. UDP 415")
    print("B. UDP 541")
    print("C. UDP 514")
    print("D. UDP 123")
    timer()
    print("Enter Your Choice\n")
    ans2 = input()
    if ans2 == 'C' or ans2 == 'c':
        score += 1
    else:
        w += 1

    print("Question No 3")
    print("As a Certified Ethical Hacker, you were contracted by a private firm to conduct an "
          "external security assessment through penetration testing. What document describes "
          "the specifics of the testing, the associated violations, and essentially protects both "
          "the organization's interest and your liabilities as a tester?")
    print("A. Project Scope")
    print("B. Service Level Agreement")
    print("C. Non-Disclosure Agreement")
    print("D. Rules of Engagement")
    timer()
    print("Enter Your Choice\n")
    ans3 = input()
    if ans3 == 'D' or ans3 == 'd':
        score += 1
    else:
        w += 1

    print("Question No 4")
    print("User A is writing a sensitive email message to user B outside the local network. User A "
          "has chosen to use PKI to secure his message and ensure only user B can read the "
          "sensitive email. At what layer of the OSI layer does the encryption and decryption of "
          "the message take place?")
    print("A. Presentation")
    print("B. Application")
    print("C. Session")
    print("D. Transport")
    timer()
    print("Enter Your Choice\n")
    ans4 = input()
    if ans4 == 'A' or ans4 == 'a':
        score += 1
    else:
        w += 1

    print("Question No 5")
    print("Which of the following is a low-tech way of gaining unauthorized access to systems?")
    print("A. Sniffing")
    print("B. Scanning")
    print("C. Social Engineering")
    print("D. Eavesdropping")
    timer()
    print("Enter Your Choice\n")
    ans5 = input()
    if ans5 == 'C' or ans5 == 'c':
        score += 1
    else:
        w += 1
    result()

    
mode()
