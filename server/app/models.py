from app.ext import model


class Letter(model.Model):
    id = model.Column(model.Integer,primary_key=True,autoincrement=True)
    letter = model.Column(model.String(1),unique=True)
    cities = model.relationship('City',backref='Letter',lazy='dynamic')




class City(model.Model):
    id = model.Column(model.Integer,primary_key=True)
    regionName = model.Column(model.String(16),)
    cityCode = model.Column(model.Integer,)
    pinYin = model.Column(model.String(64),)
    fistLetter = model.Column(model.Integer,model.ForeignKey(Letter.id))

class Movie(model.Model):
    __tablename__='movies'
    id = model.Column(model.Integer,primary_key=True,)
    showname = model.Column(model.String(32))
    shownameen = model.Column(model.String(128))
    director = model.Column(model.String(256))
    leadingRole = model.Column(model.String(256))
    type = model.Column(model.String(256))
    country = model.Column(model.String(256))
    language = model.Column(model.String(256))
    duration = model.Column(model.Integer)
    screeningmodel=model.Column(model.String(16))
    openday = model.Column(model.DateTime)
    backgroundpicture = model.Column(model.String(1024))
    flag = model.Column(model.Integer)
    isdelete = model.Column(model.Boolean)


'''
insert into cinemas(name,city,district,address,phone,score,hallnum,
servicecharge,astrict,flag,isdelete) 
values("深圳戏院影城","深圳","罗湖","罗湖区新园路1号东门步行街西口",
"0755-82175808",9.7,9,1.2,20,1,0);
'''

class Cinemas(model.Model):
    __tablename__ = 'cinemas'
    name = model.Column(model.String(128),primary_key=True)
    city = model.Column(model.String(32))
    district = model.Column(model.String(32))
    address = model.Column(model.String(1024))
    phone = model.Column(model.String(32))
    score = model.Column(model.Integer)
    hallnum = model.Column(model.Integer)
    servicecharge= model.Column(model.Integer)
    astrict = model.Column(model.Integer)
    flag = model.Column(model.Integer)
    isdelete = model.Column(model.Boolean)
