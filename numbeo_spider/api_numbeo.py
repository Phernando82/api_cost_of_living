from flask import Flask, jsonify, request, make_response
from db_script import User, app, db
import json
import jwt
from datetime import datetime, timedelta
from functools import wraps

from db_script import Cities
# Rota padrão - GET http://localhost:5000



def token_obrigatorio(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # Verificar se um token foi enviado
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'mensagem': 'Token não foi incluído!'}, 401)
        # Se temos um token, validar acesso consultando o BD
        try:
            resultado = jwt.decode(token,app.config['SECRET_KEY'],algorithms=["HS256"])
            user = User.query.filter_by(
                id_user=resultado['id_user']).first()
        except:
            return jsonify({'mensagem': 'Token é inválido'}, 401)
        return f(user, *args, **kwargs)
    return decorated


@app.route('/login')
def login():
    auth = request.authorization
    if not auth or not auth.username or not auth.password:
        return make_response('Login inválido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})
    user = User.query.filter_by(name=auth.username).first()
    if not user:
        return make_response('Login inválido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})
    if auth.password == user.senha:
        token = jwt.encode({'id_user': user.id_user, 'exp': datetime.utcnow(
        ) + timedelta(minutes=30)}, app.config['SECRET_KEY'])
        return jsonify({'token':token})
    return make_response('Login inválido', 401, {'WWW-Authenticate': 'Basic realm="Login obrigatório"'})


@app.route('/city')  
@token_obrigatorio
def get_information(name):
    cities = Cities.query.all()
    list_information = []
    for city in cities:
        city_atual = {}
        city_atual['name'] = city.name
        city_atual['common_meal'] = city.common_meal
        city_atual['meal_for_two'] = city.meal_for_two
        city_atual['one_way_ticket'] = city.one_way_ticket
        city_atual['monthly_pass'] = city.monthly_pass
        city_atual['gasoline'] = city.gasoline
        city_atual['base_cost'] = city.base_cost
        city_atual['internet'] = city.internet
        city_atual['simple_apartment_centre'] = city.simple_apartment_centre
        city_atual['simple_apartment_outside'] = city.simple_apartment_outside
        city_atual['large_apartment_centre'] = city.large_apartment_centre
        city_atual['large_apartment_outside'] = city.large_apartment_outside
        city_atual['salary'] = city.salary
        city_atual['status'] = city.status
        list_information.append(city_atual)
    return jsonify({'': list_information})

# Obter city por id - GET https://localhost:5000/city/1


@app.route('/city/<int:id_city>', methods=['GET'])
@token_obrigatorio
def get_city_by_id(name,id_city):
    city = Cities.query.filter_by(id_city=id_city).first()
    city_atual = {}
    try:
        city_atual['name'] = city.name
        city_atual['common_meal'] = city.common_meal
        city_atual['meal_for_two'] = city.meal_for_two
        city_atual['one_way_ticket'] = city.one_way_ticket
        city_atual['monthly_pass'] = city.monthly_pass
        city_atual['gasoline'] = city.gasoline
        city_atual['base_cost'] = city.base_cost
        city_atual['internet'] = city.internet
        city_atual['simple_apartment_centre'] = city.simple_apartment_centre
        city_atual['simple_apartment_outside'] = city.simple_apartment_outside
        city_atual['large_apartment_centre'] = city.large_apartment_centre
        city_atual['large_apartment_outside'] = city.large_apartment_outside
        city_atual['salary'] = city.salary
        city_atual['status'] = city.status
    except:
        pass

    return jsonify({'information': city_atual})



@app.route('/user')
@token_obrigatorio
def get_user(user):
    users = User.query.all()
    list_users = []
    for user in users:
        user_atual = {}
        user_atual['id_user'] = user.id_user
        user_atual['name'] = user.name
        user_atual['email'] = user.email
        list_users.append(user_atual)

    return jsonify({'users': list_users})


@app.route('/user/<int:id_user>', methods=['GET'])
@token_obrigatorio
def get_user_by_id(user,id_user):
    user = User.query.filter_by(id_user=id_user).first()
    if not user:
        return jsonify(f'User not find!')
    user_atual = {}
    user_atual['id_user'] = user.id_user
    user_atual['name'] = user.name
    user_atual['email'] = user.email

    return jsonify({'user': user_atual})

# Criar novo autor

@app.route('/user', methods=['POST'])
@token_obrigatorio
def new_user(user):
    new_user = request.get_json()
    user = User(
        name=new_user['name'], senha=new_user['senha'], email=new_user['email'])

    db.session.add(user)
    db.session.commit()

    return jsonify({'Message': 'User created successfully'}, 200)


@ app.route('/user/<int:id_user>', methods=['PUT'])
@token_obrigatorio
def alter_user(id_user):
    altered_user = request.get_json()
    user = User.query.filter_by(id_user=id_user).first()
    if not user:
        return jsonify({'Message': 'User not find'})
    try:
        user.name = altered_user['name']
    except:
        pass
    try:
        user.email = altered_user['email']
    except:
        pass
    try:
        user.senha = altered_user['senha']
    except:
        pass

    db.session.commit()
    return jsonify({'Message': 'User altered successfully'})


@ app.route('/user/<int:id_user>', methods=['DELETE'])
@token_obrigatorio
def remove_user(id_user):
    user_present = User.query.filter_by(id_user=id_user).first()
    if not user_present:
        return jsonify({'Message': 'User not find'})
    db.session.delete(user_present)
    db.session.commit()

    return jsonify({'Message': 'User removed successfully'})


app.run(port=5000, host='localhost', debug=True)
