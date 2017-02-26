import sys
import socket

NICK = "gwuah44son"
IDENT = "thesongwuah"
REALNAME = "gwuah"
MASTER = "oxingwuah"
channel = "#bots"

global line

HOST, PORT = "irc.freenode.net", 6667
_buffer = ""

irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def recv() :
	return _buffer + irc.recv(1024).decode("UTF-8")

def ping_pong_protocol(chunk) :
	irc.send(bytes("PONG %s\r\n" % chunk[1], "UTF-8"))

def output(chunk) :
	username = chunk[0].split(':')[1].split('!')[0]
	index = chunk.index("#bots") + 1
	container = chunk[index:]
	message = " ".join(word for word in container)
	message = message[1:]
	return (username, message)

def main():
	irc.connect((HOST, PORT))
	irc.send(bytes("NICK %s\r\n" % NICK, "UTF-8"))
	irc.send(bytes("USER %s %s bla :%s\r\n" % (IDENT, HOST, REALNAME), "UTF-8"))
	irc.send(bytes("JOIN #bots\r\n", "UTF-8"));
	irc.send(bytes("PRIVMSG %s :Hello \r\n" % MASTER, "UTF-8"))
	print('Neccesary Info Transmitted\n')
	while 1 :
		_buffer = recv()
		message = _buffer.split("\n")
		_buffer = message.pop()

		for line in message :
			line = line.rstrip()
			line = line.split()
			if len(line) <= 1 :
				pass
			else :
				if (line[0] == "PING") :
					ping_pong_protocol(line)
	
				if (line[1] == "PRIVMSG") :
					username, message = output(line)
					print("[%s] := %s" % (username, message))
	
main()


