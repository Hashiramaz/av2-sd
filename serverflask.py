import mysql.connector
from flask import Flask
import json
from flask_jsonpify import jsonify

app = Flask(__name__) 

@app.route("/albumID/<album>")
#@app.route("/tracks/<AlbumId>")
#@app.route("/interface")
#@app.route("lista_generos")
#@app.route("trilhas_por_genero")
#@app.route("valor_por_trilha")

def imprime_album(album=None):
    conn = mysql.connector.connect (host='chinook.ceznup7dvlqs.us-east-1.rds.amazonaws.com', user='caiobrabo', passwd='ninja123', port='3306', database='chinook')
    cursor = conn.cursor()
    sql = 'select AlbumId from albums where title = "%s"' %  (album)
    cursor.execute(sql)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print(records)
    result =[dict(zip(tuple(row_headers),i)) for i in records]
    print (result)
    jret2 = jsonify(result)
    print (jret2)
    conn.close()
    return jret2

@app.route("/lista_generos/")
def imprime_lista():
    conn = mysql.connector.connect (host='chinook.ceznup7dvlqs.us-east-1.rds.amazonaws.com', user='caiobrabo', passwd='ninja123', port='3306', database='chinook')
    cursor = conn.cursor()
    sql1 = 'select * from genres'
    cursor.execute(sql1)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print(records)
    result =[dict(zip(tuple(row_headers),i)) for i in records]
    print (result)
    json_generos = jsonify(result)
    print (json_generos)
    conn.close()
    return json_generos

@app.route("/trilhas_por_generos/<genre_id>")
def imprime_trilhas(genre_id=None):
    conn = mysql.connector.connect (host='chinook.ceznup7dvlqs.us-east-1.rds.amazonaws.com', user='caiobrabo', passwd='ninja123', port='3306', database='chinook')
    cursor = conn.cursor()
    sql2 = 'select TrackId from tracks where GenreId = "%s" ' % (genre_id)
    cursor.execute(sql2)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print(records)
    result =[dict(zip(tuple(row_headers),i)) for i in records]
    print (result)
    json_trilhas = jsonify(result)
    print (json_trilhas)
    conn.close()
    return json_trilhas

@app.route("/valor_por_trilha/<trilha_id>")
def imprime_valor(trilha_id=None):
    conn = mysql.connector.connect (host='chinook.ceznup7dvlqs.us-east-1.rds.amazonaws.com', user='caiobrabo', passwd='ninja123', port='3306', database='chinook')
    cursor = conn.cursor()
    sql3 = 'select TrackID, (Quantity * UnitPrice) AS VALOR_TOTAL from invoice_items where TrackID = "%s" ' % (trilha_id)
    cursor.execute(sql3)
    row_headers=[x[0] for x in cursor.description]
    records = cursor.fetchall()
    print(records)
    result =[dict(zip(tuple(row_headers),i)) for i in records]
    print (result)
    json_valor = jsonify(result)
    print (json_valor)
    conn.close()
    return json_valor





app.run(host='0.0.0.0',port='80')


#def imprime_tracks(AlbumId=None):
#conn = mysql.connector.connect (host='chinook.ceznup7dvlqs.us-eus-east-1.rds.amazonaws.com', user='caiobrabo', passwd='ninja123', p    $23', port='3306', database='chinook')

#    sql2 = 'select name from tracks where AlbumId = "%s"' % (AlbumId)

 #   cursor.execute(sql2)
  #  records2 = cursor.fetchall()

   # for row in records2:
    #    nametrack = row[0]
     #   print('Faixa do Album {0} encontrada: {1}'.format(album,nametrack))


#    jret = jsonify(records2)
#    print (jret)
#    conn.close()
#    return jret



#app.run(host='0.0.0.0',port='80')
