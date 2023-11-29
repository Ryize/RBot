function change_attack_type(type) {
    let base = document.getElementById('base')
    let smart = document.getElementById('smart')
    if (type === 1) {
        base.style = 'display: none';
        smart.style = 'display: block';
    } else {
        base.style = 'display: block';
        smart.style = 'display: none';
    }
}

function change_method() {
    let btns = document.getElementsByName('method');
    let btn = ''
    for (let i = 0; i < btns.length; i++) {
        if (btns[i].checked === true) {
            btn = btns[i]
        }
    }
    let status = btn.value !== 'udp' && btn.value !== 'tcp';
    msg_tcp_udp = document.getElementsByName('msg_tcp_udp')
    for (let i = 0; i < msg_tcp_udp.length; i++) {
        msg_tcp_udp[i].disabled = status;
        if (status) {
            msg_tcp_udp[i].style = 'color: rgba(75, 154, 153, 0.5)';
        } else {
            msg_tcp_udp[i].style = 'color: rgb(75, 154, 153)';
        }


    }
    port = document.getElementsByName('port')
    for (let i = 0; i < port.length; i++) {
        port[i].disabled = status;
        if (status) {
            port[i].style = 'color: rgba(75, 154, 153, 0.5)';
        } else {
            port[i].style = 'color: rgb(75, 154, 153)';
        }
    }
}

function change_percent(el) {
    if (el.value > 100) {
        el.value = 100;
    } else if (el.value < 0) {
        el.value = 0;
    }
}

function change_host_ip(el) {
    if (el.name === 'url') {
        document.getElementsByName('ip')[0].disabled = true;
        document.getElementsByName('ip')[0].placeholder = 'Не более 1 адреса';
    } else if (el.name === 'ip') {
        document.getElementsByName('url')[0].disabled = true;
        document.getElementsByName('url')[0].placeholder = 'Не более 1 адреса';
    }
    if (el.value === '') {
        document.getElementsByName('url')[0].disabled = false;
        document.getElementsByName('url')[0].placeholder = '';
        document.getElementsByName('ip')[0].disabled = false;
        document.getElementsByName('ip')[0].placeholder = '';
    }
}

function isValidUrl(string) {
    try {
        new URL(string);
        return true;
    } catch (err) {
        return false;
    }
}

function check_available_host_ip(el) {
    let value = '';
    let url = document.getElementsByName('url')[0];
    let ip = document.getElementsByName('ip')[0];
    if (!url.disabled) {
        value = url.value;
    } else {
        value = ip.value;
        let re = new RegExp(ip.pattern);
        if (re.test(value)) {
            el.style = 'background: rgb(2,0,36); background: linear-gradient(149deg, rgba(2,0,36,1) 0%, rgba(54,103,3,1) 0%, rgba(94,94,94,1) 100%);';
        } else {
            el.style = 'background: rgb(2,0,36); background: linear-gradient(149deg, rgba(2,0,36,1) 0%, rgba(103,3,3,1) 0%, rgba(94,94,94,1) 100%);';
        }
        setTimeout(clear_status_check, 2000);
        return;
    }
    if (isValidUrl(value)) {
        el.style = 'background: rgb(2,0,36); background: linear-gradient(149deg, rgba(2,0,36,1) 0%, rgba(54,103,3,1) 0%, rgba(94,94,94,1) 100%);';
    } else {
        el.style = 'background: rgb(2,0,36); background: linear-gradient(149deg, rgba(2,0,36,1) 0%, rgba(103,3,3,1) 0%, rgba(94,94,94,1) 100%);';
    }
    setTimeout(clear_status_check, 2000);
}

function clear_status_check() {
    let el = document.getElementById('check');
    el.style = 'background: rgb(2, 0, 36); background: linear-gradient(347deg, rgba(2, 0, 36, 1) 0%, rgba(8, 8, 8, 1) 0%, rgba(94, 94, 94, 1) 100%);color: rgb(75, 154, 153);'
}

function base_attack() {
    let timeout = document.getElementsByName('timeout')[0].value;
    let msg_tcp_udp = document.getElementsByName('msg_tcp_udp')[0].value;
    let port = document.getElementsByName('port')[0].value;
    let max_thread = document.getElementsByName('max_thread')[0].value;

    document.getElementsByName('timeout_')[0].value = timeout;
    document.getElementsByName('msg_tcp_udp_')[0].value = msg_tcp_udp;
    document.getElementsByName('port_')[0].value = port;
    document.getElementsByName('max_thread_')[0].value = max_thread;
}

function smart_attack() {
    let percent = document.getElementsByName('percent')[0].value;
    let msg_tcp_udp = document.getElementsByName('msg_tcp_udp')[0].value;
    let port = document.getElementsByName('port')[0].value;

    document.getElementsByName('percent_')[0].value = percent;
    document.getElementsByName('msg_tcp_udp_')[0].value = msg_tcp_udp;
    document.getElementsByName('port_')[0].value = port;
}

function start() {
    let host = '';
    let url = document.getElementsByName('url')[0];
    let ip = document.getElementsByName('ip')[0];
    if (!url.disabled) {
        host = url.value;
    } else {
        host = ip.value;
    }

    let btns = document.getElementsByName('method');
    let method = ''
    for (let i = 0; i < btns.length; i++) {
        if (btns[i].checked === true) {
            method = btns[i]
        }
    }
    document.getElementsByName('host_')[0].value = host;
    document.getElementsByName('method_')[0].value = method;
    base_attack()
    smart_attack()

    document.getElementById('send_form').submit();
}

change_method()
