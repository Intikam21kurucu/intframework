from pysnmp.hlapi import *

def start_pysnmp_listener(community='public', port=161):
    print(f'Starting PySNMP listener on port {port}')
    
    def callback(snmp_engine, state_reference, context_engine_id, context_name, var_binds, **kwds):
        print(f'Received SNMP message: {var_binds}')

    snmp_engine = SnmpEngine()

    ntf = NotificationType(
        ObjectType(ObjectIdentity('1.3.6.1.2.1.1.1.0')),
    )
    
    ntf.addNotificationTarget(TargetAddr(
        (community, port),
        transport=UdpTransportTarget(('0.0.0.0', port)),
    ))

    ntf.setCallback(callback)
    ntf.listen()

    # Eğer sürekli dinleme yapılacaksa, bunu bir döngü içinde tutabilirsiniz.
    import time
    while True:
        time.sleep(1)