from flask import Flask, render_template, request
import ipcalc, ipaddress
from modules import utils

app = Flask(__name__)

@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "GET":
        return render_template('index.html')

@app.route('/desenvolvimento', methods=('GET', 'POST'))
def Desenvolvimento():
    if request.method == "GET":
        return render_template('em_desenvolvimento.html')



@app.route('/calculadora-binaria', methods=('GET', 'POST'))
def CalculadoraBinaria():
    if request.method == "GET":
        return render_template('calculadora-binaria.html')

    if request.method == "POST":
        valor = request.form.get('binary-calculator-value')
        return render_template('calculadora-binaria.html', calculated_result=valor)

@app.route('/checklist', methods=('GET', 'POST'))
def checklist():
    if request.method == "GET":
        return render_template('megalink_checkbox.html')

    if request.method == "POST":
        checked_options_list = []
        checked_options_list = request.form.getlist('checkfield')

    VALORES = {
        "1":"CLIENTE COM ONU EM LOS",
        "2":"CLIENTE COM FATURA EM ABERTO",
        "3":"CLIENTE COM IP NO VOALLE" ,
        "4":"CLIENTE COM ONU SEM ENERGIA",
        "5":"RECEBO SINAL DA ONU",
        "6":"CABO CONECTADO NA WAN",
        "7":"DISCAGEM PPPOE",
        "8":"PROBLEMA GENERALIZADO",
        "9":"PON",
        "10":"TRAVADO NO CONCENTRADOR"
    }

    data = ""

    for key in VALORES:

        if key in checked_options_list:
            data += "sim[X]  não[ ] - "+VALORES.get(key)+"\n"
        else:
            data += "sim[ ]  não[X] - "+VALORES.get(key)+"\n"

        problema_verificado = request.form.get('problema')

        problemas = [
            "SEM ENERGIA",
            "CABO CONECTADO DE FORMA ERRADA",
            "BLOQUEIO FINANCEIRO",
            "EQUIPAMENTO DESLIGADO",
            "LOS",
            "ROTEADOR TRAVADO",
            "CONFIGURAÇÃO PPPOE",
            "ATENUAÇÃO",
            "PROBLEMA GENERALIZADO"
            ]

    data += "\n\n       PROBLEMA VERIFICADO:\n\n"+ problemas[int(problema_verificado)-1]

    return render_template('megalink_checkbox.html', formulario=data)

@app.route('/whois', methods=('GET', 'POST'))
def Whois():
    if request.method == "GET":
        return render_template('calculadora-binaria.html')

    if request.method == "POST":
        valor = request.form.get('binary-calculator-value')
        return render_template('calculadora-binaria.html', calculated_result=valor)


@app.route('/bgp-setup-generator', methods=('GET', 'POST'))
def bgpSetupCreator():

    if request.method == "GET":
        return render_template('bgp-setup-generator.html')

    if request.method == "POST":

        # type of vendor
        vendor = request.form.get('devices')
        ipsv4 = getSubnetHosts(request.form.get('p2pipv4'))
        ipsv6 = getSubnetHosts(request.form.get('p2pipv6'))
        ipv4network = getNetworkAddress(request.form.get('blocoipv4'))
        ipv4networkmask = getNetworkMask(request.form.get('blocoipv4'))
        ipv6network = getNetworkAddress(request.form.get('blocoipv6'))
        ipv6networkmask = getNetworkMask(request.form.get('blocoipv6'))
        community = "65269:11 65269:24 65269:31 65269:6695 65269:13538 65269:10001 65269:10002 65269:55001 65269:65001 65269:65501"

        if request.form.get('community'):
            community = request.form.get('community')

        nome = request.form.get('nome').upper().replace(" ","-")
        nomev4 = nome+"-V4"
        nomev6 = nome+"-V6"
        vlan = request.form.get('vlan')

        print(ipsv4)

        if vendor == "huawei":
            return render_template('result-huawei-template.html', bgpmyvlan=vlan,
                bgpneighboorname=nome,
                bgpmyipv4=ipsv4[0],bgpmyipv6=ipsv6[0],
                bgpneighbooripv4=ipsv4[1],
                bgpneighbooripv6=ipsv6[1],
                bgpneighboorasn=request.form.get('asn'),
                bgpneighboornamev4=nomev4,
                bgpneighboornamev6=nomev6,
                bgpneigboornetworkv4=ipv4network,
                bgpneigboornetworkv6=ipv6network,
                ipv4networkmask=ipv4networkmask,
                ipv6networkmask=ipv6networkmask,
                community=community
            
            )

        elif vendor == "juniper":
            return render_template('result-juniper-template.html', bgpmyvlan=vlan,
                bgpneighboorname=nome,
                bgpmyipv4=ipsv4[0],bgpmyipv6=ipsv6[0],
                bgpneighbooripv4=ipsv4[1],
                bgpneighbooripv6=ipsv6[1],
                bgpneighboorasn=request.form.get('asn'),
                bgpneighboornamev4=nomev4,
                bgpneighboornamev6=nomev6,
                bgpneigboornetworkv4=ipv4network,
                bgpneigboornetworkv6=ipv6network,
                ipv4networkmask=ipv4networkmask,
                ipv6networkmask=ipv6networkmask,
                community=community
            
            )

        else:
            return render_template('result.html', nome="ERRO")

