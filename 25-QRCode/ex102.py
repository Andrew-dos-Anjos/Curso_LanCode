'''📝 Exercício – QR Codes para Redes Sociais
Objetivo

Criar um script Python que gere um QR Code para cada perfil de rede social do usuário.
Passos solicitados no exercício

    Criar um dicionário chamado redes_sociais com pelo menos 3 pares rede: url_do_perfil.

        Exemplo:

            redes_sociais = {
                "instagram": "https://www.instagram.com/seu_usuario",
                "facebook": "https://www.facebook.com/seu_usuario",
                "twitter": "https://twitter.com/seu_usuario",
                "linkedin": "https://www.linkedin.com/in/seu_usuario",
                "youtube": "https://www.youtube.com/@seu_usuario"
            }

    Para cada item no dicionário:

        Gerar um QR Code para o valor (URL do perfil).

        Salvar a imagem com o nome da chave.

        O arquivo deve ser PNG.

        Exemplo: a chave "instagram" gera instagram.png.

Resultado esperado

O script deve gerar os arquivos:

    instagram.png → QR Code do perfil do Instagram

    facebook.png → QR Code do perfil do Facebook
    ...
    '''

import qrcode
linkedin = qrcode.make('https://www.linkedin.com/in/andrew_ferreira_dos_anjos')
linkedin.save('linkedin.png')

'''redes_sociais = {
    "Youtube":"https://youtube.com/@lan_code",
    "Udemy":"https://www.udemy.com/user/irlan-ferreira-da-silva-2/",
    "Linkedin":"https://www.linkedin.com/in/irlan-ferreira-b66b80263/"
}
for chave, valor in redes_sociais.items():
    img = qrcode.make(valor)
    img.save(f"qrcodes/{chave}.png")'''
