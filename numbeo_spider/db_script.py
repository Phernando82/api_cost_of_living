import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Criar uma API flask
app = Flask(__name__) # recebe o nome da app ('estrutura_banco_dados_alchemy)
# Criar uma instancia de SQLAlchemy
app.config['SECRET_KEY'] = 'Hermes82wars!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///numbeo.db' # connection string

db = SQLAlchemy(app)
db:SQLAlchemy

# Definir a estrutura da tabela admin
# id, nome, email, senha, admin, postagens
class User(db.Model):
    __tablename__ = 'user'
    id_user = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    senha = db.Column(db.String)
    admin = db.Column(db.Boolean)

class Cities(db.Model):
    __tablename__ = 'cities'
    id_city = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    common_meal = db.Column(db.String)
    meal_for_two = db.Column(db.String)
    one_way_ticket = db.Column(db.String)
    monthly_pass = db.Column(db.String)
    gasoline = db.Column(db.String)
    base_cost = db.Column(db.String)
    internet = db.Column(db.String)
    simple_apartment_centre = db.Column(db.String)
    simple_apartment_outside = db.Column(db.String)
    large_apartment_centre = db.Column(db.String)
    large_apartment_outside = db.Column(db.String)
    salary = db.Column(db.String)
    status = db.Column(db.String)

def inicializar_banco():
    # Executar o comando para criar o banco de dados
    db.drop_all()
    db.create_all()
    # Criar os administradores
    user = User(name='Fernando', email='fernandoperesvalverde@gmail.com', senha='Hermes82wars!', admin=True)
    db.session.add(user)
    db.session.commit()

# postagem = Postagem(titulo='Uma nova postagem', id_autor=1)
# db.session.add(postagem)
# db.session.commit()


if __name__ == "__main__":
    inicializar_banco()



def insert_city(name,common_meal,meal_for_two,one_way_ticket,monthly_pass,
gasoline,base_cost,internet,simple_apartment_centre,simple_apartment_outside,
large_apartment_centre,large_apartment_outside,salary,status):

    with sqlite3.connect('numbeo.db') as conexao:
        sql_insert = conexao.cursor()
        sql_insert.execute('''
            CREATE TABLE IF NOT EXISTS cities(
                id_city INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                common_meal TEXT,
                meal_for_two TEXT,
                one_way_ticket TEXT,
                monthly_pass TEXT,
                gasoline TEXT,
                base_cost TEXT,
                internet TEXT,
                simple_apartment_centre TEXT,
                simple_apartment_outside TEXT,
                large_apartment_centre TEXT,
                large_apartment_outside TEXT,
                salary TEXT,
                status TEXT
            )
        ''')
        sql_insert.execute('''
            INSERT OR IGNORE INTO cities(name,common_meal,meal_for_two,one_way_ticket,monthly_pass,gasoline,base_cost,internet,simple_apartment_centre,simple_apartment_outside,large_apartment_centre,large_apartment_outside,salary,status) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (
            name,
            common_meal,
            meal_for_two,
            one_way_ticket,
            monthly_pass,
            gasoline,
            base_cost,
            internet,
            simple_apartment_centre,
            simple_apartment_outside,
            large_apartment_centre,
            large_apartment_outside,
            salary,
            status,
        ))
        conexao.commit()


# insert_city("Messines","10","40","1,20", "35","1,71","130","35","400","250","550","350","1100","september 2022" )

def delete_city(id_city):
    with sqlite3.connect('numbeo.db') as conexao:
        sql_delete = conexao.cursor()
        cities = sql_delete.execute(f'delete from cities where id_city={id_city} ; ')
        conexao.commit()



def drop_city():
    with sqlite3.connect('numbeo.db') as conexao:
        sql_drop = conexao.cursor()
        cities = sql_drop.execute('drop table cities')
        conexao.commit()



# delete_city(8)