@app.route('/subnet_calculator', methods=('GET', 'POST'))
def SubnetCalculator():

    if request.method == "GET":
        return render_template('calculadora_IP.html')

    if request.method == "POST":

        # type of vendor
        vendor = request.form.get('devices')
        ipsv4 = getSubnetHosts(request.form.get('p2pipv4'))
        ipsv6 = getSubnetHosts(request.form.get('p2pipv6'))
        ipv4network = getNetworkAddress(request.form.get('blocoipv4'))
        ipv4networkmask = getNetworkMask(request.form.get('blocoipv4'))
        ipv6network = getNetworkAddress(request.form.get('blocoipv6'))
        ipv6networkmask = getNetworkMask(request.form.get('blocoipv6'))
        community = "65269:11 65269:24 65269:31 65269:6695 65269:13538 65269:10001 65269:10002 65269:55001 65269:65001 65269:65501"

        if request.form.get('community'):
            community = request.form.get('community')

        nome = request.form.get('nome').upper().replace(" ","-")
        nomev4 = nome+"-V4"
        nomev6 = nome+"-V6"
        vlan = request.form.get('vlan')

        print(ipsv4)

        if vendor == "huawei":
            return render_template('result-huawei-template.html', bgpmyvlan=vlan,
                bgpneighboorname=nome,
                bgpmyipv4=ipsv4[0],bgpmyipv6=ipsv6[0],
                bgpneighbooripv4=ipsv4[1],
                bgpneighbooripv6=ipsv6[1],
                bgpneighboorasn=request.form.get('asn'),
                bgpneighboornamev4=nomev4,
                bgpneighboornamev6=nomev6,
                bgpneigboornetworkv4=ipv4network,
                bgpneigboornetworkv6=ipv6network,
                ipv4networkmask=ipv4networkmask,
                ipv6networkmask=ipv6networkmask,
                community=community
            
            )

        elif vendor == "juniper":
            return render_template('result-juniper-template.html', bgpmyvlan=vlan,
                bgpneighboorname=nome,
                bgpmyipv4=ipsv4[0],bgpmyipv6=ipsv6[0],
                bgpneighbooripv4=ipsv4[1],
                bgpneighbooripv6=ipsv6[1],
                bgpneighboorasn=request.form.get('asn'),
                bgpneighboornamev4=nomev4,
                bgpneighboornamev6=nomev6,
                bgpneigboornetworkv4=ipv4network,
                bgpneigboornetworkv6=ipv6network,
                ipv4networkmask=ipv4networkmask,
                ipv6networkmask=ipv6networkmask,
                community=community
            
            )

        else:
            return render_template('result.html', nome="ERRO")


def getSubnetHosts(network):
    return [str(ipaddress.ip_address(x)) for x in ipcalc.Network(network)]

def getNetworkAddress(network):
    subnet = ipcalc.Network(network)
    return (str(ipaddress.ip_address(subnet.network())))

def getNetworkMask(network):
    subnet = ipcalc.Network(network)
    return subnet.mask


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8081)
