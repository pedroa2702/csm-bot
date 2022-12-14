from pyobigram.utils import sizeof_fmt,nice_time
import datetime
import time
import os

def dashboard():
    start_msg = '<a href="">-TGUploaderV12-</a>\n'
    start_msg += '<b>ð¨Uso: Envia Enlaces De Descarga y Archivos Para Procesar (Configure Antes De Empezar , Vea El /tutorial)</b>\n'
    return start_msg

def text_progres(index,max,size=21,step_size=5):
    try:
        if max<1:
            max += 1
        porcent = index / max
        porcent *= 100
        porcent = round(porcent)
        make_text = ''
        index_make = 1
        make_text += '\n['
        while(index_make<size):
            if porcent >= index_make * step_size:make_text+='â '
            else:make_text+='â'
            index_make+=1
        make_text += ']\n'
        return make_text
    except Exception as ex:
            return ''

def porcent(index,max):
    porcent = index / max
    porcent *= 100
    porcent = round(porcent)
    return porcent

def createDownloading(filename,totalBits,currentBits,speed,time,tid=''):
    msg = 'â¡ Obteniendo Archivo\n\n'
    msg += 'ð Archivo: ' + filename + '\n'
    msg += text_progres(currentBits, totalBits) + '\n'
    msg += 'â³ Porcentaje: ' + str(porcent(currentBits, totalBits)) + '%\n\n'
    msg += 'ð¦ Total: ' + sizeof_fmt(totalBits) + '\n\n'
    msg += 'ð¾ Descargado: ' + sizeof_fmt(currentBits) + '\n\n'
    msg += 'ð Velocidad: ' + sizeof_fmt(speed) + '/s\n\n'
    msg += 'â²ï¸ Tiempo de Descarga: ' + str(datetime.timedelta(seconds=int(time))) + 's\n\n'
    return msg
def createUploading(filename,totalBits,currentBits,speed,time,originalname=''):
    msg = 'âï¸ Agregando a la Nube âï¸\n\n'
    msg += 'ð Nombre: ' + filename + '\n'
    if originalname != '':
        msg = str(msg).replace(filename, originalname)
        msg += 'ð Nombre: ' + str(filename) + '\n'
    msg += text_progres(currentBits, totalBits) + '\n'
    msg += 'â³ Porcentaje: ' + str(porcent(currentBits, totalBits)) + '%\n\n'
    msg += 'ð¦ Total: ' + sizeof_fmt(totalBits) + '\n\n'
    msg += 'âï¸ Subido: ' + sizeof_fmt(currentBits) + '\n\n'
    msg += 'ð Velocidad: ' + sizeof_fmt(speed) + '/s\n\n'
    msg += 'â²ï¸ Tiempo de Subida: ' + str(datetime.timedelta(seconds=int(time))) + 's\n\n'
    return msg
def createCompresing(filename,filesize,splitsize):
    msg = 'ð© Fraccionando Partes \n\n'
    msg+= 'ð Nombre: ' + str(filename)+'\n'
    msg+= 'ð¦ TamaÃ±o Total: ' + str(sizeof_fmt(filesize))+'\n'
    msg+= 'ðï¸ TamaÃ±o Partes: ' + str(sizeof_fmt(splitsize))+'\n'
    msg+= 'ð Cantidad Partes: ' + str(round(int(filesize/splitsize)+1,1))+'\n\n'
    return msg
def createFinishUploading(filename,filesize,datacallback=None):
    msg = 'â ' + str(filename)+ f' Subido {str(sizeof_fmt(filesize))}\n'
    if datacallback:
       msg += 'datacallback: ' + datacallback
    return msg

def createFileMsg(filename,files):
    import urllib
    if len(files)>0:
        msg= '<b>ðEnlacesð</b>\n'
        for f in files:
            url = urllib.parse.unquote(f['directurl'],encoding='utf-8', errors='replace')
            #msg+= '<a href="'+f['url']+'">ð' + f['name'] + 'ð</a>'
            msg+= "<a href='"+url+"'>ð"+f['name']+'ð</a>\n'
        return msg
    return ''

def createFilesMsg(evfiles):
    msg = 'ðArchivos ('+str(len(evfiles))+')ð\n\n'
    i = 0
    for f in evfiles:
            try:
                fextarray = str(f['files'][0]['name']).split('.')
                fext = ''
                if len(fextarray)>=3:
                    fext = '.'+fextarray[-2]
                else:
                    fext = '.'+fextarray[-1]
                fname = f['name'] + fext
                msg+= '/txt_'+ str(i) + ' /del_'+ str(i) + '\n' + fname +'\n\n'
                i+=1
            except:pass
    return msg
def createStat(username,userdata,isadmin):
    from pyobigram.utils import sizeof_fmt
    msg = 'âï¸Configuraciones De Usuarioâï¸\n\n'
    msg+= 'ð Nombre: @' + str(username)+'\n'
    msg+= 'ð¹ User: ' + str(userdata['moodle_user'])+'\n'
    msg+= 'ð Password: ' + str(userdata['moodle_password']) +'\n'
    msg+= 'ð¡ Host: ' + str(userdata['moodle_host'])+'\n'
    if userdata['cloudtype'] == 'moodle':
        msg+= 'ð RepoID: ' + str(userdata['moodle_repo_id'])+'\n'
        msg+= 'â ï¸ UpType: ' + str(userdata['uploadtype'])+'\n'
    msg += 'âï¸ CloudType: ' + str(userdata['cloudtype']) + '\n'
    if userdata['cloudtype'] == 'cloud':
        msg+= 'ð Dir: /' + str(userdata['dir'])+'\n'
    msg+= 'ðï¸ TamaÃ±o de Zips : ' + sizeof_fmt(userdata['zips']*1024*1024) + '\n\n'
    msgAdmin = 'â'

    if isadmin:
        msgAdmin = 'â'
    msg+= 'ðª Admin : ' + msgAdmin + '\n'
    proxy = 'â'
    if userdata['proxy'] !='':
       proxy = 'â'
    rename = 'â'
    if userdata['rename'] == 1:
       rename = 'â'
    msg+= 'ð Rename : ' + rename + '\n'
    msg+= 'â¡ï¸ Proxy : ' + proxy + '\n'
    shorturl = (userdata['urlshort'] == 1)
    shortener = 'â'
    if shorturl:
       shortener = 'â'
    msg += 'ð ShortUrl : ' + shortener + '\n\n'
    return msg
