import re
from typing import Type


class CalcIpv4:
    def __init__(self, ip, mascara=None, prefixo=None):
        self.ip = ip
        self.mascara = mascara
        self.prefixo = prefixo
        self._set_broadcast()
        self._set_rede() 

    @property 
    def rede(self):
        return self._rede 

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def numero_ips(self):
        return self.get_numero_ip()

    @property
    def ip(self):
        return self._ip

    @property
    def mascara(self):
        return self._mascara

    @property
    def prefixo(self):
        return self._prefixo

    @ip.setter
    def ip(self, value):
        if not self._valida_ip(value):
            raise ValueError('Número de IP inválido') 

        self._ip = value 
        self._ip_bin = self._ip_to_bin(value)

    @mascara.setter
    def mascara(self, value):
        if not value:
            return 
        
        if not self._valida_ip(value):
            raise ValueError('Máscara inválida') 

        self._mascara = value 
        self._mascara_bin = self._ip_to_bin(value)
        if not hasattr(self, 'prefixo'):
            self.prefixo = self._mascara_bin.count('1')

    @prefixo.setter 
    def prefixo(self, value):
        if not value:
            return 

        if not isinstance(value, int):
            raise TypeError('Prefixo precisa ser inteiro')

        if value > 32:
            raise ValueError('Prefixo precisar ter 32 bits') 
        
        self._prefixo = value 
        self._mascara_bin = (value * '1').ljust(32, '0')
        if not hasattr(self, 'mascara'):
            self.mascara = self._bin_to_ip(self._mascara_bin) 

    @staticmethod
    def _valida_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True 

    @staticmethod
    def _ip_to_bin(ip):
        blocos = ip.split('.') 
        blocos_binarios = [bin(int(x)) [2:].zfill(8) for x in blocos]
        return ''.join(blocos_binarios)

    @staticmethod
    def _bin_to_ip(ip):
        n = 8 
        blocos = [str(int(ip[i:n+i], 2)) for i in range(0, 32, n)]
        ip_decimal = [x for x in blocos]
        return '.'.join(blocos)

    def _set_broadcast(self):
        hots_bits = 32 - self.prefixo
        self._broadcast_bin = self._ip_bin[:self.prefixo] + (hots_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_rede(self):
        hots_bits = 32 - self.prefixo
        self._rede_bin = self._ip_bin[:self.prefixo] + (hots_bits * '0')
        self._rede = self._bin_to_ip(self._rede_bin)
        return self._rede
        
    def get_numero_ip(self):
        return 2 ** (32 - self.prefixo)
