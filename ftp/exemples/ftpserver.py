#!/usr/bin/env python2
# coding: utf-8

import os,socket,threading,time
import traceback

currdir=os.path.abspath('.')

class FTPserverThread(threading.Thread):
    def __init__(self,(conn,addr)):
        self.conn=conn
        self.addr=addr
        self.basewd=currdir
        self.cwd=self.basewd
        threading.Thread.__init__(self)

    def run(self):
        self.conn.send('220 Welcome!\r\n')
        while True:
            cmd=self.conn.recv(256)
            if not cmd: break
            else:
                print 'Recieved:',cmd
                try:
                    func=getattr(self,cmd[:4].strip().upper())
                    func(cmd)
                except Exception,e:
                    print e
                    #traceback.print_exc()
                    self.conn.send('500 Sorry.\r\n')

    def LoadCwd(self):
        os.chdir(self.cwd)
    def SaveCwd(self):
        self.cwd=os.getcwd()
    def USER(self,cmd):
        self.conn.send('331 OK.\r\n')
    def PASS(self,cmd):
        self.conn.send('230 OK.\r\n')
    def QUIT(self,cmd):
        self.conn.send('221 Goodbye.\r\n')
    def NOOP(self,cmd):
        self.conn.send('200 OK.\r\n')
    def TYPE(self,cmd):
        self.mode=cmd[5]
        self.conn.send('200 Binary mode.\r\n')

    def CDUP(self,cmd):
        self.LoadCwd()
        os.chdir('..')
        self.SaveCwd()
        self.conn.send('200 OK.\r\n')
    def PWD(self,cmd):
        cwd=os.path.relpath(self.cwd,self.basewd)
        if cwd=='.':
            cwd='/'
        else:
            cwd='/'+cwd
        self.conn.send('257 \"%s\"\r\n' % cwd)
    def CWD(self,cmd):
        self.LoadCwd()
        print 'NOW:',os.getcwd()
        chwd=cmd[4:-2]
        if chwd=='/':
            chwd=self.basewd
        elif chwd[0]=='/':
            chwd=self.basewd+chwd
        os.chdir(chwd)
        print 'NOW:',os.getcwd()
        self.SaveCwd()
        self.conn.send('250 OK.\r\n')

    def PORT(self,cmd):
        l=cmd[5:].split(',')
        self.dataAddr='.'.join(l[:4])
        self.dataPort=(int(l[4])<<8)+int(l[5])
        self.conn.send('200 I know.\r\n')

    def LIST(self,cmd):
        self.LoadCwd()
        self.conn.send('150 Here comes the directory listing.\r\n')
        self.datasock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.datasock.connect((self.dataAddr,self.dataPort))
        l=os.listdir('.')
        for t in l:
            k=self.toListItem(t)
            #print k,
            self.datasock.send(k)
        self.datasock.close()
        self.conn.send('226 Directory send OK.\r\n')

    def toListItem(self,fn):
        st=os.stat(fn)
        fullmode='rwxrwxrwx'
        mode=''
        for i in range(9):
            mode+=((st.st_mode>>(8-i))&1) and fullmode[i] or '-'
        d=(os.path.isdir(fn)) and 'd' or '-'
        ftime=time.strftime(' %b %d %H:%M ', time.gmtime(st.st_mtime))
        return d+mode+' 1 user group '+str(st.st_size)+ftime+os.path.basename(fn)+'\r\n'

    def RETR(self,cmd):
        self.LoadCwd()
        print 'NOW:',os.getcwd()
        fn=cmd[5:-2]
        #fn=self.cwd+'/'+fn
        print 'Down:',fn
        if self.mode=='I':
            fi=open(fn,'rb')
        else:
            fi=open(fn,'r')
        self.conn.send('150 Opening data connection.\r\n')
        self.datasock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.datasock.connect((self.dataAddr,self.dataPort))
        data= fi.read(1024)
        while data:
            self.datasock.send(data)
            data=fi.read(1024)
        self.datasock.close()
        self.conn.send('226 Transfer complete.\r\n')

class FTPserver(threading.Thread):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('',8888))
        threading.Thread.__init__(self)

    def run(self):
        self.sock.listen(5)
        while True:
            th=FTPserverThread(self.sock.accept())
            th.daemon=True
            th.start()

    def stop(self):
        self.sock.close()

if __name__=='__main__':
    ftp=FTPserver()
    ftp.daemon=True
    ftp.start()
    raw_input('Enter to end...\n')
    ftp.stop()
