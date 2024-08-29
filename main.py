from hostgator_influenciadores import HostgatorInfluenciadores
from youtube_channel import YoutubeChannel


codigo_fonte_tv = YoutubeChannel('Código Fonte TV', 'codigofontetv')
attekita_dev = YoutubeChannel('Atekita Dev', 'atekitadev')
dio_linux = YoutubeChannel('Diolinux', 'diolinux')
programacao_dinamica = YoutubeChannel('Programação Dinâmica', 'programacaodinamica')
rodrigo_branas = YoutubeChannel('Rodrigo Branas', 'rodrigobranas')
tekzoom = YoutubeChannel('Tekzoom', 'tekzoom')

hostgator_influenciadores = HostgatorInfluenciadores()
hostgator_influenciadores.set_members(codigo_fonte_tv)
hostgator_influenciadores.set_members(attekita_dev)
hostgator_influenciadores.set_members(dio_linux)


hostgator_influenciadores2 = HostgatorInfluenciadores()
hostgator_influenciadores2.set_members(programacao_dinamica)
hostgator_influenciadores2.set_members(rodrigo_branas)
hostgator_influenciadores2.set_members(tekzoom)

print(f'Primeiro obj: {hostgator_influenciadores}')
print(f'Segundo obj: {hostgator_influenciadores2}')