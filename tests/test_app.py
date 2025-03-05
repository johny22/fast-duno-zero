from http import HTTPStatus


def test_root_deve_retornar_ok_e_o_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client, user_data):
    response = client.post('/users/', json={**user_data})
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': user_data['username'],
        'email': user_data['email'],
    }


def test_read_users(client, user_data):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': user_data['username'],
                'email': user_data['email'],
            }
        ]
    }
