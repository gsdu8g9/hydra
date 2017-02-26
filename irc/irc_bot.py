import sys
import socket
import string

_address = ("irc.freenode.net", 6667)
buffer = ''
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


NICK = "griffmaestro"
INDENT = "griffmaestro"
REALNAME = "gwuahnode"
MASTER = "gwuahnode"
channel = "#bots"
           

def connect(_address) :
    irc.connect(_address)
    return True

def reg_userinfo():
    irc.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
    irc.send(bytes("USER %s %s rat :%s\r\n" % (INDENT, _address[0], REALNAME), "UTF-8"))
    irc.send(bytes("JOIN %s\r\n" % channel, "UTF-8"));
    irc.send(bytes("PRIVMSG %s :ogma \r\n" % MASTER, "UTF-8"))
    return True


def recv() :
    message = buffer + irc.recv(1024).decode("UTF-8")
    return message

def output(line) :
    username = chunk[0].split(':')[1]
    index = b.index("#bots") + 1
    container = chunk[index:]
    message = " ".join(word for word in container)
    message = message[1:]
    return message
      

def ping_pong_protocol(chunk) :
    if (chunk[0] == "PING"):
        irc.send(bytes("PONG %s\r\n" % chunk[1], "UTF-8"))
        return True
    else : pass

def output(chunk) :
    username = chunk[0].split(':')[1]
    index = chunk.index("#bots") + 1
    container = chunk[index:]
    message = " ".join(word for word in container)
    message = message[1:]
    return (username, message)




def main() :
    global chunk
    global username
    
    if connect(_address) :
        if reg_userinfo():
            while True :
                buffer = recv()
                temp = buffer.split("\n")
                buffer = temp.pop()
                
                for line in temp:
                    line = line.rstrip()
                    line = line.split()
                    
                if (line[0] == "PING") :
                    ping_pong_protocol(line)

                elif (line[1] == "PRIVMSG") :
                    username, message = output(line)
                    print("%s >>> %s" % (username, message))





